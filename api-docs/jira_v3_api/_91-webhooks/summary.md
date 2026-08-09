# _91-webhooks API 요약

이 리소스 그룹은 Jira의 "동적 웹훅(dynamic webhooks)"을 등록/조회/삭제/연장하는 API 모음이다. 특정 이슈에 대해 JQL 필터로 지정한 조건이 만족될 때 지정된 URL로 이벤트를 전송받도록 설정하는 기능이며, Connect 앱 또는 OAuth 2.0 앱만 호출할 수 있다.

## 제외된 API

- 없음 (5개 엔드포인트 모두 "Jira administrators only"나 사이트 전체 관리자 권한을 요구하지 않음. "Only Connect and OAuth 2.0 apps can use this operation"은 앱 인증 방식 제약이지 Jira Global/Org admin 권한 제약이 아니므로 제외 대상이 아님)

---

### [높음] 1. 앱의 동적 웹훅 목록 조회 (GET /rest/api/3/webhook)

## 기본 정보

- **기능:** 호출한 앱(우리 통합 서비스)이 등록한 웹훅 목록을 페이지네이션으로 조회
- **Endpoint:** `GET /rest/api/3/webhook`
- **인증:** OAuth 2.0 또는 Connect 앱 인증 필요
- **권한:** Connect 앱 또는 OAuth 2.0 앱만 호출 가능 (사이트 관리자 권한 아님)

## 설명

현재 우리 앱이 Jira에 등록해 둔 웹훅 목록(이벤트 종류, JQL 필터, 대상 URL, 만료일 등)을 확인할 때 사용한다. 통합 알림/대시보드 기능에서 웹훅 설정 상태를 점검하거나, 팀 생성 자동화 시 이미 등록된 웹훅과 중복 여부를 확인하는 용도로 쓸 수 있다. 결과는 페이지 단위로 반환된다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `startAt` | integer | 아니오 | - | 반환할 결과 페이지의 시작 인덱스(오프셋) | `0` |
| `maxResults` | integer | 아니오 | - | 페이지당 최대 반환 개수 | `3` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `true` |
| `maxResults` | integer | 페이지당 최대 개수 | `3` |
| `startAt` | integer | 시작 인덱스 | `0` |
| `total` | integer | 전체 웹훅 개수 | `3` |
| `values` | array | 웹훅 객체 목록(`id`, `events`, `jqlFilter`, `url`, `expirationDate`, `fieldIdsFilter`, `issuePropertyKeysFilter` 포함) | - |

