# _83-status API 요약

이 리소스 그룹은 Jira의 "Status"(이슈 상태) 정의를 검색, 조회, 생성, 수정, 삭제하고 특정 상태가 어느 이슈 타입/프로젝트/워크플로우에서 사용되고 있는지 조회하는 API 모음이다. 여기서 다루는 "상태"는 워크플로우 상 이슈가 전이되는 상태 값(To Do/In Progress/Done 등) 자체의 정의(카탈로그)를 의미하며, 개별 이슈의 상태 전이(transition) API와는 다르다.

## 제외된 API

- 제외된 API 없음 (모든 엔드포인트가 "Administer projects" 또는 "Administer Jira" 프로젝트 권한 중 하나만 있으면 호출 가능하며, "Jira administrators only"(사이트 전체 관리자 전용)로 명시된 항목은 없었다.)

---

### [높음] 1. Bulk get statuses (GET /rest/api/3/statuses)

## 기본 정보

- **기능:** 하나 이상의 상태 ID로 상태(status) 상세 정보를 일괄 조회
- **Endpoint:** `GET /rest/api/3/statuses`
- **인증:** Bearer Token(또는 Basic/OAuth 등 Jira Cloud 인증) 필요
- **권한:** *Administer projects* 프로젝트 권한 또는 *Administer Jira* 전역 권한 중 하나

## 설명

지정한 상태 ID 목록에 해당하는 상태들의 이름, 설명, 범위(scope), 상태 카테고리를 반환한다. 대시보드나 자동화 로직에서 상태 ID를 사람이 읽을 수 있는 이름/카테고리로 변환하는 용도로 사용할 수 있다. 최소 1개, 최대 50개의 ID를 한 번에 조회할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `id` | `array` | Yes | - | 조회할 상태 ID 목록. 여러 개를 지정하려면 `&`로 구분한 리스트 형태로 전달 (최소 1개, 최대 50개) | `id=10000&id=10001` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | `string` | 상태 ID | `"1000"` |
| `name` | `string` | 상태 이름 | `"Finished"` |
| `description` | `string` | 상태 설명 | `"The issue is resolved"` |
| `statusCategory` | `enum` | 상태 카테고리 (`TODO`/`IN_PROGRESS`/`DONE`) | `"DONE"` |
| `scope` | `object` | 상태의 적용 범위(프로젝트 또는 전역) | `{"project":{"id":"1"},"type":"PROJECT"}` |

```json
[
  {
    "description": "The issue is resolved",
    "id": "1000",
    "name": "Finished",
    "scope": { "project": { "id": "1" }, "type": "PROJECT" },
    "statusCategory": "DONE"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 (잘못된 ID 형식 등) | 요청 파라미터 검증 후 재요청 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 권한 부족 | 인증 토큰 및 권한 확인 |

## 주의 사항

- `id` 파라미터는 최소 1개, 최대 50개까지만 허용된다.

---

### [높음] 2. Bulk get statuses by name (GET /rest/api/3/statuses/byNames)

## 기본 정보

- **기능:** 하나 이상의 상태 이름으로 상태 상세 정보를 일괄 조회
- **Endpoint:** `GET /rest/api/3/statuses/byNames`
- **인증:** Bearer Token 필요
- **권한:** *Administer projects*, *Administer Jira*, *Browse projects* 프로젝트 권한 중 하나

## 설명

상태 이름(예: "Done", "In Progress")을 기준으로 상태 정보를 조회한다. *Browse projects* 권한만으로도 호출 가능해 일반 프로젝트 멤버 수준 권한으로도 사용할 수 있는 조회 API다. 특정 프로젝트로 범위를 좁히려면 `projectId`를 지정하고, 생략하면 전역 상태까지 포함해 검색한다. 최소 1개, 최대 50개의 이름을 한 번에 조회할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | `array` | Yes | - | 조회할 상태 이름 목록. 여러 개를 지정하려면 `&`로 구분 (최소 1개, 최대 50개) | `name=nameXX&name=nameYY` |
| `projectId` | `string` | No | - | 상태가 속한 프로젝트 ID. 전역 상태를 조회하려면 생략(null) | `"10000"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | `string` | 상태 ID | `"1000"` |
| `name` | `string` | 상태 이름 | `"Finished"` |
| `description` | `string` | 상태 설명 | `"The issue is resolved"` |
| `statusCategory` | `enum` | 상태 카테고리 (`TODO`/`IN_PROGRESS`/`DONE`) | `"DONE"` |
| `scope` | `object` | 상태의 적용 범위 | `{"project":{"id":"1"},"type":"PROJECT"}` |

