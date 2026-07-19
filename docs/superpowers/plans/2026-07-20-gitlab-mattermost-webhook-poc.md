# GitLab·Mattermost Webhook POC Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 별도 DB 없이 GitLab webhook과 Mattermost incoming/outgoing/slash command를 실제 SSAFY 환경에서 수신·인증·파일 보관·응답까지 검증하는 FastAPI POC를 만든다.

**Architecture:** 새 `webhook-receiver/` 독립 Python 패키지에 단일 FastAPI 앱을 둔다. 공개 요청은 서비스별 route에서 검증한 뒤 민감 필드를 제거하여 `RECEIVED_DIR`의 JSON 파일 하나로 보관하고 즉시 2xx/4xx를 반환한다. Mattermost incoming webhook은 수신 route가 아니라 전용 probe script가 비밀 URL에 메시지를 POST해 발송만 검증한다.

**Tech Stack:** Python 3.12, FastAPI, Uvicorn, pytest, httpx(TestClient), Docker Compose, Traefik(기존 VPS의 TLS 종료 프록시).

## Global Constraints

- DB, Redis, worker, 큐, 재시도 처리, 이벤트 정규화는 만들지 않는다. 성공한 외부 수신 요청은 파일로만 보관한다.
- 외부 공개 URL은 HTTPS여야 하며 예시에서는 `https://<VPS_WEBHOOK_HOST>`만 사용한다. 실제 도메인·토큰·incoming webhook URL을 Git에 기록하지 않는다.
- GitLab 신규 webhook은 서명 토큰을 우선한다. legacy `X-Gitlab-Token`은 signing token이 설정되지 않은 단기 호환 테스트에서만 허용한다.
- GitLab은 `POST /webhooks/gitlab`, Mattermost outgoing은 `POST /webhooks/mattermost/outgoing`, custom slash command는 `POST /commands/mattermost/a502`만 사용한다.
- Mattermost incoming webhook은 수신 route가 아니다. `MATTERMOST_INCOMING_WEBHOOK_URL`에 `{"text":"..."}`를 POST하는 발송 통합이다.
- 허용 목록에 없는 요청 header와 `token`, `Authorization`, `response_url`, `trigger_id`, GitLab signing header는 파일·콘솔·HTTP 응답에 남기지 않는다.
- 인증 실패 또는 형식 오류 요청은 저장하지 않는다. 성공 request마다 UUID 기반 JSON 파일 하나를 남긴다.

---

## File Structure

```text
webhook-receiver/
├── app/
│   ├── __init__.py
│   ├── auth.py                 # GitLab HMAC 및 Mattermost token 비교
│   ├── config.py               # 환경 변수 로드와 검증
│   ├── main.py                 # FastAPI 앱과 health route
│   ├── recording.py            # 민감정보 제거·JSON 파일 보관
│   ├── incoming_probe.py       # Mattermost incoming webhook 발송 함수
│   └── routes/
│       ├── __init__.py
│       ├── gitlab.py           # GitLab POST handler
│       └── mattermost.py       # outgoing·slash POST handler
├── scripts/
│   └── send_mattermost_incoming_probe.py
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_recording.py
│   ├── test_gitlab_route.py
│   ├── test_mattermost_routes.py
│   └── test_incoming_probe.py
├── .env.example
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml
```

- `config.py`만 환경 변수를 읽는다. 다른 모듈은 `Settings` 인스턴스를 인자로 받거나 FastAPI app state에서 가져온다.
- `recording.py`만 파일 경로·직렬화를 다룬다. route는 인증 성공 뒤 안전한 record payload를 넘긴다.
- `auth.py`는 순수 함수만 제공해 FastAPI 없이 단위 테스트한다.
- `incoming_probe.py`는 Mattermost 발송을 담당한다. 수신 route와 공유하지 않는다.

## Task 1: POC 패키지·환경 설정·health endpoint 만들기

**Files:**
- Create: `webhook-receiver/pyproject.toml`
- Create: `webhook-receiver/app/__init__.py`
- Create: `webhook-receiver/app/config.py`
- Create: `webhook-receiver/app/main.py`
- Create: `webhook-receiver/tests/conftest.py`
- Create: `webhook-receiver/.env.example`
- Test: `webhook-receiver/tests/test_health.py`