```json
{
  "isLast": true,
  "maxResults": 3,
  "startAt": 0,
  "total": 3,
  "values": [
    {
      "events": ["jira:issue_updated", "jira:issue_created"],
      "expirationDate": "2019-06-01T12:42:30.000+0000",
      "fieldIdsFilter": ["summary", "customfield_10029"],
      "id": 10000,
      "jqlFilter": "project = PRJ",
      "url": "https://your-app.example.com/webhook-received"
    },
    {
      "events": ["jira:issue_created"],
      "expirationDate": "2019-06-01T12:42:30.000+0000",
      "id": 10001,
      "jqlFilter": "issuetype = Bug",
      "url": "https://your-app.example.com/webhook-received"
    },
    {
      "events": ["issue_property_set"],
      "expirationDate": "2019-06-01T12:42:30.000+0000",
      "id": 10002,
      "issuePropertyKeysFilter": ["my-issue-property-key"],
      "jqlFilter": "project = PRJ",
      "url": "https://your-app.example.com/webhook-received"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청 파라미터가 잘못된 경우 | `errorMessages`/`errors` 확인 후 파라미터 수정 |
| 403 | - | 호출자가 앱(Connect/OAuth 2.0)이 아닌 경우 | 앱 인증 방식으로 재시도 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- Connect 앱 또는 OAuth 2.0 앱만 호출 가능하므로, 일반 API 토큰(Basic Auth) 방식으로는 사용할 수 없을 가능성이 있다. 실제 연동 시 인증 방식을 먼저 검증해야 한다.

---

### [높음] 2. 동적 웹훅 등록 (POST /rest/api/3/webhook)

## 기본 정보

- **기능:** 지정한 URL로 특정 Jira 이벤트(이슈 생성/수정/삭제, 코멘트, 스프린트, 버전, 이슈 속성 변경 등)를 전송하는 웹훅을 등록
- **Endpoint:** `POST /rest/api/3/webhook`
- **인증:** OAuth 2.0 또는 Connect 앱 인증 필요
- **권한:** Connect 앱 또는 OAuth 2.0 앱만 호출 가능

## 설명

팀 생성 자동화 시 프로젝트별로 이슈 생성/수정, 코멘트 작성 등의 이벤트를 감지하기 위한 웹훅을 등록하는 핵심 API다. JQL 필터로 대상 이슈 범위를 제한할 수 있어 프로젝트 단위로 알림을 분리할 수 있다. non-public OAuth 앱의 경우 앱 소유자와 웹훅을 등록한 사용자가 일치해야 실제로 전달된다는 제약이 있다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `url` | string | 예 | Connect 앱과 동일한 base URL 사용, 앱당 단일 URL만 등록 가능 | 웹훅을 전송할 URL | `"https://your-app.example.com/webhook-received"` |
| `webhooks` | array | 예 | - | 등록할 웹훅 목록 | - |
| `webhooks[].events` | array(enum) | 예 | `jira:issue_created`, `jira:issue_updated`, `jira:issue_deleted`, `comment_created`, `comment_updated`, `comment_deleted`, `issue_property_set`, `issue_property_deleted`, `sprint_created`, `sprint_updated`, `sprint_closed`, `sprint_deleted`, `sprint_started`, `jira:version_released`, `jira:version_unreleased`, `jira:version_created`, `jira:version_moved`, `jira:version_updated`, `jira:version_merged`, `jira:version_deleted` | 웹훅을 트리거할 이벤트 목록 | `["jira:issue_created", "jira:issue_updated"]` |
| `webhooks[].fieldIdsFilter` | array(string) | 아니오 | - | 지정한 필드가 변경 이력에 포함될 때만 `jira:issue_updated` 전송. 미지정 시 모든 필드 변경에 대해 알림 | `["summary", "customfield_10029"]` |
| `webhooks[].issuePropertyKeysFilter` | array(string) | 아니오 | - | 지정한 이슈 속성 키 변경 시에만 `issue_property_set`/`issue_property_deleted` 전송 | `["my-issue-property-key"]` |
| `webhooks[].jqlFilter` | string | 예 | 지원 필드: `issueKey`, `project`, `issuetype`, `status`, `assignee`, `reporter`, `issue.property`, `cf[id]`(epic label만 지원). 지원 연산자: `=`, `!=`, `IN`, `NOT IN` | 웹훅 대상 이슈를 지정하는 JQL 필터 | `"project = PRJ"` |

```json
{
  "url": "https://your-app.example.com/webhook-received",
  "webhooks": [
    {
      "events": ["jira:issue_created", "jira:issue_updated"],
      "jqlFilter": "project = PRJ"
    }
  ]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `webhookRegistrationResult` | array | 각 웹훅 등록 결과(`createdWebhookId` 또는 `errors`) | - |

```json
{
  "webhookRegistrationResult": [
    { "createdWebhookId": 1000 },
    { "errors": ["The clause watchCount is unsupported"] },
    { "createdWebhookId": 1001 }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청 본문이 잘못된 경우 | `errorMessages`/`errors` 확인 후 요청 수정 |
| 403 | - | 호출자가 앱(Connect/OAuth 2.0)이 아닌 경우 | 앱 인증 방식으로 재시도 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 앱당 단일 URL만 등록 가능하다(여러 URL로 분산 불가).
- JQL 필터는 일부 필드/연산자만 지원하므로 복잡한 조건은 표현할 수 없다.
- non-public OAuth 앱은 앱 소유자와 웹훅 등록 사용자가 일치해야 실제 전달이 이루어진다.
- 등록된 웹훅은 30일 후 만료되므로(05번 API 참고) 주기적인 연장이 필요하다.

---

### [높음] 3. 웹훅 생명 연장 (PUT /rest/api/3/webhook/refresh)

## 기본 정보

- **기능:** REST API로 등록한 웹훅의 만료 시점을 연장
- **Endpoint:** `PUT /rest/api/3/webhook/refresh`
- **인증:** OAuth 2.0 또는 Connect 앱 인증 필요
- **권한:** Connect 앱 또는 OAuth 2.0 앱만 호출 가능

## 설명

REST API를 통해 등록한 웹훅은 30일이 지나면 자동 만료되므로, 지속적인 웹훅 이벤트 수신을 위해서는 주기적으로 이 API를 호출해 만료일을 연장해야 한다. 다른 앱 소유이거나 존재하지 않는 웹훅 ID는 무시된다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `webhookIds` | array(integer) | 예 | - | 연장할 웹훅 ID 목록 | `[10000, 10001]` |

```json
{
  "webhookIds": [10000, 10001]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `expirationDate` | string | 연장된 새 만료일(ISO 8601) | `"2019-06-01T12:42:30.000+0000"` |

```json
{
  "expirationDate": "2019-06-01T12:42:30.000+0000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 잘못된 경우 | `errorMessages`/`errors` 확인 후 요청 수정 |
| 403 | - | 호출자가 앱(Connect/OAuth 2.0)이 아닌 경우 | 앱 인증 방식으로 재시도 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 웹훅이 30일마다 만료되므로, 운영 환경에서는 이 API를 주기적으로(예: 배치 작업/스케줄러) 호출하는 로직이 필요하다.
- 인식되지 않는 웹훅 ID(존재하지 않거나 다른 앱 소유)는 오류 없이 무시된다.

---

### [중간] 4. 웹훅 ID로 삭제 (DELETE /rest/api/3/webhook)

## 기본 정보

- **기능:** 지정한 ID의 웹훅을 삭제
- **Endpoint:** `DELETE /rest/api/3/webhook`
- **인증:** OAuth 2.0 또는 Connect 앱 인증 필요
- **권한:** Connect 앱 또는 OAuth 2.0 앱만 호출 가능

## 설명

호출한 앱이 등록한 웹훅만 삭제되며, 다른 앱이 생성한 웹훅 ID를 지정해도 무시된다. 프로젝트 종료, 웹훅 설정 변경, 정리 작업 등 부가적인 관리 시나리오에서 사용된다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `webhookIds` | array(integer) | 예 | - | 삭제할 웹훅 ID 목록 | `[10000, 10001]` |

```json
{
  "webhookIds": [10000, 10001]
}
```

## Response

### `202 Accepted`

응답 본문 없음. 요청이 정상적으로 접수되었음을 의미한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 웹훅 ID 목록이 누락된 경우 | `webhookIds` 필드를 포함하여 재요청 |
| 403 | - | 호출자가 앱(Connect/OAuth 2.0)이 아닌 경우 | 앱 인증 방식으로 재시도 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 다른 앱이 등록한 웹훅 ID는 조용히 무시되므로, 삭제 성공 여부는 별도로 목록 조회(01번 API)를 통해 확인해야 한다.

---

### [중간] 5. 실패한 웹훅 조회 (GET /rest/api/3/webhook/failed)

## 기본 정보

- **기능:** 최대 재시도 횟수 이후에도 전달에 실패한 웹훅 목록을 조회
- **Endpoint:** `GET /rest/api/3/webhook/failed`
- **인증:** Connect 앱 인증 필요
- **권한:** Connect 앱만 호출 가능 (OAuth 2.0 앱은 불가)

## 설명

웹훅 전달이 반복적으로 실패한 이력을 확인하는 모니터링/디버깅용 API다. 실패 후 72시간이 지나면 더 이상 조회되지 않을 수 있으며, 가장 오래된 실패 건부터 반환된다. `failedAfter` 값 또는 응답의 `next` URL을 이용한 커서 기반 페이지네이션을 사용한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `maxResults` | integer | 아니오 | - | 페이지당 최대 반환 개수. 동일 실패 시각을 가진 레코드가 페이지 경계에서 분리되는 경우 해당 지시값을 무시하고 모두 포함 | `100` |
| `after` | integer | 아니오 | - | 이 시각(UNIX epoch ms) 이후 발생한 실패만 반환 | `1573118132000` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `values` | array | 실패한 웹훅 목록(`id`, `body`, `url`, `failureTime`) | - |
| `maxResults` | integer | 페이지당 최대 개수 | `100` |
| `next` | string | 다음 페이지 조회 URL | `"https://your-domain.atlassian.net/rest/api/3/webhook/failed?failedAfter=1573540473480&maxResults=100"` |

```json
{
  "values": [
    { "id": "1", "body": "{\"data\":\"webhook data\"}", "url": "https://example.com", "failureTime": 1573118132000 },
    { "id": "2", "url": "https://example.com", "failureTime": 1573540473480 }
  ],
  "maxResults": 100,
  "next": "https://your-domain.atlassian.net/rest/api/3/webhook/failed?failedAfter=1573540473480&maxResults=100"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 잘못된 요청 | `errorMessages`/`errors` 확인 후 재요청 |
| 403 | - | 호출자가 Connect 앱이 아닌 경우 | Connect 앱 인증으로 재시도 (OAuth 2.0 앱은 이 API 사용 불가) |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 다른 웹훅 API와 달리 Connect 앱에서만 호출 가능하고 OAuth 2.0 앱은 사용할 수 없다.
- 실패 이력은 72시간이 지나면 조회되지 않을 수 있으므로, 장애 모니터링을 하려면 주기적으로 폴링해야 한다.
