"""Jira Cloud REST API v3 동작 테스트용 공통 모듈.

설정 로드, HTTP 클라이언트 래퍼, 결과 수집/리포트 기능을 제공한다.
api-docs/jira-api-priority-filter.md 의 "첫 API 검증 순서"를 코드로 검증하기 위한
기반이며, test_p0_readonly.py / test_p1_readonly.py / test_webhooks.py 가 이 모듈을 사용한다.

설계 원칙 (gitlab_client.py 와 동일):
- HTTP 오류가 발생해도 예외로 전체를 중단시키지 않고 (status, error) 로 반환한다.
  검증 목적상 "어느 엔드포인트가 권한 부족(403)으로 막히는지"를 기록하는 것이 중요하다.
- 토큰 등 민감 정보는 로그에 직접 출력하지 않는다.

인증 (OAuth 2.0 3LO):
- access_token 은 "Authorization: Bearer <token>" 헤더로 전달.
- Cloud ID 를 경로에 포함한 게이트웨이 URL 사용
  (https://api.atlassian.com/ex/jira/{cloud_id}/rest/api/3).
- access_token 만료(401) 시 refresh_token 으로 1회 자동 갱신 후 재시도.
  refresh endpoint 는 https://auth.atlassian.com/oauth/token (api. 서브도메인 아님).
  응답의 새 refresh_token 은 rotate-on-use 이므로 .env 에 영속화.
- JQL 에서 username/userkey 는 privacy 상 사용할 수 없으므로 accountId 또는
  currentUser() 함수를 사용한다.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv


@dataclass
class Config:
    """.env 에서 로드한 실행 설정 (OAuth 2.0)."""

    base_url: str          # 웹 브라우저 링크용. 예: https://ssafy.atlassian.net
    oauth_token: str       # OAuth 2.0 Access Token
    cloud_id: str          # Jira Cloud ID (UUID)
    project_key: str | None
    timeout: int
    max_results: int

    # ---- OAuth2 자동 갱신용 (선택) ----
    oauth_refresh_token: str | None
    oauth_client_id: str | None
    oauth_client_secret: str | None

    @property
    def api_base(self) -> str:
        """REST API v3 루트. OAuth 2.0 게이트웨이 주소 사용."""
        return f"https://api.atlassian.com/ex/jira/{self.cloud_id}/rest/api/3"

    @property
    def has_project(self) -> bool:
        return bool(self.project_key)

    @property
    def can_refresh(self) -> bool:
        """OAuth2 자동 갱신 가능 여부. refresh 토큰과 client 정보가 모두 있어야 함."""
        return (
            bool(self.oauth_refresh_token)
            and bool(self.oauth_client_id)
            and bool(self.oauth_client_secret)
        )


def load_config() -> Config:
    """.env 를 읽어 Config 를 만든다. 필수값 누락 시 에러로 안내한다."""
    here = Path(__file__).resolve().parent
    load_dotenv(here / ".env")

    base_url = os.getenv("JIRA_BASE_URL", "").strip().rstrip("/")
    oauth_token = os.getenv("JIRA_OAUTH_TOKEN", "").strip()
    cloud_id = os.getenv("JIRA_CLOUD_ID", "").strip()

    missing = []
    if not base_url:
        missing.append("JIRA_BASE_URL")
    if not oauth_token:
        missing.append("JIRA_OAUTH_TOKEN")
    if not cloud_id:
        missing.append("JIRA_CLOUD_ID")
    if missing:
        raise SystemExit(
            "필수 환경변수가 .env 에 없습니다: " + ", ".join(missing) +
            "\n.env.example 을 복사해 .env 를 만들고 값을 채우세요."
        )

    return Config(
        base_url=base_url,
        oauth_token=oauth_token,
        cloud_id=cloud_id,
        project_key=(os.getenv("JIRA_TEST_PROJECT_KEY", "").strip().upper() or None),
        timeout=int(os.getenv("REQUEST_TIMEOUT", "30") or "30"),
        max_results=int(os.getenv("MAX_RESULTS", "50") or "50"),
        oauth_refresh_token=(os.getenv("JIRA_OAUTH_REFRESH_TOKEN", "").strip() or None),
        oauth_client_id=(os.getenv("JIRA_OAUTH_CLIENT_ID", "").strip() or None),
        oauth_client_secret=(os.getenv("JIRA_OAUTH_CLIENT_SECRET", "").strip() or None),
    )


@dataclass
class ApiResponse:
    """단일 API 호출 결과. 예외 대신 이 객체로 결과를 전달한다."""

    ok: bool                       # 2xx 여부
    status: int | None             # HTTP 상태코드 (네트워크 실패 시 None)
    data: Any                      # 파싱된 JSON(보통 list/dict). 실패 시 None
    error: str | None              # 사람이 읽을 수 있는 에러 설명
    elapsed_ms: int                # 요청 소요 시간(ms)


class JiraClient:
    """Jira Cloud REST API v3 용 얇은 HTTP 래퍼."""

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg
        self.session = requests.Session()
        # OAuth 2.0 Authorization Header: Bearer <token>
        self._apply_auth_header()
        # 401 발생 시 refresh 1회 후 재시도를 위한 가드.
        self._refresh_attempted = False

    def _apply_auth_header(self) -> None:
        """현재 access_token 으로 Authorization 헤더를 (재)설정. refresh 후 새 토큰 반영용."""
        self.session.headers.update({
            "Authorization": f"Bearer {self.cfg.oauth_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def _url(self, path: str) -> str:
        """API 경로를 전체 URL 로 변환. path 가 absolute URL 이면 그대로 반환."""
        if path.startswith("http://") or path.startswith("https://"):
            return path
        return f"{self.cfg.api_base}{path if path.startswith('/') else '/' + path}"

    def _refresh_oauth_token(self) -> bool:
        """OAuth2 refresh_token 으로 access_token 을 갱신한다.

        Atlassian OAuth 2.0 (3LO) refresh endpoint 는 auth.atlassian.com (api. 가 아님).
        응답의 새 refresh_token 은 rotate-on-use 이므로 cfg 와 .env 모두 갱신한다.
        Cloud ID 는 보통 불변이므로 재조회하지 않는다(필요시 호출측에서 별도 처리).
        성공 시 True, 실패/불가 시 False.
        """
        cfg = self.cfg
        if not cfg.can_refresh:
            return False

        # Atlassian token endpoint. (api.atlassian.com 아님에 주의)
        token_url = "https://auth.atlassian.com/oauth/token"
        # Atlassian 은 JSON body 를 받는다 (form-urlencoded 아님).
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
        except requests.RequestException as exc:
            print(f"[oauth2] refresh 네트워크 오류: {exc.__class__.__name__}: {exc}")
            return False

        if not (200 <= resp.status_code < 300):
            err_body = ""
            try:
                err_body = resp.json()
            except ValueError:
                err_body = resp.text[:200]
            print(f"[oauth2] refresh 실패: HTTP {resp.status_code} {err_body}")
            return False

        try:
            tok = resp.json()
        except ValueError:
            print("[oauth2] refresh 응답 JSON 파싱 실패")
            return False

        new_access = tok.get("access_token")
        new_refresh = tok.get("refresh_token") or cfg.oauth_refresh_token
        if not new_access:
            print("[oauth2] refresh 응답에 access_token 없음")
            return False

        # 메모리(cfg) + .env 영속화 (rotate-on-use).
        cfg.oauth_token = new_access
        cfg.oauth_refresh_token = new_refresh
        _persist_oauth_tokens(new_access, new_refresh)
        self._apply_auth_header()
        expires_in = tok.get("expires_in", "?")
        print(f"[oauth2] access_token 갱신됨 (expires_in={expires_in}s, "
              f".env 도 동기화됨)")
        return True

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
    ) -> ApiResponse:
        """요청을 보내고 ApiResponse 로 반환. 예외를 밖으로 던지지 않는다.

        access_token 만료(401) 시 refresh 1회 시도 후 재요청. refresh 불가/실패 시
        401 을 그대로 반환한다.
        """
        resp = self._do_request(method, path, params=params, json_body=json_body)

        if (
            resp.status == 401
            and not self._refresh_attempted
            and self.cfg.can_refresh
        ):
            self._refresh_attempted = True
            if self._refresh_oauth_token():
                resp = self._do_request(method, path, params=params, json_body=json_body)
        return resp

    def _do_request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
    ) -> ApiResponse:
        """실제 HTTP 요청을 수행하고 ApiResponse 로 반환."""
        url = self._url(path)
        started = datetime.now()
        try:
            resp = self.session.request(
                method=method.upper(),
                url=url,
                params=params,
                json=json_body,
                timeout=self.cfg.timeout,
            )
        except requests.RequestException as exc:
            return ApiResponse(
                ok=False, status=None, data=None,
                error=f"네트워크 오류: {exc.__class__.__name__}: {exc}",
                elapsed_ms=int((datetime.now() - started).total_seconds() * 1000),
            )

        elapsed_ms = int(resp.elapsed.total_seconds() * 1000)
        parsed: Any = None
        try:
            parsed = resp.json() if resp.content else None
        except ValueError:
            parsed = None

        ok = 200 <= resp.status_code < 300
        error = None if ok else _describe_error(resp, parsed)
        return ApiResponse(
            ok=ok, status=resp.status_code, data=parsed,
            error=error, elapsed_ms=elapsed_ms,
        )

    # ---- 편의 메서드 ----
    def get(self, path: str, params: dict[str, Any] | None = None) -> ApiResponse:
        return self.request("GET", path, params=params)

    def post(self, path: str, json_body: dict[str, Any] | None = None,
             params: dict[str, Any] | None = None) -> ApiResponse:
        return self.request("POST", path, params=params, json_body=json_body)

    def delete(self, path: str) -> ApiResponse:
        return self.request("DELETE", path)

    # ---- 헬퍼 ----
    def resolve_project(self) -> tuple[ApiResponse, str | None]:
        """대상 프로젝트 키를 결정한다.

        env 에 JIRA_TEST_PROJECT_KEY 가 있으면 그대로 사용(대문자 정규화).
        없으면 /project/search 로 접근 가능한 첫 프로젝트를 자동 선택한다.

        반환: (프로젝트 탐지용 ApiResponse, 결정된 project key)
        """
        if self.cfg.has_project:
            return ApiResponse(True, 0, None, None, 0), self.cfg.project_key

        resp = self.get("/project/search", params={"maxResults": self.cfg.max_results})
        if not resp.ok or not isinstance(resp.data, dict):
            return resp, None
        values = resp.data.get("values")
        if not isinstance(values, list) or not values:
            return resp, None
        return resp, (values[0].get("key") or None)


def _persist_oauth_tokens(access_token: str, refresh_token: str) -> None:
    """refresh 로 받은 새 토큰 쌍을 .env 에 덮어쓴다.

    Atlassian OAuth2 refresh 는 rotate-on-use: 기존 refresh_token 이 무효화된다.
    갱신 후 .env 에 저장하지 않으면 재시작 시 구(무효) 토큰을 쓰게 되므로 영속화 필요.
    .env 가 없으면(예: env 를 다른 방식으로 주입한 경우) 조용히 스킵한다.
    """
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.exists():
        return

    lines = env_path.read_text(encoding="utf-8").splitlines()
    access_written = refresh_written = False
    out: list[str] = []
    for line in lines:
        if line.startswith("JIRA_OAUTH_TOKEN="):
            out.append(f"JIRA_OAUTH_TOKEN={access_token}")
            access_written = True
        elif line.startswith("JIRA_OAUTH_REFRESH_TOKEN="):
            out.append(f"JIRA_OAUTH_REFRESH_TOKEN={refresh_token}")
            refresh_written = True
        else:
            out.append(line)
    if not access_written:
        out.append(f"JIRA_OAUTH_TOKEN={access_token}")
    if not refresh_written:
        out.append(f"JIRA_OAUTH_REFRESH_TOKEN={refresh_token}")

    env_path.write_text("\n".join(out) + "\n", encoding="utf-8")


def _describe_error(resp: requests.Response, parsed: Any) -> str:
    """HTTP 에러 응답을 사람이 읽을 수 있게 요약."""
    hint = ""
    if resp.status_code == 401:
        hint = " (OAuth Access Token이 유효하지 않거나 만료됨)"
    elif resp.status_code == 403:
        hint = " (권한 부족 — 필요 scope/앱 권한 확인 필요)"
    elif resp.status_code == 404:
        hint = " (리소스 없음 — 프로젝트 키/이슈 키 확인)"
    # Jira 에러 응답은 보통 errorMessages 배열.
    msg = None
    if isinstance(parsed, dict):
        em = parsed.get("errorMessages")
        if isinstance(em, list) and em:
            msg = "; ".join(str(x) for x in em)
        elif parsed.get("errors"):
            msg = json.dumps(parsed["errors"], ensure_ascii=False)
    msg = msg or resp.reason
    return f"{resp.status_code} {msg}{hint}"


# ===========================================================================
# 원문 URL 헬퍼 (설계 원칙: 상세 내용은 Jira 원문으로 이동)
# ===========================================================================

def issue_web_url(base_url: str, issue_key: str) -> str:
    """이슈 원문 URL. 예: https://ssafy.atlassian.net/browse/EX-1"""
    return f"{base_url.rstrip('/')}/browse/{issue_key}"


