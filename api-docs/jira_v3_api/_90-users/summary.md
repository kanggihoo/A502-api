# _90-users API 요약

이 리소스 그룹은 Jira 사용자(User)를 조회/생성/삭제하고, 사용자의 기본 이슈 테이블 컬럼과 소속 그룹, 이메일 정보를 다루는 API 모음이다.

## 제외된 API

- `02-create-user-post.md`: Create user — "Administer Jira" 글로벌 권한이 필요하며 문서에 "The caller has to be an **organization admin**"라고 명시되어 있어, 사이트 전체 조직 관리자 권한이 필요하다. 교육생(프로젝트 관리자) 계정으로는 호출 불가하여 제외.
- `03-delete-user-delete.md`: Delete user — "Site administration (that is, membership of the *site-admin* group)" 권한이 명시되어 있어 사이트 전체 관리자 전용 API이므로 제외.

---

### [높음] 1. Get user (GET /rest/api/3/user)

## 기본 정보

- **기능:** accountId로 특정 Jira 사용자의 상세 프로필 정보를 조회한다.
- **Endpoint:** `GET /rest/api/3/user`
- **인증:** Bearer Token(또는 Basic/API Token) 필요
- **권한:** *Browse users and groups* global permission

## 설명

팀 생성 자동화나 통합 알림에서 이슈 담당자/보고자/코멘트 작성자 등의 표시 이름, 아바타, 활성 상태를 보여줄 때 사용한다. 사용자의 프로필 공개 설정(Profile visibility)에 따라 이메일 등 일부 필드는 응답에서 숨겨질 수 있다. `expand` 파라미터로 소속 그룹이나 애플리케이션 롤 정보를 함께 받을 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| accountId | string | No | - | 사용자의 계정 ID (Atlassian 전역에서 사용자를 식별) | `5b10ac8d82e05b22cc7d4ef5` |
| username | string | No | - | 더 이상 사용되지 않음 (deprecated) | - |
| key | string | No | - | 더 이상 사용되지 않음 (deprecated) | - |
| expand | string | No | - | 쉼표로 구분된 확장 옵션: `groups`(소속 그룹 포함), `applicationRoles`(접근 가능한 애플리케이션 정보 포함) | `groups,applicationRoles` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| accountId | string | 사용자 계정 ID | `5b10a2844c20165700ede21g` |
| accountType | string | 계정 유형 | `atlassian` |
| active | boolean | 활성 사용자 여부 | `true` |
| displayName | string | 표시 이름 | `Mia Krystof` |
| emailAddress | string | 이메일 주소 (공개 설정에 따라 숨김 가능) | `mia@example.com` |
| avatarUrls | object | 크기별 아바타 URL | `{"48x48": "..."}` |
| timeZone | string | 사용자 타임존 | `Australia/Sydney` |

