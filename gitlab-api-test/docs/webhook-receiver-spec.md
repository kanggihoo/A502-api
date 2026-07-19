# GitLab·Mattermost Webhook POC 수신·동작 검증 사양서

## 1. 목적과 이번 범위

이 문서는 VPS의 공개 HTTPS 수신 서버와 Mattermost 통합을 사용해 다음 네 가지 흐름을 **실제 SSAFY 환경에서 독립적으로** 검증하기 위한 POC 사양이다. 성공 기준은 이벤트 또는 명령이 예상 endpoint에 도달하고, 인증·응답·원문 보관 결과를 사람이 재현 가능하게 확인하는 것이다.

| 우선순위 | 대상 | 검증 흐름 |
|---:|---|---|
| P0 | GitLab 프로젝트 webhook | GitLab 이벤트 → 수신 서버 → 인증·원문 보관 |
| P0 | Mattermost incoming webhook | 테스트 클라이언트/수신 서버 → Mattermost 채널 게시 |
| P0 | Mattermost outgoing webhook | Mattermost `#a502` 메시지 → 수신 서버 → 채널 응답 |
| P0 | Mattermost custom slash command | Mattermost `/a502 ping` → 수신 서버 → 명령 응답 |

### 범위 밖

- **Jira webhook**: `ssafy.atlassian.net`의 동적 webhook 등록은 관리자 또는 앱 권한 제약이 있으므로 이번 POC에서 제외한다. 후속 단계에서 Jira Automation이 외부 webhook 호출을 만들 수 있는지 별도 검증한다.
- Notion, Jenkins, 이벤트 정규화, DB·큐·재시도·대시보드 반영, GitLab 이벤트를 Mattermost 알림으로 변환하는 연결 시나리오.
- 운영용 고가용성, 장기 보관 정책, 다중 인스턴스 확장.

각 흐름은 서로의 성공 조건이 아니다. 예를 들어 GitLab 수신 성공은 Mattermost incoming 발송 성공을 뜻하지 않으며, 네 가지 검증 결과를 각각 남긴다.

## 2. 구성과 공통 원칙

```text
GitLab ──────────────────────────────┐
Mattermost outgoing / slash command ─┼─ HTTPS → VPS receiver
                                     │            ├─ 인증·형식 검증
                                     │            ├─ 원문/요약 보관
                                     │            └─ 즉시 HTTP 응답
테스트 클라이언트 또는 VPS receiver ──┴─ HTTPS → Mattermost incoming webhook
```

- 공개 주소는 `https://<VPS_WEBHOOK_HOST>`로 표기한다. 실제 배포에서는 유효한 인증서가 있는 HTTPS URL을 사용한다. `localhost`와 사설 IP는 Mattermost에서 기본적으로 차단될 수 있다.
- Traefik 등 기존 리버스 프록시가 TLS를 종료한다면 수신 애플리케이션은 내부 HTTP로 동작해도 된다.
- POC 수신기는 검증·파일 보관·요약 로그까지만 수행하고, 긴 처리 없이 즉시 응답한다.
- 모든 비밀값(토큰, 서명 토큰, incoming webhook URL, `Authorization`, `response_url`)은 환경 변수에만 둔다. 요청/응답 로그와 저장 JSON에는 기록하지 않는다.
- 외부 요청의 client IP는 프록시 신뢰 정책을 명시하기 전에는 `X-Forwarded-For`가 아닌 TCP peer IP만 참고값으로 취급한다.

### 공통 endpoint

| 메서드·경로 | 용도 | 외부 서비스에 등록 |
|---|---|---:|
| `GET /healthz` | 배포·TLS·리버스 프록시 확인. `200 {"status":"ok"}` | 아니요 |
| `POST /webhooks/gitlab` | GitLab 프로젝트 webhook 수신 | 예 |
| `POST /webhooks/mattermost/outgoing` | Mattermost outgoing webhook 수신 | 예 |
| `POST /commands/mattermost/a502` | Mattermost custom slash command 수신 | 예 |

