"""GitLab REST API 동작 테스트용 공통 모듈.

설정 로드, HTTP 클라이언트 래퍼, 결과 수집/리포트 기능을 제공한다.
api-docs/gitlab-api-priority-filter.md 의 "첫 API 검증 순서"를 코드로 검증하기 위한
기반이며, test_p0_readonly.py 와 test_webhooks.py 가 이 모듈을 사용한다.

설계 원칙:
- HTTP 오류가 발생해도 예외로 전체를 중단시키지 않고 (status, error) 로 반환한다.
  검증 목적상 "어느 엔드포인트가 권한 부족(403)으로 막히는지"를 기록하는 것이 중요하다.
- 토큰 등 민감 정보는 로그에 직접 출력하지 않는다.

인증 방식 (GITLAB_AUTH_METHOD env 로 선택):
- "pat" (기본값): Personal Access Token. 헤더 PRIVATE-TOKEN: <token>.
  기존 동작. 1회성 스크립트·긴급 디버그 용도.
- "oauth2": OAuth2 access_token. 헤더 Authorization: Bearer <access_token>.
  사용자가 Postman 등으로 Authorization Code + PKCE flow 를 거쳐 얻은 토큰을
  .env 의 GITLAB_OAUTH_ACCESS_TOKEN 에 넣는 구조. access_token 만료(401) 시
  refresh_token 으로 1회 자동 갱신 후 재시도. priority-filter.md 의 "POC 는
  처음부터 OAuth2" 방향에 부합.
"""

from __future__ import annotations

import json
import os
import urllib.parse
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv


# GitLab access_level → 사람이 읽기 쉬운 역할 이름.
# 멤버 조회 결과의 access_level 을 해석할 때 사용한다.
# SSAFY 팀 구성 가정: 팀장 Maintainer(40) / 팀원 Developer(30)
ACCESS_LEVEL_LABELS = {
    5: "Guest",
    10: "Reporter",
    20: "Reporter",
    30: "Developer",
    40: "Maintainer",
    50: "Owner",
}


@dataclass
class Config:
    """.env 에서 로드한 실행 설정."""

    base_url: str
    project_id: str | None
    timeout: int
    per_page: int
    webhook_test_url: str | None

    # ---- 인증 ----
    auth_method: str                      # "pat" 또는 "oauth2"
    # PAT 모드
    pat_token: str | None
    # OAuth2 모드
    oauth_access_token: str | None
    oauth_refresh_token: str | None
    oauth_client_id: str | None
    oauth_client_secret: str | None
    oauth_redirect_uri: str | None

    @property
    def api_base(self) -> str:
        """API 루트. 예: https://lab.ssafy.com/api/v4"""
        return f"{self.base_url.rstrip('/')}/api/v4"

    @property
    def has_project(self) -> bool:
        return bool(self.project_id)

    def authorization_header(self) -> dict[str, str]:
        """인증 방식에 따른 요청 헤더를 반환.

        - pat:    {"PRIVATE-TOKEN": "<token>"}
        - oauth2: {"Authorization": "Bearer <access_token>"}
        """
        if self.auth_method == "oauth2":
            return {"Authorization": f"Bearer {self.oauth_access_token}"}
        # 기본(pat). PAT 가 없으면 빈 값이라도 두어 에러를 명확히.
        return {"PRIVATE-TOKEN": self.pat_token or ""}

    @property
    def can_refresh(self) -> bool:
        """OAuth2 자동 갱신 가능 여부. refresh 토큰·client 정보가 모두 있어야 함."""
        return (
            self.auth_method == "oauth2"
            and bool(self.oauth_refresh_token)
            and bool(self.oauth_client_id)
        )


def _read_env(name: str) -> str:
    return os.getenv(name, "").strip()


