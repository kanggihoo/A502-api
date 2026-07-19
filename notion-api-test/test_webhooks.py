"""Notion webhook 지원 여부 검증 (제약 확인).

api-docs/notion-api-priority-filter.md 의 "초기 범위에서 제외할 항목"에 해당하며,
Notion REST API 는 Mattermost/Jira 와 달리 동적 webhook 등록 API 를 제공하지 않는다.
따라서 이 스크립트는 webhook 등록을 시도하는 대신, "webhook 이 없다는 제약"과
"polling 기반 연동이 필요하다는 사실"을 확인된 정보로 기록한다.

검증 항목:
  W-1 GET /users/me   봇 정체/capability 확인 — webhook 대체 수단 판단의 기준점
  W-2 (문서 기반)     Notion REST API webhook 부재를 확인된 제약으로 기록

참고:
- Notion 은 실시간 이벤트 수신을 공식적으로 지원하지 않는다. 외부 연결이 필요한 경우
  polling(search / data_sources query 를 주기 호출)하거나, Notion 자체 automation/외부
  서비스 연결을 활용해야 한다.

실행:  uv run python test_webhooks.py
"""

from __future__ import annotations

from pathlib import Path

from notion_client import (
    CheckResult,
    Config,
    NotionClient,
    Report,
    load_config,
)


def main() -> None:
    cfg: Config = load_config()
    client = NotionClient(cfg)
    report = Report(title="Webhook 지원 여부 검증 (제약 확인)", base_url=cfg.api_base)

    print(f"Notion: {cfg.api_base}")
    print("목적: Notion REST API 의 webhook 부재를 확인된 제약으로 기록")
    print("-" * 60)

    # W-1 봇 정체/capability 확인. webhook 대체 수단(polling 등)의 기준점.
    r = client.get("/users/me")
    summary = "봇 사용자 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        me = r.data
        bot = me.get("bot") or {}
        owner = bot.get("owner") or {}
        summary = (f"{me.get('name')} (owner.type={owner.get('type')}) — "
                   f"토큰 정상. webhook 대신 polling 으로 변경 감지 필요")
        sample = {"id": me.get("id"), "name": me.get("name"),
                  "owner_type": owner.get("type"),
                  "workspace_id": bot.get("workspace_id")}
    report.add(CheckResult("W-1 봇 정체/capability 확인", "GET /users/me",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # W-2 webhook 부재 — 문서화된 제약을 "확인된 제약" 으로 기록.
    # ok=True 인 것은 검증 목적(제약 확인)을 달성했기 때문. jira-api-test 의
    # test_webhooks.py 가 PAT 403 을 ok 로 기록한 것과 동일한 패턴.
    report.add(CheckResult(
        "W-2 Notion REST API webhook 부재", "(docs: developers.notion.com/reference)",
        True, None,
        "Notion REST API 는 동적 webhook 등록/조회 엔드포인트를 제공하지 않음. "
        "실시간 이벤트 수신이 필요하면 polling(search/data_sources query 주기 호출) "
        "또는 Notion automation/외부 연결을 통해서만 가능.",
        None,
        {"constraint": "no_webhook_api",
         "alternatives": [
             "polling POST /search, POST /data_sources/{id}/query",
             "Notion automations (UI 기반)",
             "외부 서비스 연결 (Zapier/Make 등)",
         ]},
        None, 0))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")
    print("\n참고: Notion 에서 변경 감지가 필요하면")
    print("  - search / data_sources query 를 주기적으로 폴링하거나")
    print("  - Notion automation 또는 외부 연결(Zapier/Make) 검토.")


if __name__ == "__main__":
    main()
