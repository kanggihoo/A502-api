# Webhook 수신 서버 구현 사양서

> **현행 기준:** 제공된 `test_webhooks.py` 4개를 기준으로 한 VPS POC의 기준 문서는 [VPS Webhook POC 수신 사양](/Users/kkh/Desktop/A502-api/docs/2026-07-19-vps-webhook-poc-spec.md)이다. 이 문서의 GitLab 수신 상세는 참고용으로 유지한다. Jira·Notion endpoint와 Notion webhook 관련 서술은 현재 테스트 코드의 결론과 일치하지 않으므로 구현 근거로 사용하지 않는다.

VPS에서 동작하는 webhook 수신 FastAPI 서버 구현 사양. 목적: GitLab·Mattermost·Jira·Notion이 실제로 발화하는 webhook을 받아 형태·내용을 확인하는 것. 대시보드·알림 연동은 본 사양 범위 밖.

## 목적과 범위

- **검증 대상**: webhook이 도달하는가, 페이로드가 어떻게 오는가, 검증 토큰이 맞는가.
- **범위 내**: HTTPS 수신, 서비스별 라우트, 토큰 검증, 원문 저장, 콘솔 출력.
- **범위 밖**: 이벤트 정규화, 알림 전파, 대시보드 연동, 큐/Redis, 재시도 정책. 필요해지면 그때 설계.

## 배포 구성

```text
GitLab / Mattermost / Jira / Notion
        │ HTTPS
        ▼
   Traefik (이미 VPS에서 동작 중)
        │ 라우팅
        ▼
   webhook-receiver 컨테이너 (FastAPI + uvicorn)
        │
        ▼
   received/*.json  (컨테이너 볼륨 마운트)
```

- 컨테이너 1개. FastAPI만. Redis·DB·worker 없음.
- Traefik이 TLS 종료. 서버 컨테이너는 내부 HTTP만.

## 라우팅 — 서브도메인 vs 경로

두 안. **경로 기반 권장** (도메인 하나면 충분, 인증서 한 장).

| 안 | 형태 | 장점 | 비용 |
|---|---|---|---|
| 경로 (권장) | `hooks.example.com/webhooks/{service}` | 인증서 1장, Traefik 라우터 1개 | 서비스 식별을 path로 |
| 서브도메인 | `gitlab-hooks.example.com` 등 | 서비스별 격리 명확 | 인증서·DNS·라우터 N배 |

경로 기반 채택 시 Traefik 라우팅 규칙 예:

```yaml
# Traefik labels (docker-compose)
- "traefik.http.routers.webhook-receiver.rule=Host(`hooks.example.com`)"
- "traefik.http.routers.webhook-receiver.tls=true"
- "traefik.http.routers.webhook-receiver.tls.certresolver=letsencrypt"
- "traefik.http.services.webhook-receiver.loadbalancer.server.port=8000"
```

## 엔드포인트

경로 기준. 각 서비스별 독립 라우트.

| 서비스 | 메서드·경로 | 검증 토큰 위치 |
|---|---|---|
| GitLab | `POST /webhooks/gitlab` | 헤더 `X-Gitlab-Token` |
| Mattermost | `POST /webhooks/mattermost` | 본문 `token` 필드 |
| Jira | `POST /webhooks/jira` | 본문 또는 shared secret (설정 의존) |
| Notion | `POST /webhooks/notion` | 헤더 Authorization 또는 shared secret |

각 라우트의 책임은 동일: 검증 → 저장 → `200 OK`.

## 페이로드 형태 — 서비스별 요약

상세는 각 서비스 원문 문서 참조. 아래는 구현에 필요한 최소 정보.

### GitLab
- Content-Type: `application/json`
- 이벤트 식별: 헤더 `X-Gitlab-Event` (예: `Push Hook`, `Merge Request Hook`, `Pipeline Hook`, `Issue Hook`, `Note Hook`) + 본문 `object_kind`.
- 검증: 헤더 `X-Gitlab-Token` == webhook 생성 시 설정한 시크릿.
- 본문 키: `object_kind`, `project`, `user_name`, 이벤트별 세부 필드 (`commits[]`, `object_attributes` 등).
- 원문: https://docs.gitlab.com/user/project/integrations/webhook_events/

### Mattermost (outgoing webhook)
- Content-Type: 기본 `application/x-www-form-urlencoded` (JSON 옵션 있음).
- 검증: 본문 `token` 필드 == webhook 생성 시 발급된 토큰.
- 본문 키: `token`, `team_id`, `channel_id`, `user_id`, `user_name`, `text`, `timestamp`.
- 원문: https://developers.mattermost.com/integrate/webhooks/outgoing/

### Jira (Cloud)
- Content-Type: `application/json`.
- 이벤트 식별: 본문 `webhookEvent` (예: `jira:issue_created`, `jira:issue_updated`, `comment_created`).
- 검증: Atlassian webhook secret (Cloud 정책 의존). SSAFY는 `ssafy.atlassian.net` (Cloud).
- 본문 키: `webhookEvent`, `issue_event_type_name`, `issue`, `changelog`, `user`.
- 참고: 핸드오프 #1에서 GitLab 내장 `jira-cloud-app` 통합이 이미 활성 확인됨. 직접 webhook이 필요한지 먼저 검토.
- 원문: https://developer.atlassian.com/cloud/jira/platform/webhooks/

