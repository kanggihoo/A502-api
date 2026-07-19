"""Mattermost incoming webhook 구성 + (옵션)전송 검증.

api-docs/mattermost-api-priority-filter.md 의 "첫 API 검증 순서" 2단계(webhooks)를
실제 PAT 로 수행한다. 이 스크립트는 쓰기(POST)를 수행한다.

중요 설계 결정:
- 생성한 incoming webhook은 **삭제하지 않고 남겨둔다.** 이 webhook은 통합 서비스가
  실제로 사용할 연동 수단이기 때문이다. (GitLab/Jira/Jenkins 이벤트 수신용)
- webhook으로 실제 메시지 전송(ping)은 MATTERMOST_WEBHOOK_URL 환경변수가 설정된
  경우에만 수행한다. webhook 생성 응답에는 token이 없어 전송 URL을 자동 조립할 수
  없으므로, Mattermost UI에서 복사한 전체 URL이 필요하다.

검증 항목:
  W-1 GET /hooks/incoming?team_id={team_id}   기존 incoming webhook 목록 (manage_webhooks 권한)
  W-2 POST /hooks/incoming                    incoming webhook 생성 (남겨둠, 삭제 X)
  W-3 (옵션) POST {webhook_url}               webhook 전송(ping). WEBHOOK_URL 설정 시만.

실행:  uv run python test_webhooks.py
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from mattermost_client import (
    ApiResponse,
    CheckResult,
    Config,
    MattermostClient,
    Report,
    channel_web_url,
    load_config,
)


def main() -> None:
    cfg: Config = load_config()
    client = MattermostClient(cfg)
    report = Report(title="Webhook 구성 및 전송 검증", base_url=cfg.base_url)

    print(f"Mattermost: {cfg.base_url}")
    print("주의: 이 스크립트는 incoming webhook을 생성합니다(삭제하지 않음).")
    print("-" * 60)

    # 대상 팀/채널 확정 (둘 다 필요).
    _, team_id = client.resolve_team()
    _, channel_id = client.resolve_channel(team_id) if team_id else (ApiResponse(True, 0, None, None, 0), None)
    if not team_id or not channel_id:
        report.add(CheckResult("대상 확정", "GET /users/me/teams...", False, None,
                               "대상 팀/채널을 찾을 수 없음", None, None,
                               "MATTERMOST_TEST_TEAM_ID / CHANNEL_ID 확인", 0))
        _finalize(report)
        return

    print(f"대상: team={team_id} channel={channel_id}\n")

    # W-1 기존 incoming webhook 목록 (manage_webhooks 권한 확인).
    r = client.get("/hooks/incoming", params={"team_id": team_id, "per_page": cfg.per_page})
    summary = "webhook 목록 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = [{"id": h.get("id"), "channel_id": h.get("channel_id"),
                 "display_name": h.get("display_name"),
                 "description": (h.get("description") or "")[:40]} for h in r.data[:5]]
        summary = f"기존 incoming webhook {len(r.data)}개"
        sample = rows
    report.add(CheckResult("W-1 기존 incoming webhook 목록",
                           f"GET /hooks/incoming?team_id={team_id}",
                           r.ok, r.status, summary, None, sample, r.error, r.elapsed_ms))

    # W-2 incoming webhook 생성 (남겨둠, 삭제 X).
    ts_label = datetime.now().strftime("%Y%m%d-%H%M%S")
    r = client.post("/hooks/incoming", json_body={
        "channel_id": channel_id,
        "display_name": f"A502 통합 알림 webhook ({ts_label})",
        "description": "POC에서 생성. GitLab/Jira/Jenkins 이벤트 수신용. 삭제 금지.",
        # channel_locked: true 면 webhook이 이 채널에 고정됨.
        "channel_locked": False,
    })
    summary = "webhook 생성 실패"
    sample = None
    webhook_id = None
    web_url = None
    if r.ok and isinstance(r.data, dict):
        h = r.data
        webhook_id = h.get("id")
        summary = (f"생성 성공 id={webhook_id} "
                   f"channel={h.get('channel_id')} "
                   f"display_name={h.get('display_name')}")
        sample = {"id": h.get("id"), "channel_id": h.get("channel_id"),
                  "display_name": h.get("display_name"),
                  "create_at": h.get("create_at")}
        print(f"\n  [생성됨] incoming webhook id: {webhook_id}")
        print(f"  [안내] webhook 전체 URL(전송용)은 Mattermost UI >")
        print(f"         통합(Integrations) > Incoming Webhooks > 해당 webhook 에서 확인하세요.")
    report.add(CheckResult("W-2 incoming webhook 생성 (남겨둠)",
                           "POST /hooks/incoming",
                           r.ok, r.status, summary, web_url, sample, r.error, r.elapsed_ms))

    # W-3 (옵션) webhook 전송(ping). MATTERMOST_WEBHOOK_URL 설정 시만.
    if not cfg.webhook_url:
        report.add(CheckResult("W-3 webhook 전송(ping)", "POST {webhook_url}", False, None,
                               "건너뜀 — MATTERMOST_WEBHOOK_URL 미설정",
                               None, None, None, 0))
    else:
        # webhook 전송은 /api/v4 밖의 URL. _url() 이 절대 URL을 그대로 통과시킴.
        r = client.post(cfg.webhook_url, json_body={
            "text": f"[POC-TEST] A502 통합 알림 webhook 연결 확인 ({ts_label})",
        })
        summary = "전송 실패"
        sample = None
        if r.ok:
            # webhook 전송 성공 응답은 보통 빈 본문 또는 "ok".
            summary = "전송 성공 (채널에 메시지 게시됨)"
            sample = {"webhook_url": cfg.webhook_url, "status": r.status}
        report.add(CheckResult("W-3 webhook 전송(ping)",
                               "POST {MATTERMOST_WEBHOOK_URL}",
                               r.ok, r.status, summary,
                               channel_web_url(cfg.base_url, "", channel_id),
                               sample, r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
