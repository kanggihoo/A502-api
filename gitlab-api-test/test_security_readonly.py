"""보안·보호규칙 진단용 읽기 전용 GitLab API 검증.

통합 워크스페이스가 "배포 환경·기본 브랜치 보안 상태" 를 점검하는 용도로 쓸
보호 규칙 엔드포인트를 실제 토큰으로 검증한다. 이 스크립트는 어떤 리소스도
생성/수정/삭제하지 않는다. 자동 변경은 절대 수행하지 않고, 확인된 규칙만
원문 링크와 함께 제안하는 것이 설계 원칙이다.

검증 항목 (전부 프로젝트 스코프 /projects/{id}/...):
  S-1 GET /projects/{id}/protected_tags           보호 태그 (전 에디션)
  S-2 GET /projects/{id}/protected_environments    보호 환경 (Premium/Ultimate 전용 → 403 예상)
  S-3 GET /projects/{id}/push_rule                 push 규칙 (단수형! Premium/Ultimate → 403 예상)

설계 원칙:
- 403 Forbidden 은 "에디션/권한 제약" 으로 해석한다. summary 에 원인을 명시하고
  ok=False 로 기록한다. (Mattermost 북마크 501, 플레이북 404 처리와 동일 철학)
- 빈 결과(0개)는 ok=True (규칙이 설정되지 않았을 뿐 API는 정상).
- 보호 브랜치는 P1(test_p1_readonly.py 3-2)에서 이미 검증했으므로 여기서는 제외.

문서상 주의사항 (api-docs/gitlab_rest_defuddle_markdown/):
- push_rule 엔드포인트는 단수형이다 (push_rules 아님). 슬래시/복수 오타 주의.
- protected_environments 는 GitLab Premium/Ultimate 에디션 필요.
  프로젝트 CI/CD 가 비활성화면 403.
- 공식 문서 기준 GET 조회 권한이 명시되지 않은 경우가 많아, 403 응답으로
  최종 권한을 확정해야 한다. defuddle markdown 에는 에디션 표기가 없다.

실행:  uv run python test_security_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from gitlab_client import (
    CheckResult,
    Config,
    GitLabClient,
    Report,
    access_label,
    load_config,
)


def main() -> None:
    cfg: Config = load_config()
    client = GitLabClient(cfg)
    report = Report(title="보안·보호규칙 읽기 전용 API 검증", base_url=cfg.base_url)

    print(f"GitLab: {cfg.base_url}")
    print(f"대상 프로젝트: {cfg.project_id or '(자동 탐지)'}")
    print("-" * 60)

    # 대상 프로젝트 확정 (P0/P1 과 동일 로직).
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
    # S-1 보호 태그 (전 에디션 지원)
    # ========================================================================
    r = client.get(f"{base}/protected_tags", params={"per_page": cfg.per_page})
    summary = "보호 태그 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for t in r.data[:10]:
            levels = t.get("create_access_levels") or []
            level_labels = [access_label(l.get("access_level")) for l in levels]
            rows.append({
                "name": t.get("name"),
                "create_access_levels": level_labels,
            })
        sample = rows
        summary = f"보호 태그 {len(r.data)}개"
    elif r.status == 403:
        summary = "403 — 보호 태그 조회 권한 없음 (역할 확인 필요)"
    report.add(CheckResult("S-1 보호 태그",
                           f"GET {base}/protected_tags",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # S-2 보호 환경 (Premium/Ultimate 전용 → 403 예상)
    # ========================================================================
    r = client.get(f"{base}/protected_environments",
                   params={"per_page": cfg.per_page})
    summary = "보호 환경 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for e in r.data[:10]:
            deploy_levels = e.get("deploy_access_levels") or []
            level_labels = [access_label(l.get("access_level")) for l in deploy_levels]
            rows.append({
                "name": e.get("name"),
                "deploy_access_levels": level_labels,
                "required_approval_count": e.get("required_approval_count"),
            })
        sample = rows
        summary = f"보호 환경 {len(r.data)}개"
    elif r.status == 403:
        summary = ("403 — 보호 환경은 GitLab Premium/Ultimate 에디션 필요 "
                   "(또는 프로젝트 CI/CD 비활성화). 에디션 제약으로 해석")
    elif r.status == 404:
        summary = "404 — 보호 환경 기능 비활성화 또는 에디션 미지원"
    report.add(CheckResult("S-2 보호 환경 (Premium 전용 예상)",
                           f"GET {base}/protected_environments",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # S-3 push 규칙 (단수형! Premium/Ultimate → 403 예상)
    # ========================================================================
    # 주의: 엔드포인트는 단수형 push_rule 이다.
    r = client.get(f"{base}/push_rule")
    summary = "push 규칙 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        d = r.data
        # 규칙 필드 중 보안 진단에 핵심인 것만 발췌.
        sample = {
            "id": d.get("id"),
            "project_id": d.get("project_id"),
            "commit_message_regex": d.get("commit_message_regex"),
            "branch_name_regex": d.get("branch_name_regex"),
            "deny_delete_tag": d.get("deny_delete_tag"),
            "member_check": d.get("member_check"),
            "prevent_secrets": d.get("prevent_secrets"),
            "max_file_size": d.get("max_file_size"),
            "reject_unsigned_commits": d.get("reject_unsigned_commits"),
        }
        # 설정된 규칙 개수를 대략 집계 (None 이 아닌 bool/값 필드).
        active_keys = [k for k in ("deny_delete_tag", "member_check",
                                   "prevent_secrets", "reject_unsigned_commits")
                       if d.get(k)]
        summary = (f"push 규칙 존재 (활성 제약 {len(active_keys)}개: "
                   f"{active_keys or '없음'})")
    elif r.status == 403:
        summary = ("403 — push 규칙은 GitLab Premium/Ultimate 에디션 필요. "
                   "에디션 제약으로 해석")
    elif r.status == 404:
        summary = "404 — push 규칙이 설정되지 않았거나 에디션 미지원"
    report.add(CheckResult("S-3 push 규칙 (단수형, Premium 전용 예상)",
                           f"GET {base}/push_rule",
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
