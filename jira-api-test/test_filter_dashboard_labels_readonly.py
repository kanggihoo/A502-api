"""필터·대시보드·라벨 조회용 읽기 전용 Jira API 검증.

통합 워크스페이스가 팀이 합의한 JQL 을 재사용하고, Jira 원문 대시보드와 연결하기
위해 필요한 메타를 검증한다. 이 스크립트는 어떤 리소스도 생성/수정/삭제하지 않는다.

검증 항목:
  FL-1 GET /filter/search?expand=jql         저장 필터 전체(favourite 말고)
  FL-2 GET /filter/{id}                       필터 상세(JQL 포함) — FL-1 에서 id 확보
  FL-3 GET /dashboard/{id}                    대시보드 상세(gadgets) — /dashboard 에서 id 확보
  FL-4 GET /label                             라벨 목록

설계 원칙:
- 빈 결과(0개)도 ok=True. "지금 데이터가 없을 뿐" 과 "API 가 막혀 있는지" 구분.
- FL-2/FL-3 은 선행 목록에서 id 를 확보 못하면 "스킵" CheckResult 로 기록.

실행:  uv run python test_filter_dashboard_labels_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from jira_client import (
    CheckResult,
    Config,
    JiraClient,
    Report,
    load_config,
)


def _skip(name: str, endpoint: str, reason: str) -> CheckResult:
    return CheckResult(name, endpoint, ok=False, status=None,
                       summary=reason, web_url=None, sample=None,
                       error=None, elapsed_ms=0)


def main() -> None:
    cfg: Config = load_config()
    client = JiraClient(cfg)
    report = Report(title="필터·대시보드·라벨 읽기 전용 API 검증",
                    base_url=cfg.base_url)

    print(f"Jira: {cfg.base_url} (cloud_id={cfg.cloud_id[:8]}...)")
    print("-" * 60)

    # ========================================================================
    # FL-1 저장 필터 전체 (favourite 아님, JQL 포함)
    # ========================================================================
    r = client.get("/filter/search",
                   params={"expand": "jql",
                           "maxResults": cfg.max_results})
    summary = "필터 검색 실패"
    sample = None
    filter_id = None
    filter_web = None
    if r.ok and isinstance(r.data, dict):
        values = r.data.get("values") or []
        rows = []
        for f in values[:10]:
            rows.append({
                "id": f.get("id"),
                "name": f.get("name"),
                "owner": (f.get("owner") or {}).get("displayName"),
                "jql": (f.get("jql") or "")[:80],
                "favourite": f.get("favourite"),
                "shared": bool(f.get("sharePermissions")),
            })
        sample = rows
        summary = f"저장 필터 {len(values)}개 (total={r.data.get('total')})"
        if values:
            filter_id = values[0].get("id")
    report.add(CheckResult("FL-1 저장 필터 (/filter/search)",
                           "GET /filter/search?expand=jql",
                           r.ok, r.status, summary, filter_web, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # FL-2 필터 상세 (JQL 포함)
    # ========================================================================
    if not filter_id:
        report.add(_skip("FL-2 필터 상세",
                         "GET /filter/{id}", "저장 필터 없음 — FL-2 스킵"))
    else:
        r = client.get(f"/filter/{filter_id}")
        summary = "필터 상세 조회 실패"
        sample = None
        if r.ok and isinstance(r.data, dict):
            sample = {
                "id": r.data.get("id"),
                "name": r.data.get("name"),
                "jql": r.data.get("jql"),
                "description": (r.data.get("description") or "")[:80],
                "owner": (r.data.get("owner") or {}).get("displayName"),
            }
            summary = (f"필터 id={r.data.get('id')} name={r.data.get('name')!r} "
                       f"jql={r.data.get('jql')!r}")
        report.add(CheckResult("FL-2 필터 상세",
                               f"GET /filter/{filter_id}",
                               r.ok, r.status, summary, None, sample,
                               r.error, r.elapsed_ms))

    # ========================================================================
    # FL-3 대시보드 상세 — 먼저 /dashboard 목록에서 id 확보
    # ========================================================================
    r_list = client.get("/dashboard",
                        params={"maxResults": cfg.max_results})
    dashboard_id = None
    if r_list.ok and isinstance(r_list.data, dict):
        dashes = r_list.data.get("dashboards") or []
        if dashes:
            dashboard_id = dashes[0].get("id")

    if not dashboard_id:
        report.add(_skip("FL-3 대시보드 상세",
                         "GET /dashboard/{id}", "접근 가능 대시보드 없음 — FL-3 스킵"))
    else:
        r = client.get(f"/dashboard/{dashboard_id}")
        summary = "대시보드 상세 조회 실패"
        sample = None
        if r.ok and isinstance(r.data, dict):
            gadgets = r.data.get("gadgets") or []
            rows = [{"id": g.get("id"), "module_key": g.get("moduleKey"),
                     "title": g.get("title")} for g in gadgets[:10]]
            sample = {
                "id": r.data.get("id"),
                "name": r.data.get("name"),
                "view": r.data.get("view"),
                "gadgets_count": len(gadgets),
                "gadgets_sample": rows,
            }
            summary = (f"대시보드 id={r.data.get('id')} name={r.data.get('name')!r} "
                       f"gadgets {len(gadgets)}개")
        report.add(CheckResult("FL-3 대시보드 상세",
                               f"GET /dashboard/{dashboard_id}",
                               r.ok, r.status, summary, None, sample,
                               r.error, r.elapsed_ms))

    # ========================================================================
    # FL-4 라벨 목록
    # ========================================================================
    r = client.get("/label", params={"maxResults": cfg.max_results})
    summary = "라벨 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        tokens = r.data.get("tokens") or []
        rows = []
        for t in tokens[:15]:
            # Jira label 은 보통 {"id":..., "label":"..."} 형식. 키 유연 처리.
            label_val = t.get("label") or t.get("name") or t.get("id")
            rows.append({"id": t.get("id"), "label": label_val})
        sample = rows
        total = r.data.get("total")
        summary = f"라벨 {len(tokens)}개 표시 (total={total})"
    report.add(CheckResult("FL-4 라벨 (/label)",
                           "GET /label",
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