**Interfaces:**
- Produces: `Settings` dataclass with `received_dir: Path`, optional GitLab/Mattermost secrets, and `from_env() -> Settings`.
- Produces: `create_app(settings: Settings) -> FastAPI`; production entrypoint is `app.main:app`.
- Consumes: later route modules are included by `create_app` only after their tasks are completed.

- [ ] **Step 1: Create the failing health test**

```python
# tests/test_health.py
from fastapi.testclient import TestClient

from app.config import Settings
from app.main import create_app


def test_healthz_returns_ok(tmp_path):
    app = create_app(Settings(received_dir=tmp_path))

    response = TestClient(app).get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```

- [ ] **Step 2: Run the test to confirm the package and factory are absent**

Run: `cd webhook-receiver && uv run pytest tests/test_health.py -q`

Expected: collection fails because `app.config` and `app.main` do not exist.

- [ ] **Step 3: Add the minimal project configuration and app factory**

```toml
# pyproject.toml
[project]
name = "webhook-receiver"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
  "fastapi>=0.115,<1.0",
  "python-dotenv>=1.0,<2.0",
  "python-multipart>=0.0.9,<1.0",
  "uvicorn[standard]>=0.30,<1.0",
]

[dependency-groups]
dev = [
  "httpx>=0.27,<1.0",
  "pytest>=8,<9",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
```

```python
# app/config.py
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    received_dir: Path
    gitlab_signing_token: str | None = None
    gitlab_legacy_token: str | None = None
    mattermost_outgoing_token: str | None = None
    mattermost_slash_token: str | None = None
    mattermost_incoming_webhook_url: str | None = None

    @classmethod
    def from_env(cls) -> "Settings":
        import os
        from dotenv import load_dotenv
        load_dotenv()
        return cls(
            received_dir=Path(os.getenv("RECEIVED_DIR", "/data/received")),
            gitlab_signing_token=os.getenv("WEBHOOK_GITLAB_SIGNING_TOKEN") or None,
            gitlab_legacy_token=os.getenv("WEBHOOK_GITLAB_LEGACY_TOKEN") or None,
            mattermost_outgoing_token=os.getenv("WEBHOOK_MATTERMOST_OUTGOING_TOKEN") or None,
            mattermost_slash_token=os.getenv("WEBHOOK_MATTERMOST_SLASH_TOKEN") or None,
            mattermost_incoming_webhook_url=os.getenv("MATTERMOST_INCOMING_WEBHOOK_URL") or None,
        )
```

```python
# app/main.py
from fastapi import FastAPI

from .config import Settings


def create_app(settings: Settings) -> FastAPI:
    app = FastAPI()
    app.state.settings = settings

    @app.get("/healthz")
    def healthz() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app(Settings.from_env())
```

- [ ] **Step 4: Add only key names to the environment template**

```dotenv
# .env.example
RECEIVED_DIR=/data/received
WEBHOOK_GITLAB_SIGNING_TOKEN=
WEBHOOK_GITLAB_LEGACY_TOKEN=
WEBHOOK_MATTERMOST_OUTGOING_TOKEN=
WEBHOOK_MATTERMOST_SLASH_TOKEN=
MATTERMOST_INCOMING_WEBHOOK_URL=
```

- [ ] **Step 5: Install the locked environment and run the health test**

Run: `cd webhook-receiver && uv sync --all-groups && uv run pytest tests/test_health.py -q`

Expected: `1 passed`.

- [ ] **Step 6: Commit the runnable skeleton**

```bash
git add webhook-receiver
git commit -m "feat: add webhook receiver health endpoint"
```

## Task 2: 안전한 수신 기록 파일 만들기

**Files:**
- Create: `webhook-receiver/app/recording.py`
- Create: `webhook-receiver/tests/test_recording.py`
- Modify: `webhook-receiver/app/main.py`

**Interfaces:**
- Produces: `record_request(settings: Settings, *, service: str, flow: str, event: str, headers: dict[str, str], payload: dict[str, object]) -> str`.
- Produces: a request ID and one file at `<RECEIVED_DIR>/<service>/<UTC-like-timestamp>_<request_id>.json`.
- Consumes: `Settings.received_dir`; routes pass a pre-sanitized header/payload dictionary.

- [ ] **Step 1: Write the failing persistence and secret-removal tests**

