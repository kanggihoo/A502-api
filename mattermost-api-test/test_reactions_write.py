"""사용자 상호작용 — 리액션 추가/조회/삭제 검증.

통합 워크스페이스가 "팀 반응 확인" 용도로 쓸 리액션 API 를 실제 PAT 로 검증한다.
이 스크립트는 쓰기(POST/DELETE)를 수행한다.

안전장치 (test_posts_write.py 와 동일한 철학):
- 대상 게시글: env 채널(MATTERMOST_TEST_CHANNEL_ID)의 최근 게시글 중 첫 번째.
  채널에 게시글이 없으면 스킵한다. (새 게시글을 만들지 않는다)
- 리액션은 추가 후 **반드시 삭제**한다. 채널에 흔적을 남기지 않는다.
- 식별 가능한 emoji_name(white_check_mark) 을 사용하고, 어디서 온 리액션인지
  로그에 [POC-TEST] 접두어로 명시한다.

문서상 정확한 엔드포인트 (api-docs/mattermost_defuddle_markdown/16-reactions/):
- 추가: POST /reactions  (단일 엔드포인트 + JSON body. /users/.../reactions/... 아님)
- 조회: GET  /posts/{post_id}/reactions
- 삭제: DELETE /users/{user_id}/posts/{post_id}/reactions/{emoji_name}  (user_id=me 가능)

주의: POST /reactions 의 body user_id 는 실제 사용자 ID 여야 한다.
(path 의 me 리터럴과 달리 body 필드에서는 me 가 허용되지 않는다 — 400 확인됨)

검증 항목:
  R-1 GET  /posts/{post_id}/reactions                          사전 리액션 스냅샷
  R-2 POST /reactions                                          리액션 추가 (read_channel 권한)
  R-3 GET  /posts/{post_id}/reactions                          추가 후 재조회 (반영 확인)
  R-4 DELETE /users/me/posts/{post_id}/reactions/{emoji_name}  정리 (원 상태 복구)

실행:  uv run python test_reactions_write.py
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
)

# 테스트용 이모지. 기본 내장 이모지라 모든 인스턴스에서 사용 가능.
TEST_EMOJI = "white_check_mark"


def _reaction_rows(reactions: list, limit: int = 10) -> list[dict]:
    """리액션 목록 응답을 요약 샘플로 변환."""
    rows = []
    for r in reactions[:limit]:
        rows.append({
            "user_id": r.get("user_id"),
            "emoji_name": r.get("emoji_name"),
            "create_at": r.get("create_at"),
        })
    return rows


def main() -> None:
    cfg: Config = load_config()
    client = MattermostClient(cfg)
    report = Report(title="리액션 추가/조회/삭제 검증", base_url=cfg.base_url)

    ts_label = datetime.now().strftime("%Y%m%d-%H%M%S")
    print(f"Mattermost: {cfg.base_url}")
    print(f"주의: 이 스크립트는 리액션을 추가한 뒤 삭제합니다(자체 정리). ts={ts_label}")
    print("-" * 60)

    # 대상 팀/채널 확정.
    _, team_id = client.resolve_team()
    if not team_id:
        report.add(CheckResult("대상 확정", "GET /users/me/teams", False, None,
                               "대상 팀을 찾을 수 없음", None, None,
                               "MATTERMOST_TEST_TEAM_ID 확인", 0))
        _finalize(report)
        return
    _, channel_id = client.resolve_channel(team_id)
    if not channel_id:
        report.add(CheckResult("대상 확정", "GET /users/me/teams/{team_id}/channels", False, None,
                               "대상 채널을 찾을 수 없음", None, None,
                               "MATTERMOST_TEST_CHANNEL_ID 확인", 0))
        _finalize(report)
        return

    # 원문 URL 조립용 team_name/channel_name.
    r_team = client.get(f"/teams/{team_id}")
    r_ch = client.get(f"/channels/{channel_id}")
    team_name = r_team.data.get("name") if (r_team.ok and isinstance(r_team.data, dict)) else ""
    channel_name = r_ch.data.get("name") if (r_ch.ok and isinstance(r_ch.data, dict)) else ""
    web_url = channel_web_url(cfg.base_url, team_name, channel_name) if (team_name and channel_name) else None

    print(f"대상: team={team_name}({team_id}) channel={channel_name}({channel_id})\n")

    # 대상 게시글 선택: 채널 최근 게시글 중 첫 번째. (새 글을 만들지 않음)
    r_posts = client.get(f"/channels/{channel_id}/posts", params={"per_page": 5})
    post_id = None
    if r_posts.ok and isinstance(r_posts.data, dict):
        order = r_posts.data.get("order") or []
        if order:
            post_id = order[0]
    if not post_id:
        report.add(CheckResult("R-1 사전 리액션 스냅샷", "GET /posts/{post_id}/reactions",
                               False, None, "대상 게시글이 없음 (채널에 게시글 필요)",
                               web_url, None, "채널에 최소 1개 게시글 필요", 0))
        report.add(CheckResult("R-2 리액션 추가", "POST /reactions",
                               False, None, "대상 게시글 없음 — 스킵",
                               None, None, None, 0))
        report.add(CheckResult("R-3 추가 후 재조회", "GET /posts/{post_id}/reactions",
                               False, None, "대상 게시글 없음 — 스킵",
                               None, None, None, 0))
        report.add(CheckResult("R-4 리액션 정리(삭제)", "DELETE /users/me/posts/{post_id}/reactions/{emoji}",
                               False, None, "대상 게시글 없음 — 스킵",
                               None, None, None, 0))
        _finalize(report)
        return

    print(f"대상 게시글: {post_id}\n")

    # R-1 사전 리액션 스냅샷
    r = client.get(f"/posts/{post_id}/reactions")
    summary = "리액션 목록 조회 실패"
    sample = None
    before_count = 0
    if r.ok:
        # Mattermost 는 빈 리액션 목록을 [] 가 아니라 빈 본문/None 으로 반환할 수 있다.
        # ok=True 면 일단 성공으로 처리하고, list 일 때만 샘플을 채운다.
        reactions = r.data if isinstance(r.data, list) else []
        before_count = len(reactions)
        sample = _reaction_rows(reactions) if reactions else None
        summary = f"사전 리액션 {before_count}개"
    report.add(CheckResult("R-1 사전 리액션 스냅샷",
                           f"GET /posts/{post_id}/reactions",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    # R-2 리액션 추가.
    # POST /reactions 의 body user_id 는 실제 사용자 ID 여야 한다. (path 의 me
    # 리터럴과 달리 body 필드에서는 me 가 허용되지 않는다 — 400 확인됨)
    # 따라서 /users/me 로 현재 사용자 id 를 먼저 조회한다.
    r_me = client.get("/users/me")
    me_id = r_me.data.get("id") if (r_me.ok and isinstance(r_me.data, dict)) else None
    if not me_id:
        report.add(CheckResult(f"R-2 리액션 추가 (:{TEST_EMOJI}:)",
                               "POST /reactions",
                               False, None, "현재 사용자 ID 조회 실패 — 추가 스킵",
                               web_url, None, r_me.error, r_me.elapsed_ms))
        report.add(CheckResult("R-3 추가 후 재조회",
                               f"GET /posts/{post_id}/reactions",
                               False, None, "사용자 ID 없음 — 스킵",
                               None, None, None, 0))
        report.add(CheckResult("R-4 리액션 정리(삭제)",
                               f"DELETE /users/me/posts/{post_id}/reactions/{TEST_EMOJI}",
                               False, None, "사용자 ID 없음 — 스킵",
                               None, None, None, 0))
        _finalize(report)
        return

    r = client.post("/reactions", json_body={
        "user_id": me_id,
        "post_id": post_id,
        "emoji_name": TEST_EMOJI,
    })
    summary = "리액션 추가 실패"
    sample = None
    added = False
    if r.ok and isinstance(r.data, dict):
        added = True
        sample = {"post_id": r.data.get("post_id"),
                  "user_id": r.data.get("user_id"),
                  "emoji_name": r.data.get("emoji_name")}
        summary = f"추가 성공 emoji=:{TEST_EMOJI}: post={post_id}"
        print(f"  [POC-TEST] 리액션 추가 :{TEST_EMOJI}: → post {post_id}")
    report.add(CheckResult(f"R-2 리액션 추가 (:{TEST_EMOJI}:)",
                           "POST /reactions",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    # R-3 추가 후 재조회 (반영 확인)
    r = client.get(f"/posts/{post_id}/reactions")
    summary = "재조회 실패"
    sample = None
    if r.ok:
        reactions = r.data if isinstance(r.data, list) else []
        sample = _reaction_rows(reactions) if reactions else None
        # 방금 추가한 이모지가 목록에 있는지 확인.
        has_mine = any((rx.get("emoji_name") == TEST_EMOJI) for rx in reactions)
        summary = (f"리액션 {len(reactions)}개 (사전 {before_count}개 → {len(reactions)}개, "
                   f"추가 반영 {'확인' if has_mine else '미확인'})")
    report.add(CheckResult("R-3 추가 후 재조회",
                           f"GET /posts/{post_id}/reactions",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    # R-4 정리: 테스트가 추가한 리액션 삭제 (원 상태 복구).
    if not added:
        report.add(CheckResult("R-4 리액션 정리(삭제)",
                               f"DELETE /users/me/posts/{post_id}/reactions/{TEST_EMOJI}",
                               False, None, "추가 실패 — 삭제 스킵",
                               None, None, None, 0))
    else:
        r = client.delete(f"/users/me/posts/{post_id}/reactions/{TEST_EMOJI}")
        summary = "삭제 실패"
        sample = None
        if r.ok:
            sample = {"status": r.data.get("status") if isinstance(r.data, dict) else "ok"}
            summary = f"삭제 성공 (:{TEST_EMOJI}: 제거, 원 상태 복구)"
            print(f"  [POC-TEST] 리액션 삭제 :{TEST_EMOJI}: ← 정리 완료")
        report.add(CheckResult("R-4 리액션 정리(삭제)",
                               f"DELETE /users/me/posts/{post_id}/reactions/{TEST_EMOJI}",
                               r.ok, r.status, summary, web_url, sample,
                               r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
