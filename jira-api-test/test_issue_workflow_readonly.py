"""이슈 상세·워크플로 맥락 집계용 읽기 전용 Jira API 검증.

통합 워크스페이스가 팀별로 이름이 다른 상태를 "할 일·진행 중·완료" 공통 진행
상태로 표시하기 위해 필요한 워크플로 메타와 이슈 상세를 검증한다.
이 스크립트는 어떤 리소스도 생성/수정/삭제하지 않는다.

검증 항목:
  IW-1 GET /status              활성 워크플로 상태 + inline statusCategory (P1 4-1 401 우회)
  IW-2 GET /statuscategory      상태 카테고리(todo/in_progress/done)
  IW-3 GET /resolution          해결 상태
  IW-4 GET /issueLinkType       이슈 연결 유형(선행·차단·관련)
  IW-5 POST /search/jql         대상 프로젝트 첫 이슈 확보 (없으면 IW-6~IW-7 스킵)
  IW-6 GET /issue/{key}         이슈 상세(expand=transitions 포함)
  IW-7 GET /issue/{key}/transitions 가능한 상태 전이 목록

설계 원칙 (P0/P1 검증으로 확정):
- 데이터가 비어 있어도(0개) API 정상 응답이면 ok=True.
- P1 4-1 의 /statuses/search 401 을 /status · /statuscategory 우회로 해소.
  (statuses/search 는 Administer projects/Administer Jira 강한 권한 필요.)
- 대상 이슈가 없으면 IW-6/IW-7 을 "대상 이슈 없음 — 스킵" ok=False CheckResult 로 기록.

실행:  uv run python test_issue_workflow_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from jira_client import (
    CheckResult,
    Config,
    JiraClient,
    Report,
    issue_web_url,
    load_config,
)


def _skip(name: str, endpoint: str, reason: str) -> CheckResult:
    """대상 이슈가 없을 때 일관된 "스킵" CheckResult."""
    return CheckResult(name, endpoint, ok=False, status=None,
                       summary=reason, web_url=None, sample=None,
                       error=None, elapsed_ms=0)


def main() -> None:
    cfg: Config = load_config()
    client = JiraClient(cfg)
    report = Report(title="이슈·워크플로 읽기 전용 API 검증", base_url=cfg.base_url)

    print(f"Jira: {cfg.base_url} (cloud_id={cfg.cloud_id[:8]}...)")
    print(f"대상 프로젝트: {cfg.project_key or '(자동 탐지)'}")
    print("-" * 60)

    # 대상 프로젝트 확정 (P0/P1 과 동일 로직).
    detect_resp, project_key = client.resolve_project()
    if not project_key:
        report.add(CheckResult(
            "대상 프로젝트 확정", "GET /project/search", False, None,
            "대상 프로젝트를 찾을 수 없음", None, None,
            detect_resp.error or "프로젝트 미확정"))
        _finalize(report)
        return
    print(f"대상 확정: {project_key}\n")

    # ========================================================================
    # IW-1 워크플로 상태 (/status — /statuses/search 401 우회)
    # ========================================================================
    # /status 는 inline statusCategory 포함. Browse projects 권한만 필요(익명 가능).
    r = client.get("/status")
    summary = "워크플로 상태 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for s in r.data[:10]:
            cat = s.get("statusCategory") or {}
            rows.append({
                "name": s.get("name"),
                "id": s.get("id"),
                "category_name": cat.get("name"),
                "category_key": cat.get("key"),
            })
        sample = rows
        # 카테고리별 집계.
        cats: dict[str, int] = {}
        for s in r.data:
            cat = (s.get("statusCategory") or {}).get("key", "unknown")
            cats[cat] = cats.get(cat, 0) + 1
        summary = f"활성 상태 {len(r.data)}개, 카테고리별: {cats}"
    report.add(CheckResult("IW-1 워크플로 상태 (/status)",
                           "GET /status",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # IW-2 상태 카테고리 (/statuscategory — todo/in_progress/done)
    # ========================================================================
    r = client.get("/statuscategory")
    summary = "상태 카테고리 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = [{"id": c.get("id"), "key": c.get("key"),
                 "name": c.get("name"),
                 "colorName": c.get("colorName")} for c in r.data[:10]]
        sample = rows
        keys = [c.get("key") for c in r.data]
        summary = f"카테고리 {len(r.data)}개: {keys}"
    report.add(CheckResult("IW-2 상태 카테고리 (/statuscategory)",
                           "GET /statuscategory",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # IW-3 해결 상태 (/resolution)
    # ========================================================================
    r = client.get("/resolution")
    summary = "해결 상태 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = [{"id": x.get("id"), "name": x.get("name"),
                 "description": (x.get("description") or "")[:40]}
                for x in r.data[:10]]
        sample = rows
        names = [x.get("name") for x in r.data]
        summary = f"해결상태 {len(r.data)}개: {names}"
    report.add(CheckResult("IW-3 해결 상태 (/resolution)",
                           "GET /resolution",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # IW-4 이슈 링크 유형 (/issueLinkType)
    # ========================================================================
    r = client.get("/issueLinkType")
    summary = "이슈 링크 유형 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict) and isinstance(r.data.get("issueLinkTypes"), list):
        items = r.data.get("issueLinkTypes") or []
        rows = []
        for t in items[:10]:
            inward = t.get("inward") or ""
            outward = t.get("outward") or ""
            rows.append({"id": t.get("id"), "name": t.get("name"),
                         "inward": inward, "outward": outward})
        sample = rows
        names = [t.get("name") for t in items]
        summary = f"링크 유형 {len(items)}개: {names}"
    elif r.ok and isinstance(r.data, list):
        # 일부 응답은 리스트를 직접 반환.
        rows = [{"id": t.get("id"), "name": t.get("name"),
                 "inward": t.get("inward"), "outward": t.get("outward")}
                for t in r.data[:10]]
        sample = rows
        summary = f"링크 유형 {len(r.data)}개"
    report.add(CheckResult("IW-4 이슈 링크 유형 (/issueLinkType)",
                           "GET /issueLinkType",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # IW-5 대상 이슈 확보 (project=... ORDER BY updated DESC)
    # ========================================================================
    r = client.post("/search/jql", json_body={
        "jql": f"project = {project_key} ORDER BY updated DESC",
        "maxResults": 5,
        "fields": ["summary", "status", "assignee", "issuetype"],
    })
    summary = "이슈 검색 실패"
    sample = None
    issue_key = None
    issue_web = None
    if r.ok and isinstance(r.data, dict):
        issues = r.data.get("issues") or []
        rows = []
        for it in issues[:5]:
            fields = it.get("fields") or {}
            status = fields.get("status") or {}
            itype = fields.get("issuetype") or {}
            assignee = fields.get("assignee") or {}
            rows.append({
                "key": it.get("key"),
                "summary": (fields.get("summary") or "")[:50],
                "status": status.get("name"),
                "type": itype.get("name"),
                "assignee": assignee.get("displayName"),
            })
        sample = rows
        total = r.data.get("total")
        summary = f"프로젝트 이슈 {len(issues)}개 표시 (total={total})"
        if issues:
            issue_key = issues[0].get("key")
            issue_web = issue_web_url(cfg.base_url, issue_key)
    report.add(CheckResult("IW-5 대상 이슈 확보",
                           f"POST /search/jql (project={project_key})",
                           r.ok, r.status, summary, issue_web, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # IW-6/IW-7: 이슈 단위. 없으면 스킵.
    # ========================================================================
    if not issue_key:
        reason = "대상 이슈 없음 — IW-6/IW-7 스킵"
        report.add(_skip("IW-6 이슈 상세 (expand=transitions)",
                         "GET /issue/{key}", reason))
        report.add(_skip("IW-7 가능한 상태 전이",
                         "GET /issue/{key}/transitions", reason))
        _finalize(report)
        return

    print(f"대상 이슈: {issue_key}\n")

    # IW-6 이슈 상세 (expand=transitions 포함)
    r = client.get(f"/issue/{issue_key}",
                   params={"expand": "transitions",
                           "fields": "summary,status,assignee,issuetype,"
                                     "priority,labels,components,fixVersions,created,updated"})
    summary = "이슈 상세 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        f = r.data.get("fields") or {}
        status = f.get("status") or {}
        cat = status.get("statusCategory") or {}
        sample = {
            "key": r.data.get("key"),
            "id": r.data.get("id"),
            "summary": f.get("summary"),
            "status_name": status.get("name"),
            "status_category": cat.get("key"),
            "issuetype": (f.get("issuetype") or {}).get("name"),
            "priority": (f.get("priority") or {}).get("name"),
            "assignee": (f.get("assignee") or {}).get("displayName"),
            "created": f.get("created"),
            "updated": f.get("updated"),
        }
        transitions = r.data.get("transitions") or []
        trans_names = [t.get("name") for t in transitions[:5]]
        summary = (f"{issue_key} status={status.get('name')} "
                   f"category={cat.get('key')} "
                   f"전이 {len(transitions)}개: {trans_names}")
    report.add(CheckResult("IW-6 이슈 상세 (expand=transitions)",
                           f"GET /issue/{issue_key}",
                           r.ok, r.status, summary, issue_web, sample,
                           r.error, r.elapsed_ms))

    # IW-7 가능한 상태 전이 (별도 엔드포인트)
    r = client.get(f"/issue/{issue_key}/transitions")
    summary = "전이 목록 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        transitions = r.data.get("transitions") or []
        rows = []
        for t in transitions[:15]:
            to = t.get("to") or {}
            rows.append({"id": t.get("id"), "name": t.get("name"),
                         "to_status": to.get("name"),
                         "to_category": (to.get("statusCategory") or {}).get("key")})
        sample = rows
        summary = f"가능한 전이 {len(transitions)}개"
    report.add(CheckResult("IW-7 가능한 상태 전이",
                           f"GET /issue/{issue_key}/transitions",
                           r.ok, r.status, summary, issue_web, sample,
                           r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