```python
# tests/test_recording.py
import json

from app.config import Settings
from app.recording import record_request


def test_record_request_writes_one_json_file(tmp_path):
    request_id = record_request(
        Settings(received_dir=tmp_path), service="gitlab", flow="webhook",
        event="Push Hook", headers={"content-type": "application/json"},
        payload={"object_kind": "push"},
    )

    paths = list((tmp_path / "gitlab").glob("*.json"))
    assert len(paths) == 1
    saved = json.loads(paths[0].read_text())
    assert saved["request_id"] == request_id
    assert saved["payload"] == {"object_kind": "push"}


def test_record_request_removes_sensitive_keys_recursively(tmp_path):
    record_request(
        Settings(received_dir=tmp_path), service="mattermost-outgoing", flow="outgoing",
        event="#a502", headers={"authorization": "Token secret"},
        payload={"token": "secret", "response_url": "https://secret", "text": "#a502 ping"},
    )

    saved = json.loads(next((tmp_path / "mattermost-outgoing").glob("*.json")).read_text())
    assert saved["headers"] == {}
    assert saved["payload"] == {"text": "#a502 ping"}
```

- [ ] **Step 2: Run the recording tests to confirm they fail**

Run: `cd webhook-receiver && uv run pytest tests/test_recording.py -q`

Expected: collection fails because `app.recording` does not exist.

- [ ] **Step 3: Implement atomic JSON record creation and sanitization**

```python
# app/recording.py
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4
import json

from .config import Settings

SENSITIVE_KEYS = {"authorization", "token", "response_url", "trigger_id", "webhook-signature", "webhook-id", "webhook-timestamp", "x-gitlab-token"}


def _safe(value: object) -> object:
    if isinstance(value, dict):
        return {str(key): _safe(item) for key, item in value.items() if str(key).lower() not in SENSITIVE_KEYS}
    if isinstance(value, list):
        return [_safe(item) for item in value]
    return value


def record_request(settings: Settings, *, service: str, flow: str, event: str,
                   headers: dict[str, str], payload: dict[str, object]) -> str:
    request_id = str(uuid4())
    received_at = datetime.now(timezone.utc)
    target: Path = settings.received_dir / service
    target.mkdir(parents=True, exist_ok=True)
    filename = f"{received_at.strftime('%Y%m%dT%H%M%S.%fZ')}_{request_id}.json"
    record = {
        "received_at": received_at.isoformat(), "request_id": request_id,
        "service": service, "flow": flow, "event": event,
        "headers": _safe(headers), "payload": _safe(payload),
    }
    temporary = target / f".{filename}.tmp"
    destination = target / filename
    temporary.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(destination)
    return request_id
```

- [ ] **Step 4: Run the storage test suite**

Run: `cd webhook-receiver && uv run pytest tests/test_recording.py -q`

Expected: `2 passed`.

- [ ] **Step 5: Commit file-backed storage**

```bash
git add webhook-receiver/app/recording.py webhook-receiver/tests/test_recording.py
git commit -m "feat: record sanitized webhook requests to files"
```

## Task 3: GitLab signature verification과 수신 route 구현

**Files:**
- Create: `webhook-receiver/app/auth.py`
- Create: `webhook-receiver/app/routes/__init__.py`
- Create: `webhook-receiver/app/routes/gitlab.py`
- Create: `webhook-receiver/tests/test_auth.py`
- Create: `webhook-receiver/tests/test_gitlab_route.py`
- Modify: `webhook-receiver/app/main.py`

**Interfaces:**
- Produces: `valid_gitlab_signature(signing_token: str, message_id: str, timestamp: str, raw_body: bytes, received_signatures: str) -> bool`.
- Produces: `gitlab_router` with `POST /webhooks/gitlab`.
- Consumes: `Settings.gitlab_signing_token`; if absent, `Settings.gitlab_legacy_token` and header `X-Gitlab-Token` are the only accepted compatibility path.
- Produces: success `200 {"accepted": true, "service": "gitlab", "event": <header>, "request_id": <uuid>}`; invalid authentication `401`; malformed JSON object `400`; storage error `500`.

- [ ] **Step 1: Add failing signature and legacy-token tests**

