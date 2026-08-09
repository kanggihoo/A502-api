# __36-issue-remote-links API 요약

이 리소스 그룹은 Jira 이슈와 외부 시스템(예: GitLab, Mattermost, 사내 지원 시스템 등)의 항목을 연결하는 "원격 이슈 링크(remote issue link)"를 조회·생성·수정·삭제하는 API 모음이다. 통합 알림/대시보드에서 이슈에 연결된 외부 링크를 보여주거나, 다른 도구의 리소스를 Jira 이슈에 자동으로 연결하는 데 사용할 수 있다.

## 제외된 API

- 없음 (모든 엔드포인트가 프로젝트 단위 권한(Browse projects / Link issues / Edit issues)만 요구하며, 사이트 전체 관리자 권한이 필요한 API는 없음)

---

### [높은 우선순위] 1. 원격 이슈 링크 목록 조회 (GET /rest/api/3/issue/{issueIdOrKey}/remotelink)

## 기본 정보

- **기능:** 이슈에 연결된 원격 이슈 링크를 조회한다. `globalId`를 지정하면 해당 링크 하나만, 지정하지 않으면 전체 목록을 반환한다.
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}/remotelink`
- **인증:** Bearer Token 필요 (단, 익명 접근 허용 설정 시 불필요할 수 있음)
- **권한:** *Browse projects* 프로젝트 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한도 필요.

## 설명

이슈 연결(issue linking) 기능이 활성화되어 있어야 호출할 수 있다. 통합 대시보드에서 이슈에 연결된 외부 시스템 항목(예: GitLab MR, 지원 티켓 등)을 보여줄 때 사용한다. `globalId`에 URL 예약 문자가 포함된 경우 URL 인코딩하여 전달해야 한다(예: `system=http://www.mycompany.com/support&id=1` → `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`).

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | `string` | Yes | 이슈의 ID 또는 키 | `MKY-1` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `globalId` | `string` | No | - | 원격 이슈 링크의 글로벌 ID | `system=http://www.mycompany.com/support&id=1` |

## Response

### `200 OK`

`globalId`를 지정하면 단일 RemoteIssueLink 객체, 그렇지 않으면 RemoteIssueLink 배열을 반환한다.

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | `number` | 원격 이슈 링크 ID | `10000` |
| `self` | `string` | 링크의 REST API URL | `https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10000` |
| `globalId` | `string` | 원격 항목의 글로벌 ID | `system=http://www.mycompany.com/support&id=1` |
| `application` | `object` | 원격 애플리케이션 정보 (`name`, `type`) | `{"name":"My Acme Tracker","type":"com.acme.tracker"}` |
| `relationship` | `string` | 이슈와 링크 항목 간의 관계 설명 | `causes` |
| `object` | `object` | 링크된 항목 상세 정보 (`title`, `url`, `summary`, `icon`, `status`) | 아래 예시 참고 |

