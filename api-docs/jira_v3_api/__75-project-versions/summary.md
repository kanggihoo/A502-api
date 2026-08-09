# __75-project-versions API 요약

이 리소스 그룹은 Jira 프로젝트의 버전(version/fixVersion)을 조회·생성·수정·이동·병합·삭제하고, 버전에 연결된 이슈 개수 및 관련 작업(related work)을 관리하는 API 모음이다. 제외된 API는 없다 (모든 엔드포인트가 프로젝트 단위 권한인 *Browse Projects*, *Administer Projects*, *Resolve/Edit issues* 수준으로 호출 가능하며, 사이트 전체 관리자 권한을 요구하지 않는다).

## 제외된 API

- 없음 (모든 15개 엔드포인트가 프로젝트 관리자 이하 권한으로 호출 가능하여 제외 대상이 아님)

---

### [높음] 1. 프로젝트 버전 목록 조회 (페이지네이션) (GET /rest/api/3/project/{projectIdOrKey}/version)

## 기본 정보

- **기능:** 프로젝트에 속한 모든 버전을 페이지 단위로 조회
- **Endpoint:** `GET /rest/api/3/project/{projectIdOrKey}/version`
- **인증:** Bearer Token 필요 (익명 접근도 가능하나 인스턴스 설정에 따름)
- **권한:** *Browse Projects* 프로젝트 권한

## 설명

프로젝트의 버전 목록을 페이지네이션 방식으로 반환한다. 정렬, 상태(released/unreleased/archived) 필터, 이름/설명 검색, expand 옵션(이슈 상태 카운트, 승인자, 드라이버 등)을 지원한다. 전체 목록을 한 번에 받고 싶다면 02번(Get project versions)을 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Yes | 프로젝트 ID 또는 키(대소문자 구분) | `PR` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `startAt` | integer | No | - | 페이지 시작 오프셋 | `0` |
| `maxResults` | integer | No | - | 페이지당 최대 항목 수 | `2` |
| `orderBy` | string | No | - | 정렬 기준: `description`, `name`, `releaseDate`, `sequence`, `startDate` | `releaseDate` |
| `query` | string | No | - | 이름/설명 부분 일치 검색(대소문자 무시) | `New` |
| `status` | string | No | - | 콤마로 구분된 상태 필터: `released`, `unreleased`, `archived` | `unreleased` |
| `expand` | string | No | - | `issuesstatus`, `operations`, `driver`, `approvers` | `issuesstatus` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `false` |
| `maxResults` | integer | 페이지당 최대 항목 수 | `2` |
| `startAt` | integer | 시작 오프셋 | `0` |
| `total` | integer | 전체 항목 수 | `7` |
| `values` | array | 버전 객체 배열 | - |

