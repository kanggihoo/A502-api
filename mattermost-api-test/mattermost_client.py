"""Mattermost REST API v4 동작 테스트용 공통 모듈.

설정 로드, HTTP 클라이언트 래퍼, 결과 수집/리포트 기능을 제공한다.
api-docs/mattermost-api-priority-filter.md 의 "첫 API 검증 순서"를 코드로 검증하기
위한 기반이며, test_p0_readonly.py / test_p1_readonly.py / test_webhooks.py /
test_posts_write.py 가 이 모듈을 사용한다.

설계 원칙 (기존 *_client.py 와 동일):
- HTTP 오류가 발생해도 예외로 전체를 중단시키지 않고 (status, error) 로 반환한다.
  검증 목적상 "어느 엔드포인트가 권한 부족(403)으로 막히는지"를 기록하는 것이 중요하다.
- 토큰 등 민감 정보는 로그에 직접 출력하지 않는다.

인증 (Mattermost 특성):
- Personal Access Token 은 "Authorization: Bearer <token>" 헤더로 전달한다.
- user_id 자리에 "me" 리터럴을 쓰면 현재 사용자를 가리킨다.
- 전체 채널 조회(GET /channels)는 시스템 관리자 전용이므로, 사용자 스코프
  GET /users/me/teams/{team_id}/channels 를 우선 사용한다.
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
    """.env 에서 로드한 실행 설정."""

    base_url: str
    token: str
    team_id: str | None
    channel_id: str | None
    webhook_url: str | None
    timeout: int
    per_page: int

    @property
    def api_base(self) -> str:
        """REST API v4 루트. 예: https://meeting.ssafy.com/api/v4"""
        return f"{self.base_url.rstrip('/')}/api/v4"

    @property
    def has_team(self) -> bool:
        return bool(self.team_id)

    @property
    def has_channel(self) -> bool:
        return bool(self.channel_id)


def load_config() -> Config:
    """.env 를 읽어 Config 를 만든다. 필수값 누락 시 에러로 안내한다."""
    here = Path(__file__).resolve().parent
    load_dotenv(here / ".env")

    base_url = os.getenv("MATTERMOST_BASE_URL", "").strip().rstrip("/")
    token = os.getenv("MATTERMOST_TOKEN", "").strip()

    missing = []
    if not base_url:
        missing.append("MATTERMOST_BASE_URL")
    if not token:
        missing.append("MATTERMOST_TOKEN")
    if missing:
        raise SystemExit(
            "필수 환경변수가 .env 에 없습니다: " + ", ".join(missing) +
            "\n.env.example 을 복사해 .env 를 만들고 값을 채우세요."
        )

    return Config(
        base_url=base_url,
        token=token,
        team_id=(os.getenv("MATTERMOST_TEST_TEAM_ID", "").strip() or None),
        channel_id=(os.getenv("MATTERMOST_TEST_CHANNEL_ID", "").strip() or None),
        webhook_url=(os.getenv("MATTERMOST_WEBHOOK_URL", "").strip() or None),
        timeout=int(os.getenv("REQUEST_TIMEOUT", "30") or "30"),
        per_page=int(os.getenv("PER_PAGE", "60") or "60"),
    )


@dataclass
class ApiResponse:
    """단일 API 호출 결과. 예외 대신 이 객체로 결과를 전달한다."""

    ok: bool                       # 2xx 여부
    status: int | None             # HTTP 상태코드 (네트워크 실패 시 None)
    data: Any                      # 파싱된 JSON(보통 list/dict). 실패 시 None
    error: str | None              # 사람이 읽을 수 있는 에러 설명
    elapsed_ms: int                # 요청 소요 시간(ms)


