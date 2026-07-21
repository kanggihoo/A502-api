"""OAuth2 토큰 상태·갱신 동작 검증 스크립트.

GITLAB_AUTH_METHOD=oauth2 일 때 현재 access_token 이 유효한지, refresh_token 으로
갱신이 잘 되는지 확인한다. PAT 모드에서는 이 스크립트가 의미 없으므로 안내만 출력하고
종료한다.

검증 항목:
  O-1 GET /user              access_token 유효성 (Authorization: Bearer 헤더)
  O-2 수동 refresh 시도       refresh_token 유효성 + rotate-on-use 동작 확인
  O-3 GET /user (갱신 후)     새 access_token 유효성

주의:
- refresh 호출은 GitLab 의 rotate-on-use 정책으로 기존 access/refresh 토큰을 모두
  무효화한다. 이 스크립트는 refresh 성공 시 .env 의 토큰을 자동으로 덮어쓴다
  (gitlab_client._persist_oauth_tokens).
- access_token 이 아직 유효해도 O-2 에서 강제 refresh 를 시도한다(만료 임박이 아니어도).
  이것이 싫으면 .env 의 GITLAB_OAUTH_REFRESH_TOKEN 을 비워 자동 갱신을 끄면 된다.

실행:  uv run python test_oauth2_tokens.py
"""

from __future__ import annotations

from pathlib import Path

import requests

from gitlab_client import (
    CheckResult,
    Config,
    GitLabClient,
    Report,
    _persist_oauth_tokens,
    load_config,
)


def main() -> None:
    cfg: Config = load_config()
    report = Report(title="OAuth2 토큰 검증", base_url=cfg.base_url)

    print(f"GitLab: {cfg.base_url}")
    print(f"인증 방식: {cfg.auth_method}")
    print("-" * 60)

    if cfg.auth_method != "oauth2":
        print("GITLAB_AUTH_METHOD 가 oauth2 가 아닙니다 "
              f"(현재: {cfg.auth_method!r}).")
        print("이 스크립트는 OAuth2 토큰 검증용입니다. PAT 모드에서는 생략하세요.")
        report.add(CheckResult(
            "OAuth2 모드 여부", "GITLAB_AUTH_METHOD env", False, None,
            f"auth_method={cfg.auth_method!r} — OAuth2 검증 불필요",
            None, None, None, 0))
        _finalize(report)
        return

    client = GitLabClient(cfg)

    # ========================================================================
    # O-1 현재 access_token 유효성 (Bearer 헤더)
    # ========================================================================
    r = client.get("/user")
    summary = "access_token 검증 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        u = r.data
        sample = u
        summary = (f"access_token 유효 — @{u.get('username')} (id={u.get('id')}) "
                   f"state={u.get('state')}")
    elif r.status == 401:
        summary = "401 — access_token 만료 또는 무효 (아래 O-2 refresh 로 갱신 시도)"
    report.add(CheckResult("O-1 access_token 유효성",
                           "GET /user (Authorization: Bearer)",
                           r.ok, r.status, summary,
                           r.data.get("web_url") if isinstance(r.data, dict) else None,
                           sample, r.error, r.elapsed_ms))

    # ========================================================================
    # O-2 수동 refresh 시도
    # ========================================================================
    if not cfg.can_refresh:
        report.add(CheckResult(
            "O-2 refresh 시도", "POST /oauth/token (grant_type=refresh_token)",
            False, None,
            "refresh 불가 — GITLAB_OAUTH_REFRESH_TOKEN 또는 GITLAB_OAUTH_CLIENT_ID 누락",
            None, None, None, 0))
        report.add(CheckResult(
            "O-3 갱신 후 재검증", "GET /user", False, None,
            "갱신 안 됨 — 스킵", None, None, None, 0))
        _finalize(report)
        return

    token_url = f"{cfg.base_url.rstrip('/')}/oauth/token"
    data = {
        "client_id": cfg.oauth_client_id,
        "refresh_token": cfg.oauth_refresh_token,
        "grant_type": "refresh_token",
    }
    if cfg.oauth_client_secret:
        data["client_secret"] = cfg.oauth_client_secret
    if cfg.oauth_redirect_uri:
        data["redirect_uri"] = cfg.oauth_redirect_uri

    try:
        resp = requests.post(token_url, data=data, timeout=cfg.timeout)
        body: object = None
        try:
            body = resp.json() if resp.content else None
        except ValueError:
            body = None
        ok = 200 <= resp.status_code < 300
        summary = "refresh 실패"
        sample = None
        if ok and isinstance(body, dict):
            new_access = body.get("access_token")
            new_refresh = body.get("refresh_token") or cfg.oauth_refresh_token
            # refresh 성공 → cfg 와 .env 에 영속화 (rotate-on-use 대응).
            if new_access:
                cfg.oauth_access_token = new_access
                cfg.oauth_refresh_token = new_refresh
                _persist_oauth_tokens(new_access, new_refresh)
                client._apply_auth_header()
            sample = body
            summary = (f"refresh 성공 — 새 access_token 발급 "
                       f"(expires_in={body.get('expires_in')}s, "
                       f"scope={body.get('scope')!r}, .env 동기화됨)")
        elif not ok:
            err_msg = body.get("error") if isinstance(body, dict) else None
            err_desc = (body.get("error_description") if isinstance(body, dict)
                        else None) or str(body)[:120]
            summary = (f"refresh 실패 HTTP {resp.status_code} "
                       f"error={err_msg!r} ({err_desc})")
        report.add(CheckResult("O-2 refresh 시도",
                               "POST /oauth/token (grant_type=refresh_token)",
                               ok, resp.status_code, summary, None, sample,
                               None if ok else summary, 0))
    except requests.RequestException as exc:
        report.add(CheckResult("O-2 refresh 시도",
                               "POST /oauth/token (grant_type=refresh_token)",
                               False, None,
                               f"네트워크 오류: {exc.__class__.__name__}: {exc}",
                               None, None, str(exc), 0))
        report.add(CheckResult("O-3 갱신 후 재검증", "GET /user",
                               False, None, "네트워크 오류로 스킵",
                               None, None, None, 0))
        _finalize(report)
        return

    # ========================================================================
    # O-3 갱신 후 새 access_token 유효성 재확인
    # ========================================================================
    r = client.get("/user")
    summary = "갱신 후 재검증 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        u = r.data
        sample = u
        summary = (f"새 access_token 유효 — @{u.get('username')} (id={u.get('id')})")
    elif r.status == 401:
        summary = "401 — refresh 는 성공했으나 새 토큰이 거부됨 (scope/앱 설정 확인)"
    report.add(CheckResult("O-3 갱신 후 재검증",
                           "GET /user (new access_token)",
                           r.ok, r.status, summary,
                           r.data.get("web_url") if isinstance(r.data, dict) else None,
                           sample, r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
