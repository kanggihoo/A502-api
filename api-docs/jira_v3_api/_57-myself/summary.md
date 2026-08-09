# _57-myself API 요약

이 리소스 그룹(`Myself`)은 현재 인증된 사용자 본인의 기본 정보, 환경설정(preferences), 로케일(locale)을 조회·생성·수정·삭제(기본값 복원)하는 API 모음이다. 제외된 API는 없다.

## 제외된 API

없음 (모든 엔드포인트가 "Permission to access Jira" 수준이거나 인증 불필요이며, 사이트 전체 관리자 권한을 요구하지 않는다.)

---

### [높음] 1. Get current user (GET /rest/api/3/myself)

## 기본 정보

- **기능:** 현재 인증된 사용자(본인)의 상세 정보 조회
- **Endpoint:** `GET /rest/api/3/myself`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** Jira 접근 권한 (Permission to access Jira)

## 설명

현재 로그인한 사용자의 accountId, 표시 이름, 이메일, 아바타, 그룹, 애플리케이션 역할, 타임존 등 상세 정보를 반환한다. `expand` 쿼리 파라미터로 그룹 및 애플리케이션 역할 정보를 추가로 포함할 수 있다. 팀 생성 자동화 시 현재 사용자의 accountId를 식별하거나, 통합 대시보드에서 로그인 사용자 정보를 표시할 때 핵심적으로 사용된다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | No | - | 쉼표로 구분된 목록. `groups`(중첩 그룹 포함 모든 그룹), `applicationRoles`(할당된 애플리케이션 역할) 확장 가능 | `groups,applicationRoles` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `accountId` | string | 사용자 계정 ID | `5b10a2844c20165700ede21g` |
| `accountType` | string | 계정 타입 | `atlassian` |
| `active` | boolean | 활성 사용자 여부 | `true` |
| `applicationRoles` | object | 할당된 애플리케이션 역할 목록(size 포함) | `{"items":[],"size":1}` |
| `avatarUrls` | object | 크기별 아바타 URL | `{"48x48":"https://..."}` |
| `displayName` | string | 표시 이름 | `Mia Krystof` |
| `emailAddress` | string | 이메일 주소 | `mia@example.com` |
| `groups` | object | 소속 그룹 목록(size 포함) | `{"items":[],"size":3}` |
| `self` | string | 사용자 리소스 URL | `https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g` |
| `timeZone` | string | 타임존 | `Australia/Sydney` |

```json
{
  "accountId": "5b10a2844c20165700ede21g",
  "accountType": "atlassian",
  "active": true,
  "applicationRoles": { "items": [], "size": 1 },
  "avatarUrls": {
    "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16",
    "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24",
    "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32",
    "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48"
  },
  "displayName": "Mia Krystof",
  "emailAddress": "mia@example.com",
  "groups": { "items": [], "size": 3 },
  "key": "",
  "name": "",
  "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g",
  "timeZone": "Australia/Sydney"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 후 재요청 |

## 주의 사항

- `expand=groups`는 중첩 그룹까지 포함하므로 대규모 조직에서는 응답이 커질 수 있다.

---

### [중간] 2. Get preference (GET /rest/api/3/mypreferences)

## 기본 정보

- **기능:** 현재 사용자의 특정 환경설정(preference) 값 조회
- **Endpoint:** `GET /rest/api/3/mypreferences`
- **인증:** Bearer Token 필요
- **권한:** Jira 접근 권한 (Permission to access Jira)

## 설명

`key` 쿼리 파라미터로 지정한 사용자 preference의 값을 문자열로 반환한다. `jira.user.locale`, `jira.user.timezone` 키는 더 이상 사용되지 않으며(deprecated), `user.notifications.*` 계열 키도 2024-07-15부로 알림 동작에 영향을 주지 않게 될 예정이다. 타임존/로케일 관리는 사용자 관리 REST API의 프로필 수정 엔드포인트 사용을 권장한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `key` | string | Yes | - | 조회할 preference의 키 | `user.notifications.mimetype` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| (body) | string | preference의 값 | `"html"` |

```json
"html"
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 후 재요청 |
| 404 | - | `key`가 제공되지 않았거나 존재하지 않음 | 올바른 key 값 지정 |

## 주의 사항

- `jira.user.locale`, `jira.user.timezone`, `user.notifications.watcher/assignee/reporter/mentions` 키는 deprecated 상태이다.

---

### [중간] 3. Set preference (PUT /rest/api/3/mypreferences)

## 기본 정보