class MattermostClient:
    """Mattermost REST API v4 용 얇은 HTTP 래퍼."""

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg
        self.session = requests.Session()
        # PAT 는 Bearer 토큰 헤더로 전달.
        self.session.headers.update({
            "Authorization": f"Bearer {cfg.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def _url(self, path: str) -> str:
        """API 경로를 전체 URL 로 변환. path 는 '/users/me' 처럼 슬래시로 시작."""
        if path.startswith("http://") or path.startswith("https://"):
            # webhook 전송처럼 api/v4 밖의 절대 URL 은 그대로 사용.
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

    def put(self, path: str, json_body: dict[str, Any] | None = None) -> ApiResponse:
        return self.request("PUT", path, json_body=json_body)

    def patch(self, path: str, json_body: dict[str, Any] | None = None) -> ApiResponse:
        return self.request("PATCH", path, json_body=json_body)

    def delete(self, path: str) -> ApiResponse:
        return self.request("DELETE", path)

    def upload_file(
        self,
        path: str,
        files: Any,
        data: dict[str, Any] | None = None,
    ) -> ApiResponse:
        """multipart/form-data 업로드 전용 요청.

        requests 가 files= 를 받으면 Content-Type 을 자동으로 multipart 로 설정하므로,
        세션의 기본 JSON Content-Type 헤더를 이 요청에서만 무시한다.
        (세션 기본 헤더 자체를 변경하지 않는다 — requests.request 호출 시 headers
        인자로 오버라이드.)

        - path: '/files' 처럼 api/v4 하위 경로.
        - files: requests 규격. 예) {"files": (filename, bytes, mime_type)}
        - data: multipart 의 폼 필드. 예) {"channel_id": "..."}
        """
        url = self._url(path)
        started = datetime.now()
        try:
            resp = self.session.request(
                method="POST",
                url=url,
                files=files,
                data=data,
                timeout=self.cfg.timeout,
                # 세션 기본 Content-Type(application/json) 을 multipart 경계로 덮어쓰기.
                # 빈 문자열을 주면 requests 가 files= 에 맞춰 boundary 를 붙인다.
                headers={"Content-Type": None},
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

    # ---- 헬퍼 ----
    def resolve_team(self) -> tuple[ApiResponse, str | None]:
        """대상 팀 ID 를 결정한다.

        env 에 MATTERMOST_TEST_TEAM_ID 가 있으면 그대로 사용.
        없으면 /users/me/teams 로 소속 첫 팀을 자동 선택한다.

        반환: (팀 탐지용 ApiResponse, 결정된 team_id)
        """
        if self.cfg.has_team:
            return ApiResponse(True, 0, None, None, 0), self.cfg.team_id

        resp = self.get("/users/me/teams", params={"per_page": self.cfg.per_page})
        if not resp.ok or not isinstance(resp.data, list) or not resp.data:
            return resp, None
        return resp, (resp.data[0].get("id") or None)

    def resolve_channel(self, team_id: str) -> tuple[ApiResponse, str | None]:
        """대상 채널 ID 를 결정한다.

        env 에 MATTERMOST_TEST_CHANNEL_ID 가 있으면 그대로 사용.
        없으면 /users/me/teams/{team_id}/channels 에서 일반 채널(type 'O'/'P')
        첫 번째를 자동 선택한다. (DM/GM type 'D'/'G' 는 게시글 테스트에 부적합)

        반환: (채널 탐지용 ApiResponse, 결정된 channel_id)
        """
        if self.cfg.has_channel:
            return ApiResponse(True, 0, None, None, 0), self.cfg.channel_id

        resp = self.get(f"/users/me/teams/{team_id}/channels")
        if not resp.ok or not isinstance(resp.data, list):
            return resp, None
        for ch in resp.data:
            if ch.get("type") in ("O", "P") and not ch.get("delete_at"):
                return resp, ch.get("id")
        # 일반 채널이 없으면 아무 채널이나.
        if resp.data:
            return resp, resp.data[0].get("id")
        return resp, None


def _describe_error(resp: requests.Response, parsed: Any) -> str:
    """HTTP 에러 응답을 사람이 읽을 수 있게 요약."""
    hint = ""
    if resp.status_code == 401:
        hint = " (토큰이 유효하지 않거나 만료됨)"
    elif resp.status_code == 403:
        hint = " (권한 부족 — 필요 permission 확인. manage_webhooks/read_bots 등)"
    elif resp.status_code == 404:
        hint = " (리소스 없음 — team_id/channel_id/post_id 또는 기능 비활성화 확인)"
    # Mattermost 에러는 보통 {"message":..., "status_code":..., "detailed_error":...}.
    msg = None
    if isinstance(parsed, dict):
        msg = parsed.get("message") or parsed.get("detailed_error")
    msg = msg or resp.reason
    return f"{resp.status_code} {msg}{hint}"


# ===========================================================================
# 원문 URL 헬퍼 (설계 원칙: 상세 내용은 Mattermost 원문으로 이동)
# ===========================================================================

def channel_web_url(base_url: str, team_name: str, channel_name: str) -> str:
    """채널 원문 URL. 예: https://meeting.ssafy.com/{team}/channels/{channel}"""
    return f"{base_url.rstrip('/')}/{team_name}/channels/{channel_name}"


def thread_web_url(base_url: str, team_name: str, post_id: str) -> str:
    """스레드 원문 URL. 예: https://meeting.ssafy.com/{team}/pl/{post_id}"""
    return f"{base_url.rstrip('/')}/{team_name}/pl/{post_id}"


# ===========================================================================
# 결과 수집 및 리포트 (기존 *_client.py 와 동일 구조)
# ===========================================================================

@dataclass
class CheckResult:
    """개별 검증 항목의 결과 레코드."""

    name: str                       # 예: "1-1 현재 사용자"
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
