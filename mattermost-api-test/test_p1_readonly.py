"""P1 읽기 전용 Mattermost API 동작 검증.

api-docs/mattermost-api-priority-filter.md 의 P1 카테고리 중 검색·명령·플레이북
가용성을 확인한다. 이 스크립트는 어떤 리소스도 생성/수정/삭제하지 않는다.

P0(test_p0_readonly.py)가 핵심 대화 맥락이라면,
P1은 팀 운영 편의 기능(검색·슬래시 명령·플레이북)의 가용성을 점검한다.

검증 항목:
  4단계 - 검색 가용성
    4-1 POST /teams/search                    팀 검색
    4-2 POST /teams/{team_id}/channels/search 채널 검색(팀 스코프)
    4-3 POST /teams/{team_id}/posts/search    게시글 검색
  5단계 - 명령·플레이북 가용성
    5-1 GET /commands?team_id={team_id}       슬래시 명령 목록
    5-2 GET /plugins/playbooks/api/v0/playbooks  플레이북(플러그인, 404 예상 가능)

설계 원칙 (P0 검증으로 확정):
- 데이터가 비어 있어도(0개) API 정상 응답이면 ok=True. "지금 데이터가 없을 뿐"
  인지와 "API가 막혀 있는지/기능이 비활성화"를 구분하는 것이 목적.
- playbooks는 플러그인 API(/plugins/playbooks/api/v0)이므로 비활성화 시 404 가능.

실행:  uv run python test_p1_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from mattermost_client import (
    ApiResponse,
    CheckResult,
    Config,
    MattermostClient,
    Report,
    load_config,
)


def _search_summary(r: ApiResponse, label: str = "항목") -> tuple[str, list | None]:
    """검색/목록 응답을 (개수 요약, 샘플) 로 정리."""
    if not r.ok or r.data is None:
        return f"{label} 조회 실패", None
    items = r.data if isinstance(r.data, list) else []
    sample = [{"id": it.get("id"), "name": it.get("name") or it.get("display_name")}
              for it in items[:5]]
    return f"{label} {len(items)}개", sample or None


def main() -> None:
    cfg: Config = load_config()
    client = MattermostClient(cfg)
    report = Report(title="P1 읽기 전용 API 검증", base_url=cfg.base_url)

    print(f"Mattermost: {cfg.base_url}")
    print(f"대상 팀: {cfg.team_id or '(자동 탐지)'}")
    print("-" * 60)

    # 대상 팀 확정 (P0와 동일 로직).
    detect_resp, team_id = client.resolve_team()
    if not team_id:
        report.add(CheckResult(
            "대상 팀 확정", "GET /users/me/teams", False, None,
            "대상 팀을 찾을 수 없음", None, None,
            detect_resp.error or "팀 미확정"))
        _finalize(report)
        return

    print(f"대상 확정: team={team_id}\n")

    # ---- 4단계: 검색 가용성 ------------------------------------------------
    print("[4단계] 검색 가용성")

    # 4-1 팀 검색
    r = client.post("/teams/search", json_body={"term": "", "page": 0, "per_page": cfg.per_page})
    summary, sample = _search_summary(r, "팀")
    if not r.ok:
        summary = "팀 검색 실패"
    report.add(CheckResult("4-1 팀 검색", "POST /teams/search",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # 4-2 채널 검색 (팀 스코프)
    r = client.post(f"/teams/{team_id}/channels/search",
                    json_body={"not_associated_to_group": "", "page": 0, "per_page": cfg.per_page})
    summary, sample = _search_summary(r, "채널")
    if not r.ok:
        summary = "채널 검색 실패"
    report.add(CheckResult(f"4-2 채널 검색 (team={team_id})",
                           f"POST /teams/{team_id}/channels/search",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # 4-3 게시글 검색
    r = client.post(f"/teams/{team_id}/posts/search",
                    json_body={"terms": "", "is_or_search": False, "page": 0, "per_page": cfg.per_page})
    summary = "게시글 검색 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        order = r.data.get("order") or []
        posts = r.data.get("posts") or {}
        rows = [{"id": posts.get(pid, {}).get("id"),
                 "message": (posts.get(pid, {}).get("message") or "")[:50]}
                for pid in order[:5]]
        summary = f"검색 결과 {len(order)}개"
        sample = rows
    report.add(CheckResult(f"4-3 게시글 검색 (team={team_id})",
                           f"POST /teams/{team_id}/posts/search",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # ---- 5단계: 명령·플레이북 가용성 ---------------------------------------
    print("\n[5단계] 명령·플레이북 가용성")

    # 5-1 슬래시 명령 목록
    r = client.get("/commands", params={"team_id": team_id, "custom_only": "false"})
    summary = "명령 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = [{"id": c.get("id") or c.get("trigger"),
                 "trigger": c.get("trigger"),
                 "display_name": c.get("display_name"),
                 "auto_complete": c.get("auto_complete")} for c in r.data[:8]]
        summary = f"슬래시 명령 {len(r.data)}개"
        sample = rows
    report.add(CheckResult(f"5-1 슬래시 명령 (team={team_id})",
                           "GET /commands?team_id={team_id}",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # 5-2 플레이북 (플러그인 API). 비활성화 시 404 예상.
    r = client.get("/plugins/playbooks/api/v0/playbooks",
                   params={"team_id": team_id, "page": 0, "per_page": cfg.per_page})
    summary = "플레이북 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = [{"id": pb.get("id"), "title": pb.get("title"),
                 "team_id": pb.get("team_id")} for pb in r.data[:5]]
        summary = f"플레이북 {len(r.data)}개"
        sample = rows
    elif r.status == 404:
        summary = "404 — 플레이북 플러그인 비활성화 (예상 가능)"
    report.add(CheckResult("5-2 플레이북 가용성",
                           "GET /plugins/playbooks/api/v0/playbooks",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
