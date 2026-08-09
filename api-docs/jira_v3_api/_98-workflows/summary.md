# _98-workflows API 요약

이 리소스 그룹은 Jira의 워크플로우(상태 흐름, 전이 규칙) 자체를 조회·생성·수정·삭제하는 API 모음이다. 팀 프로젝트 상태를 파악하거나 어떤 프로젝트/이슈타입이 어떤 워크플로우를 쓰는지 확인하는 용도로 주로 사용한다.

## 제외된 API

- `03-get-workflows-paginated-get.md`: 설명에 "*Administer Jira* global permission" 및 403 에러 메시지 "Only Jira administrators can access workflows."가 명시되어 있어 사이트 전체 관리자 권한이 있어야만 호출 가능. 또한 2026년 6월 1일 제거 예정(Deprecated)인 구버전 API.
- `04-delete-inactive-workflow-delete.md`: 설명에 "*Administer Jira* global permission"이 명시되어 있고, 403 에러 메시지 "Only Jira administrators can access the workflow configuration."로 사이트 전체 관리자 권한 필요.

---

### [높음] 1. 프로젝트 내 워크플로우를 사용하는 이슈 타입 조회 (GET /rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages)

## 기본 정보

- **기능:** 특정 프로젝트에서 주어진 워크플로우를 사용 중인 이슈 타입 목록을 페이지 단위로 조회
- **Endpoint:** `GET /rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** 문서에 별도 권한 명시 없음(일반 인증만 필요, 프로젝트 관리자 권한으로 접근 가능한 수준으로 추정)

## 설명

워크플로우 ID와 프로젝트 ID를 지정하면 해당 프로젝트에서 그 워크플로우가 적용된 이슈 타입들을 반환한다. 프로젝트-워크플로우-이슈타입 매핑을 파악해 대시보드에서 "이 프로젝트의 이슈 타입별 상태 흐름이 무엇인지" 보여줄 때 유용하다. 결과는 커서 기반(nextPageToken) 페이지네이션을 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `workflowId` | string | Y | 워크플로우 ID | `fb759d53-a3a4-45ff-9de4-547c4b638dde` |
| `projectId` | integer | Y | 프로젝트 ID | `6e2bde9f-f213-4920-95cd-28e015af59a1` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `nextPageToken` | string | N | 없음 | 페이지네이션 커서 | `eyJvIjoyfQ==` |
| `maxResults` | integer | N | 없음 | 반환할 최대 결과 수 (1~200 사이 정수) | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `issueTypes.values` | array | 워크플로우를 사용하는 이슈 타입 ID 목록 | `[{"id":"1000"}]` |
| `issueTypes.nextPageToken` | string | 다음 페이지 커서 | `eyJvIjoyfQ==` |
| `projectId` | string | 프로젝트 ID | `6e2bde9f-f213-4920-95cd-28e015af59a1` |
| `workflowId` | string | 워크플로우 ID | `fb759d53-a3a4-45ff-9de4-547c4b638dde` |

```json
{
  "issueTypes": {
    "nextPageToken": "eyJvIjoyfQ==",
    "values": [{"id": "1000"}]
  },
  "projectId": "6e2bde9f-f213-4920-95cd-28e015af59a1",
  "workflowId": "fb759d53-a3a4-45ff-9de4-547c4b638dde"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `nextPageToken` 형식이 잘못됨 | 커서 값을 이전 응답에서 그대로 전달했는지 확인 |
| 401 | - | 인증 정보 누락/오류, 또는 권한 부족 | 토큰 재발급 또는 권한 확인 |
| 404 | - | 지정한 `workflowId`의 워크플로우가 존재하지 않음 | 워크플로우 ID 재확인 |

```json
{"errorMessages": ["Invalid format of nextPageToken"], "errors": {}}
```

## 주의 사항

- `maxResults`는 1~200 범위로 제한된다.

---

### [높음] 2. 워크플로우를 사용하는 프로젝트 조회 (GET /rest/api/3/workflow/{workflowId}/projectUsages)

## 기본 정보

- **기능:** 주어진 워크플로우를 사용 중인 프로젝트 목록을 페이지 단위로 조회
- **Endpoint:** `GET /rest/api/3/workflow/{workflowId}/projectUsages`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** 문서에 별도 권한 명시 없음

## 설명

특정 워크플로우 ID를 기준으로 어떤 프로젝트들이 이 워크플로우를 사용하고 있는지 조회한다. 팀/프로젝트 생성 자동화나 통합 대시보드에서 워크플로우와 프로젝트 간 매핑 정보를 파악할 때 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `workflowId` | string | Y | 워크플로우 ID | `fb759d53-a3a4-45ff-9de4-547c4b638dde` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `nextPageToken` | string | N | 없음 | 페이지네이션 커서 | `eyJvIjoyfQ==` |
| `maxResults` | integer | N | 없음 | 반환할 최대 결과 수 (1~200 사이 정수) | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `projects.values` | array | 워크플로우를 사용하는 프로젝트 ID 목록 | `[{"id":"1003"}]` |
| `projects.nextPageToken` | string | 다음 페이지 커서 | `eyJvIjoyfQ==` |
| `workflowId` | string | 워크플로우 ID | `fb759d53-a3a4-45ff-9de4-547c4b638dde` |

```json
{
  "projects": {
    "nextPageToken": "eyJvIjoyfQ==",
    "values": [{"id": "1003"}]
  },
  "workflowId": "fb759d53-a3a4-45ff-9de4-547c4b638dde"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `nextPageToken` 형식이 잘못됨 | 커서 값 확인 |
| 401 | - | 인증 정보 누락/오류, 또는 권한 부족 | 토큰/권한 확인 |
| 404 | - | 지정한 `workflowId`의 워크플로우가 존재하지 않음 | 워크플로우 ID 재확인 |

```json
{"errorMessages": ["Invalid format of nextPageToken"], "errors": {}}
```

## 주의 사항

- `maxResults`는 1~200 범위로 제한된다.

---

### [높음] 3. 워크플로우를 사용하는 워크플로우 스킴 조회 (GET /rest/api/3/workflow/{workflowId}/workflowSchemes)

## 기본 정보

- **기능:** 주어진 워크플로우를 사용 중인 워크플로우 스킴 목록을 페이지 단위로 조회
- **Endpoint:** `GET /rest/api/3/workflow/{workflowId}/workflowSchemes`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** 문서에 별도 권한 명시 없음

## 설명

워크플로우 ID를 기준으로 해당 워크플로우를 참조하는 워크플로우 스킴들을 조회한다. 프로젝트 운영 지원 시 특정 워크플로우 변경이 어느 스킴/프로젝트에 영향을 미치는지 파악하는 데 사용할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `workflowId` | string | Y | 워크플로우 ID | `fb759d53-a3a4-45ff-9de4-547c4b638dde` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `nextPageToken` | string | N | 없음 | 페이지네이션 커서 | `eyJvIjoyfQ==` |
| `maxResults` | integer | N | 없음 | 반환할 최대 결과 수 (1~200 사이 정수) | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `workflowSchemes.values` | array | 워크플로우를 사용하는 워크플로우 스킴 ID 목록 | `[{"id":"1000"}]` |
| `workflowSchemes.nextPageToken` | string | 다음 페이지 커서 | `eyJvIjoyfQ==` |
| `workflowId` | string | 워크플로우 ID | `fb759d53-a3a4-45ff-9de4-547c4b638dde` |

```json
{
  "workflowId": "fb759d53-a3a4-45ff-9de4-547c4b638dde",
  "workflowSchemes": {
    "nextPageToken": "eyJvIjoyfQ==",
    "values": [{"id": "1000"}]
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `nextPageToken` 형식이 잘못됨 | 커서 값 확인 |
| 401 | - | 인증 정보 누락/오류, 또는 권한 부족 | 토큰/권한 확인 |
| 404 | - | 지정한 `workflowId`의 워크플로우가 존재하지 않음 | 워크플로우 ID 재확인 |

```json
{"errorMessages": ["Invalid format of nextPageToken"], "errors": {}}
```

## 주의 사항

- `maxResults`는 1~200 범위로 제한된다.

---

### [높음] 4. 워크플로우 일괄 조회 (POST /rest/api/3/workflows)

## 기본 정보

- **기능:** 워크플로우 이름, 워크플로우 ID, 또는 프로젝트+이슈타입 조합으로 워크플로우와 관련 상태(status) 목록을 일괄 조회
- **Endpoint:** `POST /rest/api/3/workflows`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** `Administer Jira` 전역 권한(모든 워크플로우 접근) 또는, 프로젝트 범위 워크플로우 접근 시 `Administer projects`/`View (read-only) workflow` 프로젝트 권한 중 하나

## 설명

여러 워크플로우를 한 번에 조회할 수 있는 API로, 워크플로우 이름 배열, 워크플로우 ID 배열, 또는 프로젝트-이슈타입 쌍의 배열 중 원하는 기준으로 질의한다. 통합 대시보드에서 여러 프로젝트의 워크플로우 상태/전이 구조를 한번에 가져올 때 유용하다. 프로젝트 범위 워크플로우는 프로젝트 관리자(또는 읽기 전용 워크플로우 조회) 권한만으로도 접근 가능하다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `projectAndIssueTypes` | array | N | - | 조회할 프로젝트-이슈타입 조합 리스트 | `[{"projectId":"10000","issueTypeId":"10001"}]` |
| `workflowIds` | array\<string\> | N | - | 조회할 워크플로우 ID 리스트 | `["b9ff2384-d3b6-4d4e-9509-3ee19f607168"]` |
| `workflowNames` | array\<string\> | N | - | 조회할 워크플로우 이름 리스트 | `["Workflow 1"]` |

```json
{
  "workflowNames": ["Workflow 1"]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `statuses` | array | 워크플로우에 포함된 상태 목록 | `[{"id":"10003","name":"Done","statusCategory":"DONE"}]` |
| `workflows` | array | 조회된 워크플로우 상세(상태, 전이 포함) | 아래 예시 참고 |

```json
{
  "statuses": [
    {"description": "", "id": "10003", "name": "Done", "scope": {"type": "GLOBAL"}, "statusCategory": "DONE", "statusReference": "10003"},
    {"description": "", "id": "10001", "name": "To Do", "scope": {"type": "GLOBAL"}, "statusCategory": "TODO", "statusReference": "10001"}
  ],
  "workflows": [
    {
      "description": "",
      "id": "b9ff2384-d3b6-4d4e-9509-3ee19f607168",
      "isEditable": true,
      "name": "Workflow 1",
      "scope": {"type": "GLOBAL"},
      "statuses": [{"deprecated": false, "statusReference": "10001"}],
      "transitions": [{"id": "1", "name": "Create", "toStatusReference": "10001", "type": "INITIAL"}],
      "version": {"id": "f010ac1b-3dd3-43a3-aa66-0ee8a447f76e", "versionNumber": 0}
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청 본문이 유효하지 않음 | 조회 기준(이름/ID/프로젝트-이슈타입) 중 하나 이상 올바르게 지정했는지 확인 |
| 401 | - | 인증 정보 누락/오류 또는 권한 부족 | 프로젝트 관리자 권한 이상 확인 |

## 주의 사항

- 세 가지 조회 기준(`projectAndIssueTypes`, `workflowIds`, `workflowNames`) 중 최소 하나를 지정해야 의미 있는 결과가 반환된다.

---

### [높음] 5. 워크플로우 미리보기 (POST /rest/api/3/workflows/preview)

## 기본 정보

- **기능:** 특정 프로젝트 내 워크플로우를 읽기 전용으로 미리보기(전체 설정은 생략된 요약 구조) 조회
- **Endpoint:** `POST /rest/api/3/workflows/preview`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** `Administer projects` 또는 `View (read-only) workflow` 프로젝트 권한 중 하나

## 설명

프로젝트 ID와 함께 워크플로우 이름/ID/이슈타입 ID 중 하나 이상을 지정하면 해당 워크플로우의 상태·전이 구조를 읽기 전용으로 반환한다. 사이트 전체 관리자 권한이 필요 없고 프로젝트 관리자 또는 읽기 전용 권한만으로 호출 가능해 SSAFY 교육생 계정 환경에 적합하며, 대시보드에서 프로젝트의 이슈 상태 흐름을 시각화할 때 사용하기 좋다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `projectId` | string | Y | - | 권한 확인에 사용되는 프로젝트 ID. `workflowNames`/`workflowIds`/`issueTypeIds` 중 최소 하나를 함께 지정해야 함 | `10000` |
| `issueTypeIds` | array\<string\> | N | 최대 25개 | 조회할 이슈 타입 ID 목록 | `["10001","10002"]` |
| `workflowIds` | array\<string\> | N | 최대 25개 | 조회할 워크플로우 ID 목록 | `["b9ff2384-d3b6-4d4e-9509-3ee19f607168"]` |
| `workflowNames` | array\<string\> | N | 최대 25개 | 조회할 워크플로우 이름 목록 | `["Sample Workflow"]` |

```json
{
  "projectId": "10000",
  "issueTypeIds": ["10001", "10002"]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `statuses` | array | 워크플로우 내 상태 목록 (rawName 포함) | `[{"id":"1","name":"Zrobic","rawName":"To Do","statusCategory":"TODO"}]` |
| `workflows` | array | 미리보기 워크플로우 목록(전이 포함, 세부 규칙 생략) | 아래 예시 참고 |

```json
{
  "statuses": [
    {"description": "The initial status for tasks", "id": "1", "name": "Zrobic", "rawName": "To Do", "scope": {"type": "GLOBAL"}, "statusCategory": "TODO", "statusReference": "1"}
  ],
  "workflows": [
    {
      "description": "A sample workflow for demonstration purposes",
      "id": "b9ff2384-d3b6-4d4e-9509-3ee19f607168",
      "name": "Sample Workflow",
      "queryContext": [{"issueTypes": ["10001", "10002"], "project": "10000"}],
      "scope": {"type": "GLOBAL"},
      "statuses": [{"deprecated": false, "statusReference": "1"}],
      "transitions": [{"id": "1", "name": "Create", "toStatusReference": "1", "type": "INITIAL"}],
      "version": {"id": "f010ac1b-3dd3-43a3-aa66-0ee8a447f76e", "versionNumber": 1}
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 (조회 기준 누락 등) | `workflowNames`/`workflowIds`/`issueTypeIds` 중 하나 이상 지정 |
| 401 | - | 인증 정보 누락/오류 또는 권한 부족 | 프로젝트 권한 확인 |
| 404 | - | 하나 이상의 미리보기 대상을 찾을 수 없음 | ID/이름 값 재확인 |

## 주의 사항

- 지정한 워크플로우는 반드시 `projectId`로 지정한 프로젝트와 연관되어 있어야 한다.
- `issueTypeIds`, `workflowIds`, `workflowNames`는 각각 최대 25개까지만 지정 가능하다.
- 전체 설정이 아닌 읽기 전용 요약 정보만 반환되므로, 상세 규칙(조건/검증자/후처리)이 필요하면 다른 API(예: 워크플로우 일괄 조회)를 사용해야 한다.

---

### [높음] 6. 워크플로우 검색 (GET /rest/api/3/workflows/search)

## 기본 정보

- **기능:** 전역 및 프로젝트 워크플로우를 페이지네이션하여 검색/목록 조회
- **Endpoint:** `GET /rest/api/3/workflows/search`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** `Administer Jira` 전역 권한(전체 워크플로우 접근) 또는, 프로젝트 범위 워크플로우 접근 시 `Administer projects`/`View (read-only) workflow` 프로젝트 권한 중 하나

## 설명

워크플로우 이름으로 부분 일치 검색을 하거나, 이름을 지정하지 않으면 전체 워크플로우를 페이지 단위로 조회한다. 기존 `Get workflows paginated`(03번, deprecated) API를 대체하는 최신 API이며, `projectId`로 필터링도 가능해 특정 프로젝트가 쓰는 워크플로우를 찾는 데 사용할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `startAt` | integer | N | 없음 | 페이지 오프셋(첫 항목 인덱스) | `0` |
| `maxResults` | integer | N | 없음 | 페이지당 최대 항목 수 | `50` |
| `expand` | string | N | 없음 | `values.transitions` 등 추가 정보 포함 옵션 (콤마 구분) | `values.transitions` |
| `queryString` | string | N | 없음 | 워크플로우 이름 대소문자 무시 부분 일치 검색어 | `SCRUM` |
| `orderBy` | string | N | 없음 | 정렬 기준: `name`, `created`, `updated` | `updated` |
| `scope` | string | N | 없음 | 워크플로우 범위: 전역(Global)/프로젝트(Project) | `PROJECT` |
| `isActive` | boolean | N | 없음 | 활성/비활성 워크플로우 필터 | `true` |
| `projectId` | integer | N | 없음 | 특정 프로젝트가 사용하는 워크플로우만 필터링 | `10000` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `false` |
| `maxResults` | integer | 페이지당 최대 항목 수 | `50` |
| `startAt` | integer | 현재 페이지 오프셋 | `0` |
| `total` | integer | 전체 결과 수 | `100` |
| `statuses` | array | 워크플로우들에 포함된 상태 목록 | `[{"id":"10001","name":"To Do"}]` |
| `values` | array | 워크플로우 목록 | 아래 예시 참고 |

```json
{
  "isLast": false,
  "maxResults": 50,
  "nextPage": "https://your-domain.atlassian.net/rest/api/3/workflows/search?startAt=50",
  "self": "https://your-domain.atlassian.net/rest/api/3/workflows/search",
  "startAt": 0,
  "total": 100,
  "statuses": [
    {"description": "", "id": "10003", "name": "Done", "scope": {"type": "GLOBAL"}, "statusCategory": "DONE", "statusReference": "10003"}
  ],
  "values": [
    {
      "description": "",
      "id": "b9ff2384-d3b6-4d4e-9509-3ee19f607168",
      "isEditable": true,
      "name": "Workflow 1",
      "scope": {"type": "GLOBAL"},
      "statuses": [{"deprecated": false, "statusReference": "10002"}],
      "transitions": [{"id": "1", "name": "Create", "toStatusReference": "10001", "type": "INITIAL"}],
      "version": {"id": "f010ac1b-3dd3-43a3-aa66-0ee8a447f76e", "versionNumber": 0}
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 쿼리 파라미터 값 확인 |
| 401 | - | 인증 정보 누락/오류 또는 권한 부족 | 프로젝트 관리자 이상 권한 확인 |

## 주의 사항

- 프로젝트 범위 워크플로우만 조회할 경우 사이트 전체 관리자 권한 없이 `Administer projects`/`View (read-only) workflow` 프로젝트 권한만으로 접근 가능하다.
- 기존 03번(`Get workflows paginated`, 구버전, deprecated) API를 대체한다.
