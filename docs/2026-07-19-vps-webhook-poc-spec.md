# VPS Webhook POC 수신 사양

제품 구조에서 메인 서버는 GitLab·Mattermost·Jira·Notion 이벤트를 수신한다. webhook은 변경 신호이며, 메인 서버는 수신한 ID·URL을 기준으로 각 도구 API를 추가 호출해 최신 원문을 조회하고 동기화·알림을 처리한다. 현재 제공된 테스트 코드는 GitLab webhook 등록만 직접 검증하며, Mattermost는 발송용 incoming webhook, Jira는 권한 확인만 검증한다. Notion 테스트의 “webhook 부재” 전제는 현재 공식 API와 달라 재작성해야 한다.

## 목적과 결정

이 문서는 메인 서버가 수신할 서비스별 유입 경로와, 현재 테스트 코드가 증명한 범위를 구분한다. 목적은 이벤트 원문과 도달 여부를 확인하는 것이며, 알림 선별·대시보드 반영·DB·큐는 이 POC 범위에 포함하지 않는다.

### 서비스별 POC 상태

| 서비스 | 제품에서 메인 서버가 할 일 | 현재 테스트 코드가 하는 일 | POC 검증 상태 |
|---|---|---:|---|
| GitLab | `POST /webhooks/gitlab` 수신 | 프로젝트 webhook 생성·조회·삭제 | 등록 가능성 검증. 전달 발화는 별도 필요. |
| Mattermost | `POST /webhooks/mattermost` 수신 또는 WebSocket 이벤트 소비 | incoming webhook 생성, 선택적으로 채널에 `text` 전송 | 발송만 검증. outgoing webhook 또는 WebSocket은 미검증. |
| Jira Cloud | `POST /webhooks/jira` 수신 | `GET /webhook` 접근 가능 여부만 기록, 생성 요청 없음 | 앱 인증·등록 권한 미확정. |
| Notion | `POST /webhooks/notion` 수신 후 Notion API 추가 조회 | `/users/me` 확인 후 webhook 부재를 코드상 제약으로 기록 | 테스트 전제가 오래됨. Connection UI에서 webhook 구독 POC 필요. |

### POC 데이터 흐름

```text
GitLab / Mattermost / Jira
        │ 각 도구가 등록된 공개 URL로 이벤트 POST
        ▼
메인 서버 (VPS에 배포)
  /webhooks/gitlab
  /webhooks/mattermost
  /webhooks/jira
        │ 검증 · 원문 보관 · 정규화/알림 처리
        ▼
대시보드 / Mattermost incoming webhook

Notion
        │ 등록된 public URL로 이벤트 POST
        ▼
동일한 이벤트 처리 경로
```

- VPS에 배포한 메인 서버가 공개 HTTPS 요청을 받을 수 있으면 별도 webhook receiver 서버는 필요 없다. webhook controller를 메인 서버에 둔다.
- 메인 서버가 private network에 있으면 VPS를 edge receiver로 두고, 인증된 내부 경로 또는 큐로 메인 서버에 전달한다. 이때만 receiver와 메인 서버를 분리한다.
- Mattermost incoming webhook URL은 메인 서버가 Mattermost 채널에 메시지를 게시하는 비밀 URL이다. GitLab 원본 payload를 그대로 보내지 않고 필요한 정보만 `{"text": "..."}` 형태로 변환한다.

## 메인 서버 유입 API 계약

### 공통 규칙

- 외부에는 HTTPS만 공개한다. VPS 애플리케이션은 리버스 프록시 뒤 내부 HTTP로 실행해도 된다.
- 수신 주소는 실제 공개 도메인으로 확정한다. 이 문서에서는 `https://<VPS_WEBHOOK_HOST>`를 사용한다.
- 요청을 검증하고 원문을 저장한 뒤 빠르게 응답한다. POC에서는 파일 I/O 외의 긴 작업을 수행하지 않는다.
- 요청·응답·저장 로그에 토큰, `Authorization`, 쿠키 같은 비밀값을 남기지 않는다.

### `GET /healthz`

배포 확인용 endpoint다. 외부 서비스 webhook 설정에는 사용하지 않는다.