```json
{
  "isLast": false,
  "maxResults": 2,
  "nextPage": "https://your-domain.atlassian.net/rest/api/3/project/PR/version?startAt=2&maxResults=2",
  "self": "https://your-domain.atlassian.net/rest/api/3/project/PR/version?startAt=0&maxResults=2",
  "startAt": 0,
  "total": 7,
  "values": [
    {
      "archived": false,
      "description": "An excellent version",
      "id": "10000",
      "name": "New Version 1",
      "overdue": true,
      "projectId": 10000,
      "releaseDate": "2010-07-06",
      "released": true,
      "self": "https://your-domain.atlassian.net/rest/api/3/version/10000",
      "userReleaseDate": "6/Jul/2010"
    },
    {
      "archived": false,
      "description": "Minor Bugfix version",
      "id": "10010",
      "issuesStatusForFixVersion": {"done": 100, "inProgress": 20, "toDo": 10, "unmapped": 0},
      "name": "Next Version",
      "overdue": false,
      "projectId": 10000,
      "released": false,
      "self": "https://your-domain.atlassian.net/rest/api/3/version/10010"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 404 | - | 프로젝트가 없거나 조회 권한이 없음 | 프로젝트 키/ID 및 권한 확인 |

## 주의 사항

- 전체 목록이 필요하면 페이지네이션 없는 02번 API를 사용한다.

---

### [높음] 2. 프로젝트 버전 목록 조회 (전체) (GET /rest/api/3/project/{projectIdOrKey}/versions)

## 기본 정보

- **기능:** 프로젝트에 속한 모든 버전을 페이지네이션 없이 한 번에 조회
- **Endpoint:** `GET /rest/api/3/project/{projectIdOrKey}/versions`
- **인증:** Bearer Token 필요 (익명 접근 가능 설정 시 불필요)
- **권한:** *Browse Projects* 프로젝트 권한

## 설명

프로젝트의 모든 버전을 배열 형태로 한 번에 반환한다. 대시보드에서 프로젝트 버전 전체를 가볍게 조회할 때 유용하다. `expand=operations`로 각 버전에서 수행 가능한 작업 목록을 포함할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Yes | 프로젝트 ID 또는 키(대소문자 구분) | `PR` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | No | - | `operations`만 지원 | `operations` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| (array) | array | 버전 객체 배열 | - |

```json
[
  {
    "archived": false,
    "description": "An excellent version",
    "id": "10000",
    "name": "New Version 1",
    "overdue": true,
    "projectId": 10000,
    "releaseDate": 1278385482288,
    "releaseDateSet": true,
    "released": true,
    "self": "https://your-domain.atlassian.net/rest/api/3/version/10000",
    "startDateSet": false,
    "userReleaseDate": "6/Jul/2010"
  },
  {
    "archived": false,
    "description": "Minor Bugfix version",
    "id": "10010",
    "issuesStatusForFixVersion": {"done": 100, "inProgress": 20, "toDo": 10, "unmapped": 0},
    "name": "Next Version",
    "overdue": false,
    "projectId": 10000,
    "releaseDateSet": false,
    "released": false,
    "self": "https://your-domain.atlassian.net/rest/api/3/version/10010",
    "startDateSet": false
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 404 | - | 프로젝트가 없거나 조회 권한이 없음 | 프로젝트 키/ID 및 권한 확인 |

## 주의 사항

- 버전이 많은 프로젝트에서는 응답이 커질 수 있으므로 필요에 따라 01번(페이지네이션) API 사용을 고려한다.

---

### [높음] 3. 버전 생성 (POST /rest/api/3/version)

## 기본 정보

- **기능:** 프로젝트에 새 버전(릴리즈 버전)을 생성
- **Endpoint:** `POST /rest/api/3/version`
- **인증:** Bearer Token 필요
- **권한:** *Administer Jira* 전역 권한 또는 대상 프로젝트의 *Administer Projects* 프로젝트 권한

## 설명

새 프로젝트 버전을 생성한다. 팀/프로젝트 생성 자동화 시 스프린트나 릴리즈 단위를 버전으로 미리 세팅하는 데 사용할 수 있다. `name`과 `projectId`가 사실상 필수이며, `releaseDate`/`startDate`는 ISO 8601(yyyy-mm-dd) 형식을 사용한다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | Yes(생성 시) | 최대 255자, 프로젝트 내 고유 | 버전 이름 | `"New Version 1"` |
| `projectId` | integer | Yes(생성 시) | - | 버전이 속할 프로젝트 ID | `10000` |
| `description` | string | No | 최대 16,384 bytes | 버전 설명 | `"An excellent version"` |
| `archived` | boolean | No | - | 아카이브 여부 | `false` |
| `released` | boolean | No | - | 릴리즈 여부 | `true` |
| `releaseDate` | string | No | ISO 8601 (yyyy-mm-dd) | 릴리즈 예정일 | `"2010-07-06"` |
| `startDate` | string | No | ISO 8601 (yyyy-mm-dd) | 시작일 | `"2010-07-01"` |
| `driver` | string | No | - | 버전 드라이버의 Atlassian 계정 ID | - |
| `approvers` | array | No | - | 승인자 목록 (`accountId`, `status` 등) | - |
| `expand` | string | No | - | `operations`, `issuesstatus`, `driver`, `approvers` | `"issuesstatus"` |

```json
{
  "name": "New Version 1",
  "projectId": 10000,
  "description": "An excellent version",
  "archived": false,
  "released": true,
  "releaseDate": "2010-07-06"
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 생성된 버전 ID | `"10000"` |
| `name` | string | 버전 이름 | `"New Version 1"` |
| `project` | string | 프로젝트 키(deprecated) | `"PXA"` |
| `projectId` | integer | 프로젝트 ID | `10000` |
| `self` | string | 버전 리소스 URL | `"https://your-domain.atlassian.net/rest/api/3/version/10000"` |

```json
{
  "archived": false,
  "description": "An excellent version",
  "id": "10000",
  "name": "New Version 1",
  "project": "PXA",
  "projectId": 10000,
  "releaseDate": "2010-07-06",
  "released": true,
  "self": "https://your-domain.atlassian.net/rest/api/3/version/10000",
  "userReleaseDate": "6/Jul/2010"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 (예: 이름 중복, 필수값 누락) | 요청 body 검증 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 토큰 확인 |
| 404 | - | 프로젝트가 없거나 필요한 권한이 없음 | 프로젝트 ID 및 권한 확인 |

## 주의 사항

- 버전 생성에는 프로젝트 관리자(Administer Projects) 권한이면 충분하다.

---

### [높음] 4. 버전 조회 (GET /rest/api/3/version/{id})

## 기본 정보

- **기능:** 단일 프로젝트 버전 상세 조회
- **Endpoint:** `GET /rest/api/3/version/{id}`
- **인증:** Bearer Token 필요 (익명 접근 가능 설정 시 불필요)
- **권한:** 버전이 속한 프로젝트의 *Browse projects* 권한

## 설명

버전 ID로 단일 버전의 상세 정보를 조회한다. `expand` 옵션으로 이슈 상태 카운트, 운영 가능한 작업 목록, 드라이버, 승인자 정보를 함께 받을 수 있어 대시보드에서 버전 상세 패널을 구성할 때 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Yes | 버전 ID | `10000` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | No | - | `operations`, `issuesstatus`, `driver`, `approvers` | `issuesstatus` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 버전 ID | `"10000"` |
| `name` | string | 버전 이름 | `"New Version 1"` |
| `released` | boolean | 릴리즈 여부 | `true` |
| `overdue` | boolean | 기한 초과 여부 | `true` |

```json
{
  "archived": false,
  "description": "An excellent version",
  "id": "10000",
  "name": "New Version 1",
  "overdue": true,
  "projectId": 10000,
  "releaseDate": "2010-07-06",
  "released": true,
  "self": "https://your-domain.atlassian.net/rest/api/3/version/10000",
  "userReleaseDate": "6/Jul/2010"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 토큰 확인 |
| 404 | - | 버전이 없거나 조회 권한이 없음 | 버전 ID 및 권한 확인 |

---

### [높음] 5. 버전 수정 (PUT /rest/api/3/version/{id})

## 기본 정보

- **기능:** 기존 프로젝트 버전의 속성 업데이트
- **Endpoint:** `PUT /rest/api/3/version/{id}`
- **인증:** Bearer Token 필요
- **권한:** *Administer Jira* 전역 권한 또는 해당 프로젝트의 *Administer Projects* 프로젝트 권한

## 설명

버전의 이름, 설명, 릴리즈/아카이브 상태, 시작일/릴리즈일 등을 수정한다. 릴리즈 처리 시 `moveUnfixedIssuesTo`로 미해결 이슈를 다른 버전으로 이관할 수 있어 스프린트/릴리즈 마감 자동화에 활용 가능하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Yes | 버전 ID | `10000` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | No | 최대 255자 | 버전 이름 | `"New Version 1"` |
| `description` | string | No | 최대 16,384 bytes | 버전 설명 | `"An excellent version"` |
| `archived` | boolean | No | - | 아카이브 여부 | `false` |
| `released` | boolean | No | - | 릴리즈 여부(이미 릴리즈된 경우 재요청 무시) | `true` |
| `releaseDate` | string | No | ISO 8601 | 릴리즈일 | `"2010-07-06"` |
| `startDate` | string | No | ISO 8601 | 시작일 | `"2010-07-01"` |
| `moveUnfixedIssuesTo` | string | No | 다른 버전의 self URL | 릴리즈 시 미해결 이슈 이관 대상 | - |

```json
{
  "name": "New Version 1",
  "released": true,
  "releaseDate": "2010-07-06"
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 버전 ID | `"10000"` |
| `released` | boolean | 릴리즈 여부 | `true` |

```json
{
  "archived": false,
  "description": "An excellent version",
  "id": "10000",
  "name": "New Version 1",
  "project": "PXA",
  "projectId": 10000,
  "releaseDate": "2010-07-06",
  "released": true,
  "self": "https://your-domain.atlassian.net/rest/api/3/version/10000",
  "userReleaseDate": "6/Jul/2010"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않거나 권한 부족 | 요청 body 및 권한 확인 |
| 401 | - | 인증 정보가 잘못됨 | 토큰 확인 |
| 404 | - | 버전을 찾을 수 없음 | 버전 ID 확인 |

---

### [높음] 6. 버전의 관련 이슈 개수 조회 (GET /rest/api/3/version/{id}/relatedIssueCounts)

## 기본 정보

- **기능:** 특정 버전과 관련된 이슈 개수(fixVersion/affectedVersion/커스텀필드 사용 건수) 조회
- **Endpoint:** `GET /rest/api/3/version/{id}/relatedIssueCounts`
- **인증:** Bearer Token 필요 (익명 접근 가능 설정 시 불필요)
- **권한:** 해당 프로젝트의 *Browse projects* 권한

## 설명

`fixVersion`, `affectedVersion`, 버전 형 커스텀 필드에 해당 버전이 설정된 이슈 개수를 각각 반환한다. 대시보드에서 버전(릴리즈)별 진행 현황 요약 카드를 만들 때 핵심적으로 사용할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Yes | 버전 ID | `10000` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `issuesFixedCount` | integer | fixVersion이 해당 버전인 이슈 수 | `23` |
| `issuesAffectedCount` | integer | affectedVersion이 해당 버전인 이슈 수 | `101` |
| `issueCountWithCustomFieldsShowingVersion` | integer | 커스텀 필드에 해당 버전이 설정된 이슈 수 | `54` |
| `customFieldUsage` | array | 커스텀 필드별 사용 현황 | - |

```json
{
  "customFieldUsage": [
    {"customFieldId": 10000, "fieldName": "Field1", "issueCountWithVersionInCustomField": 2},
    {"customFieldId": 10010, "fieldName": "Field2", "issueCountWithVersionInCustomField": 3}
  ],
  "issueCountWithCustomFieldsShowingVersion": 54,
  "issuesAffectedCount": 101,
  "issuesFixedCount": 23,
  "self": "https://your-domain.atlassian.net/rest/api/3/version/10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 잘못됨 | 토큰 확인 |
| 404 | - | 버전이 없거나 권한 부족 | 버전 ID 및 권한 확인 |

---

### [높음] 7. 버전 삭제 및 대체 (POST /rest/api/3/version/{id}/removeAndSwap)

## 기본 정보

- **기능:** 프로젝트 버전을 삭제하면서 관련 이슈의 fixVersion/affectedVersion/커스텀 필드 값을 다른 버전으로 대체
- **Endpoint:** `POST /rest/api/3/version/{id}/removeAndSwap`
- **인증:** Bearer Token 필요
- **권한:** *Administer Jira* 전역 권한 또는 해당 프로젝트의 *Administer Projects* 프로젝트 권한

## 설명

버전을 삭제하되, 대체 버전을 지정하지 않으면 관련 필드 값이 비워진다. 대체 버전은 반드시 동일 프로젝트 소속이어야 하며 삭제 대상 버전일 수 없다. 기존 06번(Delete version)의 대체 기능을 포함한 상위호환 API로 릴리즈 정리 자동화에 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Yes | 버전 ID | `10000` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `moveFixIssuesTo` | integer | No | 동일 프로젝트, 삭제 대상 아님 | fixVersion 대체 버전 ID | `10001` |
| `moveAffectedIssuesTo` | integer | No | 동일 프로젝트, 삭제 대상 아님 | affectedVersion 대체 버전 ID | `10001` |
| `customFieldReplacementList` | array | No | - | 커스텀 필드별 대체 버전 목록 (`customFieldId`, `moveTo`) | - |

```json
{
  "moveFixIssuesTo": 10001,
  "moveAffectedIssuesTo": 10001,
  "customFieldReplacementList": [
    {"customFieldId": 10000, "moveTo": 10001}
  ]
}
```

## Response

### `204 No Content`

버전이 삭제되면 본문 없이 204를 반환한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | body 값(동일 프로젝트 여부 등) 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 토큰 확인 |
| 404 | - | 삭제할 버전이 없거나 권한 부족 | 버전 ID 및 권한 확인 |

## 주의 사항

- 06번(Delete version)은 deprecated이며 이 API 사용이 권장된다.

---

### [높음] 8. 버전의 미해결 이슈 개수 조회 (GET /rest/api/3/version/{id}/unresolvedIssueCount)

## 기본 정보

- **기능:** 특정 버전에 연결된 전체 이슈 수와 미해결 이슈 수 조회
- **Endpoint:** `GET /rest/api/3/version/{id}/unresolvedIssueCount`
- **인증:** Bearer Token 필요 (익명 접근 가능 설정 시 불필요)
- **권한:** 해당 프로젝트의 *Browse projects* 권한

## 설명

릴리즈 진행률(전체 이슈 대비 미해결 이슈 비율)을 계산하는 데 바로 사용할 수 있는 카운트 API다. 대시보드의 릴리즈 진행 상황 위젯에 핵심적으로 쓰인다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Yes | 버전 ID | `10000` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `issuesCount` | integer | 버전에 연결된 전체 이슈 수 | `30` |
| `issuesUnresolvedCount` | integer | 미해결 이슈 수 | `23` |

```json
{
  "issuesCount": 30,
  "issuesUnresolvedCount": 23,
  "self": "https://your-domain.atlassian.net/rest/api/3/version/10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 토큰 확인 |
| 404 | - | 버전이 없거나 권한 부족 | 버전 ID 및 권한 확인 |

---

### [중간] 9. 버전 삭제 (DELETE /rest/api/3/version/{id})

## 기본 정보

- **기능:** 프로젝트 버전 삭제 (deprecated)
- **Endpoint:** `DELETE /rest/api/3/version/{id}`
- **인증:** Bearer Token 필요
- **권한:** *Administer Jira* 전역 권한 또는 해당 프로젝트의 *Administer Projects* 프로젝트 권한

## 설명

버전을 삭제한다. `moveFixIssuesTo`/`moveAffectedIssuesTo`로 대체 버전을 지정할 수 있으나 커스텀 필드는 대체하지 못한다. Deprecated 상태이며 커스텀 필드까지 대체 가능한 "삭제 및 대체"(removeAndSwap) API 사용이 권장된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Yes | 버전 ID | `10000` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `moveFixIssuesTo` | string | No | - | fixVersion 대체 버전 ID(동일 프로젝트, 삭제 대상 아님) | `10001` |
| `moveAffectedIssuesTo` | string | No | - | affectedVersion 대체 버전 ID | `10001` |

## Response

### `204 No Content`

버전이 삭제되면 본문 없이 204를 반환한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 파라미터 확인 |
| 401 | - | 인증 정보가 잘못되었거나 권한 부족 | 토큰/권한 확인 |
| 404 | - | 버전을 찾을 수 없음 | 버전 ID 확인 |

## 주의 사항

- Deprecated. 신규 구현에서는 13번(Delete and replace version)을 사용할 것.

---

### [중간] 10. 버전 병합 (PUT /rest/api/3/version/{id}/mergeto/{moveIssuesTo})

## 기본 정보

- **기능:** 두 프로젝트 버전을 병합 (삭제 대상 버전의 fixVersion 참조를 대상 버전으로 치환)
- **Endpoint:** `PUT /rest/api/3/version/{id}/mergeto/{moveIssuesTo}`
- **인증:** Bearer Token 필요
- **권한:** *Administer Jira* 전역 권한 또는 해당 프로젝트의 *Administer Projects* 프로젝트 권한

## 설명

`id` 버전을 삭제하면서 그 버전을 참조하던 `fixVersion`을 `moveIssuesTo` 버전으로 교체한다. `affectedVersion`과 커스텀 필드까지 치환하려면 13번(Delete and replace version) 사용이 권장된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Yes | 삭제할 버전 ID | `10000` |
| `moveIssuesTo` | string | Yes | 병합 대상(유지될) 버전 ID | `10001` |

## Response

### `204 No Content`

버전이 삭제(병합)되면 본문 없이 204를 반환한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 파라미터 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 권한 부족 | 토큰/권한 확인 |
| 404 | - | 삭제 대상 또는 병합 대상 버전을 찾을 수 없음 | 버전 ID 확인 |

## 주의 사항

- `affectedVersion`, 커스텀 필드까지 함께 치환하려면 13번 API를 대신 사용할 것.

---

### [중간] 11. 버전 이동 (POST /rest/api/3/version/{id}/move)

## 기본 정보

- **기능:** 프로젝트 내 버전의 표시 순서(sequence) 변경
- **Endpoint:** `POST /rest/api/3/version/{id}/move`
- **인증:** Bearer Token 필요
- **권한:** 해당 프로젝트의 *Browse projects* 권한

## 설명

버전을 다른 버전 뒤로 옮기거나(`after`), 절대 위치(`position`: Earlier/Later/First/Last)로 이동시킨다. `after`와 `position`은 동시에 사용할 수 없다. UI 상 버전 표시 순서만 바꾸는 보조 기능이다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Yes | 이동할 버전 ID | `10000` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `after` | string | No | `position`과 동시 사용 불가 | 이 버전 뒤에 배치할 대상 버전의 self URL | `"https://your-domain.atlassian.net/rest/api/3/version/10000"` |
| `position` | enum | No | `after`와 동시 사용 불가 | `Earlier`, `Later`, `First`, `Last` | `"Last"` |

```json
{
  "position": "Last"
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 버전 ID | `"10000"` |

```json
{
  "archived": false,
  "description": "An excellent version",
  "id": "10000",
  "name": "New Version 1",
  "overdue": true,
  "projectId": 10000,
  "releaseDate": "2010-07-06",
  "released": true,
  "self": "https://your-domain.atlassian.net/rest/api/3/version/10000",
  "userReleaseDate": "6/Jul/2010"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | body 파라미터 누락, `after`와 `position` 동시 지정, `position` 값 오류 | body 검증 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 권한 부족 | 토큰/권한 확인 |
| 404 | - | 버전 또는 `after` 대상 버전을 찾을 수 없음 | 버전 ID 확인 |

---

### [중간] 12. 관련 작업 조회 (GET /rest/api/3/version/{id}/relatedwork)

## 기본 정보

- **기능:** 버전에 연결된 관련 작업(디자인 링크, 채팅, 외부 링크 등) 목록 조회
- **Endpoint:** `GET /rest/api/3/version/{id}/relatedwork`
- **인증:** Bearer Token 필요 (익명 접근 가능 설정 시 불필요)
- **권한:** 해당 프로젝트의 *Browse projects* 권한

## 설명

버전에 첨부된 관련 작업 항목(카테고리, 제목, URL 등)을 반환한다. 릴리즈 노트나 디자인 문서 링크 등을 버전과 연결해 대시보드에 노출할 때 보조적으로 사용할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Yes | 버전 ID | `10000` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `category` | string | 관련 작업 카테고리 | `"Design"` |
| `issueId` | integer | 연관된 이슈 ID(있는 경우) | `10001` |
| `relatedWorkId` | string | 관련 작업 ID (UUID) | `"fabcdef6-7878-1234-beaf-43211234abcd"` |
| `title` | string | 관련 작업 제목 | `"Design link"` |
| `url` | string | 관련 작업 URL | `"https://www.atlassian.com"` |

```json
[
  {"category": "Design", "issueId": 10001, "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abcd", "title": "Design link", "url": "https://www.atlassian.com"},
  {"category": "Communications", "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abce", "title": "Chat application", "url": "https://www.atlassian.com"},
  {"category": "External Link", "issueId": 10003, "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abcf", "url": "https://www.atlassian.com"}
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 토큰 확인 |
| 404 | - | 버전이 없거나 권한 부족 | 버전 ID 및 권한 확인 |
| 500 | - | 관련 작업 조회 중 서버 오류 | 재시도 |

---

### [중간] 13. 관련 작업 수정 (PUT /rest/api/3/version/{id}/relatedwork)

## 기본 정보

- **기능:** 버전에 연결된 관련 작업(일반 링크 유형)의 내용 수정
- **Endpoint:** `PUT /rest/api/3/version/{id}/relatedwork`
- **인증:** Bearer Token 필요
- **권한:** 해당 프로젝트의 *Resolve issues* 및 *Edit issues* 권한

## 설명

일반 링크(generic link) 유형의 관련 작업만 REST API로 수정할 수 있으며, 아카이브된 버전의 관련 작업은 수정할 수 없다. 관련 작업 ID는 요청 본문(JSON)에 포함해서 전달한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Yes | 관련 작업을 수정할 버전 ID | `10000` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `category` | string | Yes | - | 관련 작업 카테고리 | `"Design"` |
| `issueId` | integer | No | REST API로 수정 불가 | 연관된 이슈 ID | `10001` |
| `relatedWorkId` | string | No | 네이티브 릴리즈 노트 항목은 null | 관련 작업 ID | `"fabcdef6-7878-1234-beaf-43211234abcd"` |
| `title` | string | No | - | 관련 작업 제목 | `"Design link"` |
| `url` | string | No | 네이티브 릴리즈 노트 외에는 필수 | 관련 작업 URL | `"https://www.atlassian.com"` |

```json
{
  "category": "Design",
  "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abcd",
  "title": "Design link",
  "url": "https://www.atlassian.com"
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `category` | string | 카테고리 | `"Design"` |
| `title` | string | 제목 | `"Design link"` |
| `url` | string | URL | `"https://www.atlassian.com"` |

```json
{
  "category": "Design",
  "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abcd",
  "title": "Design link",
  "url": "https://www.atlassian.com"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청 데이터가 유효하지 않음 | body 검증 |
| 401 | - | 인증 정보가 잘못됨 | 토큰 확인 |
| 403 | - | 필요한 권한이 없음 | 권한 확인 |
| 404 | - | 버전 또는 관련 작업을 찾을 수 없음 | ID 확인 |

## 주의 사항

- 일반 링크 유형만 수정 가능, 아카이브된 버전은 수정 불가.

---

### [중간] 14. 관련 작업 생성 (POST /rest/api/3/version/{id}/relatedwork)

## 기본 정보

- **기능:** 버전에 새로운 관련 작업(일반 링크) 추가
- **Endpoint:** `POST /rest/api/3/version/{id}/relatedwork`
- **인증:** Bearer Token 필요
- **권한:** 해당 프로젝트의 *Resolve issues* 및 *Edit issues* 권한

## 설명

일반 링크 유형의 관련 작업만 이 API로 생성할 수 있다. `relatedWorkId`는 서버에서 UUID로 자동 생성되므로 요청 시 제공할 필요가 없다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | Yes | 관련 작업을 추가할 버전 ID | `10000` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `category` | string | Yes | - | 관련 작업 카테고리 | `"Design"` |
| `issueId` | integer | No | - | 연관된 이슈 ID | `10001` |
| `title` | string | No | - | 관련 작업 제목 | `"Design link"` |
| `url` | string | No | 네이티브 릴리즈 노트 외에는 필수 | 관련 작업 URL | `"https://www.atlassian.com"` |

```json
{
  "category": "Design",
  "title": "Design link",
  "url": "https://www.atlassian.com"
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `category` | string | 카테고리 | `"Design"` |
| `relatedWorkId` | string | 생성된 관련 작업 ID | `"fabcdef6-7878-1234-beaf-43211234abcd"` |
| `title` | string | 제목 | `"Design link"` |
| `url` | string | URL | `"https://www.atlassian.com"` |

```json
{
  "category": "Design",
  "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abcd",
  "title": "Design link",
  "url": "https://www.atlassian.com"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | body 검증 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 토큰 확인 |
| 403 | - | 필요한 권한이 없음 | 권한 확인 |
| 404 | - | 버전을 찾을 수 없음 | 버전 ID 확인 |

---

### [중간] 15. 관련 작업 삭제 (DELETE /rest/api/3/version/{versionId}/relatedwork/{relatedWorkId})

## 기본 정보

- **기능:** 버전에 연결된 특정 관련 작업 삭제
- **Endpoint:** `DELETE /rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}`
- **인증:** Bearer Token 필요
- **권한:** 해당 프로젝트의 *Resolve issues* 및 *Edit issues* 권한

## 설명

버전에 연결된 관련 작업 하나를 ID로 지정해 삭제한다. 릴리즈 노트/디자인 링크 정리 등 보조적인 정리 작업에 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `versionId` | string | Yes | 관련 작업이 속한 버전 ID | `10000` |
| `relatedWorkId` | string | Yes | 삭제할 관련 작업 ID | `fabcdef6-7878-1234-beaf-43211234abcd` |

## Response

### `204 No Content`

관련 작업이 삭제되면 본문 없이 204를 반환한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 파라미터 확인 |
| 401 | - | 인증 정보가 잘못됨 | 토큰 확인 |
| 403 | - | 필요한 권한이 없음 | 권한 확인 |
| 404 | - | 버전 또는 관련 작업을 찾을 수 없음 | ID 확인 |
