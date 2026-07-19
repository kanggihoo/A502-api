"""검색·콘텐츠 조회용 읽기 전용 GitLab API 검증.

통합 워크스페이스가 "대시보드에서 GitLab 원문으로 빠르게 이동" 하는 보조
기능에 쓸 검색·파일 조회 엔드포인트를 실제 토큰으로 검증한다. 이 스크립트는
어떤 리소스도 생성/수정/삭제하지 않는다.

검증 항목:
  Q-1 GET /projects/{id}/search?scope=blobs&search=README         프로젝트 내 코드 검색
  Q-2 GET /projects/{id}/search?scope=merge_requests&search=...    프로젝트 내 MR 검색
  Q-3 GET /projects/{id}/repository/tree                            저장소 트리(최상위)
  Q-4 GET /projects/{id}/repository/files/README.md/raw             README 원문
  Q-5 GET /search?scope=projects&search={프로젝트명}                전역 프로젝트 검색

설계 원칙:
- 검색 결과 0건도 ok=True. "지금 매칭이 없을 뿐" 과 "API 가 막혀 있는지" 구분.
- README 원문(raw) 은 전체 본문을 sample 에 담지 않고 앞부분만 잘라 저장.
  대시보드 미리보기 용도에 맞춰 크기를 제한한다.

문서상 주의사항 (api-docs/gitlab_rest_defuddle_markdown/):
- 코드 검색은 GET /projects/{id}/search?scope=blobs 로 수행한다.
  34-code-search/ 디렉터리는 Zoekt 인덱스 관리(admin) 용도이므로 사용하지 않는다.
- 파일 원문은 GET /projects/{id}/repository/files/{file_path}/raw.
  file_path 는 URL-encoded 경로 (README.md → README.md 그대로, docs/README.md → docs%2FREADME.md).
- search API 의 scope 유효값(projets/issues/merge_requests/blobs/wiki_blobs/commits/...)
  은 defuddle markdown 에 명시되지 않아, 표준값을 사용하고 응답으로 검증.

실행:  uv run python test_search_content_readonly.py
"""

from __future__ import annotations

import urllib.parse
from pathlib import Path

from gitlab_client import (
    CheckResult,
    Config,
    GitLabClient,
    Report,
    load_config,
)


# README 원문 미리보기 최대 길이(문자). 대시보드 미리보기 용도.
_README_PREVIEW_LIMIT = 400


