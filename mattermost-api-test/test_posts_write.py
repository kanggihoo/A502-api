"""Mattermost 게시글/스레드 작성 검증.

api-docs/mattermost-api-priority-filter.md 의 "첫 API 검증 순서" 3단계(posts/threads)의
쓰기 부분을 실제 PAT 로 수행한다. 이 스크립트는 채널에 실제 메시지를 게시한다.

주의: 테스트 메시지가 채널에 노출된다. 테스트 전용 채널(MATTERMOST_TEST_CHANNEL_ID)을
사용하거나, 팀이 합의한 채널에서 실행할 것. 메시지는 [POC-TEST] 접두어로 식별한다.

검증 항목:
  P-1 POST /posts                 채널에 테스트 메시지 작성 (create_post 권한)
  P-2 POST /posts (root_id)       P-1 글에 스레드 답글 작성
  P-3 GET /posts/{root_id}/thread 작성한 스레드 확인

실행:  uv run python test_posts_write.py
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from mattermost_client import (
    CheckResult,
    Config,
    MattermostClient,
    Report,
    channel_web_url,
    load_config,
    thread_web_url,
)


def main() -> None:
    cfg: Config = load_config()
    client = MattermostClient(cfg)
    report = Report(title="게시글/스레드 작성 검증", base_url=cfg.base_url)

    print(f"Mattermost: {cfg.base_url}")
    print("주의: 채널에 실제 테스트 메시지를 게시합니다.")
    print("-" * 60)

    # 대상 팀/채널 확정.
    _, team_id = client.resolve_team()
    team_resp, _ = (None, None)
    if team_id:
        _, channel_id = client.resolve_channel(team_id)
    else:
        channel_id = None
    if not team_id or not channel_id:
        report.add(CheckResult("대상 확정", "GET /users/me/teams...", False, None,
                               "대상 팀/채널을 찾을 수 없음", None, None,
                               "MATTERMOST_TEST_TEAM_ID / CHANNEL_ID 확인", 0))
        _finalize(report)
        return

    # 팀 name 은 원문 URL 조립용. 1-3 결과 재사용 대신 직접 조회.
    team_name = ""
    t_resp = client.get(f"/teams/{team_id}")
    if t_resp.ok and isinstance(t_resp.data, dict):
        team_name = t_resp.data.get("name") or ""

    # 채널 name 도 원문 URL 용.
    ch_name = ""
    c_resp = client.get(f"/channels/{channel_id}")
    if c_resp.ok and isinstance(c_resp.data, dict):
        ch_name = c_resp.data.get("name") or ""

    ch_url = channel_web_url(cfg.base_url, team_name, ch_name) if team_name and ch_name else None
    ts_label = datetime.now().strftime("%Y%m%d-%H%M%S")

    print(f"대상: team={team_id} channel={channel_id}\n")

    # P-1 채널에 테스트 메시지 작성.
    r = client.post("/posts", json_body={
        "channel_id": channel_id,
        "message": f"[POC-TEST] A502 통합 알림 연동 확인 ({ts_label})\n이 메시지는 API 동작 검증용입니다.",
    })
    summary = "게시글 작성 실패"
    sample = None
    root_id = None
    post_web_url = None
    if r.ok and isinstance(r.data, dict):
        p = r.data
        root_id = p.get("id")
        summary = f"작성 성공 post_id={root_id}"
        sample = {"id": p.get("id"), "channel_id": p.get("channel_id"),
                  "create_at": p.get("create_at"),
                  "message": (p.get("message") or "")[:60]}
        if team_name and root_id:
            post_web_url = thread_web_url(cfg.base_url, team_name, root_id)
    report.add(CheckResult("P-1 게시글 작성", "POST /posts",
                           r.ok, r.status, summary, post_web_url, sample,
                           r.error, r.elapsed_ms))

    # P-2 P-1 글에 스레드 답글 작성.
    if not root_id:
        report.add(CheckResult("P-2 스레드 답글 작성", "POST /posts (root_id)",
                               False, None, "원글이 없어 답글 작성 불가",
                               None, None, None, 0))
    else:
        r = client.post("/posts", json_body={
            "channel_id": channel_id,
            "message": f"[POC-TEST] 스레드 답글 확인 ({ts_label})",
            "root_id": root_id,
        })
        summary = "답글 작성 실패"
        sample = None
        if r.ok and isinstance(r.data, dict):
            p = r.data
            summary = f"답글 작성 성공 post_id={p.get('id')} root_id={p.get('root_id')}"
            sample = {"id": p.get("id"), "root_id": p.get("root_id"),
                      "message": (p.get("message") or "")[:60]}
        report.add(CheckResult("P-2 스레드 답글 작성", "POST /posts (root_id)",
                               r.ok, r.status, summary, post_web_url, sample,
                               r.error, r.elapsed_ms))

    # P-3 작성한 스레드 확인.
    if not root_id:
        report.add(CheckResult("P-3 스레드 확인", "GET /posts/{root_id}/thread",
                               False, None, "원글이 없어 스레드 확인 불가",
                               None, None, None, 0))
    else:
        r = client.get(f"/posts/{root_id}/thread")
        summary = "스레드 확인 실패"
        sample = None
        if r.ok and isinstance(r.data, dict):
            order = r.data.get("order") or []
            posts = r.data.get("posts") or {}
            rows = [{"id": posts.get(pid, {}).get("id"),
                     "message": (posts.get(pid, {}).get("message") or "")[:50],
                     "root_id": posts.get(pid, {}).get("root_id")}
                    for pid in order[:5]]
            summary = f"스레드 게시글 {len(order)}개 (원글+답글 확인)"
            sample = rows
        report.add(CheckResult("P-3 스레드 확인",
                               f"GET /posts/{root_id}/thread",
                               r.ok, r.status, summary, post_web_url, sample,
                               r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
