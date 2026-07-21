"""P1 읽기 전용 GitLab API 동작 검증.

api-docs/gitlab-api-priority-filter.md 의 P1 카테고리 중 GET(읽기) 위주 후보를
실제 토큰으로 호출해 본다. 이 스크립트는 어떤 리소스도 생성/수정/삭제하지 않는다.

P0(test_p0_readonly.py)가 대시보드 핵심 데이터라면,
P1은 프로젝트 시작·운영 지원에 유용한 보조 데이터를 검증한다.

검증 항목 (전부 프로젝트 스코프 /projects/{id}/...):
  3단계 - 브랜치·태그·커밋 (저장소 구조)
    3-1 GET /projects/{id}/repository/branches    브랜치 목록
    3-2 GET /projects/{id}/protected_branches      보호 브랜치 규칙
    3-3 GET /projects/{id}/repository/commits      최근 커밋
  4단계 - 분류 체계 (스프린트/역할별 업무)
    4-1 GET /projects/{id}/labels                  라벨
    4-2 GET /projects/{id}/milestones              마일스톤
  5단계 - 배포·릴리스 가시성
    5-1 GET /projects/{id}/releases                릴리스
    5-2 GET /projects/{id}/environments            배포 환경
  6단계 - 리뷰 피드백·통합 설정 (집계 후보)
    6-1 GET /projects/{id}/integrations            활성 통합(Jenkins/Jira/Mattermost 등)
    6-2 GET /projects/{id}/hooks                   기존 webhook 목록 (P0 2-7과 동일, P1 관점 재확인)

설계 원칙 (P0 검증으로 확정):
- 항상 프로젝트 스코프 엔드포인트 사용 (/projects/{id}/...). scope=all 금지.
  타팀 데이터 노출 방지.
- 데이터가 비어 있어도(0개) API 정상 응답이면 ok=True. "지금 데이터가 없을 뿐"
  인지와 "API가 막혀 있는지"를 구분하는 것이 목적.

실행:  uv run python test_p1_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from gitlab_client import (
    ApiResponse,
    CheckResult,
    Config,
    GitLabClient,
    Report,
    load_config,
)


def _list_count(data: object) -> int:
    return len(data) if isinstance(data, list) else 0


def _name_url_sample(r: ApiResponse, key_title: str = "name",
                     key_url: str = "web_url", limit: int = 5) -> tuple[str, str | None, list | None]:
    """list 응답을 (개수 요약, 첫 web_url, 샘플) 로 정리. 공통 패턴."""
    if not (r.ok and isinstance(r.data, list)):
        return "조회 실패", None, None
    sample = []
    for item in r.data[:limit]:
        row = {}
        # 이름/제목 후보 키들.
        for k in (key_title, "title", "name", "branch", "tag"):
            v = item.get(k)
            if v is not None:
                row[key_title] = v
                break
        if key_url in item:
            row[key_url] = item[key_url]
        sample.append(row)
    summary = f"{len(r.data)}개"
    web_url = r.data[0].get(key_url) if r.data else None
    return summary, web_url, sample or None


def main() -> None:
    cfg: Config = load_config()
    client = GitLabClient(cfg)
    report = Report(title="P1 읽기 전용 API 검증", base_url=cfg.base_url)

    print(f"GitLab: {cfg.base_url}")
    print(f"대상 프로젝트: {cfg.project_id or '(자동 탐지)'}")
    print("-" * 60)

    # 대상 프로젝트 확정 (P0와 동일 로직).
    detect_resp, project_pid = client.resolve_project()
    if not project_pid:
        report.add(CheckResult(
            "대상 프로젝트 확정", "GET /projects?membership=true", False, None,
            "대상 프로젝트를 찾을 수 없음", None, None,
            detect_resp.error or "프로젝트 미확정"))
        _finalize(report)
        return

    base = f"/projects/{project_pid}"
    print(f"대상 확정: {project_pid}\n")

    # ---- 3단계: 브랜치·태그·커밋 (저장소 구조) ------------------------------
    print("[3단계] 브랜치·태그·커밋")

    # 3-1 브랜치 목록
    r = client.get(f"{base}/repository/branches", params={"per_page": cfg.per_page})
    summary, web_url, sample = "브랜치 조회 실패", None, None
    if r.ok and isinstance(r.data, list):
        rows = [{"branch": b.get("name"),
                 "default": b.get("default"),
                 "protected": b.get("protected"),
                 "merged": b.get("merged"),
                 "commit": (b.get("commit", {}) or {}).get("short_id")}
                for b in r.data[:5]]
        defaults = [b.get("name") for b in r.data if b.get("default")]
        summary = f"브랜치 {len(r.data)}개 (default: {defaults or '없음'})"
        sample = r.data
    report.add(CheckResult("3-1 브랜치 목록", f"GET {base}/repository/branches",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # 3-2 보호 브랜치 규칙
    r = client.get(f"{base}/protected_branches", params={"per_page": cfg.per_page})
    summary, web_url, sample = "보호 브랜치 조회 실패", None, None
    if r.ok and isinstance(r.data, list):
        rows = [{"name": pb.get("name"),
                 "push_access_levels": [a.get("access_level_description") for a in (pb.get("push_access_levels") or [])],
                 "merge_access_levels": [a.get("access_level_description") for a in (pb.get("merge_access_levels") or [])]}
                for pb in r.data[:5]]
        summary = f"보호 브랜치 {len(r.data)}개"
        sample = r.data
    report.add(CheckResult("3-2 보호 브랜치 규칙", f"GET {base}/protected_branches",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # 3-3 최근 커밋
    r = client.get(f"{base}/repository/commits", params={"per_page": cfg.per_page})
    summary, web_url, sample = "커밋 조회 실패", None, None
    if r.ok and isinstance(r.data, list):
        rows = [{"short_id": c.get("short_id"),
                 "title": c.get("title"),
                 "author": c.get("author_name"),
                 "created_at": c.get("created_at")}
                for c in r.data[:5]]
        summary = f"커밋 {len(r.data)}개"
        sample = r.data
    report.add(CheckResult("3-3 최근 커밋", f"GET {base}/repository/commits",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # ---- 4단계: 분류 체계 (라벨·마일스톤) ------------------------------------
    print("\n[4단계] 분류 체계 (라벨·마일스톤)")

    # 4-1 라벨
    r = client.get(f"{base}/labels", params={"per_page": cfg.per_page})
    summary, web_url, sample = "라벨 조회 실패", None, None
    if r.ok and isinstance(r.data, list):
        rows = [{"name": lb.get("name"), "color": lb.get("color"),
                 "description": (lb.get("description") or "")[:40]}
                for lb in r.data[:5]]
        summary = f"라벨 {len(r.data)}개"
        sample = r.data
    report.add(CheckResult("4-1 프로젝트 라벨", f"GET {base}/labels",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # 4-2 마일스톤
    r = client.get(f"{base}/milestones", params={"per_page": cfg.per_page})
    summary, web_url, sample = "마일스톤 조회 실패", None, None
    if r.ok and isinstance(r.data, list):
        rows = [{"title": m.get("title"), "state": m.get("state"),
                 "due_date": m.get("due_date"), "start_date": m.get("start_date")}
                for m in r.data[:5]]
        summary = f"마일스톤 {len(r.data)}개"
        sample = r.data
    report.add(CheckResult("4-2 프로젝트 마일스톤", f"GET {base}/milestones",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # ---- 5단계: 배포·릴리스 가시성 ------------------------------------------
    print("\n[5단계] 배포·릴리스")

    # 5-1 릴리스
    r = client.get(f"{base}/releases", params={"per_page": cfg.per_page})
    summary, web_url, sample = "릴리스 조회 실패", None, None
    if r.ok and isinstance(r.data, list):
        rows = [{"tag_name": rel.get("tag_name"), "name": rel.get("name"),
                 "released_at": rel.get("released_at"),
                 "_links": rel.get("_links", {}).get("self") if isinstance(rel.get("_links"), dict) else None}
                for rel in r.data[:5]]
        summary = f"릴리스 {len(r.data)}개"
        sample = r.data
    report.add(CheckResult("5-1 프로젝트 릴리스", f"GET {base}/releases",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # 5-2 배포 환경
    r = client.get(f"{base}/environments", params={"per_page": cfg.per_page})
    summary, web_url, sample = "배포 환경 조회 실패", None, None
    if r.ok and isinstance(r.data, list):
        rows = [{"name": e.get("name"), "state": e.get("state"),
                 "tier": e.get("tier"),
                 "last_deployment": (e.get("last_deployment", {}) or {}).get("created_at")}
                for e in r.data[:5]]
        summary = f"배포 환경 {len(r.data)}개"
        sample = r.data
    report.add(CheckResult("5-2 배포 환경", f"GET {base}/environments",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # ---- 6단계: 통합 설정·webhook (집계 후보) --------------------------------
    print("\n[6단계] 통합 설정·webhook")

    # 6-1 활성 통합 (services). Jenkins/Jira/Mattermost 등 외부 도구 연결 상태.
    # 주의: 문서상 엔드포인트는 /services 와 /integrations 두 표기가 섞임.
    # 우선 /integrations 시도, 실패 시 /services fallback.
    r = client.get(f"{base}/integrations", params={"per_page": cfg.per_page})
    used_path = "integrations"
    if not r.ok:
        # 구형 엔드포인트 fallback.
        r2 = client.get(f"{base}/services")
        if r2.ok or r2.status not in (404, None):
            r = r2
            used_path = "services"
    summary, web_url, sample = "통합 조회 실패", None, None
    if r.ok and isinstance(r.data, list):
        rows = [{"id": it.get("id"), "title": it.get("title"),
                 "slug": it.get("slug"), "active": it.get("active")}
                for it in r.data[:8]]
        actives = [it for it in r.data if it.get("active")]
        summary = f"통합 {len(r.data)}개 (활성 {len(actives)})"
        sample = r.data
    report.add(CheckResult("6-1 활성 통합 (Jenkins/Jira/Mattermost 등)",
                           f"GET {base}/{used_path}",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # 6-2 webhook 목록 (P1 관점: 폴링 vs webhook 비교용 재확인).
    r = client.get(f"{base}/hooks", params={"per_page": cfg.per_page})
    count = _list_count(r.data)
    sample = None
    if r.ok and isinstance(r.data, list):
        sample = r.data
    report.add(CheckResult("6-2 기존 webhook 목록", f"GET {base}/hooks",
                           r.ok, r.status, f"webhook {count}개",
                           None, sample, r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
