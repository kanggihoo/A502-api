"""팀·채널 운영 + 대시보드 정보 집계용 읽기 전용 API 검증.

통합 워크스페이스가 "팀 운영" 과 "대시보드 집계" 목적으로 사용할 GET 엔드포인트들을
실제 PAT 로 호출해 본다. 이 스크립트는 어떤 리소스도 생성/수정/삭제하지 않는다.

검증 항목:
  채널 운영/집계
    C-1 GET /channels/{channel_id}/stats              채널 멤버 수 (read_channel)
    C-2 GET /channels/{channel_id}/members             채널 멤버 목록 (msg_count/mention_count 포함)
    C-5 GET /channels/{channel_id}/pinned              pinned posts (북마크 501 대안)
    C-6 GET /users/me/channels/{channel_id}/unread     채널 unread/mention 카운트
  팀 운영/집계
    C-3 GET /teams/{team_id}/stats                     팀 전체 멤버 수 (view_team)
    C-4 GET /teams/{team_id}/members                   팀 멤버 목록
    C-7 GET /users/me/teams/{team_id}/unread           팀 단위 unread/mention 집계

설계 참고:
- members 응답에는 user_id/roles/msg_count/mention_count 가 포함된다. 사용자 상세
  (username 등)까지 필요하면 별도 GET /users?in_channel={channel_id} 로 조인한다.
- 북마크(501)의 대안으로 API_RESTRICTIONS.md 에서 제시한 pinned posts 를 검증한다.
  404/빈 결과는 "고정 메시지 없음" 으로 해석한다.

실행:  uv run python test_team_channel_ops_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from mattermost_client import (
    CheckResult,
    Config,
    MattermostClient,
    Report,
    channel_web_url,
    load_config,
)


def _member_rows(members: list, limit: int = 5) -> list[dict]:
    """채널/팀 members 응답을 요약 샘플로 변환."""
    rows = []
    for m in members[:limit]:
        rows.append({
            "user_id": m.get("user_id"),
            "roles": m.get("roles") or m.get("explicit_roles"),
            "msg_count": m.get("msg_count"),
            "mention_count": m.get("mention_count"),
            "scheme_admin": m.get("scheme_admin"),
        })
    return rows


def _post_ids(order: list, limit: int = 5) -> list[str]:
    """pinned posts 의 order(=post id 리스트)를 잘라서 반환."""
    return [pid for pid in (order or [])[:limit]]


def main() -> None:
    cfg: Config = load_config()
    client = MattermostClient(cfg)
    report = Report(title="팀·채널 운영 읽기 전용 API 검증", base_url=cfg.base_url)

    print(f"Mattermost: {cfg.base_url}")
    print(f"대상 팀: {cfg.team_id or '(자동 탐지)'} / 채널: {cfg.channel_id or '(자동 탐지)'}")
    print("-" * 60)

    # 대상 팀/채널 확정.
    _, team_id = client.resolve_team()
    if not team_id:
        report.add(CheckResult("대상 확정", "GET /users/me/teams", False, None,
                               "대상 팀을 찾을 수 없음", None, None,
                               "MATTERMOST_TEST_TEAM_ID 확인 또는 소속 팀 확인", 0))
        _finalize(report)
        return
    _, channel_id = client.resolve_channel(team_id)
    if not channel_id:
        report.add(CheckResult("대상 확정", "GET /users/me/teams/{team_id}/channels", False, None,
                               "대상 채널을 찾을 수 없음", None, None,
                               "MATTERMOST_TEST_CHANNEL_ID 확인 또는 팀 멤버십 확인", 0))
        _finalize(report)
        return

    # 원문 URL 조립용 team_name/channel_name.
    r_team = client.get(f"/teams/{team_id}")
    r_ch = client.get(f"/channels/{channel_id}")
    team_name = r_team.data.get("name") if (r_team.ok and isinstance(r_team.data, dict)) else ""
    channel_name = r_ch.data.get("name") if (r_ch.ok and isinstance(r_ch.data, dict)) else ""
    web_url = channel_web_url(cfg.base_url, team_name, channel_name) if (team_name and channel_name) else None

    print(f"대상: team={team_name}({team_id}) channel={channel_name}({channel_id})\n")

    # ========================================================================
    # 채널 운영/집계
    # ========================================================================
    print("[채널 운영/집계]")

    # C-1 채널 통계(멤버 수)
    r = client.get(f"/channels/{channel_id}/stats")
    summary = "채널 통계 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        sample = {"channel_id": r.data.get("channel_id"),
                  "member_count": r.data.get("member_count")}
        summary = f"멤버 수 {r.data.get('member_count')}"
    report.add(CheckResult("C-1 채널 멤버 수(stats)",
                           f"GET /channels/{channel_id}/stats",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    # C-2 채널 멤버 목록
    r = client.get(f"/channels/{channel_id}/members",
                   params={"per_page": cfg.per_page})
    summary = "채널 멤버 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        sample = _member_rows(r.data)
        summary = f"채널 멤버 {len(r.data)}명"
    report.add(CheckResult("C-2 채널 멤버 목록",
                           f"GET /channels/{channel_id}/members",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    # C-5 채널 pinned posts (북마크 대안)
    r = client.get(f"/channels/{channel_id}/pinned")
    summary = "pinned posts 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        order = r.data.get("order") or []
        sample = {"pinned_post_ids": _post_ids(order), "count": len(order)}
        summary = f"pinned posts {len(order)}개"
    elif r.status == 404:
        summary = "404 — pinned posts 없음 또는 채널 비공개 접근 권한 확인"
    report.add(CheckResult("C-5 채널 pinned posts (북마크 대안)",
                           f"GET /channels/{channel_id}/pinned",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    # C-6 채널 unread 카운트
    r = client.get(f"/users/me/channels/{channel_id}/unread")
    summary = "채널 unread 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        sample = {"channel_id": r.data.get("channel_id"),
                  "msg_count": r.data.get("msg_count"),
                  "mention_count": r.data.get("mention_count")}
        summary = (f"unread msg={r.data.get('msg_count')} "
                   f"mention={r.data.get('mention_count')}")
    report.add(CheckResult("C-6 채널 unread 카운트",
                           f"GET /users/me/channels/{channel_id}/unread",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # 팀 운영/집계
    # ========================================================================
    print("\n[팀 운영/집계]")

    # C-3 팀 통계(전체 멤버 수)
    r = client.get(f"/teams/{team_id}/stats")
    summary = "팀 통계 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        sample = {"team_id": r.data.get("team_id"),
                  "total_member_count": r.data.get("total_member_count")}
        summary = f"팀 전체 멤버 수 {r.data.get('total_member_count')}"
    report.add(CheckResult("C-3 팀 전체 멤버 수(stats)",
                           f"GET /teams/{team_id}/stats",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # C-4 팀 멤버 목록
    r = client.get(f"/teams/{team_id}/members",
                   params={"per_page": cfg.per_page})
    summary = "팀 멤버 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        sample = _member_rows(r.data)
        summary = f"팀 멤버 {len(r.data)}명"
    report.add(CheckResult("C-4 팀 멤버 목록",
                           f"GET /teams/{team_id}/members",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # C-7 팀 unread/mention 집계
    r = client.get(f"/users/me/teams/{team_id}/unread")
    summary = "팀 unread 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        sample = {"team_id": r.data.get("team_id"),
                  "msg_count": r.data.get("msg_count"),
                  "mention_count": r.data.get("mention_count")}
        summary = (f"팀 unread msg={r.data.get('msg_count')} "
                   f"mention={r.data.get('mention_count')}")
    report.add(CheckResult("C-7 팀 unread/mention 집계",
                           f"GET /users/me/teams/{team_id}/unread",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