- **기능:** 현재 사용자의 preference 생성 또는 값 수정
- **Endpoint:** `PUT /rest/api/3/mypreferences`
- **인증:** Bearer Token 필요
- **권한:** Jira 접근 권한 (Permission to access Jira)

## 설명

일반 텍스트 문자열 값으로 preference를 생성하거나 갱신한다. 임의의 preference는 최대 255자까지 값으로 가질 수 있다. `user.notifications.mimetype`, `user.default.share.private`, `user.keyboard.shortcuts.disabled`, `user.autowatch.disabled`, `user.notifiy.own.changes` 등 시스템 정의 키를 설정할 수 있으며, 로케일/타임존 관련 키는 deprecated 상태이다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `key` | string | Yes | - | 설정할 preference의 키 (최대 255자) | `user.notifications.mimetype` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| (body) | string | Yes | 최대 255자 | preference 값(plain text) | `"false"` |

```json
"false"
```

## Response

### `204 No Content`

응답 본문 없음(성공 시).

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 후 재요청 |
| 404 | - | `key` 또는 값이 제공되지 않았거나 유효하지 않음 | key/value 확인 후 재요청 |

## 주의 사항

- `jira.user.locale`, `jira.user.timezone` 키는 deprecated이며, 로케일/타임존은 사용자 관리 REST API의 프로필 수정 엔드포인트 사용 권장.

---

### [중간] 4. Delete preference (DELETE /rest/api/3/mypreferences)

## 기본 정보

- **기능:** 현재 사용자의 preference 삭제(시스템 정의 설정의 기본값 복원)
- **Endpoint:** `DELETE /rest/api/3/mypreferences`
- **인증:** Bearer Token 필요
- **권한:** Jira 접근 권한 (Permission to access Jira)

## 설명

지정한 키의 preference를 삭제하여 시스템 정의 설정값의 경우 기본값으로 복원한다. 로케일/타임존 관련 키는 deprecated 상태이며 사용자 관리 REST API 사용을 권장한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `key` | string | Yes | - | 삭제할 preference의 키 | `user.notifications.mimetype` |

## Response

### `204 No Content`

응답 본문 없음(성공 시).

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 후 재요청 |
| 404 | - | `key`가 제공되지 않았거나 존재하지 않음 | 올바른 key 값 지정 |

## 주의 사항

- `jira.user.locale`, `jira.user.timezone` 키는 deprecated 상태이다.

---

### [중간] 5. Get locale (GET /rest/api/3/mypreferences/locale)

## 기본 정보

- **기능:** 현재 사용자의 로케일 조회
- **Endpoint:** `GET /rest/api/3/mypreferences/locale`
- **인증:** 불필요(익명 접근 가능)
- **권한:** 없음

## 설명

사용자의 언어 preference를 반환한다. 사용자가 언어 설정을 하지 않았거나(기본값) 익명으로 접근한 경우, `Accept-Language` 헤더로 감지된 브라우저 로케일을 반환하며, 이 로케일이 Jira에서 지원되지 않으면 사이트 기본 로케일을 반환한다. 익명 접근이 가능한 몇 안 되는 엔드포인트 중 하나다.

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `locale` | string | 로케일 코드 | `en_US` |

```json
{ "locale": "en_US" }
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 있으나 잘못됨 | 인증 토큰 확인 후 재요청 |

## 주의 사항

- 익명 접근이 가능한 엔드포인트이다.

---

### [중간] 6. Set locale (PUT /rest/api/3/mypreferences/locale)

## 기본 정보

- **기능:** 현재 사용자의 로케일 설정 (Deprecated)
- **Endpoint:** `PUT /rest/api/3/mypreferences/locale`
- **인증:** Bearer Token 필요
- **권한:** Jira 접근 권한 (Permission to access Jira)

## 설명

사용자의 로케일을 설정한다. Jira 인스턴스가 지원하는 로케일이어야 한다. 이 엔드포인트는 Deprecated 상태이며, 사용자 관리 REST API의 프로필 수정 엔드포인트 사용이 권장된다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `locale` | string | Yes(생성 시 필수) | ISO 639 언어코드 + `_` + ISO 3166 국가코드 형식 | 로케일 코드 | `en_US` |

```json
{
  "locale": "en_US"
}
```

## Response

### `204 No Content`

응답 본문 없음(성공 시).

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 요청 body 형식 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 후 재요청 |

## 주의 사항

- Deprecated된 엔드포인트로, 사용자 관리 REST API의 프로필 수정(patch) 엔드포인트 사용을 권장.