def project_web_url(base_url: str, project_key: str) -> str:
    """프로젝트 보드 URL. 예: https://ssafy.atlassian.net/jira/software/c/projects/EX/boards"""
    return f"{base_url.rstrip('/')}/jira/software/c/projects/{project_key}/boards"


# ===========================================================================
# 결과 수집 및 리포트 (gitlab_client.py 와 동일 구조)
# ===========================================================================

@dataclass
class CheckResult:
    """개별 검증 항목의 결과 레코드."""

    name: str                       # 예: "1-1 현재 사용자"
    endpoint: str                   # 예: "GET /myself"
    ok: bool
    status: int | None
    summary: str                    # 한 줄 요약 (터미널 출력용)
    web_url: str | None = None      # 원문 링크(있으면)
    sample: Any = None              # 대표 응답 조각(리포트 저장용)
    error: str | None = None
    elapsed_ms: int = 0


@dataclass
class Report:
    """전체 검증 세션의 결과 모음."""

    title: str
    base_url: str
    started_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    checks: list[CheckResult] = field(default_factory=list)

    def add(self, result: CheckResult) -> None:
        self.checks.append(result)

    @property
    def passed(self) -> int:
        return sum(1 for c in self.checks if c.ok)

    @property
    def failed(self) -> int:
        return sum(1 for c in self.checks if not c.ok)

    def print_summary(self) -> None:
        print("\n" + "=" * 60)
        print(f"{self.title} — 결과 요약")
        print("=" * 60)
        for c in self.checks:
            mark = "✓" if c.ok else "✗"
            status = c.status if c.status is not None else "NET"
            print(f"  {mark} [{status:>3}] {c.name}")
            print(f"        {c.endpoint}  ({c.elapsed_ms}ms)")
            print(f"        → {c.summary}")
            if c.error:
                print(f"        !! {c.error}")
        print("-" * 60)
        print(f"통과 {self.passed} / 실패 {self.failed} / 총 {len(self.checks)}")
        print("=" * 60)

    def save(self, results_dir: Path) -> Path:
        """결과를 타임스탬프 JSON 파일로 저장. 저장 경로를 반환한다."""
        results_dir.mkdir(exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        slug = _slugify(self.title)
        path = results_dir / f"{slug}_{ts}.json"
        payload = {
            "title": self.title,
            "base_url": self.base_url,
            "started_at": self.started_at,
            "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "totals": {"passed": self.passed, "failed": self.failed, "total": len(self.checks)},
            "checks": [c.__dict__ for c in self.checks],
        }
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return path


def _slugify(text: str) -> str:
    keep = [ch if (ch.isalnum() or ch in "-_") else "_" for ch in text]
    return "".join(keep).strip("_") or "report"