```python
# tests/test_auth.py
import base64
import binascii
import hashlib
import hmac

from app.auth import valid_gitlab_signature


def test_valid_gitlab_signature_accepts_one_matching_v1_signature():
    key = b"secret"
    signing_token = "whsec_" + base64.b64encode(key).decode()
    body = b'{"object_kind":"push"}'
    digest = hmac.new(key, b"id-1.123." + body, hashlib.sha256).digest()
    signature = "v1," + base64.b64encode(digest).decode()

    assert valid_gitlab_signature(signing_token, "id-1", "123", body, "v1,bad " + signature)


def test_valid_gitlab_signature_rejects_modified_body():
    assert not valid_gitlab_signature("whsec_c2VjcmV0", "id-1", "123", b"{}", "v1,invalid")
```

```python
# tests/test_gitlab_route.py
from fastapi.testclient import TestClient

from app.config import Settings
from app.main import create_app


def test_gitlab_route_returns_401_without_configured_legacy_token(tmp_path):
    client = TestClient(create_app(Settings(received_dir=tmp_path, gitlab_legacy_token="expected")))

    response = client.post("/webhooks/gitlab", headers={"X-Gitlab-Token": "wrong"}, json={"object_kind": "push"})

    assert response.status_code == 401
    assert not (tmp_path / "gitlab").exists()
```

- [ ] **Step 2: Run the auth and route tests to confirm they fail**

Run: `cd webhook-receiver && uv run pytest tests/test_auth.py tests/test_gitlab_route.py -q`

Expected: collection fails because `app.auth` and `app.routes.gitlab` do not exist.

- [ ] **Step 3: Implement HMAC validation with constant-time comparison**

```python
# app/auth.py
import base64
import hashlib
import hmac


def valid_token(expected: str | None, received: str | None) -> bool:
    return bool(expected and received and hmac.compare_digest(expected, received))


def valid_gitlab_signature(signing_token: str, message_id: str, timestamp: str,
                           raw_body: bytes, received_signatures: str) -> bool:
    if not signing_token.startswith("whsec_"):
        return False
    try:
        key = base64.b64decode(signing_token.removeprefix("whsec_"), validate=True)
    except (ValueError, binascii.Error):
        return False
    message = message_id.encode() + b"." + timestamp.encode() + b"." + raw_body
    expected = "v1," + base64.b64encode(hmac.new(key, message, hashlib.sha256).digest()).decode()
    return any(hmac.compare_digest(expected, value) for value in received_signatures.split())
```

- [ ] **Step 4: Implement the GitLab handler before decoding the body**

```python
# app/routes/gitlab.py
import json
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..auth import valid_gitlab_signature, valid_token
from ..recording import record_request

gitlab_router = APIRouter()


@gitlab_router.post("/webhooks/gitlab")
async def receive_gitlab(request: Request) -> JSONResponse:
    settings = request.app.state.settings
    raw_body = await request.body()
    if settings.gitlab_signing_token:
        authenticated = valid_gitlab_signature(
            settings.gitlab_signing_token,
            request.headers.get("webhook-id", ""), request.headers.get("webhook-timestamp", ""),
            raw_body, request.headers.get("webhook-signature", ""),
        )
    else:
        authenticated = valid_token(settings.gitlab_legacy_token, request.headers.get("X-Gitlab-Token"))
    if not authenticated:
        return JSONResponse({"accepted": False, "error": "invalid_webhook_token"}, status_code=401)
    if "application/json" not in request.headers.get("content-type", ""):
        return JSONResponse({"accepted": False, "error": "invalid_json_payload"}, status_code=400)
    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError:
        return JSONResponse({"accepted": False, "error": "invalid_json_payload"}, status_code=400)
    if not isinstance(payload, dict):
        return JSONResponse({"accepted": False, "error": "invalid_json_payload"}, status_code=400)
    event = request.headers.get("X-Gitlab-Event", "unknown")
    request_id = record_request(settings, service="gitlab", flow="webhook", event=event,
                                headers={"content-type": request.headers.get("content-type", ""),
                                         "x-gitlab-event": event,
                                         "x-gitlab-event-uuid": request.headers.get("X-Gitlab-Event-UUID", "")},
                                payload=payload)
    return JSONResponse({"accepted": True, "service": "gitlab", "event": event, "request_id": request_id})
```