| 항목 | 값 |
|---|---|
| 성공 상태 | `200 OK` |
| 응답 `Content-Type` | `application/json` |
| 성공 본문 | `{"status":"ok"}` |

### `POST /webhooks/gitlab`

GitLab 프로젝트 webhook의 단일 수신 endpoint다. Push, Merge Request, Issue, Pipeline, Job, Note 이벤트는 경로를 나누지 않고 `X-Gitlab-Event` 헤더로 구분한다.

#### 요청 계약

| 구분 | 필수 | 규칙 |
|---|---:|---|
| Method | 예 | `POST` |
| Content-Type | 예 | `application/json` (`charset` 파라미터 허용) |
| `X-Gitlab-Token` | 예 | VPS의 `WEBHOOK_GITLAB_TOKEN`과 상수 시간 비교한다. |
| `X-Gitlab-Event` | 예 | 예: `Push Hook`, `Merge Request Hook`, `Pipeline Hook` |
| `X-Gitlab-Event-UUID` | 권장 | 저장·중복 분석에 사용한다. 없어도 거절하지 않는다. |
| 본문 | 예 | JSON object. 원문을 변경하지 않고 저장한다. |

초기 구독 이벤트는 [gitlab-api-test/test_webhooks.py](/Users/kkh/Desktop/A502-api/gitlab-api-test/test_webhooks.py)의 `WEBHOOK_EVENTS`와 동일하게 설정한다.

| GitLab 이벤트 | 헤더 값 | 대표 본문 필드 |
|---|---|---|
| Push | `Push Hook` | `object_kind`, `ref`, `commits`, `project.web_url` |
| Merge Request | `Merge Request Hook` | `object_attributes.action`, `iid`, `title`, `url` |
| Issue | `Issue Hook` | `object_attributes.action`, `iid`, `title`, `url` |
| Pipeline | `Pipeline Hook` | `object_attributes.status`, `url`, `ref` |
| Job | `Build Hook` | `build_status`, `build_name`, `pipeline_id` |
| Note | `Note Hook` | `object_attributes.note`, `noteable_type`, `url` |

#### 응답 계약

외부 서비스는 HTTP 상태 코드만 성공 여부로 판단할 수 있으므로, 아래 JSON은 운영자와 수동 테스트를 위한 응답이다.

| 상황 | 상태 | 본문 예시 | 저장 |
|---|---:|---|---|
| 검증·보관 성공 | `200 OK` | `{"accepted":true,"service":"gitlab","event":"Push Hook","request_id":"..."}` | `received/gitlab/` |
| 토큰 누락 또는 불일치 | `401 Unauthorized` | `{"accepted":false,"error":"invalid_webhook_token"}` | 저장하지 않음 |
| JSON이 아니거나 object가 아님 | `400 Bad Request` | `{"accepted":false,"error":"invalid_json_payload"}` | 저장하지 않음 |
| 파일 저장 등 내부 오류 | `500 Internal Server Error` | `{"accepted":false,"error":"internal_error","request_id":"..."}` | 오류 로그만 |

`request_id`는 서버가 생성한 UUID다. GitLab의 `X-Gitlab-Event-UUID`가 있으면 별도 필드 `event_id`로 반환·저장할 수 있으나, 서로 같은 식별자로 취급하지 않는다.

#### 보관 레코드

검증에 성공한 요청마다 파일 하나를 생성한다.

```text
<RECEIVED_DIR>/
└── gitlab/
    └── 20260719T144501.123+0900_<request_id>.json
```

```json
{
  "received_at": "2026-07-19T14:45:01.123+09:00",
  "request_id": "f0b4a40e-8f9d-4de1-a303-4bbb7f48c4c5",
  "service": "gitlab",
  "event": "Push Hook",
  "event_id": "<X-Gitlab-Event-UUID 또는 null>",
  "webhook_id": "<X-Gitlab-Webhook-UUID 또는 null>",
  "client_ip": "<프록시 신뢰 정책을 적용한 IP 또는 null>",
  "headers": {
    "content-type": "application/json",
    "x-gitlab-event": "Push Hook",
    "x-gitlab-event-uuid": "..."
  },
  "payload": {}
}
```

