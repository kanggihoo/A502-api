# __09-dashboards API 요약

이 리소스 그룹은 Jira 대시보드(dashboard)의 조회/생성/수정/삭제/복사, 대시보드에 배치된 가젯(gadget) 관리, 대시보드 아이템 속성(item property) 관리를 다룬다. SSAFY POC에서는 팀 통합 대시보드 구성 및 조회(원문 링크 제공)에 직접 활용할 수 있는 API들이다.

## 제외된 API

- 제외된 파일 없음 (모든 엔드포인트가 프로젝트 관리자 수준 이하 권한으로 호출 가능하며, `extendAdminPermissions`는 선택적 파라미터로 사이트 전체 관리자가 아니어도 API 자체는 호출 가능함)

---

### [높은 우선순위] 1. 모든 대시보드 조회 (GET /rest/api/3/dashboard)

## 기본 정보

- **기능:** 사용자가 소유하거나 공유받은 대시보드 목록을 조회한다.
- **Endpoint:** `GET /rest/api/3/dashboard`
- **인증:** 불필요 (익명 접근 가능)
- **권한:** 없음

## 설명

사용자가 소유(owned)하거나 공유(shared)받은 대시보드 목록을 반환한다. `filter` 쿼리 파라미터로 즐겨찾기(favourite) 또는 본인 소유(my) 대시보드만 필터링할 수 있다. 페이지네이션(`startAt`, `maxResults`)을 지원한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `filter` | string | 아니오 | - | 대시보드 목록에 적용할 필터. `favourite`(즐겨찾기), `my`(본인 소유) | `my` |
| `startAt` | integer | 아니오 | - | 페이지 결과의 첫 항목 인덱스(오프셋) | `10` |
| `maxResults` | integer | 아니오 | - | 페이지당 최대 반환 항목 수 | `10` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `dashboards` | array | 대시보드 객체 배열 | - |
| `dashboards[].id` | string | 대시보드 ID | `"10000"` |
| `dashboards[].name` | string | 대시보드 이름 | `"System Dashboard"` |
| `dashboards[].isFavourite` | boolean | 즐겨찾기 여부 | `false` |
| `dashboards[].owner` | object | 대시보드 소유자 | - |
| `dashboards[].sharePermissions` | array | 공유 권한 목록 | `[{"type":"global"}]` |
| `dashboards[].view` | string | 대시보드 조회 URL | - |
| `maxResults` | integer | 페이지당 최대 항목 수 | `10` |
| `startAt` | integer | 페이지 시작 인덱스 | `10` |
| `total` | integer | 전체 대시보드 수 | `143` |