Include `gitlab_router` in `create_app` and add route tests for a valid legacy request, an invalid JSON request, and a valid signed request built with the same test HMAC helper.

- [ ] **Step 5: Run GitLab-focused tests**

Run: `cd webhook-receiver && uv run pytest tests/test_auth.py tests/test_gitlab_route.py -q`

Expected: all tests pass; valid requests produce one sanitized file and invalid requests produce no file.

- [ ] **Step 6: Commit GitLab reception**

```bash
git add webhook-receiver/app webhook-receiver/tests
git commit -m "feat: receive and verify GitLab webhooks"
```

## Task 4: Mattermost outgoing webhook과 slash command route 구현

**Files:**
- Create: `webhook-receiver/app/routes/mattermost.py`
- Create: `webhook-receiver/tests/test_mattermost_routes.py`
- Modify: `webhook-receiver/app/main.py`

**Interfaces:**
- Produces: `mattermost_router` with `POST /webhooks/mattermost/outgoing` and `POST /commands/mattermost/a502`.
- Consumes: form-encoded requests, `Settings.mattermost_outgoing_token`, and `Settings.mattermost_slash_token`.
- Produces: outgoing success `200 {"response_type":"comment","text":"[POC] #a502 수신 성공"}`; slash success `200 {"response_type":"ephemeral","text":"[POC] /a502 ping 수신 성공"}`.
- Produces: both routes return `401` before storing when the expected secret is unset or does not match.

- [ ] **Step 1: Write failing outgoing and slash tests**

```python
# tests/test_mattermost_routes.py
from fastapi.testclient import TestClient

from app.config import Settings
from app.main import create_app


def test_outgoing_a502_ping_is_recorded_and_replied_to(tmp_path):
    client = TestClient(create_app(Settings(received_dir=tmp_path, mattermost_outgoing_token="out-secret")))

    response = client.post("/webhooks/mattermost/outgoing", data={
        "token": "out-secret", "team_id": "team", "channel_id": "channel", "post_id": "post",
        "text": "#a502 ping", "timestamp": "1", "trigger_word": "#a502", "user_id": "user", "user_name": "name",
    })

    assert response.status_code == 200
    assert response.json() == {"response_type": "comment", "text": "[POC] #a502 수신 성공"}
    assert len(list((tmp_path / "mattermost-outgoing").glob("*.json"))) == 1


def test_slash_requires_both_authorization_and_form_token(tmp_path):
    client = TestClient(create_app(Settings(received_dir=tmp_path, mattermost_slash_token="slash-secret")))

    response = client.post("/commands/mattermost/a502", data={"token": "slash-secret", "command": "/a502", "text": "ping"})

    assert response.status_code == 401
    assert not (tmp_path / "mattermost-slash").exists()
```

- [ ] **Step 2: Run the Mattermost route tests to confirm they fail**

Run: `cd webhook-receiver && uv run pytest tests/test_mattermost_routes.py -q`

Expected: `404` because neither Mattermost route exists.

- [ ] **Step 3: Implement strict form and token validation**

```python
# app/routes/mattermost.py
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..auth import valid_token
from ..recording import record_request

mattermost_router = APIRouter()


def unauthorized() -> JSONResponse:
    return JSONResponse({"accepted": False, "error": "invalid_webhook_token"}, status_code=401)


@mattermost_router.post("/webhooks/mattermost/outgoing")
async def receive_outgoing(request: Request) -> JSONResponse:
    if "application/x-www-form-urlencoded" not in request.headers.get("content-type", ""):
        return JSONResponse({"accepted": False, "error": "invalid_form_payload"}, status_code=400)
    form = await request.form()
    settings = request.app.state.settings
    if not valid_token(settings.mattermost_outgoing_token, form.get("token")):
        return unauthorized()
    if form.get("trigger_word") != "#a502" or not str(form.get("text", "")).startswith("#a502"):
        return JSONResponse({"accepted": False, "error": "unexpected_trigger"}, status_code=400)
    record_request(settings, service="mattermost-outgoing", flow="outgoing", event="#a502",
                   headers={"content-type": request.headers.get("content-type", "")},
                   payload={key: form.get(key, "") for key in ("team_id", "channel_id", "post_id", "text", "timestamp", "trigger_word", "user_id", "user_name")})
    return JSONResponse({"response_type": "comment", "text": "[POC] #a502 수신 성공"})
```

