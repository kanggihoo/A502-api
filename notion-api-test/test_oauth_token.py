"""OAuth 2.0 토큰 검증 스크립트.

api-docs/notion-api-priority-filter.md 의 P1 인증/연결 카테고리(03-personal-access-tokens,
04-internal-connections, 06-authorization) 중 OAuth 2.0 부분을 검증한다.

전제:
- 사용자가 Postman 등으로 OAuth 인가 코드 흐름을 거쳐 access_token (과 refresh_token)을
  이미 발급받았다고 가정한다. 절차는 docs/notion-oauth-postman.md 참고.
- NOTION_API_KEY 에는 발급받은 access_token 이 들어 있다.
- NOTION_OAUTH_CLIENT_ID / NOTION_OAUTH_CLIENT_SECRET / NOTION_OAUTH_REFRESH_TOKEN 은
  refresh 검증(선택)에만 필요하다.

검증 항목:
  O-1 GET /users/me   현재 토큰이 OAuth 기반인지 Internal 인지 식별 (bot.owner.type)
  O-2 POST /oauth/token (grant_type=refresh_token)
                      refresh_token 으로 새 access_token/refresh_token 발급 검증
                      (OAuth 변수 없으면 스킵)

주의:
- OAuth 변수가 없으면 O-2 는 스킵하고 안내 메시지만 출력한다.
- 이 스크립트는 access_token/refresh_token 의 값을 로그에 출력하지 않는다.

실행:  uv run python test_oauth_token.py
"""

from __future__ import annotations

import base64
from datetime import datetime
from pathlib import Path

import requests

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
    report = Report(title="OAuth 2.0 토큰 검증", base_url=cfg.api_base)

    print(f"Notion: {cfg.api_base}  (Notion-Version {cfg.api_version})")
    print("목적: 현재 NOTION_API_KEY 의 토큰 종류(OAuth/Internal) 식별 + refresh 흐름 검증")
    print("-" * 60)

    # ---- O-1 현재 토큰 종류 식별 ---------------------------------------------
    # bot.owner.type 이 "user" 이면 OAuth 기반, "workspace" 이면 Internal installation token.
    r = client.get("/users/me")
    summary = "토큰 정체 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        me = r.data
        bot = me.get("bot") or {}
        owner = bot.get("owner") or {}
        owner_type = owner.get("type")
        if owner_type == "user":
            kind = "OAuth 2.0 access_token (user-authorized bot)"
            owner_user = owner.get("user") or {}
            summary = (f"{kind} — bot={me.get('name')!r}, "
                       f"authorized_user={owner_user.get('name')!r} "
                       f"({owner_user.get('person') or {} and 'email 있음'})")
        elif owner_type == "workspace":
            kind = "Internal installation token (workspace-owned bot)"
            summary = (f"{kind} — bot={me.get('name')!r}, "
                       f"workspace={bot.get('workspace_name')!r}")
        else:
            kind = f"알 수 없음 (owner.type={owner_type})"
            summary = kind
        sample = {
            "bot_id": me.get("id"),
            "bot_name": me.get("name"),
            "owner_type": owner_type,
            "token_kind": kind,
            "workspace_name": bot.get("workspace_name"),
            "workspace_id": bot.get("workspace_id"),
        }
    report.add(CheckResult("O-1 토큰 종류 식별", "GET /users/me",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # ---- O-2 refresh token 검증 ---------------------------------------------
    if not cfg.has_oauth_credentials:
        report.add(CheckResult(
            "O-2 refresh_token 갱신", "POST /oauth/token (refresh_token)", True, None,
            "스킵 — NOTION_OAUTH_CLIENT_ID/CLIENT_SECRET/REFRESH_TOKEN 미설정. "
            "refresh 검증이 필요하면 .env 의 OAuth 항목을 채우세요.",
            None, None, None, 0))
        _finalize(report)
        print("\n참고: OAuth code→token 교환 절차는 docs/notion-oauth-postman.md 참고.")
        return

    # refresh 요청. Authorization: Basic base64(CLIENT_ID:CLIENT_SECRET).
    creds = f"{cfg.oauth_client_id}:{cfg.oauth_client_secret}".encode("utf-8")
    basic = base64.b64encode(creds).decode("ascii")
    headers = {
        "Authorization": f"Basic {basic}",
        "Content-Type": "application/json",
        "Notion-Version": cfg.api_version,
    }
    body = {"grant_type": "refresh_token",
            "refresh_token": cfg.oauth_refresh_token}

    started_at = datetime.now()
    try:
        resp = requests.post(f"{cfg.api_base}/oauth/token",
                             headers=headers, json=body, timeout=cfg.timeout)
        ok_flag = 200 <= resp.status_code < 300
        try:
            parsed = resp.json() if resp.content else None
        except ValueError:
            parsed = None
        elapsed_ms = int(resp.elapsed.total_seconds() * 1000)
        if ok_flag and isinstance(parsed, dict):
            # 새 access_token/refresh_token 이 발급됐는지만 확인 (값은 출력하지 않음).
            new_access = parsed.get("access_token")
            new_refresh = parsed.get("refresh_token")
            summary = (f"refresh 성공 — 새 access_token 길이={len(new_access) if new_access else 0}, "
                       f"새 refresh_token 발급={bool(new_refresh)}, "
                       f"bot_id={parsed.get('bot_id')}, "
                       f"workspace_id={parsed.get('workspace_id')}")
            sample = {
                "access_token_length": len(new_access) if new_access else 0,
                "refresh_token_issued": bool(new_refresh),
                "bot_id": parsed.get("bot_id"),
                "workspace_id": parsed.get("workspace_id"),
                "workspace_name": parsed.get("workspace_name"),
                "owner_type": (parsed.get("owner") or {}).get("type")
                              if isinstance(parsed.get("owner"), dict) else None,
            }
            err = None
        else:
            msg = (parsed or {}).get("message") if isinstance(parsed, dict) else resp.reason
            summary = f"refresh 실패 — {resp.status_code} {msg}"
            sample = parsed
            err = summary
        report.add(CheckResult("O-2 refresh_token 갱신", "POST /oauth/token (refresh_token)",
                               ok_flag, resp.status_code, summary, None, sample,
                               err, elapsed_ms))
    except requests.RequestException as exc:
        elapsed_ms = int((datetime.now() - started_at).total_seconds() * 1000)
        report.add(CheckResult("O-2 refresh_token 갱신", "POST /oauth/token (refresh_token)",
                               False, None,
                               f"네트워크 오류: {exc.__class__.__name__}: {exc}",
                               None, None, str(exc), elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