```json
{
  "dashboards": [
    {
      "id": "10000",
      "isFavourite": false,
      "name": "System Dashboard",
      "popularity": 1,
      "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/10000",
      "sharePermissions": [{"type": "global"}],
      "view": "https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000"
    }
  ],
  "maxResults": 10,
  "next": "https://your-domain.atlassian.net/rest/api/3/dashboard?startAt=10",
  "prev": "https://your-domain.atlassian.net/rest/api/3/dashboard?startAt=0",
  "startAt": 10,
  "total": 143
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 잘못됨 | 파라미터 값 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 익명 접근이 허용되지만 익명 사용자에게는 소유/공유 대시보드가 반환되지 않을 수 있음(검색 API와 동일한 제약).
- 통합 대시보드 화면에서 팀의 대시보드 목록을 보여줄 때 기본으로 사용할 수 있는 API.

---

### [높은 우선순위] 2. 대시보드 생성 (POST /rest/api/3/dashboard)

## 기본 정보

- **기능:** 새 대시보드를 생성한다.
- **Endpoint:** `POST /rest/api/3/dashboard`
- **인증:** 필요
- **권한:** 없음 (단, `extendAdminPermissions=true`는 *Administer Jira* 전역 권한이 있을 때만 사용)

## 설명

이름, 설명, 공유 권한(sharePermissions), 편집 권한(editPermissions)을 지정하여 새 대시보드를 생성한다. 팀 생성 자동화 흐름에서 팀 전용 대시보드를 프로그래밍적으로 만들 때 사용할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `extendAdminPermissions` | boolean | 아니오 | `false` | 관리자 수준 권한 사용 여부. *Administer Jira* 전역 권한 보유 시에만 `true` 권장 | `false` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | 예 | - | 대시보드 이름 | `"Team A Dashboard"` |
| `description` | string | 아니오 | - | 대시보드 설명 | `"Sprint 상황판"` |
| `sharePermissions` | array | 예 | - | 대시보드 공유 권한 목록 | - |
| `sharePermissions[].type` | enum | 예 | `user`\|`group`\|`project`\|`projectRole`\|`global`\|`loggedin`\|`authenticated`\|`project-unknown` | 공유 권한 유형 | `"global"` |
| `editPermissions` | array | 예 | - | 대시보드 편집 권한 목록 (구조는 sharePermissions와 동일) | - |

```json
{
  "name": "Team A Dashboard",
  "description": "Sprint 상황판",
  "sharePermissions": [{"type": "global"}],
  "editPermissions": []
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 생성된 대시보드 ID | `"10000"` |
| `name` | string | 대시보드 이름 | `"System Dashboard"` |
| `sharePermissions` | array | 공유 권한 | `[{"type":"global"}]` |
| `view` | string | 조회 URL | - |

```json
{
  "id": "10000",
  "isFavourite": false,
  "name": "System Dashboard",
  "popularity": 1,
  "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/10000",
  "sharePermissions": [{"type": "global"}],
  "view": "https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청 본문이 유효하지 않음 (필수 필드 누락 등) | Body 필수 필드(`name`, `sharePermissions`, `editPermissions`) 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- `sharePermissions`와 `editPermissions`는 필수 필드이며 빈 배열이라도 명시해야 함.
- `extendAdminPermissions=true`는 SSAFY 교육생(프로젝트 관리자) 계정으로는 효과가 없거나 거부될 수 있으므로 기본값(false)으로 사용 권장.

---

### [높은 우선순위] 3. 대시보드 검색 (GET /rest/api/3/dashboard/search)

## 기본 정보

- **기능:** 이름, 소유자, 그룹, 프로젝트 등 조건으로 대시보드를 검색한다(페이지네이션 지원).
- **Endpoint:** `GET /rest/api/3/dashboard/search`
- **인증:** 불필요 (익명 접근 가능, 단 익명 사용자에게는 소유/그룹 공유 대시보드는 반환 안 됨)
- **권한:** 없음

## 설명

01번(모든 대시보드 조회) API와 유사하지만 이름, 소유자 `accountId`, 그룹, 프로젝트 등 다양한 속성으로 결과를 정교하게 필터링할 수 있다. 여러 속성을 동시에 지정하면 모두 만족하는 대시보드만 반환된다. `expand`로 설명, 소유자, 조회 URL, 즐겨찾기 여부 등 부가 정보를 포함할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `dashboardName` | string | 아니오 | - | 이름 부분 일치(대소문자 무시) 검색 | `"Sprint"` |
| `accountId` | string | 아니오 | - | 소유자 accountId로 필터 (`owner`와 동시 사용 불가) | `5b10a2844c20165700ede21g` |
| `owner` | string | 아니오 | - | (deprecated) 소유자 사용자명으로 필터 | - |
| `groupname` | string | 아니오 | - | 공유 그룹명으로 필터 (`groupId`와 동시 사용 불가) | - |
| `groupId` | string | 아니오 | - | 공유 그룹 ID로 필터 | - |
| `projectId` | integer | 아니오 | - | 공유 프로젝트 ID로 필터 | `10001` |
| `orderBy` | string | 아니오 | - | 정렬 기준: `description`, `favourite_count`, `id`, `is_favourite`, `name`, `owner` | `name` |
| `startAt` | integer | 아니오 | - | 페이지 시작 오프셋 | `0` |
| `maxResults` | integer | 아니오 | `100` | 페이지당 최대 항목 수 | `50` |
| `status` | string | 아니오 | - | `active`, `archived`, `deleted` | `active` |
| `expand` | string | 아니오 | - | `description`, `owner`, `viewUrl`, `favourite`, `favouritedCount`, `sharePermissions`, `editPermissions`, `isWritable` (콤마 구분) | `owner,description` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `true` |
| `maxResults` | integer | 페이지당 최대 항목 수 | `100` |
| `startAt` | integer | 시작 오프셋 | `0` |
| `total` | integer | 전체 결과 수 | `2` |
| `values` | array | 대시보드 객체 배열 | - |
| `values[].id` | string | 대시보드 ID | `"1"` |
| `values[].name` | string | 대시보드 이름 | `"Testing"` |
| `values[].description` | string | 설명 (expand=description 시) | `"Testing program"` |
| `values[].owner` | object | 소유자 정보 (expand=owner 시) | - |

```json
{
  "isLast": true,
  "maxResults": 100,
  "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/search?expand=owner&maxResults=50&startAt=0",
  "startAt": 0,
  "total": 2,
  "values": [
    {
      "description": "Testing program",
      "id": "1",
      "isFavourite": true,
      "name": "Testing",
      "owner": {"accountId": "5b10a2844c20165700ede21g", "displayName": "Mia"},
      "popularity": 1,
      "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/1",
      "sharePermissions": [{"type": "global"}],
      "view": "https://your-domain.atlassian.net/Dashboard.jspa?selectPageId=1"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `orderBy` 값이 잘못됨 / `expand`에 잘못된 값 포함 / `accountId`와 `owner` 동시 지정 / `groupname`과 `groupId` 동시 지정 | 상호 배타 파라미터 동시 사용 금지, 허용값 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- `accountId`/`owner`, `groupname`/`groupId`는 각각 동시 사용 불가.
- 통합 대시보드 화면에서 조건별 필터링/정렬이 필요할 때 01번보다 이 API를 우선 사용.

---

### [높은 우선순위] 4. 대시보드 단건 조회 (GET /rest/api/3/dashboard/{id})

## 기본 정보

- **기능:** 특정 ID의 대시보드 상세 정보를 조회한다.
- **Endpoint:** `GET /rest/api/3/dashboard/{id}`
- **인증:** 불필요 (익명 접근 가능)
- **권한:** 없음 (단, 대시보드가 사용자와 공유되어 있거나 사용자가 소유해야 조회 가능)

## 설명

대시보드 ID로 단건 조회한다. System Dashboard는 모든 사용자와 공유된 것으로 간주되며, *Administer Jira* 전역 권한 보유자는 System Dashboard의 소유자로 간주된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | 예 | 대시보드 ID | `"10000"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 대시보드 ID | `"10000"` |
| `name` | string | 대시보드 이름 | `"System Dashboard"` |
| `isFavourite` | boolean | 즐겨찾기 여부 | `false` |
| `sharePermissions` | array | 공유 권한 | `[{"type":"global"}]` |
| `view` | string | 조회 URL | - |

```json
{
  "id": "10000",
  "isFavourite": false,
  "name": "System Dashboard",
  "popularity": 1,
  "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/10000",
  "sharePermissions": [{"type": "global"}],
  "view": "https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 잘못된 요청 | 파라미터 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 404 | - | 대시보드가 없거나 소유/공유되지 않음 | ID 및 접근 권한 확인 |

```json
{
  "errorMessages": ["The dashboard you requested either does not exist or you don't have the required permissions to perform this action."],
  "errors": {}
}
```

## 주의 사항

- 통합 대시보드 상세 화면(원문 링크 제공)에서 `view` 필드를 그대로 활용 가능.

---

### [높은 우선순위] 5. 대시보드 수정 (PUT /rest/api/3/dashboard/{id})

## 기본 정보

- **기능:** 대시보드의 모든 세부 정보를 제공된 값으로 교체(업데이트)한다.
- **Endpoint:** `PUT /rest/api/3/dashboard/{id}`
- **인증:** 필요
- **권한:** 없음 (단, 수정 대상 대시보드는 요청 사용자가 소유해야 함)

## 설명

이름, 설명, 공유/편집 권한을 포함해 대시보드 전체를 덮어쓴다. 부분 수정이 아니라 전체 교체 방식이므로 기존 값을 유지하려면 요청 본문에 그대로 포함해야 한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | 예 | 수정할 대시보드 ID | `"10000"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `extendAdminPermissions` | boolean | 아니오 | `false` | *Administer Jira* 전역 권한 보유 시에만 `true` 사용 권장 | `false` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | 예 | - | 대시보드 이름 | `"Team A Dashboard"` |
| `description` | string | 아니오 | - | 대시보드 설명 | `"업데이트된 설명"` |
| `sharePermissions` | array | 예 | - | 공유 권한 목록 | `[{"type":"global"}]` |
| `editPermissions` | array | 예 | - | 편집 권한 목록 | `[]` |

```json
{
  "name": "Team A Dashboard",
  "description": "업데이트된 설명",
  "sharePermissions": [{"type": "global"}],
  "editPermissions": []
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 대시보드 ID | `"10000"` |
| `name` | string | 변경된 이름 | `"System Dashboard"` |

```json
{
  "id": "10000",
  "isFavourite": false,
  "name": "System Dashboard",
  "popularity": 1,
  "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/10000",
  "sharePermissions": [{"type": "global"}],
  "view": "https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | Body 필수 필드 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 404 | - | 대시보드가 없거나 사용자가 소유하지 않음 | ID 및 소유권 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 대시보드는 요청 사용자가 소유해야만 수정 가능.
- 전체 교체 방식이므로 부분 필드만 보내면 나머지가 초기화될 수 있음.

---

### [높은 우선순위] 6. 대시보드 삭제 (DELETE /rest/api/3/dashboard/{id})

## 기본 정보

- **기능:** 대시보드를 삭제한다.
- **Endpoint:** `DELETE /rest/api/3/dashboard/{id}`
- **인증:** 필요
- **권한:** 없음 (단, 삭제 대상 대시보드는 요청 사용자가 소유해야 함)

## 설명

지정한 ID의 대시보드를 삭제한다. 팀 프로젝트 종료/정리 시 대시보드 정리 자동화에 사용할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | 예 | 삭제할 대시보드 ID | `"10000"` |

## Response

### `204 No Content`

삭제 성공 시 본문 없이 204 반환.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 잘못된 요청 | ID 형식 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 소유자만 삭제 가능하며 되돌릴 수 없는 작업이므로 자동화 스크립트에서 신중히 사용해야 함.

---

### [높은 우선순위] 7. 대시보드 복사 (POST /rest/api/3/dashboard/{id}/copy)

## 기본 정보

- **기능:** 기존 대시보드를 복사하여 새 대시보드를 만든다.
- **Endpoint:** `POST /rest/api/3/dashboard/{id}/copy`
- **인증:** 필요
- **권한:** 없음 (단, 원본 대시보드는 요청 사용자가 소유하거나 공유받아야 함)

## 설명

지정한 대시보드를 복제하며, 요청 본문에 제공된 값(이름, 설명, 권한 등)이 복사본에서 원본 값을 대체한다. 팀 생성 자동화 시 템플릿 대시보드를 복제해 새 팀 대시보드를 빠르게 구성하는 데 유용하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string | 예 | 복사할 원본 대시보드 ID | `"10000"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `extendAdminPermissions` | boolean | 아니오 | `false` | *Administer Jira* 전역 권한 보유 시에만 `true` 사용 권장 | `false` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | 예 | - | 새 대시보드 이름 | `"Team B Dashboard (Copy)"` |
| `description` | string | 아니오 | - | 새 대시보드 설명 | `"Team A 템플릿 복사본"` |
| `sharePermissions` | array | 예 | - | 공유 권한 목록 | `[{"type":"global"}]` |
| `editPermissions` | array | 예 | - | 편집 권한 목록 | `[]` |

```json
{
  "name": "Team B Dashboard (Copy)",
  "description": "Team A 템플릿 복사본",
  "sharePermissions": [{"type": "global"}],
  "editPermissions": []
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 새로 생성된 대시보드 ID | `"10000"` |
| `name` | string | 새 대시보드 이름 | `"System Dashboard"` |

```json
{
  "id": "10000",
  "isFavourite": false,
  "name": "System Dashboard",
  "popularity": 1,
  "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/10000",
  "sharePermissions": [{"type": "global"}],
  "view": "https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | Body 필수 필드 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 404 | - | 원본 대시보드가 없거나 소유/공유되지 않음 | ID 및 접근 권한 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 팀별 대시보드를 매번 처음부터 만들지 않고 템플릿을 복제하는 방식으로 팀 생성 자동화에 활용 가능.

---

### [중간 우선순위] 8. 대시보드 일괄 편집 (PUT /rest/api/3/dashboard/bulk/edit)

## 기본 정보

- **기능:** 여러 대시보드의 소유자 변경, 권한 변경/추가/삭제를 한 번에 처리한다.
- **Endpoint:** `PUT /rest/api/3/dashboard/bulk/edit`
- **인증:** 필요
- **권한:** 없음 (단, 대상 대시보드는 사용자가 소유하거나 사용자가 관리자여야 함)

## 설명

최대 100개의 대시보드를 한 번에 편집할 수 있다. `action` 값에 따라 소유자 변경(`changeOwner`), 권한 변경/추가/삭제(`changePermission`/`addPermission`/`removePermission`)를 수행한다. 개별 대시보드 처리 실패 시 `entityErrors`에 실패 사유가 담겨 반환된다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `action` | enum | 예 | `changeOwner`\|`changePermission`\|`addPermission`\|`removePermission` | 수행할 일괄 작업 종류 | `"changePermission"` |
| `entityIds` | array<integer> | 예 | - | 대상 대시보드 ID 목록 | `[10001, 10002]` |
| `changeOwnerDetails` | object | 아니오 | `action=changeOwner` 시 사용 | 소유자 변경 상세 정보 | - |
| `permissionDetails` | object | 아니오 | `changePermission`/`addPermission`/`removePermission` 시 사용 | 변경할 권한 상세 정보 | - |
| `extendAdminPermissions` | boolean | 아니오 | - | *Administer Jira* 전역 권한 사용자가 실행하는지 여부 | `false` |

```json
{
  "action": "changePermission",
  "entityIds": [10001, 10002],
  "permissionDetails": {}
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `action` | string | 수행된 작업 | `"changePermission"` |
| `entityErrors` | object | 대시보드 ID별 오류 목록 | - |

```json
{
  "action": "changePermission",
  "entityErrors": {
    "10002": {
      "errorMessages": ["Only owner or editors of the dashboard can change permissions."],
      "errors": {}
    }
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | `action`, `entityIds` 등 필수값 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 최대 100개 대시보드까지 한 번에 처리 가능.
- 일부 대시보드가 실패해도 나머지는 처리될 수 있으므로 응답의 `entityErrors`를 반드시 확인해야 함.

---

### [중간 우선순위] 9. 사용 가능한 가젯 목록 조회 (GET /rest/api/3/dashboard/gadgets)

## 기본 정보

- **기능:** 모든 대시보드에 추가할 수 있는 가젯 목록을 조회한다.
- **Endpoint:** `GET /rest/api/3/dashboard/gadgets`
- **인증:** 필요
- **권한:** 없음

## 설명

Jira 사이트에 설치된 앱/플러그인이 제공하는 가젯들의 목록을 반환한다. 대시보드 구성 UI를 만들 때 선택 가능한 가젯 종류를 보여주는 용도로 사용한다.

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `gadgets` | array | 가젯 목록 | - |
| `gadgets[].moduleKey` | string | 가젯 모듈 키 | `"com.atlassian.plugins...sample-dashboard-item"` |
| `gadgets[].uri` | string | 가젯 URI (모듈 키 대신 사용될 수 있음) | `"rest/gadgets/1.0/g/..."` |
| `gadgets[].title` | string | 가젯 제목 | `"Issue statistics"` |

```json
{
  "gadgets": [
    {"moduleKey": "com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item", "title": "Issue statistics"},
    {"uri": "rest/gadgets/1.0/g/com.atlassian.streams.streams-jira-plugin:activitystream-gadget/gadgets/activitystream-gadget.xml", "title": "Activity Stream"}
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 잘못된 요청 | - |
| 401 | - | 인증 오류 | 인증 토큰 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 대시보드 구성/편집 화면에서 부가적으로 사용 가능한 조회성 API.

---

### [중간 우선순위] 10. 대시보드의 가젯 목록 조회 (GET /rest/api/3/dashboard/{dashboardId}/gadget)

## 기본 정보

- **기능:** 특정 대시보드에 배치된 가젯 목록을 조회한다.
- **Endpoint:** `GET /rest/api/3/dashboard/{dashboardId}/gadget`
- **인증:** 불필요 (익명 접근 가능)
- **권한:** 없음

## 설명

ID, 모듈 키, URI로 필터링하거나 파라미터 없이 전체 가젯을 조회할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `dashboardId` | integer | 예 | 대시보드 ID | `10000` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `moduleKey` | array | 아니오 | - | 가젯 모듈 키 목록 (`&`로 구분) | `key:one&moduleKey=key:two` |
| `uri` | array | 아니오 | - | 가젯 URI 목록 (`&`로 구분) | `/rest/example/uri/1` |
| `gadgetId` | array | 아니오 | - | 가젯 ID 목록 (`&`로 구분) | `10000&gadgetId=10001` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `gadgets` | array | 가젯 목록 | - |
| `gadgets[].id` | integer | 가젯 ID | `10001` |
| `gadgets[].color` | string | 가젯 색상 | `"blue"` |
| `gadgets[].position` | object | 배치 위치(`row`, `column`) | `{"row":0,"column":0}` |
| `gadgets[].title` | string | 가젯 제목 | `"Issue statistics"` |

```json
{
  "gadgets": [
    {"id": 10001, "moduleKey": "com.atlassian.plugins...sample-dashboard-item", "color": "blue", "position": {"row": 0, "column": 0}, "title": "Issue statistics"}
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 404 | - | 대시보드를 찾을 수 없음 | 대시보드 ID 및 접근 권한 확인 |

```json
{
  "errorMessages": ["The dashboard you requested either does not exist or you don't have the required permissions to perform this action."],
  "errors": {}
}
```

## 주의 사항

- 대시보드 상세 화면에서 배치된 가젯을 렌더링할 때 사용하는 보조 조회 API.

---

### [중간 우선순위] 11. 대시보드에 가젯 추가 (POST /rest/api/3/dashboard/{dashboardId}/gadget)

## 기본 정보

- **기능:** 대시보드에 새 가젯을 추가한다.
- **Endpoint:** `POST /rest/api/3/dashboard/{dashboardId}/gadget`
- **인증:** 필요
- **권한:** 없음

## 설명

지정한 위치에 가젯을 추가하며, 같은 열(column)의 기존 가젯들은 아래로 밀려난다. `moduleKey`와 `uri`는 동시에 지정할 수 없다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `dashboardId` | integer | 예 | 대시보드 ID | `10000` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `color` | string | 아니오 | `blue`\|`red`\|`yellow`\|`green`\|`cyan`\|`purple`\|`gray`\|`white` | 가젯 색상 | `"blue"` |
| `moduleKey` | string | 아니오 | `uri`와 동시 사용 불가 | 가젯 타입의 모듈 키 | - |
| `uri` | string | 아니오 | `moduleKey`와 동시 사용 불가 | 가젯 타입의 URI | - |
| `position` | object | 아니오 | - | 가젯 배치 위치 | `{"row":0,"column":1}` |
| `title` | string | 아니오 | - | 가젯 제목 | `"Issue statistics"` |
| `ignoreUriAndModuleKeyValidation` | boolean | 아니오 | - | 모듈 키/URI 검증 생략 여부 | `false` |

```json
{
  "color": "blue",
  "moduleKey": "com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item",
  "position": {"row": 0, "column": 1},
  "title": "Issue statistics"
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 생성된 가젯 ID | `10001` |
| `color` | string | 가젯 색상 | `"blue"` |
| `position` | object | 배치 위치 | `{"column":1,"row":0}` |
| `title` | string | 가젯 제목 | `"Issue statistics"` |

```json
{
  "color": "blue",
  "id": 10001,
  "moduleKey": "com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item",
  "position": {"column": 1, "row": 0},
  "title": "Issue statistics"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 대시보드가 수용 가능한 최대 가젯 수 초과 등 | 가젯 개수 및 필드 값 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 404 | - | 대시보드를 찾을 수 없음 | 대시보드 ID 확인 |

```json
{
  "errorMessages": ["Cannot add another gadget. The maximum number of gadgets the dashboard can hold has been reached."],
  "errors": {}
}
```

## 주의 사항

- 대시보드별 최대 가젯 수 제한이 있으므로 자동화 스크립트에서 400 에러를 처리해야 함.

---

### [중간 우선순위] 12. 대시보드 가젯 수정 (PUT /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId})

## 기본 정보

- **기능:** 대시보드에 배치된 가젯의 제목, 위치, 색상을 변경한다.
- **Endpoint:** `PUT /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}`
- **인증:** 필요
- **권한:** 없음

## 설명

가젯의 표시 속성(제목/위치/색상)만 변경하며 가젯이 다루는 데이터 자체는 변경하지 않는다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `dashboardId` | integer | 예 | 대시보드 ID | `10000` |
| `gadgetId` | integer | 예 | 가젯 ID | `10001` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `color` | string | 아니오 | `blue`\|`red`\|`yellow`\|`green`\|`cyan`\|`purple`\|`gray`\|`white` | 가젯 색상 | `"red"` |
| `position` | object | 아니오 | - | 가젯 배치 위치 | `{"row":1,"column":0}` |
| `title` | string | 아니오 | - | 가젯 제목 | `"Activity stream"` |

```json
{
  "color": "red",
  "position": {"row": 1, "column": 0},
  "title": "Activity stream"
}
```

## Response

### `204 No Content`

수정 성공 시 본문 없이 204 반환.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 선택한 행(row)이 대시보드에 존재하지 않는 등 잘못된 요청 | 위치 값 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 404 | - | 가젯 또는 대시보드를 찾을 수 없음 | ID 확인 |

```json
{
  "errorMessages": ["The gadget cannot be placed in the selected row. The selected row does not exist on the dashboard."],
  "errors": {}
}
```

## 주의 사항

- 존재하지 않는 행/열로 이동 시 400 오류 발생.

---

### [중간 우선순위] 13. 대시보드 가젯 삭제 (DELETE /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId})

## 기본 정보

- **기능:** 대시보드에서 가젯을 제거한다.
- **Endpoint:** `DELETE /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}`
- **인증:** 필요
- **권한:** 없음

## 설명

가젯을 제거하면 같은 열(column)의 나머지 가젯들이 위로 당겨져 빈 자리를 채운다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `dashboardId` | integer | 예 | 대시보드 ID | `10000` |
| `gadgetId` | integer | 예 | 가젯 ID | `10001` |

## Response

### `204 No Content`

삭제 성공 시 본문 없이 204 반환.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 404 | - | 가젯 또는 대시보드를 찾을 수 없음 | ID 확인 |

```json
{
  "errorMessages": ["The dashboard gadget was not found."],
  "errors": {}
}
```

## 주의 사항

- 삭제 후 같은 열의 가젯 위치가 자동으로 재정렬됨에 유의.

---

### [중간 우선순위] 14. 대시보드 아이템 속성 키 목록 조회 (GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties)

## 기본 정보

- **기능:** 특정 대시보드 아이템(가젯)에 저장된 모든 속성(property)의 키 목록을 조회한다.
- **Endpoint:** `GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties`
- **인증:** 불필요 (익명 접근 가능)
- **권한:** 대시보드에 대한 읽기 권한 보유 또는 공유받은 사용자

## 설명

앱이 대시보드 아이템에 저장해 둔 커스텀 데이터(속성)의 키 목록만 반환한다. 값 자체는 15번 API로 별도 조회해야 한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `dashboardId` | string | 예 | 대시보드 ID | `10000` |
| `itemId` | string | 예 | 대시보드 아이템 ID | `10001` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `keys` | array | 속성 키 목록 | - |
| `keys[].key` | string | 속성 키 | `"issue.support"` |
| `keys[].self` | string | 속성 조회 URL | - |

```json
{
  "keys": [
    {"key": "issue.support", "self": "https://your-domain.atlassian.net/rest/api/3/issue/EX-2/properties/issue.support"}
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 404 | - | 대시보드 또는 아이템을 찾을 수 없거나 접근 권한 없음 | ID 및 공유 상태 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 주로 앱(add-on) 개발 시 가젯의 설정/상태 데이터를 다루는 용도로, POC의 핵심 흐름보다는 보조적 기능.

---

### [중간 우선순위] 15. 대시보드 아이템 속성 조회 (GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey})

## 기본 정보

- **기능:** 대시보드 아이템의 특정 속성 키/값을 조회한다.
- **Endpoint:** `GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}`
- **인증:** 불필요 (익명 접근 가능)
- **권한:** 대시보드에 대한 읽기 권한 보유 또는 공유받은 사용자

## 설명

대시보드 아이템(가젯)이 사용자별로 저장한 콘텐츠나 설정 정보를 조회한다. 앱이 가젯을 렌더링하거나 사용자가 설정을 편집할 때 사용하는 콜백 데이터 저장소 개념이다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `dashboardId` | string | 예 | 대시보드 ID | `10000` |
| `itemId` | string | 예 | 대시보드 아이템 ID | `10001` |
| `propertyKey` | string | 예 | 속성 키 | `"issue.support"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `key` | string | 속성 키 | `"issue.support"` |
| `value` | object | 속성 값(임의 JSON) | `{"system.conversation.id":"b1bf38be-5e94-4b40-a3b8-9278735ee1e6"}` |

```json
{
  "key": "issue.support",
  "value": {
    "system.conversation.id": "b1bf38be-5e94-4b40-a3b8-9278735ee1e6",
    "system.support.time": "1m"
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 404 | - | 대시보드, 아이템, 속성을 찾을 수 없거나 접근 권한 없음 | ID 및 공유 상태 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 앱 개발용 API로, 대시보드 아이템 자체를 생성/조회하는 리소스는 없음(속성만 다룸).

---

### [중간 우선순위] 16. 대시보드 아이템 속성 설정 (PUT /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey})

## 기본 정보

- **기능:** 대시보드 아이템의 속성 값을 생성하거나 갱신한다.
- **Endpoint:** `PUT /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}`
- **인증:** 불필요 (익명 접근 가능하다고 명시되어 있으나 실제 편집은 권한 필요)
- **권한:** 대시보드에 대한 편집 권한 보유

## 설명

앱이 대시보드 아이템(가젯)에 커스텀 데이터를 저장할 때 사용한다. 요청 본문은 유효하고 비어있지 않은 JSON이어야 하며 최대 길이는 32768자다. `propertyKey`가 `"config"`이고 아이템이 spec URI만 있고 완전한 module key가 없는 경우, 요청 JSON은 모든 키/값이 문자열인 객체여야 한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `dashboardId` | string | 예 | 대시보드 ID | `10000` |
| `itemId` | string | 예 | 대시보드 아이템 ID | `10001` |
| `propertyKey` | string | 예 | 속성 키 (최대 255자) | `"issue.support"` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| (본문 전체) | any | 예 | 유효한 비어있지 않은 JSON, 최대 32768자 | 저장할 속성 값 | `{"system.support.time":"1m"}` |

```json
{
  "system.conversation.id": "b1bf38be-5e94-4b40-a3b8-9278735ee1e6",
  "system.support.time": "1m"
}
```

## Response

### `200 OK` / `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| (본문) | any | 갱신(200) 또는 생성(201) 결과, 본문 스키마는 임의(any) | - |

```json
{}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음, 또는 `propertyKey=config`이면서 JSON 키/값이 문자열이 아님 | JSON 형식 및 propertyKey 조건 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 403 | - | 사용자가 대시보드 소유자가 아님 | 편집 권한 확인 |
| 404 | - | 대시보드 아이템을 찾을 수 없거나 대시보드가 공유되지 않음 | ID 및 공유 상태 확인 |

```json
{
  "errorMessages": ["The JSON data provided for the property has too many levels. It must be an object with all keys and values as strings."],
  "errors": {}
}
```

## 주의 사항

- `propertyKey`가 `"config"`인 특수 케이스에서 JSON 값 제약이 다름에 유의.
- 최대 길이 32768자 제한이 있음.

---

### [중간 우선순위] 17. 대시보드 아이템 속성 삭제 (DELETE /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey})

## 기본 정보

- **기능:** 대시보드 아이템의 속성을 삭제한다.
- **Endpoint:** `DELETE /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}`
- **인증:** 불필요 (익명 접근 가능하다고 명시되어 있으나 실제 삭제는 권한 필요)
- **권한:** 대시보드에 대한 편집 권한 보유

## 설명

지정한 대시보드 아이템의 특정 속성 값을 삭제한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `dashboardId` | string | 예 | 대시보드 ID | `10000` |
| `itemId` | string | 예 | 대시보드 아이템 ID | `10001` |
| `propertyKey` | string | 예 | 속성 키 | `"issue.support"` |

## Response

### `204 No Content`

삭제 성공 시 본문 없이 204 반환.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 대시보드 또는 아이템 ID가 유효하지 않음 | ID 형식 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 403 | - | 사용자가 대시보드 소유자가 아님 | 편집 권한 확인 |
| 404 | - | 대시보드 아이템을 찾을 수 없거나 대시보드가 공유되지 않음 | ID 및 공유 상태 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 앱 개발용 API로 POC의 핵심 흐름(팀 생성/알림/운영 지원)과는 직접 관련이 적음.
