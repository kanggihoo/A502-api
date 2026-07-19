"""P1 읽기 전용 Jira Cloud API 동작 검증.

api-docs/jira-api-priority-filter.md 의 P1 카테고리 중 GET(읽기) 위주 후보를
실제 PAT 로 호출해 본다. 이 스크립트는 어떤 리소스도 생성/수정/삭제하지 않는다.

P0(test_p0_readonly.py)가 대시보드 핵심 데이터라면,
P1은 프로젝트 운영·분류 지원에 유용한 보조 데이터를 검증한다.

검증 항목 (대부분 프로젝트 스코프):
  4단계 - 분류 체계 (우선순위·이슈타입)
    4-1 GET /priority                    우선순위
    4-2 GET /issuetype                   이슈 타입
  5단계 - 프로젝트 분류 (컴포넌트·버전)
    5-1 GET /component?projectIds=...    프로젝트 컴포넌트(기능 영역)
    5-2 GET /project/{key}/versions      프로젝트 버전(배포 버전)
  6단계 - 대시보드·JQL 검증 (집계 후보)
    6-1 GET /dashboard                   대시보드 목록
    6-2 POST /jql/parse                  JQL 유효성 사전 점검

설계 원칙 (P0 검증으로 확정):
- 데이터가 비어 있어도(0개) API 정상 응답이면 ok=True. "지금 데이터가 없을 뿐"
  인지와 "API가 막혀 있는지"를 구분하는 것이 목적.

실행:  uv run python test_p1_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from jira_client import (
    ApiResponse,
    CheckResult,
    Config,
    JiraClient,
    Report,
    load_config,
    project_web_url,
)


def _count_of(r: ApiResponse, list_keys: tuple[str, ...] = ("values",)) -> int:
    """응답에서 리스트 길이를 추출. Jira는 list 또는 {values:[...]} 형태를 섞어 쓴다."""
    if not r.ok or r.data is None:
        return 0
    if isinstance(r.data, list):
        return len(r.data)
    if isinstance(r.data, dict):
        for k in list_keys:
            v = r.data.get(k)
            if isinstance(v, list):
                return len(v)
    return 0


def _name_url_sample(r: ApiResponse, name_key: str = "name",
                     url_key: str = "self", limit: int = 5) -> tuple[str, list | None]:
    """list/values 응답을 (개수 요약, 샘플) 로 정리. 공통 패턴."""
    if not r.ok or r.data is None:
        return "조회 실패", None
    items = r.data if isinstance(r.data, list) else []
    if not items and isinstance(r.data, dict):
        for k in ("values",):
            v = r.data.get(k)
            if isinstance(v, list):
                items = v
                break
    sample = []
    for it in items[:limit]:
        row = {}
        for nk in (name_key, "name", "title"):
            v = it.get(nk)
            if v is not None:
                row[name_key] = v
                break
        if url_key in it:
            row[url_key] = it[url_key]
        sample.append(row)
    return f"{len(items)}개", sample or None


def main() -> None:
    cfg: Config = load_config()
    client = JiraClient(cfg)
    report = Report(title="P1 읽기 전용 API 검증", base_url=cfg.base_url)

    print(f"Jira: {cfg.base_url}")
    print(f"대상 프로젝트: {cfg.project_key or '(자동 탐지)'}")
    print("-" * 60)

    # 대상 프로젝트 확정 (P0와 동일 로직).
    detect_resp, project_key = client.resolve_project()
    if not project_key:
        report.add(CheckResult(
            "대상 프로젝트 확정", "GET /project/search", False, None,
            "대상 프로젝트를 찾을 수 없음", None, None,
            detect_resp.error or "프로젝트 미확정"))
        _finalize(report)
        return

    print(f"대상 확정: {project_key}\n")

    # ---- 4단계: 분류 체계 (우선순위·이슈타입) --------------------------
    print("[4단계] 분류 체계 (우선순위·이슈타입)")

    # 4-1 우선순위
    r = client.get("/priority")
    summary, sample = "우선순위 조회 실패", None
    if r.ok:
        items = r.data if isinstance(r.data, list) else []
        rows = [{"name": p.get("name"), "id": p.get("id")} for p in items[:8]]
        summary = f"우선순위 {len(items)}개"
        sample = rows
    report.add(CheckResult("4-1 우선순위", "GET /priority",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # 4-2 이슈 타입
    r = client.get("/issuetype")
    summary, sample = "이슈 타입 조회 실패", None
    if r.ok:
        items = r.data if isinstance(r.data, list) else []
        rows = [{"name": it.get("name"), "id": it.get("id"),
                 "subtask": it.get("subtask")} for it in items[:8]]
        summary = f"이슈 타입 {len(items)}개"
        sample = rows
    report.add(CheckResult("4-2 이슈 타입", "GET /issuetype",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # ---- 5단계: 프로젝트 분류 (컴포넌트·버전) --------------------------------
    print("\n[5단계] 프로젝트 분류 (컴포넌트·버전)")

    # 5-1 프로젝트 컴포넌트. /component 는 projectIds 쿼리 파라미터로 필터.
    r = client.get("/component", params={"projectIds": project_key,
                                          "maxResults": cfg.max_results})
    summary, sample = "컴포넌트 조회 실패", None
    if r.ok:
        items = r.data if isinstance(r.data, list) else (r.data.get("values") if isinstance(r.data, dict) else []) or []
        rows = [{"name": c.get("name"), "id": c.get("id"),
                 "description": (c.get("description") or "")[:40]} for c in items[:5]]
        summary = f"컴포넌트 {len(items)}개"
        sample = rows
    report.add(CheckResult(f"5-1 프로젝트 컴포넌트 ({project_key})",
                           f"GET /component?projectIds={project_key}",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # 5-2 프로젝트 버전 (배포 버전 후보)
    r = client.get(f"/project/{project_key}/versions")
    summary, sample = "버전 조회 실패", None
    if r.ok:
        items = r.data if isinstance(r.data, list) else []
        rows = [{"name": v.get("name"), "id": v.get("id"),
                 "released": v.get("released"),
                 "releaseDate": v.get("releaseDate")} for v in items[:5]]
        summary = f"버전 {len(items)}개"
        sample = rows
    report.add(CheckResult(f"5-2 프로젝트 버전 ({project_key})",
                           f"GET /project/{project_key}/versions",
                           r.ok, r.status, summary,
                           project_web_url(cfg.base_url, project_key),
                           sample, r.error, r.elapsed_ms))

    # ---- 6단계: 대시보드·JQL 검증 ------------------------------------------
    print("\n[6단계] 대시보드·JQL 검증")

    # 6-1 대시보드 목록
    r = client.get("/dashboard", params={"maxResults": cfg.max_results})
    summary, sample = "대시보드 조회 실패", None
    if r.ok and isinstance(r.data, dict):
        dashboards = r.data.get("dashboards") or []
        rows = [{"id": d.get("id"), "name": d.get("name"),
                 "owner": (d.get("owner") or {}).get("displayName"),
                 "view": d.get("view")} for d in dashboards[:5]]
        summary = f"대시보드 {len(dashboards)}개 (total={r.data.get('total')})"
        sample = rows
    report.add(CheckResult("6-1 대시보드 목록", "GET /dashboard",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # 6-2 JQL 파싱/검증. 저장 전 JQL 유효성 사전 점검에 활용.
    test_jql = f"project = {project_key} AND resolution = Unresolved ORDER BY updated DESC"
    r = client.post("/jql/parse", json_body={"queries": [test_jql]},
                    params={"validation": "strict"})
    summary = "JQL 파싱 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        queries = r.data.get("queries") or []
        q0 = queries[0] if queries else {}
        if q0.get("errors"):
            summary = f"JQL 오류: {q0['errors']}"
        elif q0.get("warnings"):
            summary = f"JQL 경고(유효함): {q0['warnings']}"
        else:
            summary = "JQL 유효 (구조 파싱됨)"
        sample = {"query": q0.get("query"),
                  "errors": q0.get("errors"),
                  "warnings": q0.get("warnings")}
    report.add(CheckResult("6-2 JQL 파싱/검증",
                           f"POST /jql/parse (project={project_key})",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
