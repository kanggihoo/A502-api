"""CI/CD 자동화 후보 진단용 읽기 전용 GitLab API 검증.

통합 워크스페이스가 "정기 상태 수집·배포 전 점검·운영 자동화" 용도로 쓸
CI/CD 엔드포인트를 실제 토큰으로 검증한다. 이 스크립트는 어떤 리소스도
생성/수정/삭제(파이프라인 실행·재시도·취소 포함)하지 않는다.

검증 항목 (전부 프로젝트 스코프 /projects/{id}/...):
  C-1 GET /projects/{id}/triggers                          CI 트리거 토큰 목록 (token 마스킹)
  C-2 GET /projects/{id}/pipeline_schedules                정기 실행 스케줄
  C-3 GET /projects/{id}/variables                         CI 변수 (value 마스킹)
  C-4 GET /projects/{id}/pipelines                         최근 파이프라인 (대상 확보)
  C-5 GET /projects/{id}/pipelines/{pipeline_id}           파이프라인 상세 (있을 때만)
  C-6 GET /projects/{id}/pipelines/{pipeline_id}/jobs      파이프라인 잡 목록 (있을 때만)

보안 설계 (★ 핵심):
- CI 트리거 응답의 token 필드는 평문 비밀값이다. sample 에 절대 평문으로 담지 않고
  "***" 로 마스킹한다. id/description/last_used/expires_at 메타만 기록.
- CI 변수 응답의 value 는 평문 비밀값이다. sample 에 value 를 담지 않고
  key/protected/masked/environment_scope/hidden 메타만 기록.
- 잡 로그(trace)는 이번 검증에서 의도적 제외. 대용량(수 MB) + 평문 비밀값 노출 위험.
  필요시 별도 스크립트에서 byte_offset/byte_limit 로 샘플링.
- 마스킹은 리포트 JSON(sample 필드) 에만 적용. 터미널 summary 에도 비밀값 출력 금지.

설계 원칙 (P0/P1 검증으로 확정):
- 항상 프로젝트 스코프. 빈 결과(0개)도 ok=True.
- 파이프라인이 없는 경우 C-5/C-6 을 "대상 없음 — 스킵" ok=False 로 개별 기록.

문서상 주의사항 (api-docs/gitlab_rest_defuddle_markdown/):
- 진단용 잡 API 는 24-ci-jobs/ 디렉터리 (/projects/{id}/jobs/...).
  80-jobs/ 는 러너 전용(artifact 업로드, trace patch)이므로 사용 금지.
- 트리거 토큰/CI 변수 는 403 시 권한 부족으로 기록 (Maintainer 권한 필요 가능).

실행:  uv run python test_cicd_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from gitlab_client import (
    CheckResult,
    Config,
    GitLabClient,
    Report,
    load_config,
)


# 비밀값 마스킹 표시.
_MASK = "***"


def _skip_check(name: str, endpoint: str, reason: str) -> CheckResult:
    """파이프라인이 없을 때 일관된 "스킵" CheckResult."""
    return CheckResult(name, endpoint, ok=False, status=None,
                       summary=reason, web_url=None, sample=None,
                       error=None, elapsed_ms=0)


def main() -> None:
    cfg: Config = load_config()
    client = GitLabClient(cfg)
    report = Report(title="CI/CD 읽기 전용 API 검증", base_url=cfg.base_url)

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
    # C-1 CI 트리거 토큰 (★ token 마스킹)
    # ========================================================================
    r = client.get(f"{base}/triggers", params={"per_page": cfg.per_page})
    summary = "트리거 토큰 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for t in r.data[:10]:
            owner = t.get("owner") or {}
            rows.append({
                "id": t.get("id"),
                "description": t.get("description"),
                # ★ token 은 평문 비밀값 — 절대 평문으로 담지 않는다.
                "token": _MASK,
                "last_used": t.get("last_used"),
                "expires_at": t.get("expires_at"),
                "owner": owner.get("username"),
            })
        sample = rows
        summary = f"트리거 토큰 {len(r.data)}개 (token 은 마스킹됨)"
    elif r.status == 403:
        summary = "403 — 트리거 토큰 조회 권한 없음 (Maintainer 필요 가능)"
    report.add(CheckResult("C-1 CI 트리거 토큰 (token 마스킹)",
                           f"GET {base}/triggers",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # C-2 파이프라인 스케줄 (목록엔 variables 미포함)
    # ========================================================================
    r = client.get(f"{base}/pipeline_schedules",
                   params={"per_page": cfg.per_page})
    summary = "파이프라인 스케줄 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for s in r.data[:10]:
            owner = s.get("owner") or {}
            rows.append({
                "id": s.get("id"),
                "description": s.get("description"),
                "ref": s.get("ref"),
                "cron": s.get("cron"),
                "cron_timezone": s.get("cron_timezone"),
                "next_run_at": s.get("next_run_at"),
                "active": s.get("active"),
                "owner": owner.get("username"),
            })
        sample = rows
        summary = f"스케줄 {len(r.data)}개"
    elif r.status == 403:
        summary = "403 — 파이프라인 스케줄 조회 권한 없음"
    report.add(CheckResult("C-2 파이프라인 스케줄",
                           f"GET {base}/pipeline_schedules",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # C-3 CI 변수 (★ value 마스킹 — 메타만 기록)
    # ========================================================================
    r = client.get(f"{base}/variables", params={"per_page": cfg.per_page})
    summary = "CI 변수 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for v in r.data[:20]:
            rows.append({
                "key": v.get("key"),
                "variable_type": v.get("variable_type"),
                "protected": v.get("protected"),
                "masked": v.get("masked"),
                "hidden": v.get("hidden"),
                "raw": v.get("raw"),
                "environment_scope": v.get("environment_scope"),
                # ★ value 는 평문 비밀값 — 절대 담지 않는다. 메타만 기록.
            })
        sample = rows
        summary = f"CI 변수 {len(r.data)}개 (value 는 마스킹/생략됨)"
    elif r.status == 403:
        summary = "403 — CI 변수 조회 권한 없음 (Maintainer 필요 가능)"
    report.add(CheckResult("C-3 CI 변수 (value 마스킹)",
                           f"GET {base}/variables",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # C-4 최근 파이프라인 (대상 확보)
    # ========================================================================
    r = client.get(f"{base}/pipelines", params={"per_page": 5})
    summary = "파이프라인 목록 조회 실패"
    sample = None
    pipeline_id = None
    pipeline_web_url = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for p in r.data[:5]:
            rows.append({
                "id": p.get("id"),
                "iid": p.get("iid"),
                "ref": p.get("ref"),
                "status": p.get("status"),
                "source": p.get("source"),
                "web_url": p.get("web_url"),
                "created_at": p.get("created_at"),
            })
        sample = rows
        statuses = [p.get("status") for p in r.data]
        summary = f"파이프라인 {len(r.data)}개, 상태: {statuses or '없음'}"
        if r.data:
            pipeline_id = r.data[0].get("id")
            pipeline_web_url = r.data[0].get("web_url")
    report.add(CheckResult("C-4 최근 파이프라인",
                           f"GET {base}/pipelines",
                           r.ok, r.status, summary, pipeline_web_url, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # C-5/C-6: 파이프라인 상세 + 잡. 없으면 스킵.
    # ========================================================================
    if not pipeline_id:
        skip_reason = "파이프라인 없음 — C-5/C-6 스킵"
        report.add(_skip_check("C-5 파이프라인 상세",
                               f"GET {base}/pipelines/{{id}}", skip_reason))
        report.add(_skip_check("C-6 파이프라인 잡",
                               f"GET {base}/pipelines/{{id}}/jobs", skip_reason))
        _finalize(report)
        return

    pipe_path = f"{base}/pipelines/{pipeline_id}"
    print(f"대상 파이프라인: {pipeline_id}\n")

    # C-5 파이프라인 상세
    r = client.get(pipe_path)
    summary = "파이프라인 상세 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        d = r.data
        sample = {
            "id": d.get("id"),
            "iid": d.get("iid"),
            "sha": d.get("sha"),
            "ref": d.get("ref"),
            "status": d.get("status"),
            "source": d.get("source"),
            "created_at": d.get("created_at"),
            "updated_at": d.get("updated_at"),
            "duration": d.get("duration"),
            "queued_duration": d.get("queued_duration"),
            "coverage": d.get("coverage"),
            "web_url": d.get("web_url"),
        }
        summary = (f"id={d.get('id')} status={d.get('status')} "
                   f"ref={d.get('ref')} duration={d.get('duration')}s")
    report.add(CheckResult("C-5 파이프라인 상세",
                           f"GET {pipe_path}",
                           r.ok, r.status, summary, pipeline_web_url, sample,
                           r.error, r.elapsed_ms))

    # C-6 파이프라인 잡 목록
    r = client.get(f"{pipe_path}/jobs", params={"per_page": cfg.per_page})
    summary = "잡 목록 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for j in r.data[:15]:
            rows.append({
                "id": j.get("id"),
                "name": j.get("name"),
                "stage": j.get("stage"),
                "status": j.get("status"),
                "ref": j.get("ref"),
                "allow_failure": j.get("allow_failure"),
                "duration": j.get("duration"),
                "web_url": j.get("web_url"),
                "failure_reason": j.get("failure_reason"),
            })
        sample = rows
        # 상태별 집계.
        status_counts: dict[str, int] = {}
        for j in r.data:
            s = j.get("status") or "unknown"
            status_counts[s] = status_counts.get(s, 0) + 1
        summary = f"잡 {len(r.data)}개, 상태별: {status_counts}"
    report.add(CheckResult("C-6 파이프라인 잡",
                           f"GET {pipe_path}/jobs",
                           r.ok, r.status, summary, pipeline_web_url, sample,
                           r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