Mattermost **incoming webhook에는 수신 서버 endpoint를 등록하지 않는다**. 이는 Mattermost가 제공한 비밀 `/hooks/<token>` URL로 메시지를 보내는 발송용 통합이다.

## 3. 사전 조건과 권한 확인

| 대상 | 필요한 권한·설정 | 권한/설정이 없을 때 |
|---|---|---|
| GitLab | 대상 프로젝트 Maintainer 이상, `api` scope 토큰(등록 API 테스트), 외부 HTTPS URL 접근 가능 | 등록·전달을 시도하지 않고 상태와 HTTP 오류를 결과에 기록 |
| Mattermost incoming | Incoming Webhooks 활성화, 통합 생성 권한, 대상 채널 게시 권한 | 시스템 관리자에게 Integration Management 설정 또는 권한 확인 요청 |
| Mattermost outgoing | Outgoing Webhooks 활성화, 통합 생성 권한, 공개 callback URL 접근 가능 | 일반 메시지 테스트를 생략하고 권한 제약만 결과에 기록 |
| Mattermost slash command | Custom Slash Commands 활성화, 명령 생성 권한, 공개 request URL 접근 가능 | 명령 POC를 생략하고 권한 제약만 결과에 기록 |

Mattermost의 통합 메뉴가 보이지 않는 경우, 사용자 실수가 아니라 서버 관리자가 해당 통합을 비관리자에게 비활성화했을 수 있다. 설정 우회를 시도하지 않는다.

## 4. GitLab 프로젝트 webhook

### 4.1 등록과 인증 정책

신규 webhook은 GitLab의 **서명 토큰**을 우선 사용한다. 수신기는 raw JSON body를 변경하기 전에 아래 Standard Webhooks 헤더를 검증한다.

| 헤더 | 역할 |
|---|---|
| `webhook-id` | GitLab delivery 식별자 |
| `webhook-timestamp` | 서명 대상 timestamp |
| `webhook-signature` | `v1,<base64 HMAC-SHA256>` 서명(여러 값 가능) |
| `X-Gitlab-Event` | 이벤트 이름(예: `Push Hook`) |
| `X-Gitlab-Event-UUID` | 이벤트 식별자. 없으면 거절하지 않음 |

`webhook-signature`가 있으면 서명 토큰의 `whsec_` 접두사를 제거·base64 디코딩한 키로 `"{webhook-id}.{webhook-timestamp}.{raw_body}"`를 HMAC-SHA256 계산하고 상수 시간 비교한다. 서명값 목록 중 하나라도 일치하면 통과다.

기존 `test_webhooks.py`는 `X-Gitlab-Token`과 고정 POC 토큰을 사용한다. 이 방식은 **호환성 확인용 단기 테스트에만** 허용한다. 새 장기 테스트 webhook에는 난수 토큰과 SSL 검증을 사용하며, `X-Gitlab-Token` 검증은 서명 미지원 GitLab 환경에서만 fallback으로 둔다. 서명과 token을 함께 설정한 전환 기간에는 서명을 우선하고, header token도 별도로 비교해 둘 중 하나를 무조건 우회하지 않는다.

### 4.2 요청·응답 계약

| 항목 | 규칙 |
|---|---|
| Method | `POST` |
| Content-Type | `application/json` (`charset` 파라미터 허용) |
| 본문 | JSON object. 검증을 위해 raw body를 먼저 확보하고, 보관 시 원문 구조를 바꾸지 않음 |
| 성공 | `200 OK`, 예: `{"accepted":true,"service":"gitlab","event":"Push Hook","request_id":"..."}` |
| 인증 실패 | `401 Unauthorized`, 본문 저장 안 함 |
| JSON/Content-Type 오류 | `400 Bad Request`, 본문 저장 안 함 |
| 보관 실패 | `500 Internal Server Error`, 오류 로그만 남김 |

초기 구독 이벤트는 Push, Merge Request, Issue, Pipeline, Job, Note로 한정한다. 각 이벤트는 하나씩 실제 발화해 payload 차이를 확보한다.