def load_config() -> Config:
    """.env 를 읽어 Config 를 만든다. 필수값 누락 시 에러로 안내한다."""
    here = Path(__file__).resolve().parent
    load_dotenv(here / ".env")

    base_url = _read_env("GITLAB_BASE_URL").rstrip("/")
    if not base_url:
        raise SystemExit(
            "필수 환경변수가 .env 에 없습니다: GITLAB_BASE_URL\n"
            ".env.example 을 복사해 .env 를 만들고 값을 채우세요."
        )

    auth_method = _read_env("GITLAB_AUTH_METHOD").lower() or "pat"
    if auth_method not in ("pat", "oauth2"):
        raise SystemExit(
            f"GITLAB_AUTH_METHOD 가 잘못되었습니다: {auth_method!r} (pat 또는 oauth2)"
        )

    pat_token = _read_env("GITLAB_TOKEN") or None
    oauth_access_token = _read_env("GITLAB_OAUTH_ACCESS_TOKEN") or None
    oauth_refresh_token = _read_env("GITLAB_OAUTH_REFRESH_TOKEN") or None
    oauth_client_id = _read_env("GITLAB_OAUTH_CLIENT_ID") or None
    oauth_client_secret = _read_env("GITLAB_OAUTH_CLIENT_SECRET") or None
    oauth_redirect_uri = _read_env("GITLAB_OAUTH_REDIRECT_URI") or None

    # 선택한 인증 방식의 토큰이 비어 있으면 명시적으로 에러.
    if auth_method == "pat" and not pat_token:
        raise SystemExit(
            "GITLAB_AUTH_METHOD=pat 인데 GITLAB_TOKEN 이 비어 있습니다.\n"
            "PAT 를 발급해 .env 의 GITLAB_TOKEN 에 넣거나, OAuth2 를 쓰려면 "
            "GITLAB_AUTH_METHOD=oauth2 로 설정하세요."
        )
    if auth_method == "oauth2" and not oauth_access_token:
        raise SystemExit(
            "GITLAB_AUTH_METHOD=oauth2 인데 GITLAB_OAUTH_ACCESS_TOKEN 이 비어 있습니다.\n"
            "Postman 등으로 OAuth2 flow 를 거쳐 얻은 access_token 을 .env 에 넣으세요."
        )

    return Config(
        base_url=base_url,
        project_id=(_read_env("GITLAB_TEST_PROJECT_ID") or None),
        timeout=int(_read_env("REQUEST_TIMEOUT") or "30"),
        per_page=int(_read_env("PER_PAGE") or "20"),
        webhook_test_url=(_read_env("WEBHOOK_TEST_URL") or None),
        auth_method=auth_method,
        pat_token=pat_token,
        oauth_access_token=oauth_access_token,
        oauth_refresh_token=oauth_refresh_token,
        oauth_client_id=oauth_client_id,
        oauth_client_secret=oauth_client_secret,
        oauth_redirect_uri=oauth_redirect_uri,
    )


@dataclass
class ApiResponse:
    """단일 API 호출 결과. 예외 대신 이 객체로 결과를 전달한다."""

    ok: bool                       # 2xx 여부
    status: int | None             # HTTP 상태코드 (네트워크 실패 시 None)
    data: Any                      # 파싱된 JSON(보통 list/dict). 실패 시 None
    error: str | None              # 사람이 읽을 수 있는 에러 설명
    elapsed_ms: int                # 요청 소요 시간(ms)