### Notion
- Content-Type: `application/json`.
- 이벤트 식별: 본문 `type` (예: `page.created`, `page.content_updated`, `database.content_updated`, `database.schema_updated`).
- 검증: shared secret (설정 의존).
- 헤더 `Notion-Version`: 응답 스키마 버전 (예: `2025-09-03`).
- ⚠️ 미검증: Notion webhook은 2025년 도입, API 버전 변화 빠름. SSAFY Notion에서 webhook 활성화 권한이 있는지 확인 필요. 검증 전까지 폴링 fallback 설계 권장.
- 원문: https://developers.notion.com/reference/webhooks

## 저장 형식

수신 시마다 파일 1개 생성. 사람이 읽고 확인하기 위한 검증 단계 포맷.

```text
received/
├─ gitlab/
│  ├─ 20260716_143012_a1b2c3.json
│  └─ ...
├─ mattermost/
├─ jira/
└─ notion/
```

파일 내용 (JSON, 들여쓰기):

```json
{
  "received_at": "2026-07-16T14:30:12+09:00",
  "service": "gitlab",
  "event": "Push Hook",
  "client_ip": "203.0.113.10",
  "headers": {
    "content-type": "application/json",
    "x-gitlab-event": "Push Hook",
    "x-gitlab-token": "<검증 후 마스킹 또는 제외>",
    "x-gitlab-webhook-uuid": "..."
  },
  "payload": { }
}
```

- `received_at`: 서버 수신 시각 (ISO 8601, 타임존 포함).
- `event`: 이벤트 식별자 (헤더 또는 본문에서 추출).
- `payload`: 원문 그대로. 정규화·가공 금지. 검증 목적이므로 원형 보존.
- ⚠️ 민감 정보: 토큰 원문은 저장하지 않거나 마스킹. 파일에 토큰 값 남기지 않기.

## 검증 실패 시 동작

- 토큰 불일치: `401 Unauthorized`. 본문 저장 **안 함** (또는 별도 `rejected/` 디렉토리에만 저장).
- Content-Type 예외: `400 Bad Request`.
- 검증 단계이므로 실패도 기록에서 확인할 수 있게 둘 것. 단 원문 수신 서비스가 아니면 무시.

## 콘솔 출력

수신 시 터미널에 한 줄 요약:

```
[2026-07-16 14:30:12] gitlab Push Hook from 203.0.113.10 → saved received/gitlab/20260716_143012_a1b2c3.json
```

- `uvicorn` 로그와 구분 위해 명확한 접두어.
- 페이로드 전체 출력은 파일로. 콘솔은 요약만.

## 환경 변수

```dotenv
# 검증용 시크릿. 각 서비스 webhook 설정에 입력한 값과 동일.
WEBHOOK_GITLAB_TOKEN=...
WEBHOOK_MATTERMOST_TOKEN=...
WEBHOOK_JIRA_SECRET=...
WEBHOOK_NOTION_SECRET=...

# 선택
RECEIVED_DIR=/data/received
LOG_LEVEL=INFO
```

- 시크릿은 컨테이너 환경 변수로 주입. 코드·이미지·Git에 두지 않는다.
- `.env`는 gitignored. `.env.example`만 커밋.

## 컨테이너 구성 (Dockerfile + Compose)

최소 구성.

**Dockerfile**:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv && uv sync --frozen --no-dev
COPY app ./app
EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml** (Traefik 통합 부분만):
```yaml
services:
  webhook-receiver:
    build: .
    restart: unless-stopped
    volumes:
      - ./received:/data/received
    environment:
      - RECEIVED_DIR=/data/received
      - WEBHOOK_GITLAB_TOKEN=${WEBHOOK_GITLAB_TOKEN}
      # ...나머지 시크릿
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.webhook-receiver.rule=Host(`hooks.example.com`)"
      - "traefik.http.routers.webhook-receiver.entrypoints=websecure"
      - "traefik.http.routers.webhook-receiver.tls=true"
      - "traefik.http.routers.webhook-receiver.tls.certresolver=letsencrypt"
      - "traefik.http.services.webhook-receiver.loadbalancer.server.port=8000"
    networks:
      - traefik-public   # 기존 Traefik 네트워크 이름에 맞춤

networks:
  traefik-public:
    external: true
```

## 구현 체크리스트

- [ ] FastAPI 앱 구조 (`app/main.py`, 라우트별 파일 분리 또는 단일 파일).
- [ ] 4개 서비스 라우트 + 토큰 검증.
- [ ] `received/{service}/` 파일 저장. 민감 정보 마스킹.
- [ ] 콘솔 요약 출력.
- [ ] Dockerfile·docker-compose. Traefik 라벨.
- [ ] `.env.example`. `.env` gitignored.
- [ ] 각 서비스에서 테스트 발화 후 파일로 형태 확인.

## 검증 순서 (권장)

1. GitLab 우선 — 핸드오프에서 읽기 권한·토큰 확보됨. `test_webhooks.py`로 webhook 생성 가능 (Maintainer + api scope).
2. 도달 확인 후 Mattermost — outgoing webhook 설정 권한 확인 필요.
3. Jira — 내장 통합(jira-cloud-app)으로 충분한지 먼저 판단. 직접 webhook이 꼭 필요한 경우만.
4. Notion — webhook 활성화 권한 미확정. 폴링 fallback 병행 설계.

## 의도적으로 미루는 것

- 이벤트 정규화(공통 스키마 변환) — 대시보드 연동 단계에서.
- 알림 전파(Mattermost 발송 등) — 수신 검증 먼저.
- Redis/큐/DB — 필요해지면. 지금은 파일 저장으로 충분.
- 재시도·멱등성·순서 보장 — 검증 단계 불필요.
- 다중 컨테이너·스케일아웃 — 단일 인스턴스로 충분.