### 4.3 등록 테스트와 실제 전달 테스트의 분리

`gitlab-api-test/test_webhooks.py`는 webhook 생성·조회·삭제 권한을 확인하는 도구다. 동일 URL의 기존 hook도 마지막에 삭제할 수 있으므로, **지속 delivery 테스트 webhook URL을 이 스크립트에 넣지 않는다**.

1. 별도 테스트 프로젝트 또는 테스트 전용 URL에 장기 webhook을 UI/API로 생성한다.
2. URL, 구독 이벤트, 서명 토큰, SSL 검증 활성화를 확인한다.
3. Push → Merge Request → Issue → Pipeline → Job → Note 순으로 실제 이벤트를 하나씩 발화한다.
4. GitLab delivery 결과의 HTTP 상태와 수신기 보관 파일을 같은 시각·이벤트로 대조한다.

## 5. Mattermost incoming webhook — 채널 발송 검증

### 5.1 구성

Mattermost UI에서 **Integrations → Incoming Webhooks**를 열어 테스트 채널용 webhook을 만든다. 생성 후 표시되는 전체 URL `https://meeting.ssafy.com/hooks/<incoming-token>`은 채널 쓰기 권한과 같으므로 `MATTERMOST_INCOMING_WEBHOOK_URL` 환경 변수로만 보관한다.

기본 payload는 아래와 같다.

```json
{"text":"[POC] Mattermost incoming webhook 연결 확인"}
```

`Content-Type: application/json`으로 POST하고 `200 OK` 및 본문 `ok`를 확인한다. `channel`, `username`, `icon_url` 같은 override는 서버 설정 의존성이 있으므로 기본 연결 검증에는 사용하지 않는다.

### 5.2 성공·실패 기준

| 사례 | 기대 결과 | 증적 |
|---|---|---|
| 정상 `text` POST | HTTP `200`, 대상 테스트 채널에 BOT 표시 메시지 | HTTP 응답 상태, 채널 게시물 URL 또는 캡처 |
| 잘못된 URL/token | 4xx 또는 전송 실패, 게시물 없음 | 상태·오류 유형만 기록. URL 전문은 금지 |
| 잘못된 JSON | 오류 응답, 게시물 없음 | 상태·오류 유형만 기록 |

기존 `mattermost-api-test/test_webhooks.py`는 incoming webhook 생성 후 선택적으로 ping을 보낸다. 실행마다 webhook을 추가로 만들 수 있으므로, 생성 검증과 ping 재검증을 분리한다. ping만 다시 할 때는 이미 보관된 환경 변수 URL에 직접 POST한다.

## 6. Mattermost outgoing webhook — 일반 메시지 기반 수신

### 6.1 UI 설정

테스트 전용 공개 채널에서 **Integrations → Outgoing Webhooks**로 다음과 같이 만든다.

| 설정 | 값 |
|---|---|
| Content Type | `application/x-www-form-urlencoded` |
| Callback URL | `https://<VPS_WEBHOOK_HOST>/webhooks/mattermost/outgoing` |
| Trigger Word | `#a502` |
| Trigger Condition | 첫 번째 단어가 `#a502`와 정확히 일치 |
| Channel | 테스트 전용 공개 채널(가능하면 함께 제한) |

발급되는 Token은 `WEBHOOK_MATTERMOST_OUTGOING_TOKEN`에 저장한다. 일반 대화가 callback으로 전송되지 않도록 `#a502` 외의 메시지에서는 발화하지 않는 것을 별도 확인한다.

### 6.2 요청·응답 계약

| 구분 | 규칙 |
|---|---|
| Method / Content-Type | `POST` / `application/x-www-form-urlencoded` |
| 필수 form 필드 | `token`, `team_id`, `channel_id`, `post_id`, `text`, `timestamp`, `trigger_word`, `user_id`, `user_name` |
| 인증 | form의 `token`을 환경 변수와 상수 시간 비교 |
| 성공 응답 | `200 OK`, `Content-Type: application/json`, 예: `{"response_type":"comment","text":"[POC] #a502 수신 성공"}` |
| token 누락·불일치 | `401 Unauthorized`, Mattermost 게시 응답 없음 |
| form 형식 오류 | `400 Bad Request`, Mattermost 게시 응답 없음 |