```json
[
  {
    "description": "The issue is resolved",
    "id": "1000",
    "name": "Finished",
    "scope": { "project": { "id": "1" }, "type": "PROJECT" },
    "statusCategory": "DONE"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 요청 파라미터 검증 후 재요청 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 권한 부족 | 인증 토큰 및 권한 확인 |

## 주의 사항

- `name` 파라미터는 최소 1개, 최대 50개까지만 허용된다.
- *Browse projects* 권한만으로도 호출 가능해 세 API 중 접근 장벽이 가장 낮다.

---

### [높음] 3. Search statuses paginated (GET /rest/api/3/statuses/search)

## 기본 정보

- **기능:** 이름 또는 프로젝트를 기준으로 상태를 검색하는 페이지네이션 목록 API
- **Endpoint:** `GET /rest/api/3/statuses/search`
- **인증:** Bearer Token 필요
- **권한:** *Administer projects* 프로젝트 권한 또는 *Administer Jira* 전역 권한 중 하나

## 설명

검색어(`searchString`), 프로젝트(`projectId`), 상태 카테고리(`statusCategory`) 조건으로 상태 목록을 페이지 단위로 조회한다. 대시보드에서 프로젝트별 사용 가능한 상태 전체 목록을 보여주거나, 상태 카테고리(TODO/IN_PROGRESS/DONE)별 필터링 UI를 만들 때 활용할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---|---:|---|---|
| `projectId` | `string` | No | - | 상태가 속한 프로젝트 ID. 전역 상태는 null | `"10000"` |
| `startAt` | `integer` | No | - | 페이지 오프셋(첫 결과의 인덱스) | `0` |
| `maxResults` | `integer` | No | - | 페이지당 최대 결과 수 | `2` |
| `searchString` | `string` | No | - | 상태 이름 매칭 검색어. 생략 시 검색 범위 내 전체 상태 반환 | `"done"` |
| `statusCategory` | `string` | No | - | 필터링할 상태 카테고리 (`TODO`, `IN_PROGRESS`, `DONE`) | `"DONE"` |
| `includeGlobalStatuses` | `boolean` | No | `false` | 전역 상태(scope=null)를 결과에 포함할지 여부. 프로젝트 범위 쿼리에서만 유효 | `true` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | `boolean` | 마지막 페이지 여부 | `true` |
| `maxResults` | `integer` | 페이지당 최대 결과 수 | `2` |
| `startAt` | `integer` | 현재 페이지 시작 인덱스 | `0` |
| `total` | `integer` | 전체 결과 수 | `5` |
| `self` | `string` | 현재 요청 URL | `"https://your-domain.atlassian.net/rest/api/3/statuses/search?startAt=0&maxResults=2"` |
| `nextPage` | `string` | 다음 페이지 URL | `"https://your-domain.atlassian.net/rest/api/3/statuses/search?startAt=2&maxResults=2"` |
| `values` | `array` | 상태 객체 목록 | `[{"id":"1000","name":"Finished", ...}]` |

```json
{
  "isLast": true,
  "maxResults": 2,
  "nextPage": "https://your-domain.atlassian.net/rest/api/3/statuses/search?startAt=2&maxResults=2",
  "self": "https://your-domain.atlassian.net/rest/api/3/statuses/search?startAt=0&maxResults=2",
  "startAt": 0,
  "total": 5,
  "values": [
    {
      "description": "The issue is resolved",
      "id": "1000",
      "name": "Finished",
      "scope": { "project": { "id": "1" }, "type": "PROJECT" },
      "statusCategory": "DONE"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 요청 파라미터 검증 후 재요청 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 권한 부족 | 인증 토큰 및 권한 확인 |

## 주의 사항

- `includeGlobalStatuses`는 `projectId`가 지정된 프로젝트 범위 쿼리에서만 의미가 있다.
- 페이지네이션은 `startAt`/`maxResults`/`nextPage` 방식(오프셋 기반)이다.

---

### [중간] 4. Bulk update statuses (PUT /rest/api/3/statuses)

## 기본 정보

- **기능:** 상태(status) 정의를 ID로 일괄 수정
- **Endpoint:** `PUT /rest/api/3/statuses`
- **인증:** Bearer Token 필요
- **권한:** *Administer projects* 프로젝트 권한 또는 *Administer Jira* 전역 권한 중 하나

## 설명

기존 상태의 이름, 설명, 카테고리를 일괄 수정한다. 워크플로우에 사용 중인 상태 정의 자체를 바꾸는 관리자용 작업으로, 팀 생성 자동화나 알림/대시보드 같은 핵심 POC 흐름에서 직접 호출할 일은 적다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `statuses` | `array` | Yes | - | 수정할 상태 목록 | 아래 예시 참고 |
| `statuses[].id` | `string` | Yes | - | 상태 ID | `"1000"` |
| `statuses[].name` | `string` | Yes | - | 상태 이름 | `"Finished"` |
| `statuses[].description` | `string` | No | - | 상태 설명 | `"The issue is resolved"` |
| `statuses[].statusCategory` | `enum` | Yes | `TODO`/`IN_PROGRESS`/`DONE` | 상태 카테고리 | `"DONE"` |

```json
{
  "statuses": [
    {
      "description": "The issue is resolved",
      "id": "1000",
      "name": "Finished",
      "statusCategory": "DONE"
    }
  ]
}
```

## Response

### `204 No Content`

응답 본문 없음(성공 시).

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 (예: 이름 길이 초과) | 요청 값 검증 후 재요청 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 권한 부족 | 인증 토큰 및 권한 확인 |
| 409 | - | 다른 워크플로우 설정 변경 작업이 진행 중 | 잠시 후 재시도 |

```json
{ "errorMessages": ["The name is too long, maxSize=255"], "errors": {} }
```

## 주의 사항

- 다른 워크플로우 구성 변경 작업과 동시에 실행하면 409 충돌이 발생할 수 있다.

---

### [중간] 5. Bulk create statuses (POST /rest/api/3/statuses)

## 기본 정보

- **기능:** 전역 또는 프로젝트 범위의 상태(status)를 일괄 생성
- **Endpoint:** `POST /rest/api/3/statuses`
- **인증:** Bearer Token 필요
- **권한:** *Administer projects* 프로젝트 권한 또는 *Administer Jira* 전역 권한 중 하나

## 설명

새 상태를 회사 관리(company-managed, `GLOBAL`) 또는 팀 관리(team-managed, `PROJECT`) 범위로 생성한다. 팀 생성 자동화 시 프로젝트 전용 커스텀 상태를 세팅하고 싶을 때 보조적으로 쓰일 수 있으나, 필수 핵심 흐름은 아니다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `scope` | `object` | Yes | - | 상태의 적용 범위 | `{"project":{"id":"1"},"type":"PROJECT"}` |
| `scope.type` | `enum` | Yes | `PROJECT`/`GLOBAL` | `GLOBAL`은 회사 관리 프로젝트, `PROJECT`는 팀 관리 프로젝트용 | `"PROJECT"` |
| `scope.project.id` | `string` | Yes | - | 프로젝트 ID | `"1"` |
| `statuses` | `array` | Yes | - | 생성할 상태 목록 | 아래 예시 참고 |
| `statuses[].name` | `string` | Yes | - | 상태 이름 | `"Finished"` |
| `statuses[].description` | `string` | No | - | 상태 설명 | `"The issue is resolved"` |
| `statuses[].statusCategory` | `enum` | Yes | `TODO`/`IN_PROGRESS`/`DONE` | 상태 카테고리 | `"DONE"` |

```json
{
  "scope": {
    "project": { "id": "1" },
    "type": "PROJECT"
  },
  "statuses": [
    {
      "description": "The issue is resolved",
      "name": "Finished",
      "statusCategory": "DONE"
    }
  ]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | `string` | 생성된 상태 ID | `"1000"` |
| `name` | `string` | 상태 이름 | `"Finished"` |
| `description` | `string` | 상태 설명 | `"The issue is resolved"` |
| `statusCategory` | `enum` | 상태 카테고리 | `"DONE"` |
| `scope` | `object` | 적용 범위 | `{"project":{"id":"1"},"type":"PROJECT"}` |

```json
[
  {
    "description": "The issue is resolved",
    "id": "1000",
    "name": "Finished",
    "scope": { "project": { "id": "1" }, "type": "PROJECT" },
    "statusCategory": "DONE"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 (예: 이름 길이 초과) | 요청 값 검증 후 재요청 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 권한 부족 | 인증 토큰 및 권한 확인 |
| 409 | - | 다른 워크플로우 설정 변경 작업이 진행 중 | 잠시 후 재시도 |

```json
{ "errorMessages": ["The name is too long, maxSize=255"], "errors": {} }
```

## 주의 사항

- `scope.type`이 `GLOBAL`이면 회사 관리 프로젝트용, `PROJECT`이면 팀 관리 프로젝트 전용 상태가 생성된다.
- 다른 워크플로우 구성 변경 작업과 동시에 실행하면 409 충돌이 발생할 수 있다.

---

### [중간] 6. Bulk delete Statuses (DELETE /rest/api/3/statuses)

## 기본 정보

- **기능:** 상태(status)를 ID로 일괄 삭제
- **Endpoint:** `DELETE /rest/api/3/statuses`
- **인증:** Bearer Token 필요
- **권한:** *Administer projects* 프로젝트 권한 또는 *Administer Jira* 전역 권한 중 하나

## 설명

지정한 상태 ID들을 삭제한다. 상태 카탈로그를 정리하는 관리 작업으로, 워크플로우/이슈 타입에서 사용 중인 상태를 삭제하면 오류가 발생할 수 있어 신중하게 사용해야 한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `id` | `array` | Yes | - | 삭제할 상태 ID 목록. 여러 개는 `&`로 구분 (최소 1개, 최대 50개) | `id=10000&id=10001` |

## Response

### `204 No Content`

응답 본문 없음(성공 시).

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 요청 파라미터 검증 후 재요청 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 권한 부족 | 인증 토큰 및 권한 확인 |

```json
{ "errorMessages": ["The name is too long, maxSize=255"], "errors": {} }
```

## 주의 사항

- 워크플로우나 이슈 타입에서 사용 중인 상태를 삭제하려고 하면 실패할 수 있으므로, 삭제 전 사용처(07~09 API)를 확인하는 것이 안전하다.

---

### [중간] 7. Get issue type usages by status and project (GET /rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages)

## 기본 정보

- **기능:** 특정 프로젝트에서 특정 상태를 사용하는 이슈 타입 목록을 페이지 단위로 조회
- **Endpoint:** `GET /rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages`
- **인증:** Bearer Token 필요
- **권한:** 문서에 별도 명시 없음(엔드포인트 특성상 프로젝트 조회 권한 수준으로 추정)

## 설명

주어진 상태가 특정 프로젝트 내 어느 이슈 타입에서 사용되고 있는지 확인한다. 상태 삭제/수정 전 영향 범위를 파악하는 용도로 유용하지만, 알림/대시보드/이슈 CRUD 같은 핵심 흐름에는 직접 관여하지 않는 보조 조회 API다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `statusId` | `string` | Yes | 이슈 타입 사용 현황을 조회할 상태 ID | `"1000"` |
| `projectId` | `string` | Yes | 이슈 타입 사용 현황을 조회할 프로젝트 ID | `"2000"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---|---:|---|---|
| `nextPageToken` | `string` | No | - | 페이지네이션 커서 | `"eyJvIjoyfQ=="` |
| `maxResults` | `integer` | No | - | 반환할 최대 결과 수 (1~200 사이 정수) | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `statusId` | `string` | 상태 ID | `"1000"` |
| `projectId` | `string` | 프로젝트 ID | `"2000"` |
| `issueTypes.values` | `array` | 해당 상태를 사용하는 이슈 타입 목록 | `[{"id":"1000"}]` |
| `issueTypes.nextPageToken` | `string` | 다음 페이지 커서 | `"eyJvIjoyfQ=="` |

```json
{
  "issueTypes": {
    "nextPageToken": "eyJvIjoyfQ==",
    "values": [{ "id": "1000" }]
  },
  "projectId": "2000",
  "statusId": "1000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `nextPageToken` 형식이 잘못됨 등 요청이 유효하지 않음 | 파라미터 검증 후 재요청 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 권한 부족 | 인증 토큰 및 권한 확인 |
| 404 | - | 해당 ID의 상태가 존재하지 않음 | 상태 ID 확인 |

```json
{ "errorMessages": ["Invalid format of nextPageToken"], "errors": {} }
```

## 주의 사항

- 페이지네이션은 토큰 기반(`nextPageToken`)이며 오프셋 방식이 아니다.
- `maxResults`는 1~200 범위로 제한된다.

---

### [중간] 8. Get project usages by status (GET /rest/api/3/statuses/{statusId}/projectUsages)

## 기본 정보

- **기능:** 특정 상태를 사용하는 프로젝트 목록을 페이지 단위로 조회
- **Endpoint:** `GET /rest/api/3/statuses/{statusId}/projectUsages`
- **인증:** Bearer Token 필요
- **권한:** 문서에 별도 명시 없음

## 설명

주어진 상태 ID가 어느 프로젝트들에서 사용되고 있는지 확인한다. 상태 삭제 전 영향 범위 파악, 또는 여러 프로젝트에 걸친 상태 사용 현황 감사(audit) 용도로 활용할 수 있는 보조 조회 API다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `statusId` | `string` | Yes | 프로젝트 사용 현황을 조회할 상태 ID | `"1000"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---|---:|---|---|
| `nextPageToken` | `string` | No | - | 페이지네이션 커서 | `"eyJvIjoyfQ=="` |
| `maxResults` | `integer` | No | - | 반환할 최대 결과 수 (1~200 사이 정수) | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `statusId` | `string` | 상태 ID | `"1000"` |
| `projects.values` | `array` | 해당 상태를 사용하는 프로젝트 목록 | `[{"id":"1000"}]` |
| `projects.nextPageToken` | `string` | 다음 페이지 커서 | `"eyJvIjoyfQ=="` |

```json
{
  "projects": {
    "nextPageToken": "eyJvIjoyfQ==",
    "values": [{ "id": "1000" }]
  },
  "statusId": "1000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `nextPageToken` 형식이 잘못됨 등 요청이 유효하지 않음 | 파라미터 검증 후 재요청 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 권한 부족 | 인증 토큰 및 권한 확인 |
| 404 | - | 해당 ID의 상태가 존재하지 않음 | 상태 ID 확인 |

```json
{ "errorMessages": ["Invalid format of nextPageToken"], "errors": {} }
```

## 주의 사항

- 페이지네이션은 토큰 기반(`nextPageToken`)이다.
- `maxResults`는 1~200 범위로 제한된다.

---

### [중간] 9. Get workflow usages by status (GET /rest/api/3/statuses/{statusId}/workflowUsages)

## 기본 정보

- **기능:** 특정 상태를 사용하는 워크플로우 목록을 페이지 단위로 조회
- **Endpoint:** `GET /rest/api/3/statuses/{statusId}/workflowUsages`
- **인증:** Bearer Token 필요
- **권한:** 문서에 별도 명시 없음

## 설명

주어진 상태 ID가 어느 워크플로우들에서 사용되고 있는지 확인한다. 상태 삭제나 워크플로우 변경 작업 전 영향 범위를 파악하는 보조 조회 API다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `statusId` | `string` | Yes | 워크플로우 사용 현황을 조회할 상태 ID | `"1000"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---|---:|---|---|
| `nextPageToken` | `string` | No | - | 페이지네이션 커서 | `"eyJvIjoyfQ=="` |
| `maxResults` | `integer` | No | - | 반환할 최대 결과 수 (1~200 사이 정수) | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `statusId` | `string` | 상태 ID | `"1000"` |
| `workflows.values` | `array` | 해당 상태를 사용하는 워크플로우 목록 | `[{"id":"545d80a3-91ff-4949-8b0d-a2bc484e70e5"}]` |
| `workflows.nextPageToken` | `string` | 다음 페이지 커서 | `"eyJvIjoyfQ=="` |

```json
{
  "statusId": "1000",
  "workflows": {
    "nextPageToken": "eyJvIjoyfQ==",
    "values": [{ "id": "545d80a3-91ff-4949-8b0d-a2bc484e70e5" }]
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `nextPageToken` 형식이 잘못됨 등 요청이 유효하지 않음 | 파라미터 검증 후 재요청 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 권한 부족 | 인증 토큰 및 권한 확인 |
| 404 | - | 해당 ID의 상태가 존재하지 않음 | 상태 ID 확인 |

```json
{ "errorMessages": ["Invalid format of nextPageToken"], "errors": {} }
```

## 주의 사항

- 페이지네이션은 토큰 기반(`nextPageToken`)이다.
- 워크플로우 ID는 UUID 형태로 반환된다 (예: `545d80a3-91ff-4949-8b0d-a2bc484e70e5`).