Implement the slash route in the same module with these exact checks before `record_request`:

```python
authorization = request.headers.get("authorization", "")
header_token = authorization.removeprefix("Token ") if authorization.startswith("Token ") else ""
if not (valid_token(settings.mattermost_slash_token, header_token)
        and valid_token(settings.mattermost_slash_token, form.get("token"))):
    return unauthorized()
if form.get("command") != "/a502":
    return JSONResponse({"accepted": False, "error": "invalid_command"}, status_code=400)
if form.get("text", "").strip() == "ping":
    return JSONResponse({"response_type": "ephemeral", "text": "[POC] /a502 ping 수신 성공"})
return JSONResponse({"response_type": "ephemeral", "text": "사용법: /a502 ping"})
```

Store only `command`, `text`, `team_id`, `channel_id`, `user_id`, and `user_name` for slash requests. Do not pass `response_url`, `trigger_id`, or either token into `record_request`.

- [ ] **Step 4: Add missing behavioral tests**

Add test cases for outgoing token mismatch (`401`, no file), outgoing non-`#a502` trigger (`400`, no file), slash `/a502 ping` with both tokens (`200` and one file), and `/a502 unknown` (ephemeral usage response).

- [ ] **Step 5: Run all HTTP route tests**

Run: `cd webhook-receiver && uv run pytest tests/test_gitlab_route.py tests/test_mattermost_routes.py -q`

Expected: all cases pass and every rejected request leaves no record file.

- [ ] **Step 6: Commit Mattermost inbound interactions**

```bash
git add webhook-receiver/app/routes/mattermost.py webhook-receiver/app/main.py webhook-receiver/tests/test_mattermost_routes.py
git commit -m "feat: handle Mattermost outgoing and slash requests"
```

## Task 5: Mattermost incoming webhook 발송 probe 구현

**Files:**
- Create: `webhook-receiver/app/incoming_probe.py`
- Create: `webhook-receiver/scripts/send_mattermost_incoming_probe.py`
- Create: `webhook-receiver/tests/test_incoming_probe.py`

**Interfaces:**
- Produces: `send_incoming_probe(url: str, text: str, opener: Callable[..., object] = urlopen) -> int`.
- Consumes: a complete Mattermost incoming webhook URL and a nonempty probe text.
- Produces: only the remote HTTP status. The URL is never printed; the script prints a redacted host and status only.

- [ ] **Step 1: Write a failing request-body test using a fake opener**

```python
# tests/test_incoming_probe.py
import json

from app.incoming_probe import send_incoming_probe


def test_incoming_probe_posts_json_text_without_logging_url():
    captured = {}

    class Response:
        status = 200
        def __enter__(self): return self
        def __exit__(self, *_): return False

    def opener(request, timeout):
        captured["url"] = request.full_url
        captured["body"] = request.data
        captured["content_type"] = request.get_header("Content-type")
        return Response()

    status = send_incoming_probe("https://meeting.ssafy.com/hooks/secret", "[POC] ping", opener)

    assert status == 200
    assert captured["url"].endswith("/hooks/secret")
    assert captured["content_type"] == "application/json"
    assert json.loads(captured["body"]) == {"text": "[POC] ping"}
```

- [ ] **Step 2: Run the probe test to confirm it fails**

Run: `cd webhook-receiver && uv run pytest tests/test_incoming_probe.py -q`

Expected: collection fails because `app.incoming_probe` does not exist.

- [ ] **Step 3: Implement the standard-library HTTP POST helper**

```python
# app/incoming_probe.py
import json
from collections.abc import Callable
from urllib.request import Request, urlopen


def send_incoming_probe(url: str, text: str, opener: Callable = urlopen) -> int:
    if not url.startswith("https://"):
        raise ValueError("MATTERMOST_INCOMING_WEBHOOK_URL must use HTTPS")
    if not text.strip():
        raise ValueError("probe text must not be empty")
    request = Request(
        url,
        data=json.dumps({"text": text}).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with opener(request, timeout=10) as response:
        return response.status
```

The script must load `Settings.from_env()`, exit with status `2` if `MATTERMOST_INCOMING_WEBHOOK_URL` is unset, call `send_incoming_probe`, and print only `Mattermost incoming probe: status=<status> host=meeting.ssafy.com`. It must never print a path, token, or complete URL.

