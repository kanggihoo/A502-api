"""P0 읽기 전용 GitLab API 동작 검증.

api-docs/gitlab-api-priority-filter.md 의 "첫 API 검증 순서" 1~2단계(GET만)를
실제 토큰으로 호출해 본다. 이 스크립트는 어떤 리소스도 생성/수정/삭제하지 않는다.

검증 항목:
  1단계 - 토큰 정체·팀 역할 확인
    1-1 GET /user                         현재 사용자
    1-2 GET /projects?membership=true     접근 가능 프로젝트(대상 탐지)
    1-3 GET /projects/{id}                대상 프로젝트 상세
    1-4 GET /projects/{id}/members/all    팀 멤버·역할
    1-5 GET /groups                       그룹 구조 존재 여부
  2단계 - 읽기 전용 대시보드 데이터
    2-1 GET /projects/{id}/merge_requests 리뷰 대기 MR
    2-2 GET /issues?scope=all             이슈 현황(사용자 단위)
    2-3 GET /projects/{id}/issues         프로젝트 단위 이슈
    2-4 GET /projects/{id}/pipelines      최근 파이프라인 상태
    2-5 GET /events                       사용자 활동 이벤트
    2-6 GET /todos                        할 일
    2-7 GET /projects/{id}/hooks          기존 webhook 목록(조회만)

실행:  uv run python test_p0_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from gitlab_client import (
    ApiResponse,
    CheckResult,
    Config,
    GitLabClient,
    Report,
    access_label,
    load_config,
)


def _list_count(data: object) -> int:
    return len(data) if isinstance(data, list) else 0


def _pick(data: dict, *keys: str, default: str = "-") -> str:
    """여러 후보 키 중 첫 번째로 존재하는 값을 반환."""
    for k in keys:
        if k in data and data[k] not in (None, ""):
            return str(data[k])
    return default


def main() -> None:
    cfg: Config = load_config()
    client = GitLabClient(cfg)
    report = Report(title="P0 읽기 전용 API 검증", base_url=cfg.base_url)

    print(f"GitLab: {cfg.base_url}")
    print(f"대상 프로젝트: {cfg.project_id or '(자동 탐지)'}")
    print("-" * 60)

    # ---- 1단계: 토큰 정체·팀 역할 확인 -------------------------------------
    print("\n[1단계] 토큰 정체·팀 역할 확인")

    # 1-1 현재 사용자
    r = client.get("/user")
    summary = "사용자 조회 실패"
    web_url = None
    sample = None
    if r.ok and isinstance(r.data, dict):
        me = r.data
        summary = f"@{me.get('username')} ({me.get('name')}) state={me.get('state')}"
        web_url = me.get("web_url")
        sample = me
    report.add(CheckResult("1-1 현재 사용자", "GET /user", r.ok, r.status,
                           summary, web_url, sample, r.error, r.elapsed_ms))

    # 1-2 접근 가능 프로젝트 (대상 프로젝트 탐지에도 사용)
    r_projects = client.get("/projects",
                            params={"membership": "true", "per_page": cfg.per_page})
    count = _list_count(r_projects.data)
    sample = None
    if r_projects.ok and isinstance(r_projects.data, list):
        sample = r_projects.data
    report.add(CheckResult("1-2 접근 가능 프로젝트", "GET /projects?membership=true",
                           r_projects.ok, r_projects.status, f"프로젝트 {count}개",
                           None, sample, r_projects.error, r_projects.elapsed_ms))

    # 대상 프로젝트 식별자 확정
    detect_resp, project_pid = client.resolve_project()
    if not project_pid:
        # 대상 프로젝트를 못 정했으면 1-3 이후는 건너뛴다.
        report.add(CheckResult(
            "1-3 대상 프로젝트 상세", "GET /projects/{id}", False, None,
            "대상 프로젝트를 찾을 수 없음 (GITLAB_TEST_PROJECT_ID 설정 또는 멤버십 확인)",
            None, None, detect_resp.error or "프로젝트 미확정", 0))
        _finalize(report)
        return

    project_path_in_url = f"/projects/{project_pid}"

    # 1-3 대상 프로젝트 상세
    r = client.get(f"{project_path_in_url}")
    summary = "프로젝트 상세 조회 실패"
    web_url = None
    sample = None
    if r.ok and isinstance(r.data, dict):
        p = r.data
        summary = (f"{p.get('path_with_namespace')} "
                   f"default_branch={p.get('default_branch')} "
                   f"archived={p.get('archived')}")
        web_url = p.get("web_url")
        sample = p
    report.add(CheckResult("1-3 대상 프로젝트 상세", f"GET {project_path_in_url}",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # 1-4 프로젝트 멤버·역할
    r = client.get(f"{project_path_in_url}/members/all",
                   params={"per_page": cfg.per_page})
    summary = "멤버 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for m in r.data:
            rows.append({
                "username": m.get("username"),
                "name": m.get("name"),
                "access_level": m.get("access_level"),
                "role": access_label(m.get("access_level")),
                "state": m.get("state"),
            })
        # Maintainer/Developer 수로 팀 구성 가정(1 Maintainer + N Developer) 확인.
        maintainers = sum(1 for x in rows if x["access_level"] == 40)
        developers = sum(1 for x in rows if x["access_level"] == 30)
        summary = (f"멤버 {len(rows)}명 "
                   f"(Maintainer {maintainers} / Developer {developers})")
        sample = r.data
    report.add(CheckResult("1-4 프로젝트 멤버·역할",
                           f"GET {project_path_in_url}/members/all",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # 1-5 그룹 목록
    r = client.get("/groups", params={"per_page": cfg.per_page})
    count = _list_count(r.data)
    sample = None
    if r.ok and isinstance(r.data, list):
        sample = r.data
    report.add(CheckResult("1-5 그룹 목록", "GET /groups", r.ok, r.status,
                           f"그룹 {count}개", None, sample, r.error, r.elapsed_ms))

    # ---- 2단계: 읽기 전용 대시보드 데이터 ----------------------------------
    print("\n[2단계] 읽기 전용 대시보드 데이터")

    # 2-1 프로젝트 MR (opened)
    r = client.get(f"{project_path_in_url}/merge_requests",
                   params={"state": "opened", "per_page": cfg.per_page})
    mr_summary, mr_url, mr_sample = _summarize_mr(r)
    report.add(CheckResult(name="2-1 프로젝트 MR (opened)",
                           endpoint=f"GET {project_path_in_url}/merge_requests?state=opened",
                           ok=r.ok, status=r.status, summary=mr_summary,
                           web_url=mr_url, sample=mr_sample, error=r.error, elapsed_ms=r.elapsed_ms))

    # 2-2 이슈 (사용자 단위, scope=all)
    r = client.get("/issues", params={"scope": "all", "state": "opened",
                                      "per_page": cfg.per_page})
    iss_summary, iss_url, iss_sample = _summarize_issue(r)
    report.add(CheckResult(name="2-2 이슈 (사용자 단위, scope=all)",
                           endpoint="GET /issues?scope=all&state=opened",
                           ok=r.ok, status=r.status, summary=iss_summary,
                           web_url=iss_url, sample=iss_sample, error=r.error, elapsed_ms=r.elapsed_ms))

    # 2-3 프로젝트 이슈
    r = client.get(f"{project_path_in_url}/issues",
                   params={"state": "opened", "per_page": cfg.per_page})
    iss2_summary, iss2_url, iss2_sample = _summarize_issue(r)
    report.add(CheckResult(name="2-3 프로젝트 이슈 (opened)",
                           endpoint=f"GET {project_path_in_url}/issues?state=opened",
                           ok=r.ok, status=r.status, summary=iss2_summary,
                           web_url=iss2_url, sample=iss2_sample, error=r.error, elapsed_ms=r.elapsed_ms))

    # 2-4 파이프라인
    r = client.get(f"{project_path_in_url}/pipelines",
                   params={"per_page": cfg.per_page})
    summary = "파이프라인 조회 실패"
    web_url = None
    sample = None
    if r.ok and isinstance(r.data, list):
        sample = r.data
        statuses = [p.get("status") for p in r.data]
        summary = f"파이프라인 {len(statuses)}개, 상태: {statuses or '없음'}"
        if r.data:
            web_url = r.data[0].get("web_url")
    report.add(CheckResult("2-4 파이프라인", f"GET {project_path_in_url}/pipelines",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # 2-5 사용자 활동 이벤트
    r = client.get("/events", params={"per_page": cfg.per_page})
    count = _list_count(r.data)
    sample = None
    if r.ok and isinstance(r.data, list):
        sample = r.data
    report.add(CheckResult("2-5 사용자 활동 이벤트", "GET /events",
                           r.ok, r.status, f"이벤트 {count}개", None, sample, r.error, r.elapsed_ms))

    # 2-6 할 일 (to-do)
    r = client.get("/todos", params={"per_page": cfg.per_page})
    count = _list_count(r.data)
    sample = None
    if r.ok and isinstance(r.data, list):
        sample = r.data
    report.add(CheckResult("2-6 할 일 (to-do)", "GET /todos",
                           r.ok, r.status, f"할 일 {count}개", None, sample, r.error, r.elapsed_ms))

    # 2-7 기존 webhook 목록 (조회만)
    r = client.get(f"{project_path_in_url}/hooks", params={"per_page": cfg.per_page})
    count = _list_count(r.data)
    sample = None
    if r.ok and isinstance(r.data, list):
        sample = r.data
    report.add(CheckResult("2-7 기존 webhook 목록 (조회만)",
                           f"GET {project_path_in_url}/hooks",
                           r.ok, r.status, f"webhook {count}개",
                           None, sample, r.error, r.elapsed_ms))

    _finalize(report)


def _summarize_mr(r: ApiResponse) -> tuple[str, str | None, list | None]:
    """MR 응답을 (summary, web_url, sample) 으로 정리."""
    if not (r.ok and isinstance(r.data, list)):
        return "MR 조회 실패", None, None
    sample = r.data
    draft = sum(1 for m in r.data if m.get("draft"))
    summary = f"MR {len(r.data)}개 (draft {draft})"
    web_url = r.data[0].get("web_url") if r.data else None
    return summary, web_url, sample


def _summarize_issue(r: ApiResponse) -> tuple[str, str | None, list | None]:
    """이슈 응답을 (summary, web_url, sample) 으로 정리."""
    if not (r.ok and isinstance(r.data, list)):
        return "이슈 조회 실패", None, None
    sample = r.data
    summary = f"이슈 {len(r.data)}개"
    web_url = r.data[0].get("web_url") if r.data else None
    return summary, web_url, sample


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
