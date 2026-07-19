"""P0 읽기 전용 Jira Cloud API 동작 검증.

api-docs/jira-api-priority-filter.md 의 "첫 API 검증 순서" 1~3단계(GET만)를
실제 PAT 로 호출해 본다. 이 스크립트는 어떤 리소스도 생성/수정/삭제하지 않는다.

검증 항목:
  1단계 - 토큰 정체·접근 프로젝트 확인
    1-1 GET /myself                          현재 사용자(accountId)
    1-2 GET /project/search                  접근 가능 프로젝트(대상 탐지)
    1-3 GET /project/{key}                   대상 프로젝트 상세
  2단계 - 읽기 전용 대시보드 데이터 (JQL/이슈)
    2-1 GET /search?jql=assignee=currentUser()...  내 할 일
    2-2 GET /search?jql=project={key}...            프로젝트 이슈 현황
    2-3 GET /issue/{key}                            대표 이슈 상세(필드 구조)
  3단계 - 이슈 맥락 연결 (댓글·외부링크·저장필터)
    3-1 GET /issue/{key}/comment             이슈 댓글
    3-2 GET /issue/{key}/remotelink          외부 링크(GitLab MR/배포 URL 연결 후보)
    3-3 GET /filter/favourite                즐겨찾기 필터(저장 JQL 재사용 후보)

실행:  uv run python test_p0_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from jira_client import (
    ApiResponse,
    CheckResult,
    Config,
    JiraClient,
    Report,
    issue_web_url,
    load_config,
    project_web_url,
)


def _issue_rows(issues: list, limit: int = 5) -> list[dict]:
    """검색 결과 이슈 리스트를 요약 샘플로 변환."""
    rows = []
    for it in issues[:limit]:
        f = it.get("fields") or {}
        status = (f.get("status") or {}).get("name")
        assignee = (f.get("assignee") or {}).get("displayName")
        rows.append({
            "key": it.get("key"),
            "summary": f.get("summary"),
            "status": status,
            "assignee": assignee,
            "web_url": issue_web_url("", it.get("key") or "") if it.get("key") else None,
        })
    return rows


def _summarize_search(r: ApiResponse, base_url: str
                      ) -> tuple[str, str | None, list | None]:
    """/search 응답을 (summary, 첫 이슈 web_url, sample) 로 정리."""
    if not (r.ok and isinstance(r.data, dict)):
        return "검색 실패", None, None
    issues = r.data.get("issues") or []
    sample = _issue_rows(issues)
    total = r.data.get("total")
    total_str = str(total) if total is not None else f"{len(issues)}+"
    summary = f"이슈 {len(issues)}개 (total={total_str})"
    web_url = issue_web_url(base_url, issues[0]["key"]) if issues else None
    return summary, web_url, sample


def main() -> None:
    cfg: Config = load_config()
    client = JiraClient(cfg)
    report = Report(title="P0 읽기 전용 API 검증", base_url=cfg.base_url)

    print(f"Jira: {cfg.base_url}")
    print(f"대상 프로젝트: {cfg.project_key or '(자동 탐지)'}")
    print("-" * 60)

    # ---- 1단계: 토큰 정체·접근 프로젝트 확인 --------------------------------
    print("\n[1단계] 토큰 정체·접근 프로젝트 확인")

    # 1-1 현재 사용자 (OAuth 2.0 호환을 위해 /me 호출)
    r = client.get("https://api.atlassian.com/me")
    summary = "사용자 조회 실패"
    web_url = None
    sample = None
    if r.ok and isinstance(r.data, dict):
        me = r.data
        summary = (f"{me.get('name')} (accountId={me.get('account_id')}) "
                   f"active={me.get('account_status')}")
        sample = {"accountId": me.get("account_id"),
                  "displayName": me.get("name"),
                  "emailAddress": me.get("email"),
                  "active": me.get("account_status")}
    report.add(CheckResult("1-1 현재 사용자", "GET https://api.atlassian.com/me", r.ok, r.status,
                           summary, web_url, sample, r.error, r.elapsed_ms))

    # 1-2 접근 가능 프로젝트 (대상 탐지에도 사용)
    r_projects = client.get("/project/search",
                            params={"maxResults": cfg.max_results})
    sample = None
    if r_projects.ok and isinstance(r_projects.data, dict):
        values = r_projects.data.get("values") or []
        sample = [{"key": p.get("key"), "name": p.get("name"),
                   "style": p.get("style")} for p in values[:5]]
        summary = f"프로젝트 {len(values)}개 (total={r_projects.data.get('total')})"
    else:
        summary = "프로젝트 조회 실패"
    report.add(CheckResult("1-2 접근 가능 프로젝트", "GET /project/search",
                           r_projects.ok, r_projects.status, summary,
                           None, sample, r_projects.error, r_projects.elapsed_ms))

    # 대상 프로젝트 키 확정
    detect_resp, project_key = client.resolve_project()
    if not project_key:
        report.add(CheckResult(
            "1-3 대상 프로젝트 상세", "GET /project/{key}", False, None,
            "대상 프로젝트를 찾을 수 없음 (JIRA_TEST_PROJECT_KEY 설정 또는 접근 권한 확인)",
            None, None, detect_resp.error or "프로젝트 미확정", 0))
        _finalize(report)
        return

    project_path = f"/project/{project_key}"

    # 1-3 대상 프로젝트 상세
    r = client.get(project_path)
    summary = "프로젝트 상세 조회 실패"
    web_url = project_web_url(cfg.base_url, project_key)
    sample = None
    if r.ok and isinstance(r.data, dict):
        p = r.data
        issue_types = [it.get("name") for it in (p.get("issueTypes") or [])]
        lead = (p.get("lead") or {}).get("displayName")
        summary = (f"{p.get('key')} {p.get('name')} "
                   f"style={p.get('style')} lead={lead} "
                   f"issueTypes={issue_types or '없음'}")
        sample = {"id": p.get("id"), "key": p.get("key"), "name": p.get("name"),
                  "style": p.get("style"),
                  "lead": lead,
                  "issueTypes": issue_types}
    report.add(CheckResult("1-3 대상 프로젝트 상세", f"GET {project_path}",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # ---- 2단계: 읽기 전용 대시보드 데이터 (JQL/이슈) ------------------------
    print("\n[2단계] 읽기 전용 대시보드 데이터 (JQL/이슈)")

    # 2-1 내 할 일 (currentUser). username/userkey 사용 금지 → currentUser().
    my_jql = "assignee = currentUser() AND resolution = Unresolved ORDER BY updated DESC"
    r = client.post("/search/jql", json_body={
        "jql": my_jql,
        "maxResults": cfg.max_results,
        "fields": ["summary", "status", "assignee", "updated"],
    })
    s_summary, s_url, s_sample = _summarize_search(r, cfg.base_url)
    report.add(CheckResult("2-1 내 할 일 (assignee=currentUser())",
                           "POST /search/jql (assignee=currentUser())",
                           r.ok, r.status, s_summary, s_url, s_sample,
                           r.error, r.elapsed_ms))

    # 2-2 프로젝트 이슈 현황
    proj_jql = f"project = {project_key} ORDER BY updated DESC"
    r = client.post("/search/jql", json_body={
        "jql": proj_jql,
        "maxResults": cfg.max_results,
        "fields": ["summary", "status", "assignee", "updated"],
    })
    p_summary, p_url, p_sample = _summarize_search(r, cfg.base_url)
    report.add(CheckResult(f"2-2 프로젝트 이슈 ({project_key})",
                           f"POST /search/jql (project={project_key})",
                           r.ok, r.status, p_summary, p_url, p_sample,
                           r.error, r.elapsed_ms))

    # 2-3 대표 이슈 상세. 2-2 결과의 첫 이슈 키를 재사용, 없으면 2-1 결과 사용.
    issues_for_pick = []
    if isinstance(p_sample, list):
        issues_for_pick = p_sample
    elif isinstance(s_sample, list):
        issues_for_pick = s_sample
    sample_issue_key = issues_for_pick[0].get("key") if issues_for_pick else None
    if not sample_issue_key:
        report.add(CheckResult("2-3 대표 이슈 상세", "GET /issue/{key}", False, None,
                               "조회할 이슈가 없음(프로젝트에 이슈 0개)",
                               None, None, None, 0))
    else:
        r = client.get(f"/issue/{sample_issue_key}",
                       params={"fields": "summary,status,assignee,reporter,created,updated,priority,issuetype"})
        summary = "이슈 상세 조회 실패"
        web_url = issue_web_url(cfg.base_url, sample_issue_key)
        sample = None
        if r.ok and isinstance(r.data, dict):
            f = r.data.get("fields") or {}
            summary = (f"{r.data.get('key')} {f.get('summary')} "
                       f"[{(f.get('status') or {}).get('name')}] "
                       f"type={(f.get('issuetype') or {}).get('name')} "
                       f"priority={(f.get('priority') or {}).get('name')}")
            sample = {"key": r.data.get("key"), "id": r.data.get("id"),
                      "fields": {
                          "summary": f.get("summary"),
                          "status": (f.get("status") or {}).get("name"),
                          "issuetype": (f.get("issuetype") or {}).get("name"),
                          "priority": (f.get("priority") or {}).get("name"),
                          "assignee": (f.get("assignee") or {}).get("displayName"),
                          "reporter": (f.get("reporter") or {}).get("displayName"),
                      }}
        report.add(CheckResult("2-3 대표 이슈 상세",
                               f"GET /issue/{sample_issue_key}",
                               r.ok, r.status, summary, web_url, sample,
                               r.error, r.elapsed_ms))

    # ---- 3단계: 이슈 맥락 연결 (댓글·외부링크·저장필터) --------------------
    print("\n[3단계] 이슈 맥락 연결 (댓글·외부링크·저장필터)")

    # 3-1 이슈 댓글. 샘플 이슈가 있을 때만.
    if sample_issue_key:
        r = client.get(f"/issue/{sample_issue_key}/comment",
                       params={"maxResults": cfg.max_results})
        summary = "댓글 조회 실패"
        sample = None
        if r.ok and isinstance(r.data, dict):
            comments = r.data.get("comments") or []
            rows = [{"id": c.get("id"),
                     "author": (c.get("author") or {}).get("displayName"),
                     "updated": c.get("updated")} for c in comments[:5]]
            summary = f"댓글 {len(comments)}개 (total={r.data.get('total')})"
            sample = rows
        report.add(CheckResult("3-1 이슈 댓글",
                               f"GET /issue/{sample_issue_key}/comment",
                               r.ok, r.status, summary,
                               issue_web_url(cfg.base_url, sample_issue_key),
                               sample, r.error, r.elapsed_ms))
    else:
        report.add(CheckResult("3-1 이슈 댓글", "GET /issue/{key}/comment", False, None,
                               "조회할 이슈가 없음", None, None, None, 0))

    # 3-2 외부 링크 (remote links). GitLab MR/배포 URL 연결 후보.
    if sample_issue_key:
        r = client.get(f"/issue/{sample_issue_key}/remotelink")
        summary = "remote link 조회 실패"
        sample = None
        if r.ok:
            links = r.data if isinstance(r.data, list) else []
            rows = [{"id": lk.get("id"),
                     "title": (lk.get("object") or {}).get("title"),
                     "url": (lk.get("object") or {}).get("url"),
                     "relationship": lk.get("relationship")} for lk in links[:5]]
            summary = f"remote link {len(links)}개"
            sample = rows
        report.add(CheckResult("3-2 외부 링크 (remote links)",
                               f"GET /issue/{sample_issue_key}/remotelink",
                               r.ok, r.status, summary,
                               issue_web_url(cfg.base_url, sample_issue_key),
                               sample, r.error, r.elapsed_ms))
    else:
        report.add(CheckResult("3-2 외부 링크 (remote links)",
                               "GET /issue/{key}/remotelink", False, None,
                               "조회할 이슈가 없음", None, None, None, 0))

    # 3-3 즐겨찾기 필터 (저장 JQL 재사용 후보)
    r = client.get("/filter/favourite")
    summary = "필터 조회 실패"
    sample = None
    web_url = None
    if r.ok and isinstance(r.data, list):
        rows = [{"id": fl.get("id"), "name": fl.get("name"),
                 "jql": fl.get("jql"),
                 "viewUrl": fl.get("viewUrl")} for fl in r.data[:5]]
        summary = f"즐겨찾기 필터 {len(r.data)}개"
        sample = rows
        web_url = r.data[0].get("viewUrl") if r.data else None
    report.add(CheckResult("3-3 즐겨찾기 필터 (저장 JQL)",
                           "GET /filter/favourite",
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