- [ ] **Step 4: Run the probe tests**

Run: `cd webhook-receiver && uv run pytest tests/test_incoming_probe.py -q`

Expected: `1 passed`.

- [ ] **Step 5: Commit the outgoing-to-Mattermost probe**

```bash
git add webhook-receiver/app/incoming_probe.py webhook-receiver/scripts/send_mattermost_incoming_probe.py webhook-receiver/tests/test_incoming_probe.py
git commit -m "feat: add Mattermost incoming webhook probe"
```

## Task 6: Docker/Traefik 배포 구성과 로컬 smoke test 추가

**Files:**
- Create: `webhook-receiver/Dockerfile`
- Create: `webhook-receiver/docker-compose.yml`
- Modify: `webhook-receiver/.env.example`
- Modify: `webhook-receiver/README.md`

**Interfaces:**
- Produces: `webhook-receiver` container listening on port `8000` in the Traefik external network.
- Consumes: `.env` values and host path `./received` mounted at `/data/received`.
- Produces: `GET /healthz` accessible through `https://<VPS_WEBHOOK_HOST>/healthz` after Traefik configuration.

- [ ] **Step 1: Add a deployment documentation check before writing configuration**

Create `README.md` with the exact local smoke command and expected JSON:

```bash
docker compose up --build -d
curl --fail http://127.0.0.1:8000/healthz
# {"status":"ok"}
```

State that the real `TRAEFIK_NETWORK` value must match the existing VPS external Docker network, and that no TLS certificate or domain value belongs in the repository.

- [ ] **Step 2: Write the minimal image and Compose configuration**

```dockerfile
# Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv && uv sync --frozen --no-dev
COPY app ./app
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
services:
  webhook-receiver:
    build: .
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./received:/data/received
    labels:
      - traefik.enable=true
      - traefik.http.routers.webhook-receiver.rule=Host(`${VPS_WEBHOOK_HOST}`)
      - traefik.http.routers.webhook-receiver.entrypoints=websecure
      - traefik.http.routers.webhook-receiver.tls=true
      - traefik.http.services.webhook-receiver.loadbalancer.server.port=8000
    networks:
      - traefik-public

networks:
  traefik-public:
    external: true
    name: ${TRAEFIK_NETWORK}
```

Add `VPS_WEBHOOK_HOST=` and `TRAEFIK_NETWORK=` to `.env.example`. Generate `uv.lock` with `uv lock` before building; never hand-edit it.

- [ ] **Step 3: Build and execute the local health smoke test**

Run: `cd webhook-receiver && docker compose config`

Expected: configuration resolves only when local `.env` has non-secret host/network values.

Run: `cd webhook-receiver && docker build -t webhook-receiver-poc .`

Expected: image builds successfully.

Run: `docker run --rm -p 8000:8000 -e RECEIVED_DIR=/tmp/received webhook-receiver-poc`

Expected: Uvicorn starts and remains running; use another terminal to run `curl --fail http://127.0.0.1:8000/healthz` and receive `{"status":"ok"}`. Stop the temporary container after the check.

- [ ] **Step 4: Commit deployment assets**

```bash
git add webhook-receiver/Dockerfile webhook-receiver/docker-compose.yml webhook-receiver/.env.example webhook-receiver/README.md webhook-receiver/uv.lock
git commit -m "build: containerize webhook receiver POC"
```

## Task 7: 실제 서비스별 POC 실행과 결과 기록

**Files:**
- Create: `webhook-receiver/results/.gitkeep`
- Modify: `gitlab-api-test/docs/webhook-receiver-spec.md` only if an observed external payload contradicts the documented contract.
- Create: `webhook-receiver/results/<YYYYMMDD>-poc-summary.md` with redacted evidence.

**Interfaces:**
- Consumes: deployed HTTPS receiver, GitLab Maintainer/API permission, Mattermost integration permission, and `.env` secrets stored only on the VPS.
- Produces: one redacted result summary per run; raw received JSON remains in the VPS mounted volume and is not committed.

- [ ] **Step 1: Verify receiver exposure before registering external integrations**

Run from a network outside the VPS: `curl --fail https://<VPS_WEBHOOK_HOST>/healthz`

