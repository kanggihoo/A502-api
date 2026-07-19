"""P0 읽기 전용 Mattermost API 동작 검증.

api-docs/mattermost-api-priority-filter.md 의 "첫 API 검증 순서" 1, 3단계(GET만)를
실제 PAT 로 호출해 본다. 이 스크립트는 어떤 리소스도 생성/수정/삭제하지 않는다.

검증 항목:
  1단계 - 토큰 정체·소속 팀·채널 확인
    1-1 GET /users/me                            현재 사용자
    1-2 GET /users/me/teams                       소속 팀 목록(대상 탐지)
    1-3 GET /teams/{team_id}                      대상 팀 상세
    1-4 GET /users/me/teams/{team_id}/channels    팀 채널 목록
    1-5 GET /channels/{channel_id}                대상 채널 상세
  3단계 - 대화 맥락 (게시글·스레드·봇·상태·북마크)
    3-1 GET /channels/{channel_id}/posts          채널 최근 게시글
    3-2 GET /posts/{post_id}/thread               스레드 조회
    3-3 GET /users/me/status                      현재 사용자 상태
    3-4 GET /bots                                 bot 계정 가용성
    3-5 GET /channels/{channel_id}/bookmarks      채널 북마크(v9.5+)

실행:  uv run python test_p0_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from mattermost_client import (
    ApiResponse,
    CheckResult,
    Config,
    MattermostClient,
    Report,
    channel_web_url,
    load_config,
)


def _post_rows(order: list, posts: dict, limit: int = 5) -> list[dict]:
    """posts 응답의 {order:[ids], posts:{id:post}} 를 요약 샘플로 변환."""
    rows = []
    for pid in order[:limit]:
        p = posts.get(pid, {}) if isinstance(posts, dict) else {}
        rows.append({
            "id": p.get("id"),
            "message": (p.get("message") or "")[:60],
            "user_id": p.get("user_id"),
            "create_at": p.get("create_at"),
            "root_id": p.get("root_id"),
        })
    return rows


def main() -> None:
    cfg: Config = load_config()
    client = MattermostClient(cfg)
    report = Report(title="P0 읽기 전용 API 검증", base_url=cfg.base_url)

    print(f"Mattermost: {cfg.base_url}")
    print(f"대상 팀: {cfg.team_id or '(자동 탐지)'} / 채널: {cfg.channel_id or '(자동 탐지)'}")
    print("-" * 60)

    # ---- 1단계: 토큰 정체·소속 팀·채널 확인 --------------------------------
    print("\n[1단계] 토큰 정체·소속 팀·채널 확인")

    # 1-1 현재 사용자
    r = client.get("/users/me")
    summary = "사용자 조회 실패"
    sample = None
    me_id = None
    if r.ok and isinstance(r.data, dict):
        me = r.data
        me_id = me.get("id")
        summary = (f"@{me.get('username')} ({me.get('email') or '이메일 숨김'}) "
                   f"roles={me.get('roles')}")
        sample = {"id": me.get("id"), "username": me.get("username"),
                  "email": me.get("email"), "roles": me.get("roles")}
    report.add(CheckResult("1-1 현재 사용자", "GET /users/me", r.ok, r.status,
                           summary, None, sample, r.error, r.elapsed_ms))

    # 1-2 소속 팀 목록
    r_teams = client.get("/users/me/teams", params={"per_page": cfg.per_page})
    sample = None
    if r_teams.ok and isinstance(r_teams.data, list):
        sample = [{"id": t.get("id"), "name": t.get("name"),
                   "display_name": t.get("display_name"),
                   "type": t.get("type")} for t in r_teams.data[:5]]
        summary = f"소속 팀 {len(r_teams.data)}개"
    else:
        summary = "팀 목록 조회 실패"
    report.add(CheckResult("1-2 소속 팀 목록", "GET /users/me/teams",
                           r_teams.ok, r_teams.status, summary,
                           None, sample, r_teams.error, r_teams.elapsed_ms))

    # 대상 팀 확정
    detect_resp, team_id = client.resolve_team()
    if not team_id:
        report.add(CheckResult(
            "1-3 대상 팀 상세", "GET /teams/{team_id}", False, None,
            "대상 팀을 찾을 수 없음 (MATTERMOST_TEST_TEAM_ID 설정 또는 소속 확인)",
            None, None, detect_resp.error or "팀 미확정", 0))
        _finalize(report)
        return

    # 1-3 대상 팀 상세
    r = client.get(f"/teams/{team_id}")
    summary = "팀 상세 조회 실패"
    team_name = None
    sample = None
    if r.ok and isinstance(r.data, dict):
        t = r.data
        team_name = t.get("name")
        summary = (f"{t.get('name')} ({t.get('display_name')}) "
                   f"type={t.get('type')} open_invite={t.get('allow_open_invite')}")
        sample = {"id": t.get("id"), "name": t.get("name"),
                  "display_name": t.get("display_name"), "type": t.get("type")}
    report.add(CheckResult("1-3 대상 팀 상세", f"GET /teams/{team_id}",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # 1-4 팀 채널 목록 (사용자 스코프)
    r_chs = client.get(f"/users/me/teams/{team_id}/channels")
    sample = None
    channel_id_for_pick = None
    channel_name_for_url = None
    if r_chs.ok and isinstance(r_chs.data, list):
        rows = [{"id": c.get("id"), "name": c.get("name"),
                 "display_name": c.get("display_name"),
                 "type": c.get("type")} for c in r_chs.data if c.get("type") in ("O", "P")][:8]
        sample = rows
        summary = f"채널 {len(r_chs.data)}개 (일반 O/P {len(rows)}개)"
    else:
        summary = "채널 목록 조회 실패"
    report.add(CheckResult("1-4 팀 채널 목록",
                           f"GET /users/me/teams/{team_id}/channels",
                           r_chs.ok, r_chs.status, summary,
                           None, sample, r_chs.error, r_chs.elapsed_ms))

    # 대상 채널 확정
    detect_ch, channel_id = client.resolve_channel(team_id)
    if not channel_id:
        report.add(CheckResult(
            "1-5 대상 채널 상세", "GET /channels/{channel_id}", False, None,
            "대상 채널을 찾을 수 없음 (MATTERMOST_TEST_CHANNEL_ID 설정 또는 팀 멤버십 확인)",
            None, None, detect_ch.error or "채널 미확정", 0))
        _finalize(report)
        return

    # 1-5 대상 채널 상세
    r = client.get(f"/channels/{channel_id}")
    summary = "채널 상세 조회 실패"
    web_url = None
    sample = None
    if r.ok and isinstance(r.data, dict):
        c = r.data
        channel_name_for_url = c.get("name")
        summary = (f"{c.get('name')} ({c.get('display_name')}) "
                   f"type={c.get('type')} msgs={c.get('total_msg_count')}")
        if team_name and channel_name_for_url:
            web_url = channel_web_url(cfg.base_url, team_name, channel_name_for_url)
        sample = {"id": c.get("id"), "name": c.get("name"),
                  "display_name": c.get("display_name"),
                  "type": c.get("type"),
                  "total_msg_count": c.get("total_msg_count")}
    report.add(CheckResult("1-5 대상 채널 상세", f"GET /channels/{channel_id}",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # ---- 3단계: 대화 맥락 (게시글·스레드·봇·상태·북마크) --------------------
    print("\n[3단계] 대화 맥락 (게시글·스레드·봇·상태·북마크)")

    # 3-1 채널 최근 게시글
    r = client.get(f"/channels/{channel_id}/posts",
                   params={"per_page": cfg.per_page})
    summary = "게시글 조회 실패"
    sample = None
    sample_post_id = None
    if r.ok and isinstance(r.data, dict):
        order = r.data.get("order") or []
        posts = r.data.get("posts") or {}
        sample = _post_rows(order, posts)
        sample_post_id = order[0] if order else None
        summary = f"게시글 {len(order)}개"
    report.add(CheckResult("3-1 채널 최근 게시글",
                           f"GET /channels/{channel_id}/posts",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    # 3-2 스레드 조회 (게시글이 있을 때)
    if sample_post_id:
        r = client.get(f"/posts/{sample_post_id}/thread")
        summary = "스레드 조회 실패"
        sample = None
        if r.ok and isinstance(r.data, dict):
            order = r.data.get("order") or []
            posts = r.data.get("posts") or {}
            sample = _post_rows(order, posts)
            summary = f"스레드 게시글 {len(order)}개"
        report.add(CheckResult("3-2 스레드 조회",
                               f"GET /posts/{sample_post_id}/thread",
                               r.ok, r.status, summary, web_url, sample,
                               r.error, r.elapsed_ms))
    else:
        report.add(CheckResult("3-2 스레드 조회", "GET /posts/{post_id}/thread",
                               False, None, "조회할 게시글이 없음",
                               None, None, None, 0))

    # 3-3 현재 사용자 상태
    r = client.get("/users/me/status")
    summary = "상태 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        s = r.data
        summary = f"status={s.get('status')} (마지막 활동: {s.get('last_activity_at')})"
        sample = {"status": s.get("status"),
                  "last_activity_at": s.get("last_activity_at")}
    report.add(CheckResult("3-3 현재 사용자 상태", "GET /users/me/status",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # 3-4 bot 계정 가용성
    r = client.get("/bots", params={"per_page": cfg.per_page})
    summary = "bot 목록 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = [{"user_id": b.get("user_id"), "username": b.get("username"),
                 "display_name": b.get("display_name"),
                 "owner_id": b.get("owner_id")} for b in r.data[:5]]
        summary = f"bot {len(r.data)}개"
        sample = rows
    report.add(CheckResult("3-4 bot 계정 가용성", "GET /bots",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # 3-5 채널 북마크 (v9.5+)
    r = client.get(f"/channels/{channel_id}/bookmarks")
    summary = "북마크 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = [{"id": b.get("bookmark_id") or b.get("id"),
                 "type": b.get("type"),
                 "title": b.get("title")} for b in r.data[:5]]
        summary = f"북마크 {len(r.data)}개"
        sample = rows
    elif r.status == 404:
        summary = "404 — 북마크 기능 비활성화 또는 서버 버전 < 9.5"
    report.add(CheckResult("3-5 채널 북마크",
                           f"GET /channels/{channel_id}/bookmarks",
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