`response_type: "comment"`는 트리거한 메시지의 답글로 결과를 붙여, 테스트 결과가 채널 대화와 섞이는 것을 줄인다. 응답 body에는 요청 토큰·사용자 식별자·원문 전체를 포함하지 않는다.

### 6.3 실행 시나리오

1. 테스트 채널에 `#a502 ping`을 전송한다.
2. 수신기 로그와 보관 파일에 `outgoing` 요청이 남고, token을 제외한 허용 필드가 확인되는지 본다.
3. 해당 게시물의 답글에 `[POC] #a502 수신 성공`이 표시되는지 확인한다.
4. `안녕하세요 #a502 ping`과 `#a502x ping`을 전송해 callback이 발화하지 않는지 확인한다.
5. 수신기의 token을 의도적으로 다른 테스트 값으로 설정한 뒤 `401` 및 Mattermost 응답 메시지 미생성을 확인하고, 즉시 정상 값으로 복구한다.

## 7. Mattermost custom slash command — 명령 기반 수신

### 7.1 UI 설정

Mattermost UI에서 **Integrations → Slash Commands**로 다음 명령을 만든다.

| 설정 | 값 |
|---|---|
| Command Trigger Word | `a502` (UI에서는 slash 없이 입력, 사용 시 `/a502`) |
| Request URL | `https://<VPS_WEBHOOK_HOST>/commands/mattermost/a502` |
| Request Method | `POST` |
| Autocomplete | 활성화, hint: `ping` |
| Description | `A502 통합 POC 연결 확인` |

발급된 Token은 `WEBHOOK_MATTERMOST_SLASH_TOKEN`에 저장한다. outgoing webhook token과 공유하지 않는다.

### 7.2 요청·응답 계약

| 구분 | 규칙 |
|---|---|
| Method / Content-Type | `POST` / `application/x-www-form-urlencoded` |
| 인증 | `Authorization: Token <token>` 및 form `token`이 모두 환경 변수와 일치해야 함 |
| 주요 form 필드 | `command`, `text`, `response_url`, `trigger_id`, `team_id`, `channel_id`, `user_id`, `user_name` |
| 즉시 성공 응답 | `200 OK`, `Content-Type: application/json`, `{"response_type":"ephemeral","text":"[POC] /a502 ping 수신 성공"}` |
| 인증 실패 | `401 Unauthorized`, 응답 메시지 없음 |
| 형식 오류 | `400 Bad Request`, 응답 메시지 없음 |

초기 POC 명령은 `/a502 ping` 하나만 지원한다. 그 외 인수는 `ephemeral` 형식의 사용법 오류로 응답한다. 동작이 3초를 넘을 가능성이 있는 후속 기능은 먼저 수신 확인을 응답하고, 요청에 포함된 `response_url`로 30분 안에 최대 5회 추가 메시지를 보낸다. `response_url`은 비밀 URL이므로 저장·로그 출력 금지다.

### 7.3 실행 시나리오

1. 공개 채널, 비공개 채널 또는 DM 중 허용된 위치에서 `/a502 ping`을 실행한다.
2. 실행자에게만 ephemeral 성공 메시지가 보이는지와 수신기 보관 기록을 확인한다.
3. `/a502 unknown`을 실행해 사용법 오류가 ephemeral로 보이는지 확인한다.
4. token 불일치 테스트로 `401`과 Mattermost 메시지 미생성을 확인한다.
5. 지연 응답은 별도 케이스로 `/a502 delayed`를 임시 지원한 경우에만 검증한다. 즉시 확인 메시지 1개와 `response_url` 추가 메시지 1개를 확인한 뒤 임시 명령은 제거한다.