class GitLabClient:
    """GitLab REST API 용 얇은 HTTP 래퍼."""

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg
        self.session = requests.Session()
        # 인증 방식에 따라 헤더 세팅. (PAT: PRIVATE-TOKEN, OAuth2: Authorization Bearer)
        self._apply_auth_header()
        # 401 발생 시 refresh 1회 후 재시도를 위한 가드.
        self._refresh_attempted = False

    def _apply_auth_header(self) -> None:
        """현재 토큰으로 세션 헤더를 (재)설정. refresh 후 새 토큰 반영용."""
        # 기존 인증 헤더 제거 후 다시 세팅 (PAT↔Bearer 전환/갱신 시 누적 방지).
        self.session.headers.pop("PRIVATE-TOKEN", None)
        self.session.headers.pop("Authorization", None)
        self.session.headers.update(self.cfg.authorization_header())

    def _url(self, path: str) -> str:
        """API 경로를 전체 URL 로 변환. path 는 '/user' 처럼 슬래시로 시작."""
        return f"{self.cfg.api_base}{path if path.startswith('/') else '/' + path}"

    def _refresh_oauth_token(self) -> bool:
        """OAuth2 refresh_token 으로 access_token 을 갱신한다.

        GitLab 의 refresh 는 rotate-on-use: 기존 access/refresh 둘 다 무효화되고
        새 쌍이 발급된다. 따라서 갱신 성공 시 cfg 와 .env 를 모두 갱신한다.
        성공 시 True, 실패/불가 시 False.
        """
        cfg = self.cfg
        if not cfg.can_refresh:
            return False

        token_url = f"{cfg.base_url.rstrip('/')}/oauth/token"
        data = {
            "client_id": cfg.oauth_client_id,
            "refresh_token": cfg.oauth_refresh_token,
            "grant_type": "refresh_token",
        }
        # confidential 앱이면 client_secret 포함 (Postman flow 와 동일).
        if cfg.oauth_client_secret:
            data["client_secret"] = cfg.oauth_client_secret
        if cfg.oauth_redirect_uri:
            data["redirect_uri"] = cfg.oauth_redirect_uri

        try:
            resp = requests.post(token_url, data=data, timeout=cfg.timeout)
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

        # 메모리(cfg) 갱신.
        cfg.oauth_access_token = new_access
        cfg.oauth_refresh_token = new_refresh
        # .env 파일 갱신 (rotate-on-use 이므로 저장하지 않으면 재시작 시 구 토큰 사용).
        _persist_oauth_tokens(new_access, new_refresh)
        # 세션 헤더도 새 토큰으로.
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

        OAuth2 모드에서 401 Unauthorized 가 돌아오면 refresh 1회 시도 후 재요청.
        PAT 모드이거나 refresh 불가/실패 시 401 을 그대로 반환한다.
        """
        resp = self._do_request(method, path, params=params, json_body=json_body)

        # OAuth2 자동 갱신: 401 이고 아직 시도 안 했고 refresh 가능할 때만.
        if (
            resp.status == 401
            and not self._refresh_attempted
            and self.cfg.auth_method == "oauth2"
            and self.cfg.can_refresh
        ):
            self._refresh_attempted = True
            if self._refresh_oauth_token():
                # 새 access_token 으로 1회 재시도.
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

    def post(self, path: str, json_body: dict[str, Any] | None = None) -> ApiResponse:
        return self.request("POST", path, json_body=json_body)

    def delete(self, path: str) -> ApiResponse:
        return self.request("DELETE", path)

    def get_text(self, path: str, params: dict[str, Any] | None = None) -> ApiResponse:
        """raw 텍스트 응답 전용 GET (예: /repository/files/.../raw, /jobs/{id}/trace).

        기본 request() 는 JSON 파싱만 시도한다. raw 파일 응답(Content-Type: text/plain)
        은 JSON 이 아니어서 parsed 가 None 이 된다. 이 메서드는 본문을 문자열 그대로
        ApiResponse.data 에 담아 반환한다.

        대용량 응답(trace 등)은 params 의 byte_offset/byte_limit 로 잘라 호출할 것.
        """
        url = self._url(path)
        started = datetime.now()
        try:
            resp = self.session.request(
                method="GET", url=url, params=params, timeout=self.cfg.timeout,
            )
        except requests.RequestException as exc:
            return ApiResponse(
                ok=False, status=None, data=None,
                error=f"네트워크 오류: {exc.__class__.__name__}: {exc}",
                elapsed_ms=int((datetime.now() - started).total_seconds() * 1000),
            )

        elapsed_ms = int(resp.elapsed.total_seconds() * 1000)
        # 텍스트를 그대로 data 에. 빈 본문이면 빈 문자열.
        text = resp.text if resp.content else ""
        ok = 200 <= resp.status_code < 300
        error = None if ok else _describe_error(resp, None)
        return ApiResponse(
            ok=ok, status=resp.status_code, data=text,
            error=error, elapsed_ms=elapsed_ms,
        )

    # ---- 헬퍼 ----
    def resolve_project(self) -> tuple[ApiResponse, str | None]:
        """대상 프로젝트 식별자(id 또는 경로)를 결정한다.

        env 에 GITLAB_TEST_PROJECT_ID 가 있으면 그대로 사용.
        없으면 membership=true 로 접근 가능한 첫 프로젝트를 자동 선택한다.

        반환: (프로젝트 목록/탐지용 ApiResponse, 결정된 project 식별자)
        """
        if self.cfg.has_project:
            # 식별자가 경로 형식(슬래시 포함)이면 URL path 에 넣기 전 인코딩.
            pid = encode_project_id(self.cfg.project_id)
            return ApiResponse(True, 0, None, None, 0), pid

        resp = self.get("/projects", params={"membership": "true", "per_page": self.cfg.per_page})
        if not resp.ok or not isinstance(resp.data, list) or not resp.data:
            return resp, None
        first = resp.data[0]
        # path_with_namespace 를 인코딩해 경로 식별자로 사용.
        return resp, encode_project_id(first.get("path_with_namespace") or str(first.get("id")))


def _persist_oauth_tokens(access_token: str, refresh_token: str) -> None:
    """refresh 로 받은 새 토큰 쌍을 .env 에 덮어쓴다.

    GitLab OAuth2 refresh 는 rotate-on-use: 기존 토큰이 무효화된다. 갱신 후 .env 에
    저장하지 않으면 프로세스 재시작 시 구(무효) 토큰을 쓰게 되므로 영속화가 필요하다.

    .env 가 없으면(예: env 를 다른 방식으로 주입한 경우) 조용히 스킵한다.
    """
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.exists():
        return

    lines = env_path.read_text(encoding="utf-8").splitlines()
    access_written = refresh_written = False
    out: list[str] = []
    for line in lines:
        if line.startswith("GITLAB_OAUTH_ACCESS_TOKEN="):
            out.append(f"GITLAB_OAUTH_ACCESS_TOKEN={access_token}")
            access_written = True
        elif line.startswith("GITLAB_OAUTH_REFRESH_TOKEN="):
            out.append(f"GITLAB_OAUTH_REFRESH_TOKEN={refresh_token}")
            refresh_written = True
        else:
            out.append(line)
    # 키가 .env 에 없으면 맨 뒤에 추가.
    if not access_written:
        out.append(f"GITLAB_OAUTH_ACCESS_TOKEN={access_token}")
    if not refresh_written:
        out.append(f"GITLAB_OAUTH_REFRESH_TOKEN={refresh_token}")

    env_path.write_text("\n".join(out) + "\n", encoding="utf-8")


def _describe_error(resp: requests.Response, parsed: Any) -> str:
    """HTTP 에러 응답을 사람이 읽을 수 있게 요약."""
    hint = ""
    if resp.status_code == 401:
        hint = " (토큰이 유효하지 않거나 만료됨)"
    elif resp.status_code == 403:
        hint = " (권한 부족 — 필요 scope/역할 확인 필요)"
    elif resp.status_code == 404:
        hint = " (리소스 없음 — 프로젝트 ID/경로 확인)"
    msg = parsed.get("message") if isinstance(parsed, dict) else None
    msg = msg or (parsed.get("error") if isinstance(parsed, dict) else None) or resp.reason
    return f"{resp.status_code} {msg}{hint}"


def encode_project_id(project_id: str) -> str:
    """프로젝트 식별자를 URL path 세그먼트에 안전하게 인코딩.

    숫자 ID 는 그대로, 'group/sub/project' 같은 경로는 슬래시를 %2F 로 인코딩한다.
    """
    pid = str(project_id).strip()
    if pid.isdigit():
        return pid
    # 이미 인코딩된 %2F 가 있으면 다시 인코딩하지 않도록 quote 로 처리.
    return urllib.parse.quote(pid, safe="")


# ===========================================================================
# 결과 수집 및 리포트
# ===========================================================================

@dataclass
class CheckResult:
    """개별 검증 항목의 결과 레코드."""

    name: str                       # 예: "1-1 현재 사용자"
    endpoint: str                   # 예: "GET /user"
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


def access_label(level: Any) -> str:
    """access_level 숫자 → 역할 라벨. 모르는 값은 원시값을 표시."""
    try:
        n = int(level)
    except (TypeError, ValueError):
        return str(level)
    return ACCESS_LEVEL_LABELS.get(n, f"level_{n}")
