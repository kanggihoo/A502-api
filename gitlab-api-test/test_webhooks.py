"""프로젝트 webhook 생성·조회·삭제 검증 (쓰기 작업, Maintainer 전제).

api-docs/gitlab-api-priority-filter.md 의 "첫 API 검증 순서" 3단계.
폴링 대신 push/MR/pipeline 이벤트를 수신하는 webhook을 실제로 만들어 보고,
조회한 뒤, 마지막에 반드시 삭제한다. 이 스크립트는 리소스를 "생성"한다.

안전장치:
- .env 의 WEBHOOK_TEST_URL 이 비어 있으면 쓰기 작업을 수행하지 않고 종료한다.
- 생성에 실패해도, 생성된 webhook id 가 있으면 삭제를 시도한다(try/finally).
- 이미 존재하는 동일 URL webhook이 있으면 새로 만들지 않고 그 id로 테스트한다.

권한 전제:
- Maintainer(40) 이상 역할 + api scope 토큰 필요.
- 403 이면 인스턴스 정책/권한 부족으로 기록한다.

실행:  uv run python test_webhooks.py   (WEBHOOK_TEST_URL 설정 시에만 동작)
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


# 이 테스트가 구독할 이벤트. 통합 대시보드/알림에 가장 유용한 핵심 이벤트.
WEBHOOK_EVENTS = {
    "push_events": True,
    "merge_requests_events": True,
    "issues_events": True,
    "pipeline_events": True,
    "job_events": True,
    # 노트(댓글) 이벤트는 리뷰 피드백 알림 후보.
    "note_events": True,
}


def main() -> None:
    cfg: Config = load_config()
    client = GitLabClient(cfg)
    report = Report(title="Webhook 생성·조회·삭제 검증", base_url=cfg.base_url)

    # 안전장치: 수신 URL 미설정 시 쓰기 금지.
    if not cfg.webhook_test_url:
        print("WEBHOOK_TEST_URL 이 .env 에 설정되지 않았습니다.")
        print("webhook 쓰기 테스트(생성/삭제)를 건너뜁니다. P0 읽기(test_p0_readonly.py)만 사용하세요.")
        report.add(CheckResult(
            "webhook 쓰기 (안전장치)", "POST/DELETE /projects/{id}/hooks",
            ok=False, status=None,
            summary="WEBHOOK_TEST_URL 미설정으로 쓰기 테스트 중단",
            error="WEBHOOK_TEST_URL 필요"))
        _finalize(report)
        return

    print(f"GitLab: {cfg.base_url}")
    print(f"대상 프로젝트: {cfg.project_id or '(자동 탐지)'}")
    print(f"수신 URL: {cfg.webhook_test_url}")
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

    hooks_path = f"/projects/{project_pid}/hooks"
    created_hook_id: int | None = None

    try:
        # ---- W-1 기존 webhook 목록에서 동일 URL 탐색 ------------------------
        r = client.get(hooks_path, params={"per_page": cfg.per_page})
        existing = []
        if r.ok and isinstance(r.data, list):
            existing = [h for h in r.data if h.get("url") == cfg.webhook_test_url]
        summary = (f"기존 webhook {len(r.data) if isinstance(r.data, list) else 0}개, "
                   f"동일 URL {len(existing)}개")
        report.add(CheckResult("W-1 기존 webhook 목록", f"GET {hooks_path}",
                               r.ok, r.status, summary, None,
                               r.data, r.error, r.elapsed_ms))

        # ---- W-2 webhook 생성 (또는 기존 id 재사용) --------------------------
        if existing:
            created_hook_id = existing[0].get("id")
            r_create: ApiResponse = ApiResponse(
                True, 200, existing[0], None, 0)
            summary = f"기존 webhook 재사용 (id={created_hook_id})"
        else:
            r_create = client.post(hooks_path, json_body={
                "url": cfg.webhook_test_url,
                "enable_ssl_verification": False,
                "token": "gitlab-api-test-poc",  # 페이로드 검증용 시크릿(POC용 더미)
                **WEBHOOK_EVENTS,
            })
            summary = "webhook 생성 실패"
            if r_create.ok and isinstance(r_create.data, dict):
                created_hook_id = r_create.data.get("id")
                events_on = [k for k, v in WEBHOOK_EVENTS.items() if v]
                summary = f"webhook 생성됨 (id={created_hook_id}, events={events_on})"
        report.add(CheckResult("W-2 webhook 생성", f"POST {hooks_path}",
                               r_create.ok, r_create.status, summary, None,
                               r_create.data, r_create.error, r_create.elapsed_ms))

        # ---- W-3 생성 확인 (단건 조회) --------------------------------------
        if created_hook_id is not None:
            r = client.get(f"{hooks_path}/{created_hook_id}")
            summary = "단건 조회 실패"
            if r.ok and isinstance(r.data, dict):
                summary = (f"id={r.data.get('id')} "
                           f"push={r.data.get('push_events')} "
                           f"mr={r.data.get('merge_requests_events')} "
                           f"pipeline={r.data.get('pipeline_events')}")
            report.add(CheckResult("W-3 webhook 단건 조회",
                                   f"GET {hooks_path}/{created_hook_id}",
                                   r.ok, r.status, summary, None,
                                   r.data, r.error, r.elapsed_ms))
        else:
            report.add(CheckResult("W-3 webhook 단건 조회",
                                   f"GET {hooks_path}/{{id}}", False, None,
                                   "생성된 hook id 없음 — 건너뜀", None, None,
                                   "W-2에서 id 획득 실패"))

    finally:
        # ---- W-4 삭제 (항상 시도) -------------------------------------------
        if created_hook_id is not None:
            r = client.delete(f"{hooks_path}/{created_hook_id}")
            summary = "삭제 실패 — 수동 삭제 필요!"
            if r.ok:
                summary = f"webhook 삭제됨 (id={created_hook_id})"
            report.add(CheckResult("W-4 webhook 삭제",
                                   f"DELETE {hooks_path}/{created_hook_id}",
                                   r.ok, r.status, summary, None,
                                   None, r.error, r.elapsed_ms))
        else:
            report.add(CheckResult("W-4 webhook 삭제",
                                   f"DELETE {hooks_path}/{{id}}", True, None,
                                   "삭제 대상 id 없음 — 건너뜀", None, None, None))

    _finalize(report)


def _hook_sample(r: ApiResponse):
    if not (r.ok and isinstance(r.data, list)):
        return None
    return [{"id": h.get("id"), "url": h.get("url"),
             "push_events": h.get("push_events"),
             "merge_requests_events": h.get("merge_requests_events"),
             "pipeline_events": h.get("pipeline_events")} for h in r.data[:5]]


def _hook_detail(r: ApiResponse):
    if not (r.ok and isinstance(r.data, dict)):
        return None
    d = r.data
    return {"id": d.get("id"), "url": d.get("url"),
            "push_events": d.get("push_events"),
            "merge_requests_events": d.get("merge_requests_events"),
            "issues_events": d.get("issues_events"),
            "pipeline_events": d.get("pipeline_events"),
            "job_events": d.get("job_events"),
            "note_events": d.get("note_events"),
            "enable_ssl_verification": d.get("enable_ssl_verification"),
            "created_at": d.get("created_at")}


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