```json
{
  "accountId": "5b10a2844c20165700ede21g",
  "accountType": "atlassian",
  "active": true,
  "applicationRoles": { "items": [], "size": 1 },
  "avatarUrls": {
    "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16",
    "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48"
  },
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
| 401 | - | 인증 정보 누락/오류 | 인증 토큰 확인 후 재요청 |
| 403 | - | *Browse users and groups* 권한 없음 | 계정 권한 확인 |
| 404 | - | 해당 accountId의 사용자를 찾을 수 없음 | accountId 값 검증 |

## 주의 사항

- 사용자의 프로필 공개 설정에 따라 emailAddress 등 일부 필드가 응답에서 제외될 수 있다.
- `username`, `key` 쿼리 파라미터는 더 이상 사용되지 않는다(GDPR 관련 마이그레이션).

---

### [높음] 2. Bulk get users (GET /rest/api/3/user/bulk)

## 기본 정보

- **기능:** 여러 accountId를 한 번에 지정하여 사용자 목록을 페이지네이션으로 조회한다.
- **Endpoint:** `GET /rest/api/3/user/bulk`
- **인증:** Bearer Token 필요
- **권한:** Permission to access Jira (일반 Jira 접근 권한)

## 설명

여러 이슈에 관련된 담당자/워치어 등 다수 사용자의 정보를 한 번에 조회할 때 사용한다. 프로젝트 관리자 권한 수준에서도 호출 가능해 알림/대시보드 기능에서 사용자 목록을 배치로 가져오는 데 적합하다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---|---:|---|---|
| startAt | integer | No | - | 페이지 오프셋(첫 결과 인덱스) | `0` |
| maxResults | integer | No | - | 페이지당 최대 항목 수 | `100` |
| username | array | No | - | deprecated | - |
| key | array | No | - | deprecated | - |
| accountId | array | Yes | - | 사용자 accountId (여러 개 지정 가능, 각각 별도 파라미터로 전달) | `accountId=5b10a2844c20165700ede21g&accountId=5b10ac8d82e05b22cc7d4ef5` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| isLast | boolean | 마지막 페이지 여부 | `true` |
| maxResults | integer | 페이지당 최대 항목 수 | `100` |
| startAt | integer | 시작 인덱스 | `0` |
| total | integer | 전체 결과 수 | `1` |
| values | array | 사용자 객체 배열 | - |

```json
{
  "isLast": true,
  "maxResults": 100,
  "startAt": 0,
  "total": 1,
  "values": [
    {
      "accountId": "5b10a2844c20165700ede21g",
      "accountType": "atlassian",
      "active": true,
      "avatarUrls": { "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" },
      "displayName": "Mia Krystof",
      "emailAddress": "mia@example.com",
      "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g",
      "timeZone": "Australia/Sydney"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `accountId`가 누락됨 | 요청에 accountId 파라미터 포함 여부 확인 |
| 401 | - | 인증 정보 누락/오류 | 인증 토큰 확인 |

## 주의 사항

- `accountId`는 필수이며 여러 개를 지정할 때는 파라미터를 반복해서 전달해야 한다.

---

### [높음] 3. Get user groups (GET /rest/api/3/user/groups)

## 기본 정보

- **기능:** 특정 사용자가 속한 그룹 목록을 조회한다.
- **Endpoint:** `GET /rest/api/3/user/groups`
- **인증:** Bearer Token 필요
- **권한:** *Browse users and groups* global permission

## 설명

팀 생성 자동화 과정에서 특정 사용자가 어떤 그룹(예: 프로젝트 역할과 연관된 그룹)에 속해 있는지 확인할 때 사용한다. 결과는 사용자가 속한 그룹들의 배열로 반환된다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| accountId | string | Yes | - | 사용자 계정 ID | `5b10ac8d82e05b22cc7d4ef5` |
| username | string | No | - | deprecated | - |
| key | string | No | - | deprecated | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| groupId | string | 그룹 ID | `276f955c-63d7-42c8-9520-92d01dca0625` |
| name | string | 그룹 이름 | `jira-administrators` |
| self | string | 그룹 리소스 URL | `https://your-domain.atlassian.net/rest/api/3/group?groupId=...` |

```json
{
  "groupId": "276f955c-63d7-42c8-9520-92d01dca0625",
  "name": "jira-administrators",
  "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 누락/오류 | 인증 토큰 확인 |
| 403 | - | *Browse users and groups* 권한 없음 | 계정 권한 확인 |
| 404 | - | 사용자를 찾을 수 없음 | accountId 검증 |

## 주의 사항

- `accountId`는 필수 파라미터다.

---

### [높음] 4. Get all users default (GET /rest/api/3/users)

## 기본 정보

- **기능:** 활성/비활성/삭제된 사용자를 포함한 전체 사용자 목록을 조회한다.
- **Endpoint:** `GET /rest/api/3/users`
- **인증:** Bearer Token 필요
- **권한:** *Browse users and groups* global permission

## 설명

팀 생성 자동화 시 조직 내 전체 사용자 목록을 가져와 팀원 후보를 선택하거나 매핑하는 데 사용할 수 있다. 페이지네이션 파라미터로 결과를 나눠 받을 수 있으며, 응답에는 비활성/삭제된 계정도 포함될 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| startAt | integer | No | - | 반환할 첫 항목의 인덱스 | `0` |
| maxResults | integer | No | - | 반환할 최대 항목 수 (최대 1000) | `50` |
| expand | string | No | - | 확장 옵션 (문서에 상세 값 명시 없음) | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| accountId | string | 사용자 계정 ID | `5b10a2844c20165700ede21g` |
| accountType | string | 계정 유형 | `atlassian` |
| active | boolean | 활성 여부 | `false` |
| displayName | string | 표시 이름 | `Mia Krystof` |
| avatarUrls | object | 아바타 URL | `{"48x48": "..."}` |

```json
[
  {
    "accountId": "5b10a2844c20165700ede21g",
    "accountType": "atlassian",
    "active": false,
    "avatarUrls": { "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" },
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  {
    "accountId": "5b10ac8d82e05b22cc7d4ef5",
    "accountType": "atlassian",
    "active": false,
    "avatarUrls": { "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=48&s=48" },
    "displayName": "Emma Richards",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10ac8d82e05b22cc7d4ef5"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 잘못됨 | 파라미터 값 확인 |
| 403 | - | 필요한 권한 없음 | 계정 권한 확인 |
| 409 | - | 요청이 10초 이상 걸리거나 중단됨 | 재시도 |

## 주의 사항

- `expand`로 사용 가능한 값이 문서에 구체적으로 명시되어 있지 않다.
- 대규모 조직에서는 요청이 10초를 초과하면 409가 반환될 수 있다.

---

### [높음] 5. Get all users (GET /rest/api/3/users/search)

## 기본 정보

- **기능:** 활성/비활성/삭제된 사용자를 포함한 전체 사용자 목록을 검색/조회한다.
- **Endpoint:** `GET /rest/api/3/users/search`
- **인증:** Bearer Token 필요
- **권한:** *Browse users and groups* global permission

## 설명

`GET /rest/api/3/users`와 동일한 목적이지만 검색용 엔드포인트로 제공되며, 페이지네이션을 지원한다. 팀 생성 자동화에서 사용자 검색/선택 UI를 만들 때 이 엔드포인트를 우선 사용하는 것이 권장된다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| startAt | integer | No | - | 반환할 첫 항목의 인덱스 | `0` |
| maxResults | integer | No | - | 반환할 최대 항목 수 (최대 1000) | `50` |
| expand | string | No | - | 확장 옵션 (문서에 상세 값 명시 없음) | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| accountId | string | 사용자 계정 ID | `5b10a2844c20165700ede21g` |
| accountType | string | 계정 유형 | `atlassian` |
| active | boolean | 활성 여부 | `false` |
| displayName | string | 표시 이름 | `Emma Richards` |

```json
[
  {
    "accountId": "5b10a2844c20165700ede21g",
    "accountType": "atlassian",
    "active": false,
    "avatarUrls": { "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" },
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 잘못됨 | 파라미터 값 확인 |
| 403 | - | 필요한 권한 없음 | 계정 권한 확인 |
| 409 | - | 요청이 10초 이상 걸리거나 중단됨 | 재시도 |

## 주의 사항

- `/users`(default)와 기능이 거의 동일하며, 검색 목적으로는 이 엔드포인트(`/users/search`) 사용을 권장한다.

---

### [중간] 6. Get account IDs for users (GET /rest/api/3/user/bulk/migration)

## 기본 정보

- **기능:** `username` 또는 `key`로 지정한 사용자들의 accountId를 조회한다.
- **Endpoint:** `GET /rest/api/3/user/bulk/migration`
- **인증:** Bearer Token 필요
- **권한:** Permission to access Jira

## 설명

과거 username/key 기반 데이터를 accountId 기반으로 마이그레이션할 때 사용하는 보조 API다. `username`과 `key` 중 하나만 지정할 수 있으며 여러 개를 반복 파라미터로 전달할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| startAt | integer | No | - | 페이지 오프셋 | `0` |
| maxResults | integer | No | - | 페이지당 최대 항목 수 | `100` |
| username | array | No | - | 사용자명. `key`가 없으면 필수. `key`와 동시 사용 불가 | `username=fred&username=barney` |
| key | array | No | - | 사용자 키. `username`이 없으면 필수. `username`과 동시 사용 불가 | `key=fred&key=barney` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| username | string | 사용자명 | `mia` |
| accountId | string | 계정 ID | `5b10a2844c20165700ede21g` |

```json
[
  { "username": "mia", "accountId": "5b10a2844c20165700ede21g" },
  { "username": "emma", "accountId": "5b10ac8d82e05b22cc7d4ef5" }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `key` 또는 `username` 관련 오류 | 두 파라미터 중 하나만 정확히 전달했는지 확인 |
| 401 | - | 인증 정보 누락/오류 | 인증 토큰 확인 |

## 주의 사항

- `username`, `key`는 레거시 마이그레이션 용도이며 신규 통합 로직에서는 accountId를 직접 사용하는 것이 권장된다.

---

### [중간] 7. Get user default columns (GET /rest/api/3/user/columns)

## 기본 정보

- **기능:** 사용자의 기본 이슈 테이블 컬럼 설정을 조회한다.
- **Endpoint:** `GET /rest/api/3/user/columns`
- **인증:** Bearer Token 필요
- **권한:** 다른 사용자 컬럼 조회 시 *Administer Jira* global permission, 본인 컬럼 조회 시 Permission to access Jira

## 설명

`accountId`를 지정하지 않으면 호출한 사용자 본인의 기본 컬럼 설정을 반환한다. 대시보드에서 이슈 목록을 표시할 기본 컬럼 구성을 파악하는 등 보조적인 용도로 사용할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| accountId | string | No | - | 사용자 계정 ID (미지정 시 호출자 본인) | `5b10ac8d82e05b22cc7d4ef5` |
| username | string | No | - | deprecated | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| label | string | 이슈 네비게이터 컬럼 라벨 | `Summary` |
| value | string | 이슈 네비게이터 컬럼 값 | `summary` |

```json
[
  { "label": "Summary", "value": "summary" }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 누락/오류 | 인증 토큰 확인 |
| 403 | - | 권한 없음 또는 본인 레코드가 아님 | 권한/accountId 확인 |
| 404 | - | 요청한 사용자를 찾을 수 없음 | accountId 검증 |

## 주의 사항

- 다른 사용자의 컬럼을 조회하려면 *Administer Jira* 권한이 필요하다(프로젝트 관리자 권한으로 본인 조회는 가능).

---

### [중간] 8. Set user default columns (PUT /rest/api/3/user/columns)

## 기본 정보

- **기능:** 사용자의 기본 이슈 테이블 컬럼을 설정한다.
- **Endpoint:** `PUT /rest/api/3/user/columns`
- **인증:** Bearer Token 필요
- **권한:** 다른 사용자 컬럼 설정 시 *Administer Jira* global permission, 본인 컬럼 설정 시 Permission to access Jira

## 설명

`accountId`를 지정하지 않으면 호출자 본인의 기본 컬럼을 설정하며, 컬럼 값을 보내지 않으면 모든 기본 컬럼이 제거된다. 파라미터는 HTML form data 형식으로 전달된다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| accountId | string | No | - | 사용자 계정 ID (미지정 시 호출자 본인) | `5b10ac8d82e05b22cc7d4ef5` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| columns | string[] | No | - | 설정할 이슈 테이블 컬럼 값 목록 (form data, `columns` 파라미터 반복) | `["summary", "description"]` |

```json
{
  "columns": ["summary", "description"]
}
```

## Response

### `200 OK`

응답 스키마가 `any`로 정의되어 있으며 구체적인 필드는 문서에 명시되어 있지 않다.

```json
{}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 누락/오류 | 인증 토큰 확인 |
| 403 | - | 권한 없음 또는 본인 레코드가 아님 | 권한/accountId 확인 |
| 404 | - | 요청한 사용자를 찾을 수 없음 | accountId 검증 |
| 429 | - | Rate limit 초과 (사용자 검색 엔드포인트는 테넌트 단위로 rate limit 공유) | `Retry-After` 헤더를 준수하여 재시도 |
| 500 | - | 잘못된 이슈 테이블 컬럼 ID 전송 | 컬럼 값 검증 |

## 주의 사항

- 요청은 JSON이 아닌 HTML form data 형식으로 전달해야 한다. 예: `curl -X PUT -d columns=summary -d columns=description '.../user/columns?accountId=...'`
- 컬럼 값을 하나도 보내지 않으면 모든 기본 컬럼이 제거된다.

---

### [중간] 9. Reset user default columns (DELETE /rest/api/3/user/columns)

## 기본 정보

- **기능:** 사용자의 기본 이슈 테이블 컬럼을 시스템 기본값으로 초기화한다.
- **Endpoint:** `DELETE /rest/api/3/user/columns`
- **인증:** Bearer Token 필요
- **권한:** 다른 사용자 컬럼 초기화 시 *Administer Jira* global permission, 본인 컬럼 초기화 시 Permission to access Jira

## 설명

`accountId`를 지정하지 않으면 호출자 본인의 기본 컬럼을 시스템 기본값으로 리셋한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| accountId | string | No | - | 사용자 계정 ID (미지정 시 호출자 본인) | `5b10ac8d82e05b22cc7d4ef5` |
| username | string | No | - | deprecated | - |

## Response

### `204 No Content`

응답 본문 없음.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 누락/오류 | 인증 토큰 확인 |
| 403 | - | 권한 없음 또는 본인 레코드가 아님 | 권한/accountId 확인 |

## 주의 사항

- 성공 시 응답 본문 없이 204만 반환된다.

---

### [중간] 10. Get user email (GET /rest/api/3/user/email)

## 기본 정보

- **기능:** 사용자의 프로필 공개 설정과 무관하게 이메일 주소를 조회한다.
- **Endpoint:** `GET /rest/api/3/user/email`
- **인증:** Bearer Token 필요 (단, Connect/Forge 앱 전용 API 성격이 강함)
- **권한:** 문서에 별도 Jira 권한 명시 없음 (단 Connect 앱은 Atlassian 승인 필요, Forge 앱은 asApp() 요청만 지원)

## 설명

일반 사용자 컨텍스트로는 호출이 제한되며(401), 승인된 Connect 앱 또는 asApp() 방식의 Forge 앱에서만 사용 가능하다. 통합 알림에서 이메일로 사용자에게 알림을 보내야 할 때 유용하지만 접근 제약이 있어 핵심 흐름으로 보기는 어렵다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---|---:|---|---|
| accountId | string | Yes | - | 사용자 계정 ID | `5b10ac8d82e05b22cc7d4ef5` |

## Response

### `200 OK`

```json
"name@example.com"
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 호출 앱이 이 API 사용을 승인받지 않음 | Atlassian 승인 절차 확인 |
| 401 | - | 인증 정보 누락/오류 (일반 사용자가 접근 시도하는 경우 포함) | 앱 인증 방식 확인 |
| 404 | - | 해당 accountId의 사용자가 존재하지 않음 | accountId 검증 |
| 503 | - | API가 현재 비활성화됨 | 재시도 또는 상태 확인 |

## 주의 사항

- Connect 앱은 Atlassian의 별도 승인이 필요하고, Forge 앱은 `asApp()` 요청만 지원한다. 일반 사용자 인증으로는 401이 반환될 수 있다.

---

### [중간] 11. Get user email bulk (GET /rest/api/3/user/email/bulk)

## 기본 정보

- **기능:** 여러 사용자의 이메일 주소를 프로필 공개 설정과 무관하게 한 번에 조회한다.
- **Endpoint:** `GET /rest/api/3/user/email/bulk`
- **인증:** Bearer Token 필요 (Connect/Forge 앱 전용 API 성격)
- **권한:** 문서에 별도 Jira 권한 명시 없음 (Connect 앱은 Atlassian 승인 필요, Forge 앱은 asApp() 요청만 지원)

## 설명

`09-Get user email`의 벌크 버전으로, 여러 accountId에 대한 이메일을 한 번에 조회한다. 동일하게 앱 승인/인증 방식 제약이 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---|---:|---|---|
| accountId | array | Yes | - | 이메일을 조회할 사용자들의 accountId 목록 | `accountId=5b10ac8d82e05b22cc7d4ef5` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| accountId | string | 사용자 accountId | `5b10ac8d82e05b22cc7d4ef5` |
| email | string | 사용자 이메일 | `name@example.com` |

```json
{
  "accountId": "5b10ac8d82e05b22cc7d4ef5",
  "email": "name@example.com"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 호출 앱이 이 API 사용을 승인받지 않음 | Atlassian 승인 절차 확인 |
| 401 | - | 인증 정보 누락/오류 (일반 사용자가 접근 시도하는 경우 포함) | 앱 인증 방식 확인 |
| 503 | - | API가 현재 비활성화됨 | 재시도 또는 상태 확인 |

## 주의 사항

- Connect 앱은 Atlassian의 별도 승인이 필요하고, Forge 앱은 `asApp()` 요청만 지원한다.
