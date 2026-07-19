"""Notion REST API 동작 테스트용 공통 모듈.

설정 로드, HTTP 클라이언트 래퍼, 결과 수집/리포트 기능을 제공한다.
api-docs/notion-api-priority-filter.md 의 "첫 검증 순서"를 코드로 검증하기 위한
기반이며, test_p0_readonly.py / test_p1_readonly.py / test_oauth_token.py /
test_webhooks.py 가 이 모듈을 사용한다.

설계 원칙 (jira_client.py / gitlab_client.py 와 동일):
- HTTP 오류가 발생해도 예외로 전체를 중단시키지 않고 (status, error) 로 반환한다.
  검증 목적상 "어느 엔드포인트가 권한 부족(403)으로 막히는지"를 기록하는 것이 중요하다.
- 토큰 등 민감 정보는 로그에 직접 출력하지 않는다.

인증 (token-agnostic):
- .env 의 NOTION_API_KEY 는 Internal installation token 또는 OAuth 2.0 access_token
  어느 쪽이든 상관없이 "Authorization: Bearer <token>" 헤더로 전달된다.
- OAuth 토큰 획득 절차 자체는 본 스크립트 범위가 아니며, Postman 등으로 발급받은
  access_token 을 NOTION_API_KEY 에 넣는 것을 전제로 한다.
- 모든 요청에 Notion-Version 헤더가 필요하다.
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


DEFAULT_API_BASE = "https://api.notion.com/v1"
DEFAULT_API_VERSION = "2026-03-11"


@dataclass
class Config:
    """.env 에서 로드한 실행 설정."""

    api_key: str                 # Bearer 토큰 (Internal or OAuth access_token)
    api_base: str                # https://api.notion.com/v1
    api_version: str             # Notion-Version 헤더값
    page_id: str | None          # 검증 대상 페이지 ID (없으면 search 로 자동 탐지)
    database_id: str | None      # 검증 대상 DB ID (없으면 search 로 자동 탐지)
    timeout: int
    max_results: int

    # OAuth (선택) — test_oauth_token.py 용.
    oauth_client_id: str | None
    oauth_client_secret: str | None
    oauth_refresh_token: str | None
    oauth_redirect_uri: str | None

    @property
    def has_oauth_credentials(self) -> bool:
        """OAuth refresh 검증에 필요한 최소 정보가 있는지."""
        return bool(self.oauth_client_id and self.oauth_client_secret
                    and self.oauth_refresh_token)


def load_config() -> Config:
    """.env 를 읽어 Config 를 만든다. 필수값 누락 시 에러로 안내한다."""
    here = Path(__file__).resolve().parent
    load_dotenv(here / ".env")

    api_key = os.getenv("NOTION_API_KEY", "").strip()
    if not api_key:
        raise SystemExit(
            "필수 환경변수가 .env 에 없습니다: NOTION_API_KEY\n"
            ".env.example 을 복사해 .env 를 만들고 값을 채우세요."
        )

    return Config(
        api_key=api_key,
        api_base=os.getenv("NOTION_BASE_URL", "").strip().rstrip("/") or DEFAULT_API_BASE,
        api_version=os.getenv("NOTION_API_VERSION", "").strip() or DEFAULT_API_VERSION,
        page_id=(os.getenv("NOTION_TEST_PAGE_ID", "").strip() or None),
        database_id=(os.getenv("NOTION_TEST_DATABASE_ID", "").strip() or None),
        timeout=int(os.getenv("REQUEST_TIMEOUT", "30") or "30"),
        max_results=int(os.getenv("MAX_RESULTS", "10") or "10"),
        oauth_client_id=(os.getenv("NOTION_OAUTH_CLIENT_ID", "").strip() or None),
        oauth_client_secret=(os.getenv("NOTION_OAUTH_CLIENT_SECRET", "").strip() or None),
        oauth_refresh_token=(os.getenv("NOTION_OAUTH_REFRESH_TOKEN", "").strip() or None),
        oauth_redirect_uri=(os.getenv("NOTION_OAUTH_REDIRECT_URI", "").strip() or None),
    )


@dataclass
class ApiResponse:
    """단일 API 호출 결과. 예외 대신 이 객체로 결과를 전달한다."""

    ok: bool                       # 2xx 여부
    status: int | None             # HTTP 상태코드 (네트워크 실패 시 None)
    data: Any                      # 파싱된 JSON(보통 list/dict). 실패 시 None
    error: str | None              # 사람이 읽을 수 있는 에러 설명
    elapsed_ms: int                # 요청 소요 시간(ms)


class NotionClient:
    """Notion REST API 용 얇은 HTTP 래퍼."""

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg
        self.session = requests.Session()
        # 토큰은 Internal 이든 OAuth access_token 이든 동일한 Bearer 헤더.
        self.session.headers.update({
            "Authorization": f"Bearer {cfg.api_key}",
            "Notion-Version": cfg.api_version,
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def _url(self, path: str) -> str:
        """API 경로를 전체 URL 로 변환. path 가 absolute URL 이면 그대로 반환."""
        if path.startswith("http://") or path.startswith("https://"):
            return path
        return f"{self.cfg.api_base}{path if path.startswith('/') else '/' + path}"

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
    ) -> ApiResponse:
        """요청을 보내고 ApiResponse 로 반환. 예외를 밖으로 던지지 않는다."""
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

    def patch(self, path: str, json_body: dict[str, Any] | None = None) -> ApiResponse:
        return self.request("PATCH", path, json_body=json_body)

    def delete(self, path: str) -> ApiResponse:
        return self.request("DELETE", path)

    # ---- 헬퍼 ----
    def resolve_page_or_db(self) -> tuple[ApiResponse, str | None, str | None]:
        """검증 대상 페이지/데이터베이스 ID 를 결정한다.

        env 에 NOTION_TEST_PAGE_ID / NOTION_TEST_DATABASE_ID 가 있으면 그대로 사용.
        둘 다 없으면 POST /search 로 접근 가능한 첫 페이지를 자동 선택한다.

        반환: (탐지용 ApiResponse, page_id|None, database_id|None)
        """
        if self.cfg.page_id or self.cfg.database_id:
            return ApiResponse(True, 0, None, None, 0), self.cfg.page_id, self.cfg.database_id

        resp = self.post("/search", json_body={"page_size": self.cfg.max_results})
        if not resp.ok or not isinstance(resp.data, dict):
            return resp, None, None

        page_id: str | None = None
        db_id: str | None = None
        for item in resp.data.get("results") or []:
            obj_type = item.get("object")
            item_id = item.get("id")
            if obj_type == "page" and not page_id:
                page_id = item_id
            elif obj_type == "database" and not db_id:
                db_id = item_id
            if page_id and db_id:
                break
        return resp, page_id, db_id


def _describe_error(resp: requests.Response, parsed: Any) -> str:
    """HTTP 에러 응답을 사람이 읽을 수 있게 요약."""
    hint = ""
    if resp.status_code == 401:
        hint = " (토큰 무효/만료 — NOTION_API_KEY 확인)"
    elif resp.status_code == 403:
        hint = " (리소스를 Integration/OAuth 연결에 공유하지 않았거나 capability 부족)"
    elif resp.status_code == 404:
        hint = " (리소스 없음 — 페이지/DB ID 또는 공유 범위 확인)"
    elif resp.status_code == 429:
        hint = " (rate limit — 요청 간격 조정 필요)"

    # Notion 에러 응답: {"object":"error","status":...,"code":"...","message":"..."}
    msg = None
    if isinstance(parsed, dict):
        msg = parsed.get("message") or parsed.get("code")
    msg = msg or resp.reason
    return f"{resp.status_code} {msg}{hint}"


# ===========================================================================
# 원문 URL 헬퍼 (설계 원칙: 상세 내용은 Notion 원문으로 이동)
# ===========================================================================

def page_web_url(base_url: str, page_id: str) -> str:
    """Notion 페이지 원문 URL.

    base_url 은 여기서 api_base (api.notion.com/v1) 가 아니라
    앱 도메인(https://www.notion.so) 기준이어야 한다. UUID 는 하이픈 제거 형태도 동작.
    """
    app_base = "https://www.notion.so"
    compact = page_id.replace("-", "")
    return f"{app_base}/{compact}"


def database_web_url(database_id: str) -> str:
    """Notion DB 원문 URL. 페이지와 동일하게 www.notion.so/{uuid} 형태로 열린다."""
    app_base = "https://www.notion.so"
    compact = database_id.replace("-", "")
    return f"{app_base}/{compact}"


# ===========================================================================
# 결과 수집 및 리포트 (jira_client.py 와 동일 구조)
# ===========================================================================

@dataclass
class CheckResult:
    """개별 검증 항목의 결과 레코드."""

    name: str                       # 예: "1-1 현재 봇 사용자"
    endpoint: str                   # 예: "GET /users/me"
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