- `X-Gitlab-Token`은 저장하지 않는다. 헤더 전체를 그대로 덤프하지 말고 허용 목록만 저장한다.
- 원문 `payload`는 이후 필드 해석 근거이므로 정규화·축약하지 않는다.
- 프록시를 신뢰하도록 명시적으로 설정하기 전에는 `X-Forwarded-For`를 client IP로 사용하지 않는다.

### `POST /webhooks/mattermost` — 예정

Mattermost에서 서버로 이벤트를 보내려면 incoming webhook이 아니라 **outgoing webhook** 또는 Mattermost WebSocket 이벤트를 선택해야 한다.

- outgoing webhook을 선택하면 이 경로가 공개 수신 endpoint가 된다. 요청 형식·token 위치·응답 메시지 형식은 outgoing webhook 생성 POC로 실제 payload를 확보한 뒤 확정한다.
- WebSocket을 선택하면 공개 `POST /webhooks/mattermost`는 만들지 않는다. 메인 서버가 Mattermost에 outbound WebSocket 연결을 유지한다.
- 현재 `mattermost-api-test/test_webhooks.py`는 incoming webhook만 생성하므로, 이 endpoint의 요청·응답 계약을 증명하지 않는다.

### `POST /webhooks/jira` — 예정

Jira Cloud 앱이 webhook을 등록할 수 있도록 인증·scope·테넌트 권한을 확정한 뒤 사용한다.

- 현재 `jira-api-test/test_webhooks.py`는 `GET /webhook`만 호출한다. webhook 생성과 payload는 검증하지 않는다.
- 앱 유형(Forge, Connect, OAuth 2.0)을 결정한 뒤 secret 검증 방식, 구독 event, 재시도 대응, 요청 예시를 이 문서에 추가한다.
- endpoint를 먼저 구현할 수는 있으나, 외부 공개·운영 전환은 Jira의 실제 test event 수신으로 검증한 뒤 한다.

### `POST /webhooks/notion`

Notion Connection의 Webhooks 탭에서 이 공개 HTTPS URL을 구독 주소로 등록한다. Notion 이벤트에는 전체 변경 내용이 아닌 변경 대상 ID·이벤트 종류가 오므로, 검증 후 Notion API를 추가 호출해 최신 페이지·데이터 소스 정보를 가져온다.

| 단계 | 메인 서버 동작 |
|---|---|
| 구독 생성 검증 | 최초 `POST` 본문의 `verification_token`을 보관한다. Notion Connection UI에 이 값을 입력해 구독을 활성화한다. |
| 일반 이벤트 검증 | raw request body와 보관한 `verification_token`으로 `X-Notion-Signature` HMAC-SHA256을 계산해 상수 시간 비교한다. |
| 수신 성공 | 원문 저장 후 `200 OK`를 즉시 반환한다. |
| 후속 동기화 | `event.type`, `entity.id`를 기준으로 Notion API를 호출해 최신 상태를 조회한다. |

- endpoint는 SSL이 적용된 public URL이어야 한다. `localhost`는 등록할 수 없다.
- `verification_token`과 `X-Notion-Signature`는 로그·파일에 저장하지 않는다.
- `page.content_updated` 같은 이벤트는 여러 변경을 묶어 지연 전달할 수 있다. 이벤트 ID를 멱등 키로 저장하고, webhook 수신 자체를 변경 원문으로 취급하지 않는다.

## 환경 변수와 외부 도구 설정

### VPS receiver

```dotenv
# 실제 도메인과 HTTPS 인증서는 리버스 프록시에서 설정한다.
WEBHOOK_GITLAB_TOKEN=<long-random-secret>
RECEIVED_DIR=/data/received
LOG_LEVEL=INFO
```

`WEBHOOK_GITLAB_TOKEN`은 GitLab webhook 생성 요청의 `token`과 정확히 같아야 한다. 소스 코드, 이미지, 결과 JSON, 저장 파일에 이 값을 넣지 않는다.

### GitLab 테스트 스크립트

`gitlab-api-test/.env`의 현재 코드 관련 값은 다음과 같다.

```dotenv
GITLAB_BASE_URL=https://lab.ssafy.com
GITLAB_TOKEN=<api-scope-token>
GITLAB_TEST_PROJECT_ID=<선택: 프로젝트 ID 또는 경로>
WEBHOOK_TEST_URL=https://<VPS_WEBHOOK_HOST>/webhooks/gitlab
```