```json
[
  {
    "application": { "name": "My Acme Tracker", "type": "com.acme.tracker" },
    "globalId": "system=http://www.mycompany.com/support&id=1",
    "id": 10000,
    "object": {
      "icon": { "title": "Support Ticket", "url16x16": "http://www.mycompany.com/support/ticket.png" },
      "status": {
        "icon": { "link": "http://www.mycompany.com/support?id=1&details=closed", "title": "Case Closed", "url16x16": "http://www.mycompany.com/support/resolved.png" },
        "resolved": true
      },
      "summary": "Customer support issue",
      "title": "TSTSUP-111",
      "url": "http://www.mycompany.com/support?id=1"
    },
    "relationship": "causes",
    "self": "https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10000"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 파라미터 형식(특히 `globalId` 인코딩) 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 403 | - | 이슈 연결(issue linking) 기능이 비활성화됨 | Jira 설정에서 issue linking 활성화 필요 |
| 404 | - | 이슈나 원격 링크를 찾을 수 없거나 조회 권한 없음 | 이슈 키/ID 및 권한 확인 |
| 413 | - | 이슈당 원격 링크 개수 제한 초과 | 불필요한 링크 정리 필요 |

## 주의 사항

- 익명 접근이 가능하도록 설정되어 있을 수 있으나, 일반적으로는 Bearer Token 인증을 사용한다.
- `globalId`에 특수문자가 있으면 반드시 URL 인코딩해서 전달해야 한다.

---

### [높은 우선순위] 2. 원격 이슈 링크 생성/수정 (POST /rest/api/3/issue/{issueIdOrKey}/remotelink)

## 기본 정보

- **기능:** 이슈에 원격 이슈 링크를 생성하거나, 기존 `globalId`가 일치하는 링크가 있으면 갱신한다.
- **Endpoint:** `POST /rest/api/3/issue/{issueIdOrKey}/remotelink`
- **인증:** Bearer Token 필요
- **권한:** *Browse projects* 및 *Link issues* 프로젝트 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한도 필요.

## 설명

`globalId`가 요청에 포함되어 있고 동일한 글로벌 ID를 가진 링크가 이미 존재하면 그 링크를 갱신하며, 이때 요청에 값이 없는 필드는 null로 설정된다. 존재하지 않으면 새 링크를 생성한다. 팀 생성 자동화나 통합 알림 흐름에서 GitLab MR, Mattermost 스레드 등 외부 리소스를 Jira 이슈에 자동으로 연결하는 핵심 API다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | `string` | Yes | 이슈의 ID 또는 키 | `MKY-1` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `application` | `any` | No | - | 원격 애플리케이션 상세 정보 (예: Trello) | `{"name":"My Acme Tracker","type":"com.acme.tracker"}` |
| `globalId` | `string` | No | 최대 255자 | 원격 시스템에서의 원격 항목 식별자. 설정 시 이후 Jira ID 대신 이 값으로 링크를 조회/수정/삭제 가능 | `appId=456&pageId=123` |
| `object` | `any` | Yes | - | 링크된 항목의 상세 정보 | `{"url":"http://www.mycompany.com/support?id=1","title":"TSTSUP-111"}` |
| `relationship` | `string` | No | - | 이슈와 링크 항목 간의 관계 설명. 미지정 시 "links to" 사용 | `causes` |

```json
{
  "application": { "name": "My Acme Tracker", "type": "com.acme.tracker" },
  "globalId": "system=http://www.mycompany.com/support&id=1",
  "object": {
    "icon": { "title": "Support Ticket", "url16x16": "http://www.mycompany.com/support/ticket.png" },
    "status": {
      "icon": { "link": "http://www.mycompany.com/support?id=1&details=closed", "title": "Case Closed", "url16x16": "http://www.mycompany.com/support/resolved.png" },
      "resolved": true
    },
    "summary": "Customer support issue",
    "title": "TSTSUP-111",
    "url": "http://www.mycompany.com/support?id=1"
  },
  "relationship": "causes"
}
```

## Response

### `200 OK` (갱신된 경우) / `201 Created` (생성된 경우)

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | `number` | 생성/갱신된 원격 이슈 링크 ID | `10000` |
| `self` | `string` | 링크의 REST API URL | `https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10000` |

```json
{
  "id": 10000,
  "self": "https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청 본문이 유효하지 않음 (예: 필수 필드 누락) | 오류 메시지의 필드 확인 후 재요청 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 403 | - | 이슈 연결 권한 없음 | *Link issues* 권한 확인 |
| 404 | - | 이슈를 찾을 수 없거나 조회 권한 없음 | 이슈 키/ID 및 권한 확인 |

```json
{
  "errorMessages": [],
  "errors": { "title": "'title' is required." }
}
```

## 주의 사항

- `globalId`를 지정하면 이후 이 값을 키로 삼아 링크를 조회/수정/삭제할 수 있어, 외부 시스템 리소스 ID와 1:1 매핑하기 좋다.
- 이슈 연결 기능이 비활성화되어 있으면 호출할 수 없다.

---

### [중간 우선순위] 3. 글로벌 ID로 원격 이슈 링크 삭제 (DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink)

## 기본 정보

- **기능:** 원격 이슈 링크의 글로벌 ID를 이용해 이슈에서 해당 링크를 삭제한다.
- **Endpoint:** `DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink`
- **인증:** Bearer Token 필요
- **권한:** *Browse projects* 및 *Link issues* 프로젝트 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한도 필요.

## 설명

`globalId` 쿼리 파라미터로 삭제할 링크를 지정한다. 글로벌 ID에 URL 예약 문자가 포함되어 있으면 인코딩해서 전달해야 한다. 외부 시스템 리소스 ID로 링크를 관리하는 통합 시나리오(예: GitLab 이슈 삭제 시 연결된 Jira 링크 정리)에 유용하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | `string` | Yes | 이슈의 ID 또는 키 | `MKY-1` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `globalId` | `string` | Yes | - | 삭제할 원격 이슈 링크의 글로벌 ID | `system=http://www.mycompany.com/support&id=1` |

## Response

### `204 No Content`

요청이 성공하면 별도의 응답 본문 없이 204를 반환한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `globalId`가 제공되지 않음 | 쿼리 파라미터 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 403 | - | 이슈 연결 권한 없음 | *Link issues* 권한 확인 |
| 404 | - | 이슈나 원격 링크를 찾을 수 없거나 조회 권한 없음 | 이슈 키/ID 및 `globalId` 확인 |

## 주의 사항

- `globalId`는 필수 쿼리 파라미터이며, 인코딩 여부에 유의해야 한다.

---

### [중간 우선순위] 4. ID로 원격 이슈 링크 조회 (GET /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId})

## 기본 정보

- **기능:** 이슈에 연결된 특정 원격 이슈 링크를 ID로 조회한다.
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`
- **인증:** Bearer Token 필요
- **권한:** *Browse projects* 프로젝트 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한도 필요.

## 설명

Jira 내부 링크 ID(`linkId`)를 이용해 단일 원격 이슈 링크의 상세 정보를 조회한다. 링크 목록 조회(1번 API) 후 특정 링크의 최신 상태만 확인하고 싶을 때 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | `string` | Yes | 이슈의 ID 또는 키 | `MKY-1` |
| `linkId` | `string` | Yes | 원격 이슈 링크의 ID | `10000` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | `number` | 원격 이슈 링크 ID | `10000` |
| `self` | `string` | 링크의 REST API URL | `https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10000` |
| `globalId` | `string` | 원격 항목의 글로벌 ID | `system=http://www.mycompany.com/support&id=1` |
| `application` | `object` | 원격 애플리케이션 정보 | `{"name":"My Acme Tracker","type":"com.acme.tracker"}` |
| `relationship` | `string` | 이슈와 링크 항목 간의 관계 설명 | `causes` |
| `object` | `object` | 링크된 항목 상세 정보 | 아래 예시 참고 |

```json
{
  "application": { "name": "My Acme Tracker", "type": "com.acme.tracker" },
  "globalId": "system=http://www.mycompany.com/support&id=1",
  "id": 10000,
  "object": {
    "icon": { "title": "Support Ticket", "url16x16": "http://www.mycompany.com/support/ticket.png" },
    "status": {
      "icon": { "link": "http://www.mycompany.com/support?id=1&details=closed", "title": "Case Closed", "url16x16": "http://www.mycompany.com/support/resolved.png" },
      "resolved": true
    },
    "summary": "Customer support issue",
    "title": "TSTSUP-111",
    "url": "http://www.mycompany.com/support?id=1"
  },
  "relationship": "causes",
  "self": "https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 링크 ID가 유효하지 않거나 해당 이슈에 속하지 않음 | `linkId`와 `issueIdOrKey` 조합 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 403 | - | 이슈 연결 기능이 비활성화됨 | Jira 설정에서 issue linking 활성화 필요 |
| 404 | - | 이슈나 원격 링크를 찾을 수 없거나 조회 권한 없음 | 이슈 키/ID 및 권한 확인 |

## 주의 사항

- 없음

---

### [중간 우선순위] 5. ID로 원격 이슈 링크 수정 (PUT /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId})

## 기본 정보

- **기능:** Jira 내부 링크 ID를 이용해 특정 원격 이슈 링크를 수정한다.
- **Endpoint:** `PUT /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`
- **인증:** Bearer Token 필요
- **권한:** *Browse projects* 및 *Link issues* 프로젝트 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한도 필요.

## 설명

`globalId` 대신 Jira 내부 `linkId`를 식별자로 사용해 원격 이슈 링크를 갱신한다. 요청에 값이 없는 필드는 null로 설정되므로 전체 필드를 다시 보내야 한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | `string` | Yes | 이슈의 ID 또는 키 | `MKY-1` |
| `linkId` | `string` | Yes | 원격 이슈 링크의 ID | `10000` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `application` | `any` | No | - | 원격 애플리케이션 상세 정보 | `{"name":"My Acme Tracker","type":"com.acme.tracker"}` |
| `globalId` | `string` | No | 최대 255자 | 원격 시스템에서의 원격 항목 식별자 | `appId=456&pageId=123` |
| `object` | `any` | Yes | - | 링크된 항목의 상세 정보 | `{"url":"http://www.mycompany.com/support?id=1","title":"TSTSUP-111"}` |
| `relationship` | `string` | No | - | 이슈와 링크 항목 간의 관계 설명 | `causes` |

```json
{
  "application": { "name": "My Acme Tracker", "type": "com.acme.tracker" },
  "globalId": "system=http://www.mycompany.com/support&id=1",
  "object": {
    "icon": { "title": "Support Ticket", "url16x16": "http://www.mycompany.com/support/ticket.png" },
    "status": {
      "icon": { "link": "http://www.mycompany.com/support?id=1&details=closed", "title": "Case Closed", "url16x16": "http://www.mycompany.com/support/resolved.png" },
      "resolved": true
    },
    "summary": "Customer support issue",
    "title": "TSTSUP-111",
    "url": "http://www.mycompany.com/support?id=1"
  },
  "relationship": "causes"
}
```

## Response

### `204 No Content`

요청이 성공하면 별도의 응답 본문 없이 204를 반환한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 링크 ID가 유효하지 않거나, 해당 이슈에 속하지 않거나, 요청 본문이 유효하지 않음 | `linkId` 및 필수 필드 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 403 | - | 이슈 연결 권한 없음 | *Link issues* 권한 확인 |
| 404 | - | 이슈나 원격 링크를 찾을 수 없거나 조회 권한 없음 | 이슈 키/ID 및 `linkId` 확인 |

```json
{
  "errorMessages": [],
  "errors": { "title": "'title' is required." }
}
```

## 주의 사항

- 값이 없는 필드는 null로 덮어써지므로 부분 업데이트가 아닌 전체 필드 전송이 필요하다.

---

### [중간 우선순위] 6. ID로 원격 이슈 링크 삭제 (DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId})

## 기본 정보

- **기능:** Jira 내부 링크 ID를 이용해 이슈에서 특정 원격 이슈 링크를 삭제한다.
- **Endpoint:** `DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`
- **인증:** Bearer Token 필요
- **권한:** *Browse projects*, *Edit issues*, *Link issues* 프로젝트 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한도 필요.

## 설명

`globalId`가 아닌 Jira 내부 `linkId`로 원격 이슈 링크를 삭제한다. 3번 API(글로벌 ID 삭제)와 달리 *Edit issues* 권한까지 요구한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | `string` | Yes | 이슈의 ID 또는 키 | `MKY-1` |
| `linkId` | `string` | Yes | 원격 이슈 링크의 ID | `10000` |

## Response

### `204 No Content`

요청이 성공하면 별도의 응답 본문 없이 204를 반환한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 링크 ID가 유효하지 않거나 해당 이슈에 속하지 않음 | `linkId`와 `issueIdOrKey` 조합 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 403 | - | 이슈 연결 권한 없음 | *Link issues* 권한 확인 |
| 404 | - | 이슈나 원격 링크를 찾을 수 없거나 조회 권한 없음 | 이슈 키/ID 및 `linkId` 확인 |

## 주의 사항

- 다른 삭제/수정 API와 달리 *Edit issues* 권한도 요구한다는 점에 유의한다.
