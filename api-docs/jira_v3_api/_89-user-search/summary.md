# _89-user-search API 요약

이 리소스 그룹은 Jira 사용자를 다양한 조건(프로젝트/이슈 할당 가능 여부, 권한 보유 여부, 검색어, 구조화된 쿼리 등)으로 검색하는 API 모음이다. 팀 생성 자동화 시 담당자/워처 후보를 찾거나, 통합 알림·대시보드에서 이슈 관련 사용자(assignee, watcher, commenter 등)를 조회하는 데 활용할 수 있다.

## 제외된 API

- 없음 (이 그룹의 모든 API는 사이트 전체 시스템 관리자 권한이 필수가 아니며, 최소 프로젝트 관리자 또는 그 이하 권한으로 호출 가능하여 전부 채택함)

---

### [높음] 1. Find users assignable to projects (GET /rest/api/3/user/assignable/multiProjectSearch)

## 기본 정보

- **기능:** 하나 이상의 프로젝트에 이슈 담당자로 지정 가능한 사용자 목록 조회
- **Endpoint:** `GET /rest/api/3/user/assignable/multiProjectSearch`
- **인증:** 익명 호출 가능 (Bearer/Basic 인증 없이도 호출 가능)
- **권한:** `projectKeys`에 지정된 각 프로젝트에 대한 *Browse Projects* 프로젝트 권한

## 설명

주어진 프로젝트들에서 이슈에 배정 가능한 사용자를 검색어(`query`) 또는 정확한 `accountId`로 찾는다. `startAt`/`maxResults` 범위 내 사용자 중 배정 가능한 사용자만 반환되므로 응답 개수가 `maxResults`보다 적을 수 있다. 사용자 프라이버시 설정에 따라 이메일 등 일부 필드가 숨겨질 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `query` | string | No | - | `displayName`, `emailAddress`의 접두사와 매칭되는 검색어. `accountId` 미지정 시 필수 | `john` |
| `username` | string | No | - | 더 이상 사용되지 않음 (deprecated) | - |
| `accountId` | string | No | - | 정확히 일치하는 사용자 accountId. `query` 미지정 시 필수 | `5b10a2844c20165700ede21g` |
| `projectKeys` | string | Yes | - | 쉼표로 구분된 프로젝트 키 목록 (대소문자 구분) | `PROJ1,PROJ2` |
| `startAt` | integer | No | - | 페이지 오프셋 | `0` |
| `maxResults` | integer | No | - | 페이지당 최대 항목 수 | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `accountId` | string | 사용자 계정 ID | `5b10a2844c20165700ede21g` |
| `accountType` | string | 계정 유형 | `atlassian` |
| `active` | boolean | 활성 여부 | `false` |
| `avatarUrls` | object | 아바타 URL 모음 | - |
| `displayName` | string | 표시 이름 | `Mia Krystof` |