- 필요 권한은 코드 주석 기준으로 프로젝트 `Maintainer(40)` 이상과 `api` scope 토큰이다.
- 현재 `test_webhooks.py`는 webhook 생성 시 `token: "gitlab-api-test-poc"`와 `enable_ssl_verification: false`를 고정해 보낸다. 따라서 **코드를 수정하지 않고 POC를 실행하면** receiver의 토큰도 그 값이어야 하며 TLS 검증도 꺼진다.
- 공개 VPS 운영 또는 장기 webhook에는 이 두 하드코딩 값을 사용하지 않는다. 실행 전에 난수 시크릿 주입과 `enable_ssl_verification: true`로 변경하는 작업이 필요하다.

### Mattermost incoming webhook

`mattermost-api-test/.env`의 관련 설정은 다음과 같다.

```dotenv
MATTERMOST_BASE_URL=https://meeting.ssafy.com
MATTERMOST_TOKEN=<PAT>
MATTERMOST_TEST_TEAM_ID=<선택>
MATTERMOST_TEST_CHANNEL_ID=<선택>
MATTERMOST_WEBHOOK_URL=https://meeting.ssafy.com/hooks/<incoming-webhook-token>
```

- `MATTERMOST_WEBHOOK_URL`은 생성 응답에 포함되지 않아 Mattermost UI의 **Integrations → Incoming Webhooks**에서 복사한다.
- 이 URL은 채널 쓰기 권한과 같으므로 VPS 환경 변수에만 보관하고 문서·로그·Git에는 남기지 않는다.
- 이후 알림 발송은 이 URL로 `POST`하고 최소 본문은 `{"text":"알림 내용"}`이다.

## 테스트별 실제 검증 범위와 주의점

### GitLab `test_webhooks.py`

이 스크립트는 다음 순서로 프로젝트 webhook을 조회·생성(또는 재사용)·단건 조회·삭제한다.

1. `GET /projects/{id}/hooks`로 `WEBHOOK_TEST_URL`과 같은 URL을 찾는다.
2. 없으면 `POST /projects/{id}/hooks`로 webhook을 만든다.
3. `GET /projects/{id}/hooks/{hook_id}`로 생성 결과를 확인한다.
4. `finally`에서 `DELETE /projects/{id}/hooks/{hook_id}`를 실행한다.

이것은 **CRUD 권한 검증**이며, Push나 Merge Request를 실제로 발생시키지 않으므로 VPS 도달·페이로드 검증은 완료하지 않는다. 수신 검증은 별도의 지속 webhook을 만든 뒤 이벤트를 수동 발화하여 `received/gitlab/` 파일과 GitLab의 webhook delivery 화면을 함께 확인해야 한다.

주의할 점:

- 같은 `WEBHOOK_TEST_URL`의 기존 webhook을 찾으면 새로 만들지 않지만, 그 기존 ID도 마지막에 삭제한다. 운영용 endpoint URL을 넣고 실행하지 않는다.
- 생성 실패 뒤에도 ID가 생긴 경우를 정리하려는 `finally` 구조는 유효하지만, 영구 webhook 테스트와 분리해야 한다.
- HTTPS receiver가 준비되기 전에는 `WEBHOOK_TEST_URL`을 비워 둔다. 이 경우 스크립트는 쓰기 작업을 하지 않고 종료한다.

### Mattermost `test_webhooks.py`

이 코드는 메인 서버로 들어오는 Mattermost webhook을 수신하지 않는다. Mattermost REST API의 `POST /hooks/incoming`으로 채널용 incoming webhook을 만든 뒤, `MATTERMOST_WEBHOOK_URL`이 있을 때만 그 URL로 ping 메시지를 보낸다.

- 생성한 incoming webhook은 의도적으로 삭제하지 않는다. 실행할 때마다 새 리소스가 생긴다.
- 생성 후 URL을 환경 변수에 넣고 스크립트를 다시 실행하면 또 하나의 webhook을 만들고, ping은 환경 변수에 있던 기존 URL로 보낸다. ping만 재검증할 때는 스크립트를 재실행하지 말고, 기존 URL에 직접 POST하거나 스크립트를 수정한 뒤 실행한다.
- 제품에서 Mattermost 이벤트가 필요하면 outgoing webhook POC 또는 WebSocket event POC를 추가한다. 이 단계가 끝나면 메인 서버 `/webhooks/mattermost` 계약을 확정한다.