## 8. 저장·로그 규칙

검증이 통과한 외부 수신 요청마다 한 파일을 생성한다. incoming webhook 발송은 수신 요청이 아니므로 파일 대신 발송 결과 요약만 남긴다.

```text
<RECEIVED_DIR>/
├── gitlab/
├── mattermost-outgoing/
└── mattermost-slash/
```

저장 레코드의 최소 형식은 다음과 같다.

```json
{
  "received_at": "2026-07-20T14:30:12.123+09:00",
  "request_id": "<server-generated-uuid>",
  "service": "mattermost",
  "flow": "outgoing",
  "event": "#a502",
  "headers": {"content-type": "application/x-www-form-urlencoded"},
  "payload": {"text": "#a502 ping"}
}
```

- GitLab은 `X-Gitlab-Token`, 서명 관련 헤더를 저장하지 않는다. Mattermost는 `token`, `Authorization`, `response_url`, `trigger_id`를 저장하지 않는다.
- 허용 목록 기반으로 필요한 헤더·본문 필드만 기록한다. 원문 보관이 필요한 GitLab JSON은 인증 정보를 제외하고 유지한다.
- 콘솔은 한 줄 요약만 출력한다. 예: `[time] mattermost outgoing #a502 → accepted request_id=...`.

## 9. 환경 변수

```dotenv
RECEIVED_DIR=/data/received
LOG_LEVEL=INFO

# GitLab: signing token 우선, legacy token은 필요할 때만 설정
WEBHOOK_GITLAB_SIGNING_TOKEN=whsec_...
WEBHOOK_GITLAB_LEGACY_TOKEN=...

# Mattermost
MATTERMOST_INCOMING_WEBHOOK_URL=https://meeting.ssafy.com/hooks/<secret>
WEBHOOK_MATTERMOST_OUTGOING_TOKEN=...
WEBHOOK_MATTERMOST_SLASH_TOKEN=...
```

`.env`는 커밋하지 않으며 `.env.example`에는 키 이름만 둔다. 모든 token과 incoming webhook URL은 테스트 결과 JSON, 문서 예시, 터미널 출력에서 마스킹한다.

## 10. 완료 기준과 결과 기록

각 항목은 아래 증적이 모두 있어야 완료로 판정한다.

| 항목 | 필수 성공 증적 | 필수 실패 증적 |
|---|---|---|
| GitLab | 실제 이벤트별 GitLab delivery `2xx` + 수신 파일 + 이벤트 식별 확인 | 잘못된 인증 `401`, 파일 미생성 |
| Mattermost incoming | HTTP `200`/`ok` + 대상 채널의 BOT 메시지 | 잘못된 URL 또는 JSON 오류, 게시물 없음 |
| Mattermost outgoing | `#a502 ping` 수신 파일 + 트리거 게시물 답글 | token 불일치 `401`; 비트리거 메시지 미발화 |
| Mattermost slash | `/a502 ping` 수신 파일 + 실행자에게만 보이는 ephemeral 메시지 | token 불일치 `401`; 잘못된 인수의 사용법 응답 |

결과 파일에는 실행 시각, 대상 서비스, 설정한 이벤트/명령, HTTP 상태, 성공 여부, 비밀값을 제외한 오류 요약, 증적 위치만 기록한다. 개인 사용자 식별자·채널 ID는 필요한 경우에도 결과 공유본에서 마스킹한다.

## 11. 후속 결정

1. 네 흐름이 모두 검증되면 GitLab 이벤트를 선별해 Mattermost incoming webhook으로 알리는 최소 변환 POC를 별도 사양으로 작성한다.
2. GitLab 프로젝트 webhook을 그룹 webhook으로 확장하기 전에는 SSAFY GitLab의 그룹 Owner 권한과 요금제·정책을 확인한다.
3. Jira는 Jira Automation에서 외부 webhook action을 생성할 권한, 인증 헤더 설정 가능 여부, 재시도 동작을 확인한 뒤 별도 endpoint와 보안 계약을 설계한다.