```json
[
  {
    "accountId": "5b10a2844c20165700ede21g",
    "accountType": "atlassian",
    "active": false,
    "avatarUrls": {
      "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48"
    },
    "displayName": "Mia Krystof",
    "key": "",
    "name": "",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `projectKeys` 누락 / `query`·`accountId` 둘 다 없거나 둘 다 있음 | 요청 파라미터 확인 |
| 401 | - | 인증 정보 없음 또는 오류 | 인증 토큰 확인 |
| 404 | - | 프로젝트를 찾을 수 없음 | 프로젝트 키 확인 |
| 429 | - | Rate limit 초과 (사용자 검색 API 공용 한도) | `Retry-After` 헤더 준수 후 재시도 |

## 주의 사항

- `startAt`/`maxResults` 범위 내에서 최대 1000명까지만 대상이 되며, 배정 가능 여부 필터링 후 반환되므로 실제 반환 수가 `maxResults`보다 적을 수 있다.
- 전체 사용자를 원하면 Get all users API로 가져온 뒤 애플리케이션 코드에서 필터링해야 한다.

---

### [높음] 2. Find users assignable to issues (GET /rest/api/3/user/assignable/search)

## 기본 정보

- **기능:** 특정 이슈(신규/기존/전환 중)에 담당자로 지정 가능한 사용자 목록 조회
- **Endpoint:** `GET /rest/api/3/user/assignable/search`
- **인증:** Bearer Token 필요 (익명 접근 불가)
- **권한:** *Browse users and groups* 글로벌 권한 또는 *Assign issues* 프로젝트 권한

## 설명

신규 이슈는 `projectKeyOrId`(project 파라미터)로, 기존 이슈는 `issueKey`/`issueId`로, 워크플로 전환 중에는 `actionDescriptorId`까지 함께 지정해 배정 가능한 사용자를 조회한다. `sessionId`를 사용하면 담당자가 확정될 때까지 동일 세션으로 유지할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `query` | string | No | - | 사용자 속성 검색어. `username`/`accountId` 미지정 시 필수 | `john` |
| `sessionId` | string | No | - | 요청 세션 ID (담당자 확정 전까지 동일) | - |
| `username` | string | No | - | deprecated | - |
| `accountId` | string | No | - | 정확히 일치하는 accountId. `query` 미지정 시 필수 | `5b10a2844c20165700ede21g` |
| `project` | string | No | - | 프로젝트 ID/키. `issueKey`/`issueId` 미지정 시 필수 | `PROJ` |
| `issueKey` | string | No | - | 이슈 키. `issueId`/`project` 미지정 시 필수 | `PROJ-123` |
| `issueId` | string | No | - | 이슈 ID | `10001` |
| `startAt` | integer | No | - | 페이지 오프셋 | `0` |
| `maxResults` | integer | No | - | 최대 반환 수 | `50` |
| `actionDescriptorId` | integer | No | - | 전환(transition) ID | `21` |
| `recommend` | boolean | No | - | - | `true` |
| `accountType` | array | No | - | - | - |
| `appType` | array | No | - | - | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `accountId` | string | 사용자 계정 ID | `5b10a2844c20165700ede21g` |
| `displayName` | string | 표시 이름 | `Mia Krystof` |
| `emailAddress` | string | 이메일 | `mia@example.com` |
| `timeZone` | string | 타임존 | `Australia/Sydney` |

```json
{
  "accountId": "5b10a2844c20165700ede21g",
  "accountType": "atlassian",
  "active": true,
  "applicationRoles": { "items": [], "size": 1 },
  "displayName": "Mia Krystof",
  "emailAddress": "mia@example.com",
  "groups": { "items": [], "size": 3 },
  "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g",
  "timeZone": "Australia/Sydney"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `issueKey`/`issueId`/`project` 모두 없음, `issueId` 형식 오류, `query`/`accountId` 조합 오류 | 요청 파라미터 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 404 | - | 프로젝트, 이슈, 전환을 찾을 수 없음 | 대상 키/ID 확인 |
| 429 | - | Rate limit 초과 | `Retry-After` 헤더 준수 |

## 주의 사항

- 이슈 담당자 배정 UI(자동화된 이슈 배정 플로우)에서 핵심적으로 쓰이는 API.
- `expand=transitions`로 얻은 전환 ID를 `actionDescriptorId`에 넘겨 전환 시점의 배정 가능 사용자를 확인할 수 있다.

---

### [높음] 3. Find users (GET /rest/api/3/user/search)

## 기본 정보

- **기능:** 검색어/속성과 일치하는 활성 사용자 목록 조회
- **Endpoint:** `GET /rest/api/3/user/search`
- **인증:** 익명 호출 가능하나, 권한 없을 시 빈 결과 반환
- **권한:** *Browse users and groups* 글로벌 권한

## 설명

`query`, `accountId`, `property` 중 하나로 필터링하여 활성 사용자 목록을 반환하는 범용 사용자 검색 API다. 팀 생성 자동화에서 채널 멤버 후보를 찾거나 담당자 매핑을 만들 때 기본적으로 사용할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `query` | string | No | - | `displayName`, `emailAddress` 검색어. `accountId`/`property` 미지정 시 필수 | `john` |
| `username` | string | No | - | - | - |
| `accountId` | string | No | - | 정확히 일치하는 accountId. `query`/`property` 미지정 시 필수 | `5b10a2844c20165700ede21g` |
| `startAt` | integer | No | - | 페이지 오프셋 | `0` |
| `maxResults` | integer | No | - | 페이지당 최대 항목 수 | `50` |
| `property` | string | No | - | 사용자 프로퍼티 검색 경로 쿼리. `accountId`/`query` 미지정 시 필수 | `thepropertykey.something.nested=1` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `accountId` | string | 계정 ID | `5b10a2844c20165700ede21g` |
| `active` | boolean | 활성 여부 | `false` |
| `displayName` | string | 표시 이름 | `Mia Krystof` |

```json
[
  {
    "accountId": "5b10a2844c20165700ede21g",
    "accountType": "atlassian",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `accountId`/`query`/`property` 모두 없음, `query`와 `accountId` 동시 지정, `property` 형식 오류 | 요청 파라미터 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 429 | - | Rate limit 초과 | `Retry-After` 헤더 준수 |

## 주의 사항

- 권한이 없는 사용자나 익명 호출은 빈 배열을 반환하며 에러가 아니다.
- 최대 1000명까지만 검색 대상이 된다.

---

### [높음] 4. Find users by query (GET /rest/api/3/user/search/query)

## 기본 정보

- **기능:** 구조화된 쿼리(assignee/reporter/watcher/voter/commenter/transitioner 조건)로 사용자 목록을 검색
- **Endpoint:** `GET /rest/api/3/user/search/query`
- **인증:** Bearer Token 필요
- **권한:** *Browse users and groups* 글로벌 권한

## 설명

`is assignee of PROJ`, `is watcher of (PROJ-1, PROJ-2)`, `is commenter of (...)` 등 구조화된 질의문으로 이슈와 사용자의 관계를 조회한다. 통합 알림·대시보드에서 특정 이슈의 담당자·워처·코멘트 작성자·투표자·전환 수행자를 한 번에 조회하는 데 유용하다. `AND`/`OR`로 복합 조건을 구성할 수 있고, 사용자 엔티티 프로퍼티 조건도 결합 가능하다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `query` | string | Yes | - | 구조화된 검색 쿼리 | `is watcher of (PROJ-1, PROJ-2)` |
| `startAt` | integer | No | - | 페이지 오프셋 | `0` |
| `maxResults` | integer | No | - | 페이지당 최대 항목 수 | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `true` |
| `maxResults` | integer | 반환 가능한 최대 항목 수 | `50` |
| `startAt` | integer | 첫 항목 인덱스 | `0` |
| `total` | integer | 반환된 항목 수 | `2` |
| `values[].accountId` | string | 사용자 계정 ID | `5b10ac8d82e05b22cc7d4ef5` |
| `values[].displayName` | string | 표시 이름 | `Mia Krystof` |
| `values[].active` | boolean | 활성 여부 | `true` |

```json
{
  "isLast": true,
  "maxResults": 50,
  "startAt": 0,
  "total": 1,
  "values": [
    {
      "accountId": "5b10ac8d82e05b22cc7d4ef5",
      "accountType": "atlassian",
      "active": true,
      "displayName": "Mia Krystof",
      "emailAddress": "mia@example.com",
      "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10ac8d82e05b22cc7d4ef5"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 쿼리 문법 오류 | `query` 문법 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 403 | - | 필요한 권한 없음 | 권한 확인 |
| 408 | - | 검색 타임아웃 | 쿼리 범위 축소 후 재시도 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 알림/대시보드에서 "이 이슈의 워처·코멘트 작성자·투표자 전체 조회" 같은 기능 구현 시 가장 직접적으로 쓰이는 API.
- 최대 1000명까지만 대상이 되며 그 범위 내에서 조건에 맞는 사용자만 반환된다.

---

### [중간] 5. Find users with permissions (GET /rest/api/3/user/permission/search)

## 기본 정보

- **기능:** 검색어와 일치하고 특정 프로젝트/이슈에 대한 권한을 가진 사용자 목록 조회
- **Endpoint:** `GET /rest/api/3/user/permission/search`
- **인증:** 익명 호출 가능
- **권한:** *Administer Jira* 글로벌 권한(모든 프로젝트 대상) 또는 *Administer Projects* 프로젝트 권한(해당 프로젝트만 대상)

## 설명

검색어(또는 accountId)와 `permissions`(쉼표 구분 권한 목록)를 조합하여, 지정한 프로젝트(`projectKey`) 또는 이슈(`issueKey`)에 대해 해당 권한을 가진 사용자만 걸러서 반환한다. 검색어가 없으면 해당 권한을 가진 모든 사용자를 반환한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `query` | string | No | - | 검색어. `accountId` 미지정 시 필수 | `john` |
| `username` | string | No | - | deprecated | - |
| `accountId` | string | No | - | 정확히 일치하는 accountId. `query` 미지정 시 필수 | `5b10a2844c20165700ede21g` |
| `permissions` | string | Yes | - | 쉼표로 구분된 권한 목록 (Get all permissions 참고 또는 deprecated 값) | `BROWSE,CREATE_ISSUE` |
| `issueKey` | string | No | - | 이슈 키 | `PROJ-123` |
| `projectKey` | string | No | - | 프로젝트 키 (대소문자 구분) | `PROJ` |
| `startAt` | integer | No | - | 페이지 오프셋 | `0` |
| `maxResults` | integer | No | - | 페이지당 최대 항목 수 | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `accountId` | string | 계정 ID | `5b10a2844c20165700ede21g` |
| `displayName` | string | 표시 이름 | `Mia Krystof` |

```json
[
  {
    "accountId": "5b10a2844c20165700ede21g",
    "accountType": "atlassian",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `issueKey`/`projectKey` 누락, `query`/`accountId` 조합 오류, `permissions` 비어있거나 잘못된 값 | 요청 파라미터 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 403 | - | 필요 권한 없음 | 권한 확인 (프로젝트 관리자 권한 필요) |
| 404 | - | 이슈/프로젝트를 찾을 수 없음 | 대상 키 확인 |
| 429 | - | Rate limit 초과 | `Retry-After` 헤더 준수 |

## 주의 사항

- 사이트 전체 관리자(Administer Jira)가 아니어도 해당 프로젝트의 프로젝트 관리자(Administer Projects) 권한만으로 그 프로젝트에 한해 호출 가능하다.
- 특정 권한(예: 코멘트 삭제, 이슈 편집)을 가진 담당자 후보를 찾는 보조 기능으로 활용 가능.

---

### [중간] 6. Find users for picker (GET /rest/api/3/user/picker)

## 기본 정보

- **기능:** 검색어와 매칭되는 사용자 목록을 하이라이트(HTML strong 태그)와 함께 조회 (사용자 선택 UI용)
- **Endpoint:** `GET /rest/api/3/user/picker`
- **인증:** 익명 호출 가능 (단, 권한 없으면 정확한 이름 일치만 반환)
- **권한:** *Browse users and groups* 글로벌 권한

## 설명

담당자 지정 등 사용자 선택 UI에서 자동완성 기능을 구현할 때 사용하는 API로, 일치 부분이 `<strong>` 태그로 감싸진 `html` 필드를 함께 반환한다. `excludeAccountIds`로 특정 사용자를 결과에서 제외할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `query` | string | Yes | - | 검색어 | `john` |
| `maxResults` | integer | No | - | 최대 반환 수 (전체 매칭 수는 `total`에 반환) | `20` |
| `showAvatar` | boolean | No | - | 아바타 URI 포함 여부 | `true` |
| `exclude` | array | No | - | deprecated | - |
| `excludeAccountIds` | array | No | - | 제외할 accountId 목록 (쉼표 또는 & 구분) | `5b10a2844c20165700ede21g,5b10a0effa615349cb016cd8` |
| `avatarSize` | string | No | - | - | - |
| `excludeConnectUsers` | boolean | No | - | - | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `header` | string | 결과 요약 문구 | `Showing 20 of 25 matching groups` |
| `total` | integer | 전체 매칭 수 | `25` |
| `users[].accountId` | string | 계정 ID | `5b10a2844c20165700ede21g` |
| `users[].html` | string | 하이라이트된 표시 텍스트 | `<strong>Mi</strong>a Krystof - <strong>mi</strong>a@example.com` |

```json
{
  "header": "Showing 20 of 25 matching groups",
  "total": 25,
  "users": [
    {
      "accountId": "5b10a2844c20165700ede21g",
      "accountType": "atlassian",
      "avatarUrl": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16",
      "displayName": "Mia Krystof",
      "html": "<strong>Mi</strong>a Krystof - <strong>mi</strong>a@example.com (<strong>mi</strong>a)",
      "key": "mia",
      "name": "mia"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `exclude`와 `excludeAccountIds` 동시 지정 | 둘 중 하나만 사용 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 429 | - | Rate limit 초과 | `Retry-After` 헤더 준수 |

## 주의 사항

- 팀 생성 자동화 시 사용자 선택 UI(담당자/멤버 지정 자동완성)를 만들 때 보조적으로 활용 가능하나 핵심 CRUD 흐름은 아니다.

---

### [중간] 7. Find user keys by query (GET /rest/api/3/user/search/query/key)

## 기본 정보

- **기능:** 구조화된 쿼리로 사용자를 검색해 accountId/key 목록만 반환
- **Endpoint:** `GET /rest/api/3/user/search/query/key`
- **인증:** Bearer Token 필요
- **권한:** *Browse users and groups* 글로벌 권한

## 설명

06번(Find users by query)과 동일한 구조화된 질의 문법을 사용하지만, 사용자 상세 정보 대신 `accountId`와 (더 이상 사용되지 않는) `key`만 반환하는 경량 버전이다. `key` 필드는 deprecated 상태로 곧 제거될 예정이라 실질적으로 `accountId` 목록 조회 용도로만 유효하다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `query` | string | Yes | - | 구조화된 검색 쿼리 | `is assignee of PROJ` |
| `startAt` | integer | No | - | 페이지 오프셋 | `0` |
| `maxResult` | integer | No | - | 페이지당 최대 항목 수 (오타 아님, `maxResult` 단수형) | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `true` |
| `total` | integer | 반환된 항목 수 | `1` |
| `values[].accountId` | string | 계정 ID (삭제/손상된 레코드는 `unknown`) | `5b10ac8d82e05b22cc7d4ef5` |
| `values[].key` | string | deprecated | - |

```json
{
  "isLast": true,
  "maxResults": 50,
  "startAt": 0,
  "total": 1,
  "values": [
    { "accountId": "5b10ac8d82e05b22cc7d4ef5" }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 쿼리 문법 오류 | `query` 문법 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 403 | - | 필요한 권한 없음 | 권한 확인 |
| 408 | - | 검색 타임아웃 | 쿼리 범위 축소 후 재시도 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {},
  "status": 400
}
```

## 주의 사항

- 06번 API(Find users by query)와 기능이 겹치며, `accountId`만 필요한 경량 조회 상황에서만 06번 대신 사용할 가치가 있다.

---

### [중간] 8. Find users with browse permission (GET /rest/api/3/user/viewissue/search)

## 기본 정보

- **기능:** 검색어와 일치하고 이슈/프로젝트 열람(Browse) 권한을 가진 사용자 목록 조회
- **Endpoint:** `GET /rest/api/3/user/viewissue/search`
- **인증:** 익명 호출 가능 (권한 없으면 빈 결과)
- **권한:** *Browse users and groups* 글로벌 권한

## 설명

특정 이슈(`issueKey`)나 프로젝트(`projectKey`)의 이슈를 열람할 수 있는 사용자를 검색어로 필터링해 조회한다. 알림 대상(해당 이슈를 볼 수 있는 사용자)을 판별하는 보조 기능으로 쓸 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `query` | string | No | - | 검색어. `accountId` 미지정 시 필수 | `john` |
| `username` | string | No | - | deprecated | - |
| `accountId` | string | No | - | 정확히 일치하는 accountId. `query` 미지정 시 필수 | `5b10a2844c20165700ede21g` |
| `issueKey` | string | No | - | 이슈 키. `projectKey` 미지정 시 필수 | `PROJ-123` |
| `projectKey` | string | No | - | 프로젝트 키. `issueKey` 미지정 시 필수 | `PROJ` |
| `startAt` | integer | No | - | 페이지 오프셋 | `0` |
| `maxResults` | integer | No | - | 페이지당 최대 항목 수 | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `accountId` | string | 계정 ID | `5b10a2844c20165700ede21g` |
| `displayName` | string | 표시 이름 | `Mia Krystof` |

```json
[
  {
    "accountId": "5b10a2844c20165700ede21g",
    "accountType": "atlassian",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `issueKey`/`projectKey` 누락, `query`/`accountId` 조합 오류 | 요청 파라미터 확인 |
| 401 | - | 인증 오류 | 인증 토큰 확인 |
| 404 | - | 이슈/프로젝트를 찾을 수 없음 | 대상 키 확인 |
| 429 | - | Rate limit 초과 | `Retry-After` 헤더 준수 |

## 주의 사항

- 06번(구조화된 쿼리)과 달리 단순 "볼 수 있는 사람" 목록만 제공하며, 워처/코멘트 작성자 등 관계 정보는 없다.
