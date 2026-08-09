# __65-project-components API 요약

이 리소스 그룹은 Jira 프로젝트 컴포넌트(Project Components)를 조회·생성·수정·삭제하고, 프로젝트별 컴포넌트 목록과 컴포넌트별 이슈 개수를 조회하는 API 모음이다. 제외된 API는 없다 (전 엔드포인트가 프로젝트 관리자 수준 또는 그 이하 권한으로 호출 가능).

## 제외된 API

없음

---

### [높음] 1. Create component (POST /rest/api/3/component)

## 기본 정보

- **기능:** 프로젝트 내 이슈를 담는 컨테이너인 컴포넌트를 새로 생성
- **Endpoint:** `POST /rest/api/3/component`
- **인증:** Bearer Token 필요 (익명 접근도 허용되나 실제로는 인증 필요)
- **권한:** 컴포넌트가 생성될 프로젝트에 대한 *Administer projects* 프로젝트 권한 또는 *Administer Jira* 전역 권한

## 설명

팀 생성 자동화 시 프로젝트 구조(컴포넌트 단위)를 코드로 세팅할 때 핵심적으로 쓰인다. `project`(프로젝트 키)와 `name`은 필수이며, `assigneeType`으로 컴포넌트 생성 시 이슈의 기본 담당자 결정 방식을 지정할 수 있다. 프로젝트 관리자 권한으로 호출 가능하다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | Y | 최대 255자, 프로젝트 내 유일 | 컴포넌트 이름 | `"Component 1"` |
| `project` | string | Y | 생성 후 변경 불가 | 컴포넌트가 속할 프로젝트 키 | `"HSP"` |
| `description` | string | N | - | 컴포넌트 설명 | `"This is a Jira component"` |
| `assigneeType` | enum | N | `PROJECT_DEFAULT`\|`COMPONENT_LEAD`\|`PROJECT_LEAD`\|`UNASSIGNED`, 기본값 `PROJECT_DEFAULT` | 컴포넌트로 생성된 이슈의 명목상 담당자 결정 방식 | `"PROJECT_LEAD"` |
| `leadAccountId` | string | N | - | 컴포넌트 리드 사용자의 accountId | `"5b10ac8d82e05b22cc7d4ef5"` |
| `projectId` | integer | N | - | 프로젝트 ID | `10000` |