def main() -> None:
    cfg: Config = load_config()
    client = GitLabClient(cfg)
    report = Report(title="검색·콘텐츠 읽기 전용 API 검증", base_url=cfg.base_url)

    print(f"GitLab: {cfg.base_url}")
    print(f"대상 프로젝트: {cfg.project_id or '(자동 탐지)'}")
    print("-" * 60)

    # 대상 프로젝트 확정.
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

    # ========================================================================
    # Q-1 프로젝트 내 코드 검색 (scope=blobs)
    # ========================================================================
    r = client.get(f"{base}/search",
                   params={"scope": "blobs", "search": "README",
                           "per_page": cfg.per_page})
    summary = "코드 검색 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for b in r.data[:5]:
            rows.append({
                "basename": b.get("basename"),
                "path": b.get("path"),
                "filename": b.get("filename"),
                "ref": b.get("ref"),
                "startline": b.get("startline"),
                "project_id": b.get("project_id"),
            })
        sample = rows
        summary = f"코드 검색 결과 {len(r.data)}개 (search=README, scope=blobs)"
    elif r.status == 400:
        summary = "400 — scope/search 파라미터 오류 (스코프 유효값 확인 필요)"
    report.add(CheckResult("Q-1 프로젝트 코드 검색 (blobs)",
                           f"GET {base}/search?scope=blobs",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # Q-2 프로젝트 내 MR 검색 (scope=merge_requests)
    # ========================================================================
    r = client.get(f"{base}/search",
                   params={"scope": "merge_requests", "search": "test",
                           "per_page": cfg.per_page})
    summary = "MR 검색 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for m in r.data[:5]:
            rows.append({
                "iid": m.get("iid"),
                "title": (m.get("title") or "")[:60],
                "state": m.get("state"),
                "web_url": m.get("web_url"),
            })
        sample = rows
        summary = f"MR 검색 결과 {len(r.data)}개 (search=test)"
    elif r.status == 400:
        summary = "400 — scope/search 파라미터 오류"
    report.add(CheckResult("Q-2 프로젝트 MR 검색",
                           f"GET {base}/search?scope=merge_requests",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # Q-3 저장소 트리 (최상위)
    # ========================================================================
    r = client.get(f"{base}/repository/tree", params={"per_page": cfg.per_page})
    summary = "저장소 트리 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for e in r.data[:15]:
            rows.append({
                "name": e.get("name"),
                "type": e.get("type"),
                "path": e.get("path"),
                "mode": e.get("mode"),
            })
        sample = rows
        type_counts: dict[str, int] = {}
        for e in r.data:
            t = e.get("type") or "unknown"
            type_counts[t] = type_counts.get(t, 0) + 1
        summary = f"트리 엔트리 {len(r.data)}개, 타입별: {type_counts}"
    report.add(CheckResult("Q-3 저장소 트리",
                           f"GET {base}/repository/tree",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # Q-4 README 원문 (raw). file_path URL 인코딩.
    # ========================================================================
    # raw 응답은 text/plain 이라 JSON 파싱이 안 된다. get_text() 로 문자열 그대로 수신.
    readme_path_encoded = urllib.parse.quote("README.md", safe="")
    r = client.get_text(f"{base}/repository/files/{readme_path_encoded}/raw")
    summary = "README 원문 조회 실패"
    sample = None
    web_url = None
    if r.ok and isinstance(r.data, str):
        # r.data 는 raw 텍스트(문자열). 앞부분만 잘라 미리보기로 저장.
        preview = r.data[:_README_PREVIEW_LIMIT]
        sample = {
            "file": "README.md",
            "total_length": len(r.data),
            "preview_length": len(preview),
            "preview": preview,
        }
        summary = (f"README 원문 {len(r.data)}자 "
                   f"(미리보기 {len(preview)}자 sample 저장)")
    elif r.status == 404:
        summary = "404 — README.md 없음 (또는 기본 브랜치에 없음)"
    report.add(CheckResult("Q-4 README 원문 (raw)",
                           f"GET {base}/repository/files/README.md/raw",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # Q-5 전역 프로젝트 검색 (대시보드에서 프로젝트 찾기)
    # ========================================================================
    # project_pid 가 경로형이면 마지막 세그먼트를 검색어로 사용.
    # 숫자 ID 면 빈 검색어가 될 수 있어, 그땐 "ssafy" 같은 보편 키워드로 대체.
    search_term = ""
    if isinstance(project_pid, str) and not project_pid.isdigit():
        # encode_project_id 가 %2F 로 인코딩해둔 경로를 다시 풀어 마지막 세그먼트 사용.
        decoded = urllib.parse.unquote(project_pid)
        search_term = decoded.rsplit("/", 1)[-1]
    if not search_term:
        search_term = "ssafy"
    r = client.get("/search",
                   params={"scope": "projects", "search": search_term,
                           "per_page": cfg.per_page})
    summary = "전역 프로젝트 검색 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for p in r.data[:5]:
            rows.append({
                "id": p.get("id"),
                "name": p.get("name"),
                "path_with_namespace": p.get("path_with_namespace"),
                "web_url": p.get("web_url"),
                "description": (p.get("description") or "")[:60],
            })
        sample = rows
        summary = f"전역 프로젝트 검색 결과 {len(r.data)}개 (search={search_term!r})"
    elif r.status == 400:
        summary = "400 — scope/search 파라미터 오류"
    report.add(CheckResult(f"Q-5 전역 프로젝트 검색 (search={search_term!r})",
                           "GET /search?scope=projects",
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