Expected: `200` and `{"status":"ok"}`. Stop here if TLS fails, redirects incorrectly, or the host is not publicly reachable.

- [ ] **Step 2: Verify GitLab failure paths before creating a persistent hook**

Send a JSON request with an intentionally invalid legacy token to the deployed route.

Expected: `401` and no new `received/gitlab/` file.

Send a valid authenticated request with a non-JSON content type.

Expected: `400` and no new `received/gitlab/` file.

- [ ] **Step 3: Create a separate persistent GitLab test hook and fire all six events**

Create the hook in the target project with the deployed URL, SSL verification enabled, a signing token, and Push/Merge Request/Issue/Pipeline/Job/Note enabled. Do not run `gitlab-api-test/test_webhooks.py` against this URL because its cleanup can delete an existing hook.

For each event, confirm all three items: GitLab delivery shows 2xx; one `received/gitlab/*.json` file exists; the stored `event` value matches the delivery type. Verify that the file has no signing or legacy token field.

- [ ] **Step 4: Verify Mattermost incoming webhook separately**

Run: `cd webhook-receiver && uv run python scripts/send_mattermost_incoming_probe.py`

Expected: `status=200` output without a URL token and exactly one BOT-marked probe message in the configured test channel.

- [ ] **Step 5: Configure and verify Mattermost outgoing webhook**

In a test-only public channel, configure form encoding, callback `https://<VPS_WEBHOOK_HOST>/webhooks/mattermost/outgoing`, trigger word `#a502`, exact-first-word condition, and the outgoing token in the VPS `.env`.

Send `#a502 ping` and confirm: one `mattermost-outgoing` file without token; a `comment` reply with `[POC] #a502 수신 성공`; delivery HTTP 200 in Mattermost logs/UI if available. Send `hello #a502 ping` and `#a502x ping`; confirm no file is added.

- [ ] **Step 6: Configure and verify Mattermost custom slash command**

Create `/a502` with POST request URL `https://<VPS_WEBHOOK_HOST>/commands/mattermost/a502`, autocomplete hint `ping`, and the generated token in VPS `.env`.

Run `/a502 ping` and confirm: one `mattermost-slash` file without `response_url`, token, or `trigger_id`; only the invoking user sees `[POC] /a502 ping 수신 성공`. Run `/a502 unknown` and confirm the ephemeral usage message.

- [ ] **Step 7: Record the exact observed result without secrets**

Create `webhook-receiver/results/<YYYYMMDD>-poc-summary.md` containing service, tested action, UTC/KST timestamp, HTTP status, stored file name with request ID, and channel/GitLab delivery evidence location. Replace hostnames, IDs, tokens, URLs, usernames, and payload text containing project data with `<redacted>` before committing.

- [ ] **Step 8: Commit only redacted evidence and documentation corrections**

```bash
git add webhook-receiver/results/.gitkeep webhook-receiver/results/<YYYYMMDD>-poc-summary.md gitlab-api-test/docs/webhook-receiver-spec.md
git commit -m "docs: record webhook POC results"
```

## Final Verification Checklist

- [ ] Run: `cd webhook-receiver && uv run pytest -q` — all unit and route tests pass.
- [ ] Run: `cd webhook-receiver && docker build -t webhook-receiver-poc .` — image builds successfully.
- [ ] Run: `git diff --check` — no whitespace errors.
- [ ] Run: `git status --short` — only intentionally uncommitted VPS runtime data, if any, is present.
- [ ] Confirm no `.env`, `received/`, or `results` raw payload file is tracked by Git.
- [ ] Confirm GitLab 6 event types, Mattermost incoming, outgoing `#a502`, and slash `/a502 ping` each have independent success and failure evidence.

## Spec Coverage Review

| Specification requirement | Plan task |
|---|---:|
| DB 없이 JSON 파일 보관 | 2 |
| GitLab signed webhook와 legacy 호환 | 3 |
| GitLab 즉시 `200` acknowledgement | 3, 7 |
| Mattermost incoming 발송 | 5, 7 |
| Mattermost outgoing `#a502` | 4, 7 |
| Mattermost slash `/a502 ping`과 token 이중 확인 | 4, 7 |
| 비밀값 비보관·비로그 | 2–5, 7 |
| HTTPS/Traefik 배포 | 6, 7 |
| Jira 범위 제외 | Global Constraints |