```json
{
  "name": "Component 1",
  "description": "This is a Jira component",
  "project": "HSP",
  "assigneeType": "PROJECT_LEAD",
  "leadAccountId": "5b10a2844c20165700ede21g"
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 생성된 컴포넌트의 고유 ID | `"10000"` |
| `name` | string | 컴포넌트 이름 | `"Component 1"` |
| `description` | string | 컴포넌트 설명 | `"This is a Jira component"` |
| `project` | string | 프로젝트 키 | `"HSP"` |
| `projectId` | integer | 프로젝트 ID | `10000` |
| `assigneeType` | enum | 담당자 결정 방식 | `"PROJECT_LEAD"` |
| `isAssigneeTypeValid` | boolean | assigneeType에 해당하는 사용자가 실제로 존재하는지 | `false` |
| `self` | string | 컴포넌트 API URL | `"https://your-domain.atlassian.net/rest/api/3/component/10000"` |

```json
{
  "id": "10000",
  "name": "Component 1",
  "description": "This is a Jira component",
  "project": "HSP",
  "projectId": 10000,
  "assigneeType": "PROJECT_LEAD",
  "isAssigneeTypeValid": false,
  "self": "https://your-domain.atlassian.net/rest/api/3/component/10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | Bad Request | 사용자를 찾을 수 없음 / `name` 미제공 / `name`이 255자 초과 / `projectId` 미제공 / `assigneeType` 값이 잘못됨 | 요청 바디 필수값과 형식 검증 |
| 401 | Unauthorized | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 403 | Forbidden | 프로젝트 관리 권한 또는 Jira 관리 권한 없음 | 계정 권한 확인 |
| 404 | Not Found | 프로젝트를 찾을 수 없거나 프로젝트를 볼 권한이 없음 | 프로젝트 키/ID 및 Browse 권한 확인 |

```json
{
  "errorMessages": [],
  "errors": {
    "name": "Component name is required"
  }
}
```

## 주의 사항

- `project` 필드는 생성 후 변경할 수 없다.
- `ari`, `metadata`는 Compass 컴포넌트 전용 필드로 일반 프로젝트 컴포넌트 생성 시에는 불필요하다.

---

### [높음] 2. Update component (PUT /rest/api/3/component/{id})

## 기본 정보

- **기능:** 기존 컴포넌트의 필드를 수정
- **Endpoint:** `PUT /rest/api/3/component/{id}`
- **인증:** Bearer Token 필요
- **권한:** 컴포넌트가 속한 프로젝트에 대한 *Administer projects* 프로젝트 권한 또는 *Administer Jira* 전역 권한

## 설명

요청에 포함된 필드는 모두 덮어써진다. `leadAccountId`를 빈 문자열("")로 보내면 컴포넌트 리드가 제거된다. 프로젝트 운영 지원(컴포넌트 재구성, 리드 변경 등) 흐름에 직접 사용된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Y | 컴포넌트 ID | `"10000"` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | N | 최대 255자 | 컴포넌트 이름 | `"Component 1"` |
| `description` | string | N | - | 컴포넌트 설명 | `"This is a Jira component"` |
| `assigneeType` | enum | N | `PROJECT_DEFAULT`\|`COMPONENT_LEAD`\|`PROJECT_LEAD`\|`UNASSIGNED` | 담당자 결정 방식 | `"PROJECT_LEAD"` |
| `leadAccountId` | string | N | 빈 문자열이면 리드 제거 | 컴포넌트 리드 accountId | `"5b10ac8d82e05b22cc7d4ef5"` |

```json
{
  "name": "Component 1",
  "description": "This is a Jira component",
  "assigneeType": "PROJECT_LEAD",
  "leadAccountId": "5b10a2844c20165700ede21g"
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 컴포넌트 ID | `"10000"` |
| `name` | string | 컴포넌트 이름 | `"Component 1"` |
| `description` | string | 컴포넌트 설명 | `"This is a Jira component"` |
| `assigneeType` | enum | 담당자 결정 방식 | `"PROJECT_LEAD"` |
| `self` | string | 컴포넌트 API URL | `"https://your-domain.atlassian.net/rest/api/3/component/10000"` |

```json
{
  "id": "10000",
  "name": "Component 1",
  "description": "This is a Jira component",
  "assigneeType": "PROJECT_LEAD",
  "self": "https://your-domain.atlassian.net/rest/api/3/component/10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | Bad Request | 사용자를 찾을 수 없음 / `assigneeType` 값이 잘못됨 / `name`이 255자 초과 | 요청 바디 검증 |
| 401 | Unauthorized | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 403 | Forbidden | 프로젝트 관리 권한 또는 Jira 관리 권한 없음 | 계정 권한 확인 |
| 404 | Not Found | 컴포넌트를 찾을 수 없거나 프로젝트를 볼 권한이 없음 | 컴포넌트 ID 및 권한 확인 |

```json
{
  "errorMessages": [],
  "errors": {
    "assigneeType": "Invalid assignee type"
  }
}
```

## 주의 사항

- 요청에 포함되지 않은 필드는 유지되지만, 포함된 필드는 전부 덮어쓴다 (부분 병합이 아님).
- `ari`, `project`는 이 API로 변경할 수 없다.

---

### [높음] 3. Get project components paginated (GET /rest/api/3/project/{projectIdOrKey}/component)

## 기본 정보

- **기능:** 프로젝트의 모든 컴포넌트를 페이지 단위로 조회
- **Endpoint:** `GET /rest/api/3/project/{projectIdOrKey}/component`
- **인증:** Bearer Token 필요 (익명 접근 허용되나 일반적으로 인증 사용)
- **권한:** 해당 프로젝트에 대한 *Browse Projects* 프로젝트 권한

## 설명

통합 대시보드에서 프로젝트별 컴포넌트 목록(이슈 개수 포함)을 페이지네이션으로 가져올 때 사용한다. Compass 컴포넌트를 사용하는 프로젝트의 경우 연동된 Compass 컴포넌트 목록도 반환할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Y | 프로젝트 ID 또는 키(대소문자 구분) | `"PR"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `startAt` | integer | N | - | 페이지 시작 오프셋 | `0` |
| `maxResults` | integer | N | - | 페이지당 최대 항목 수 | `2` |
| `orderBy` | string | N | - | 정렬 기준: `description`, `issueCount`, `lead`, `name` | `"name"` |
| `componentSource` | string | N | `jira` | 컴포넌트 출처: `jira`, `compass`, `auto` | `"jira"` |
| `query` | string | N | - | 이름/설명에 대한 대소문자 무시 필터 문자열 | `"backend"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `false` |
| `maxResults` | integer | 페이지당 최대 항목 수 | `2` |
| `startAt` | integer | 시작 오프셋 | `0` |
| `total` | integer | 전체 항목 수 | `7` |
| `nextPage` | string | 다음 페이지 URL | `"https://your-domain.atlassian.net/rest/api/3/project/PR/component?startAt=2&maxResults=2"` |
| `values[].id` | string | 컴포넌트 ID | `"10000"` |
| `values[].name` | string | 컴포넌트 이름 | `"Component 1"` |
| `values[].issueCount` | integer | 컴포넌트에 연결된 이슈 수 | `1` |

```json
{
  "isLast": false,
  "maxResults": 2,
  "startAt": 0,
  "total": 7,
  "nextPage": "https://your-domain.atlassian.net/rest/api/3/project/PR/component?startAt=2&maxResults=2",
  "values": [
    {
      "id": "10000",
      "name": "Component 1",
      "description": "This is a Jira component",
      "issueCount": 1,
      "project": "HSP",
      "projectId": 10000
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | Unauthorized | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 404 | Not Found | 프로젝트를 찾을 수 없거나 볼 권한 없음 | 프로젝트 키/ID 및 Browse 권한 확인 |

```json
{
  "errorMessages": ["The project is not found."],
  "errors": {}
}
```

## 주의 사항

- 페이지네이션이 필요 없는 경우 08(Get project components)을 사용할 수 있다.
- `componentSource=auto`인 경우 프로젝트가 Compass에 연동되어 있으면 Compass 컴포넌트를, 아니면 Jira 컴포넌트를 반환한다.

---

### [높음] 4. Get project components (GET /rest/api/3/project/{projectIdOrKey}/components)

## 기본 정보

- **기능:** 프로젝트의 모든 컴포넌트를 페이지네이션 없이 전체 조회
- **Endpoint:** `GET /rest/api/3/project/{projectIdOrKey}/components`
- **인증:** Bearer Token 필요 (익명 접근 허용되나 일반적으로 인증 사용)
- **권한:** 해당 프로젝트에 대한 *Browse Projects* 프로젝트 권한

## 설명

대시보드나 자동화 스크립트에서 프로젝트의 전체 컴포넌트 목록을 한 번에 가져와야 할 때 간단히 사용할 수 있는 API다. Compass 컴포넌트를 사용하는 프로젝트에서는 페이지네이션된 Compass 컴포넌트 목록을 반환한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Y | 프로젝트 ID 또는 키(대소문자 구분) | `"PR"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `componentSource` | string | N | `jira` | 컴포넌트 출처: `jira`, `compass`, `auto` | `"jira"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| (배열) `id` | string | 컴포넌트 ID | `"10000"` |
| (배열) `name` | string | 컴포넌트 이름 | `"Component 1"` |
| (배열) `description` | string | 컴포넌트 설명 | `"This is a Jira component"` |
| (배열) `project` | string | 프로젝트 키 | `"HSP"` |

```json
[
  {
    "id": "10000",
    "name": "Component 1",
    "description": "This is a Jira component",
    "project": "HSP",
    "projectId": 10000,
    "self": "https://your-domain.atlassian.net/rest/api/3/component/10000"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | Unauthorized | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 404 | Not Found | 프로젝트를 찾을 수 없거나 볼 권한 없음 | 프로젝트 키/ID 및 Browse 권한 확인 |

```json
{
  "errorMessages": ["The project is not found."],
  "errors": {}
}
```

## 주의 사항

- 컴포넌트 수가 매우 많은 프로젝트에서는 07(paginated 버전)을 우선 고려한다.

---

### [중간] 5. Find components for projects (GET /rest/api/3/component)

## 기본 정보

- **기능:** 여러 프로젝트를 대상으로 컴포넌트를 검색/조회 (Compass 전역 컴포넌트 포함 가능)
- **Endpoint:** `GET /rest/api/3/component`
- **인증:** Bearer Token 필요 (익명 접근 허용되나 일반적으로 인증 사용)
- **권한:** 해당 프로젝트에 대한 *Browse Projects* 프로젝트 권한

## 설명

특정 프로젝트에 한정하지 않고 여러 프로젝트의 컴포넌트를 이름/설명 기준으로 검색할 때 사용하는 보조 조회 API다. 프로젝트별 컴포넌트 목록 조회(07, 08)와 달리 여러 프로젝트를 한 번에 다룰 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `projectIdsOrKeys` | array | N | - | 조회할 프로젝트 ID/키 목록(대소문자 구분) | `["PR","HSP"]` |
| `startAt` | integer | N | - | 페이지 시작 오프셋 | `0` |
| `maxResults` | integer | N | - | 페이지당 최대 항목 수 | `2` |
| `orderBy` | string | N | - | 정렬 기준: `description`, `name` | `"name"` |
| `query` | string | N | - | 이름/설명에 대한 대소문자 무시 필터 문자열 | `"backend"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `false` |
| `maxResults` | integer | 페이지당 최대 항목 수 | `2` |
| `startAt` | integer | 시작 오프셋 | `0` |
| `total` | integer | 전체 항목 수 | `2` |
| `values[].id` | string | 컴포넌트 ID | `"10000"` |
| `values[].name` | string | 컴포넌트 이름 | `"Component1"` |
| `values[].ari` | string | Compass 전역 컴포넌트의 ARI(전역 컴포넌트만) | `"ari:cloud:graph::integration-context/.../component/10001"` |

```json
{
  "isLast": false,
  "maxResults": 2,
  "startAt": 0,
  "total": 2,
  "values": [
    {
      "description": "This is a component",
      "id": "10000",
      "name": "Component1",
      "self": "http://www.example.com/jira/rest/api/2/component/10000"
    },
    {
      "ari": "ari:cloud:graph::integration-context/ecda99d9-9b42-4bf7-8b4f-ecb5fcf5868c/component/10001",
      "description": "This is a global component",
      "id": "10001",
      "metadata": { "key1": "value1", "key2": "value2" },
      "name": "Component2",
      "self": "http://www.example.com/jira/rest/api/2/component/10001"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | Unauthorized | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 404 | Not Found | 프로젝트를 찾을 수 없거나 볼 권한 없음 | 프로젝트 키/ID 및 Browse 권한 확인 |

```json
{
  "errorMessages": ["The project is not found."],
  "errors": {}
}
```

## 주의 사항

- Compass 전역 컴포넌트가 포함될 경우 `ari`, `metadata` 필드가 추가로 반환된다.

---

### [중간] 6. Get component (GET /rest/api/3/component/{id})

## 기본 정보

- **기능:** 단일 컴포넌트의 상세 정보 조회
- **Endpoint:** `GET /rest/api/3/component/{id}`
- **인증:** Bearer Token 필요 (익명 접근 허용되나 일반적으로 인증 사용)
- **권한:** 컴포넌트가 속한 프로젝트에 대한 *Browse projects* 프로젝트 권한

## 설명

컴포넌트 ID로 단건 상세 정보(리드, 담당자 타입, 설명 등)를 조회한다. 대시보드에서 특정 컴포넌트를 드릴다운해서 보여줄 때 사용할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Y | 컴포넌트 ID | `"10000"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 컴포넌트 ID | `"10000"` |
| `name` | string | 컴포넌트 이름 | `"Component 1"` |
| `description` | string | 컴포넌트 설명 | `"This is a Jira component"` |
| `assigneeType` | enum | 담당자 결정 방식 | `"PROJECT_LEAD"` |
| `lead` | object | 컴포넌트 리드 사용자 정보 | `{"accountId": "5b10a2844c20165700ede21g", "displayName": "Mia Krystof"}` |
| `project` | string | 프로젝트 키 | `"HSP"` |
| `self` | string | 컴포넌트 API URL | `"https://your-domain.atlassian.net/rest/api/3/component/10000"` |

```json
{
  "id": "10000",
  "name": "Component 1",
  "description": "This is a Jira component",
  "assigneeType": "PROJECT_LEAD",
  "isAssigneeTypeValid": false,
  "lead": {
    "accountId": "5b10a2844c20165700ede21g",
    "displayName": "Mia Krystof"
  },
  "project": "HSP",
  "projectId": 10000,
  "self": "https://your-domain.atlassian.net/rest/api/3/component/10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | Unauthorized | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 404 | Not Found | 컴포넌트를 찾을 수 없거나 프로젝트를 볼 권한이 없음 | 컴포넌트 ID 및 권한 확인 |

```json
{
  "errorMessages": ["The component was not found."],
  "errors": {}
}
```

## 주의 사항

- 없음

---

### [중간] 7. Delete component (DELETE /rest/api/3/component/{id})

## 기본 정보

- **기능:** 컴포넌트를 삭제
- **Endpoint:** `DELETE /rest/api/3/component/{id}`
- **인증:** Bearer Token 필요
- **권한:** 컴포넌트가 속한 프로젝트에 대한 *Administer projects* 프로젝트 권한 또는 *Administer Jira* 전역 권한

## 설명

컴포넌트를 삭제한다. `moveIssuesTo` 쿼리 파라미터로 대체 컴포넌트를 지정하면 삭제되는 컴포넌트에 연결된 이슈들이 해당 컴포넌트로 이동한다. 프로젝트 구조 정리 등 부가적인 운영 작업에 쓰인다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Y | 삭제할 컴포넌트의 ID | `"10000"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `moveIssuesTo` | string | N | null(대체 없음) | 삭제된 컴포넌트를 대체할 컴포넌트 ID | `"10010"` |

## Response

### `204 No Content`

삭제 성공 시 본문 없이 204를 반환한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | Unauthorized | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 403 | Forbidden | 프로젝트 관리 권한 또는 Jira 관리 권한 없음 | 계정 권한 확인 |
| 404 | Not Found | 컴포넌트를 찾을 수 없음 / 대체 컴포넌트를 찾을 수 없음 / 프로젝트를 볼 권한 없음 | 컴포넌트 ID 및 `moveIssuesTo` 값 확인 |

```json
{
  "errorMessages": ["The component was not found."],
  "errors": {}
}
```

## 주의 사항

- 삭제는 되돌릴 수 없으므로, 이슈가 남아있는 컴포넌트를 삭제할 때는 `moveIssuesTo`로 이슈 이관을 고려해야 한다.

---

### [중간] 8. Get component issues count (GET /rest/api/3/component/{id}/relatedIssueCounts)

## 기본 정보

- **기능:** 특정 컴포넌트에 연결된 이슈 개수 조회
- **Endpoint:** `GET /rest/api/3/component/{id}/relatedIssueCounts`
- **인증:** Bearer Token 필요 (익명 접근 허용)
- **권한:** 없음(단, 결과는 호출자의 이슈 조회 권한 범위 내에서 계산됨)

## 설명

컴포넌트별 이슈 개수를 대시보드 통계용으로 조회할 때 사용한다. 별도의 권한 요구사항이 없어 접근성이 높지만, 2024-06-15부터 OAuth 2.0 스코프가 변경될 예정이라는 지원 종료(Deprecation) 공지가 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Y | 컴포넌트 ID | `"10000"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `issueCount` | integer | 컴포넌트에 연결된 이슈 개수 | `23` |
| `self` | string | 컴포넌트 API URL | `"https://your-domain.atlassian.net/rest/api/3/component/10000"` |

```json
{
  "issueCount": 23,
  "self": "https://your-domain.atlassian.net/rest/api/3/component/10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | Unauthorized | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 404 | Not Found | 컴포넌트를 찾을 수 없음 | 컴포넌트 ID 확인 |

```json
{
  "errorMessages": ["The component was not found."],
  "errors": {}
}
```

## 주의 사항

- 필요 OAuth 2.0 스코프가 변경 예정(Classic: `read:jira-work`, Granular: `read:field:jira`, `read:project.component:jira`)이므로 스코프 설정 시 최신 문서를 확인해야 한다.
