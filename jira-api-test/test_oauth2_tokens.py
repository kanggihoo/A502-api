"""OAuth2 access_token 상태·갱신 동작 검증 스크립트.

현재 JIRA_OAUTH_TOKEN 이 유효한지, refresh_token 으로 갱신이 잘 되는지 확인한다.
refresh 설정(.env 의 REFRESH_TOKEN/CLIENT_ID/CLIENT_SECRET)이 없으면 O-1 만 수행하고 종료.

검증 항목:
  O-1 GET /myself                       access_token 유효성 (Authorization: Bearer)
  O-2 수동 refresh (auth.atlassian.com) refresh_token 유효성 + rotate-on-use 동작
  O-3 GET /myself (갱신 후)             새 access_token 유효성

주의:
- Atlassian OAuth2 refresh endpoint 는 auth.atlassian.com/oauth/token (api. 가 아님).
- 응답의 새 refresh_token 은 rotate-on-use 이므로, refresh 성공 시 .env 의 토큰 값을
  자동으로 덮어쓴다 (jira_client._persist_oauth_tokens).
- access_token 이 아직 유효해도 O-2 에서 강제 refresh 를 시도한다. 이것이 싫으면
  .env 의 JIRA_OAUTH_REFRESH_TOKEN 을 비우면 된다.

실행:  uv run python test_oauth2_tokens.py
"""

from __future__ import annotations

from pathlib import Path

import requests

from jira_client import (
    CheckResult,
    Config,
    JiraClient,
    Report,
    _persist_oauth_tokens,
    load_config,
)


def main() -> None:
    cfg: Config = load_config()
    client = JiraClient(cfg)
    report = Report(title="OAuth2 토큰 검증", base_url=cfg.base_url)

    print(f"Jira: {cfg.base_url} (cloud_id={cfg.cloud_id[:8]}...)")
    print(f"자동 갱신 가능: {cfg.can_refresh}")
    print("-" * 60)

    # ========================================================================
    # O-1 현재 access_token 유효성 (Bearer 헤더)
    # ========================================================================
    # /myself 는 access_token 의 정체를 가장 명확히 보여줌 (accountId/displayName).
    r = client.get("/myself")
    summary = "access_token 검증 실패"
    sample = None
    web_url = None
    if r.ok and isinstance(r.data, dict):
        u = r.data
        sample = {"accountId": u.get("accountId"),
                  "displayName": u.get("displayName"),
                  "emailAddress": u.get("emailAddress"),
                  "active": u.get("active"),
                  "accountType": u.get("accountType")}
        summary = (f"access_token 유효 — {u.get('displayName')} "
                   f"(accountId={u.get('accountId')}) active={u.get('active')}")
    elif r.status == 401:
        summary = "401 — access_token 만료 또는 무효 (아래 O-2 refresh 로 갱신 시도)"
    report.add(CheckResult("O-1 access_token 유효성",
                           "GET /myself (Authorization: Bearer)",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # O-2 수동 refresh 시도
    # ========================================================================
    if not cfg.can_refresh:
        report.add(CheckResult(
            "O-2 refresh 시도", "POST auth.atlassian.com/oauth/token", False, None,
            "refresh 불가 — JIRA_OAUTH_REFRESH_TOKEN / CLIENT_ID / CLIENT_SECRET 누락. "
            "Postman 등에서 받은 값으로 .env 를 채우면 자동 갱신 동작.",
            None, None, None, 0))
        report.add(CheckResult(
            "O-3 갱신 후 재검증", "GET /myself", False, None,
            "갱신 안 됨 — 스킵", None, None, None, 0))
        _finalize(report)
        return

    # Atlassian token endpoint (api. 가 아님, auth. 서브도메인).
    token_url = "https://auth.atlassian.com/oauth/token"
    body = {
        "grant_type": "refresh_token",
        "client_id": cfg.oauth_client_id,
        "client_secret": cfg.oauth_client_secret,
        "refresh_token": cfg.oauth_refresh_token,
    }

    try:
        resp = requests.post(
            token_url, json=body,
            headers={"Content-Type": "application/json"},
            timeout=cfg.timeout,
        )
        tok: object = None
        try:
            tok = resp.json() if resp.content else None
        except ValueError:
            tok = None
        ok = 200 <= resp.status_code < 300
        summary = "refresh 실패"
        sample = None
        if ok and isinstance(tok, dict):
            new_access = tok.get("access_token")
            new_refresh = tok.get("refresh_token") or cfg.oauth_refresh_token
            if new_access:
                # 메모리(cfg) + .env 영속화 (rotate-on-use 대응).
                cfg.oauth_token = new_access
                cfg.oauth_refresh_token = new_refresh
                _persist_oauth_tokens(new_access, new_refresh)
                client._apply_auth_header()
            sample = {
                "access_token": "***" if new_access else None,
                "refresh_token": "***" if tok.get("refresh_token") else "(재사용)",
                "expires_in": tok.get("expires_in"),
                "scope": tok.get("scope"),
                "env_persisted": bool(new_access),
            }
            summary = (f"refresh 성공 — 새 access_token 발급 "
                       f"(expires_in={tok.get('expires_in')}s, "
                       f"scope={tok.get('scope')!r}, .env 동기화됨)")
        elif not ok:
            err = tok.get("error") if isinstance(tok, dict) else None
            err_desc = (tok.get("error_description") if isinstance(tok, dict)
                        else None) or str(tok)[:120]
            summary = (f"refresh 실패 HTTP {resp.status_code} "
                       f"error={err!r} ({err_desc})")
        report.add(CheckResult("O-2 refresh 시도",
                               "POST auth.atlassian.com/oauth/token",
                               ok, resp.status_code, summary, None, sample,
                               None if ok else summary, 0))
    except requests.RequestException as exc:
        report.add(CheckResult("O-2 refresh 시도",
                               "POST auth.atlassian.com/oauth/token",
                               False, None,
                               f"네트워크 오류: {exc.__class__.__name__}: {exc}",
                               None, None, str(exc), 0))
        report.add(CheckResult("O-3 갱신 후 재검증", "GET /myself",
                               False, None, "네트워크 오류로 스킵",
                               None, None, None, 0))
        _finalize(report)
        return

    # ========================================================================
    # O-3 갱신 후 새 access_token 유효성 재확인
    # ========================================================================
    r = client.get("/myself")
    summary = "갱신 후 재검증 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        u = r.data
        sample = {"accountId": u.get("accountId"),
                  "displayName": u.get("displayName")}
        summary = (f"새 access_token 유효 — {u.get('displayName')} "
                   f"(accountId={u.get('accountId')})")
    elif r.status == 401:
        summary = "401 — refresh 는 성공했으나 새 토큰이 거부됨 (scope/앱 설정 확인)"
    report.add(CheckResult("O-3 갱신 후 재검증",
                           "GET /myself (new access_token)",
                           r.ok, r.status, summary,
                           r.data.get("self") if isinstance(r.data, dict) else None,
                           sample, r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
