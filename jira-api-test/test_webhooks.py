"""Jira Cloud webhook 권한 검증.

api-docs/jira-api-priority-filter.md 의 "첫 검증 순서" 4단계(91-webhooks)를
실제 PAT 로 시도한다.

중요: /rest/api/3/webhook 엔드포인트는 문서상 Connect 앱·OAuth 2.0 앱 전용이다.
PAT(사용자 계정 Basic Auth) 로는 403 이 거의 확실하다. 이 스크립트는
"시도 자체를 증거로 기록"하는 것이 목적이며, POST(생성)는 하지 않는다.
GET 조차 막히면 쓰기는 무의미하기 때문이다.

검증 항목:
  W-1 GET /webhook   동적 웹훅 목록 조회 시도 → 403 예상 (PAT 한계 증명)

실행:  uv run python test_webhooks.py
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
)


def main() -> None:
    cfg: Config = load_config()
    client = JiraClient(cfg)
    report = Report(title="Webhook 권한 검증", base_url=cfg.base_url)

    print(f"Jira: {cfg.base_url}")
    print("목적: PAT 로 /rest/api/3/webhook 접근 가능 여부 확인 (403 예상)")
    print("-" * 60)

    # W-1 동적 웹훅 목록 조회 시도.
    # 문서(91-webhooks/01-get-dynamic-webhooks-for-app-get.md)에 따르면
    # "Only Connect and OAuth 2.0 apps can use this operation".
    r = client.get("/webhook", params={"maxResults": cfg.max_results})

    summary = "웹훅 목록 조회 실패"
    sample = None
    web_url = None
    if r.ok and isinstance(r.data, dict):
        values = r.data.get("values") or []
        rows = [{"id": w.get("id"), "url": w.get("url"),
                 "events": w.get("events"),
                 "jqlFilter": w.get("jqlFilter")} for w in values[:5]]
        summary = (f"웹훅 {len(values)}개 (total={r.data.get('total')}) "
                   f"— 예상과 다르게 PAT 로 접근 가능함")
        sample = rows
    elif r.status == 403:
        # 이것이 예상 결과. 검증 "실패"가 아니라 "확인된 제약"으로 기록.
        summary = ("403 — PAT 로는 웹훅 API 접근 불가 (예상된 결과). "
                   "실시간 알림 수신에는 Connect/Forge 앱 또는 OAuth 2.0 연동 필요")
        # 권한 제약은 ok=True 로 기록 (예상된 동작이므로 검증 목적 달성).
        report.add(CheckResult("W-1 동적 웹훅 목록 (GET /webhook)",
                               "GET /webhook",
                               True, r.status, summary, web_url, sample,
                               None, r.elapsed_ms))
        _finalize(report)
        return

    report.add(CheckResult("W-1 동적 웹훅 목록 (GET /webhook)",
                           "GET /webhook",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")
    print("\n참고: PAT 로 웹훅이 막혔다면, 실시간 이벤트 수신을 위해서는")
    print("  - Forge/Connect 앱 등록, 또는")
    print("  - OAuth 2.0 (3LO) 앱으로 webhook 구독 등록이 필요합니다.")


if __name__ == "__main__":
    main()