### Jira `test_webhooks.py`

이 코드는 `GET /webhook`만 호출하고 `POST /webhook`을 하지 않는다. 코드 주석은 PAT 제약을 설명하지만, 현재 클라이언트 설정은 `JIRA_OAUTH_TOKEN`을 Bearer 토큰으로 사용한다. 따라서 실제 계정·앱 유형과 무관하게 이 POC 결과는 “이 토큰으로 동적 webhook API를 쓸 수 있는가”의 증거로만 해석한다.

- `403`은 테스트 목적상 예상된 권한 제약으로 기록된다.
- 제품 구조상 Jira 이벤트 수신 endpoint는 필요하다. 단, Connect/Forge/OAuth 앱 등록 방식, 허용 scope, 테넌트 정책을 확정한 뒤 공개한다.

### Notion `test_webhooks.py`

이 코드는 `GET /users/me`으로 연결 토큰을 확인한 뒤, REST webhook 등록 API가 없다는 제약을 기록한다. 이 결론은 현재 Notion 공식 문서와 맞지 않는다. Notion은 Connection UI의 Webhooks 탭에서 public URL과 event type을 등록하고, 최초 수신한 `verification_token`을 UI에서 확인하는 방식이다.

- `test_webhooks.py`는 “webhook 부재”를 기록하는 대신 Connection webhook 구독 생성·검증 POC로 바꿔야 한다.
- webhook 이벤트는 변경 신호다. `entity.id`로 페이지 또는 data source를 API 조회해 최신 원문을 가져온다.
- polling은 webhook 지원이 없는 이벤트를 보완하거나 장애 복구용 정합성 점검으로만 사용한다.

## 배포 및 검증 절차

1. VPS에 유효한 HTTPS 도메인을 연결하고 `GET /healthz`가 `200`인지 확인한다.
2. `POST /webhooks/gitlab`에 잘못된 토큰·잘못된 JSON을 보내 각각 `401`, `400`이며 파일이 생성되지 않는지 확인한다.
3. GitLab용 장기 테스트 webhook을 별도로 만들고 token, URL, 이벤트 6개를 설정한다. `test_webhooks.py`의 CRUD 실행과 같은 URL을 사용하지 않는다.
4. Push 이벤트를 발생시킨다. receiver `200` 응답, `received/gitlab/*.json` 생성, 파일의 `event`·`payload.project.web_url`을 확인한다.
5. Merge Request, Issue, Pipeline, Job, Note를 하나씩 발화해 실제 payload 차이를 보관한다.
6. Mattermost incoming webhook URL로 시험 메시지를 보내 채널 게시를 확인한다. 이후 outgoing webhook 또는 WebSocket POC를 수행해 메인 서버 이벤트 수신을 검증한다.
7. Jira 앱 인증을 확정하고 test event를 메인 서버 `/webhooks/jira`로 수신한다. Notion Connection에서 webhook 구독을 생성·검증한 뒤 test event를 메인 서버 `/webhooks/notion`으로 수신한다.

## 결정이 필요한 항목

- VPS webhook 공개 도메인과 TLS 종료 방식(기존 Traefik, Nginx, Caddy 등)
- 수신 원문 파일의 보관 기간·백업 위치·VPS 접근 권한
- GitLab 장기 테스트 webhook을 프로젝트 단위로 둘지, 팀/그룹 단위로 확장할지
- GitLab 수신 검증이 끝난 뒤 Mattermost 알림 변환을 같은 프로세스에 둘지 별도 worker로 분리할지

## 최종 요약

제품 메인 서버는 GitLab·Mattermost·Jira·Notion 이벤트를 모두 수신한다. webhook은 변경 신호이고, 수신 뒤 도구 API를 추가 호출해 최신 원문을 조회·동기화한다. 현재 코드로는 GitLab 등록만 직접 검증됐고 Mattermost는 발송, Jira는 권한만 확인됐다. Notion 테스트의 webhook 부재 결론은 현재 공식 API와 달라 Connection webhook POC로 교체해야 한다.
