# GitLab REST API — 91-members

---

## 1. List all direct members of a group

## 기본 정보

- **기능:** 지정된 그룹의 직접(direct) 멤버 목록을 조회한다. 상위 그룹이나 초대된 그룹으로부터 상속된 멤버는 포함하지 않는다.
- **Endpoint:** `GET /api/v4/groups/{id}/members`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** GET은 멱등

## 설명

인증된 사용자가 볼 수 있는 지정 그룹의 직접 멤버만 반환한다. 상속 멤버나 초대된 그룹의 멤버는 제외된다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|:---|
| `id` | `string` | Y | 그룹 ID |

### Query parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|:---|
| `query` | `string` | N | 멤버 검색어 |
| `user_ids` | `array` | N | 조회할 사용자 ID 배열 |
| `skip_users` | `array` | N | 건너뛸 사용자 ID 배열 |
| `show_seat_info` | `boolean` | N | 시트 정보 표시 여부 |
| `with_saml_identity` | `boolean` | N | SAML ID 연결된 멤버만 조회 |
| `page` | `integer` | N | 페이지 번호 (기본값: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본값: 20) |

## Response

### `200 OK`

| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 멤버 ID |
| `username` | `string` | 사용자명 |
| `public_email` | `string` | 공개 이메일 |
| `name` | `string` | 이름 |
| `state` | `string` | 계정 상태 (`active`, `blocked` 등) |
| `locked` | `boolean` | 계정 잠김 여부 |
| `avatar_url` | `string` | 아바타 URL |
| `avatar_path` | `string` | 아바타 경로 |
| `custom_attributes` | `array` | 커스텀 속성 목록 (`key` / `value`) |
| `web_url` | `string` | 프로필 URL |
| `access_level` | `string` | 접근 수준 |
| `created_at` | `string` (datetime) | 생성 일시 |
| `created_by` | `object` | 생성자 정보 (id, username, name, web_url 등) |
| `expires_at` | `string` (date) | 만료 일시 |
| `group_saml_identity` | `object` | Group SAML ID (`provider`, `extern_uid`, `saml_provider_id`) |
| `group_scim_identity` | `object` | Group SCIM ID (`extern_uid`, `group_id`, `active`) |
| `email` | `string` | 이메일 |
| `is_using_seat` | `string` | 시트 사용 여부 |
| `override` | `string` | override 여부 |
| `membership_state` | `string` | 멤버십 상태 |
| `member_role` | `object` | 멤버 역할 상세 (id, group_id, name, description, base_access_level 및 각 권한 boolean 필드) |

## Errors

| 상태 코드 | 설명 |
|---:|:---|
| `400 Bad Request` | 요청 파라미터가 잘못됨 |
| `401 Unauthorized` | 인증 실패 또는 토큰 없음 |
| `403 Forbidden` | 권한 부족 (`read_api` 없음) |
| `404 Not Found` | 그룹을 찾을 수 없음 |

---

## 2. List all members of a group

## 기본 정보

- **기능:** 지정된 그룹의 모든 멤버 목록을 조회한다. 상위 그룹이나 초대된 그룹으로부터 상속된 멤버도 포함한다.
- **Endpoint:** `GET /api/v4/groups/{id}/members/all`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** GET은 멱등

## 설명

인증된 사용자가 볼 수 있는 그룹의 모든 멤버(직접 + 상속)를 반환한다. 사용자가 현재 그룹과 하나 이상의 상위 그룹에 모두 속한 경우 가장 높은 `access_level`만 반환한다. 초대된 그룹의 멤버는 초대된 그룹이 공개이거나, 요청자가 해당 그룹의 멤버이거나, 공유된 그룹/프로젝트의 멤버인 경우에만 반환된다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|:---|
| `id` | `string` | Y | 그룹 ID |

### Query parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|:---|
| `query` | `string` | N | 멤버 검색어 |
| `user_ids` | `array` | N | 조회할 사용자 ID 배열 |
| `show_seat_info` | `boolean` | N | 시트 정보 표시 여부 |
| `state` | `string` | N | 멤버 상태 필터 |
| `page` | `integer` | N | 페이지 번호 (기본값: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본값: 20) |

## Response

### `200 OK`

응답 스키마는 "List all direct members of a group"과 동일하다.

| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 멤버 ID |
| `username` | `string` | 사용자명 |
| `public_email` | `string` | 공개 이메일 |
| `name` | `string` | 이름 |
| `state` | `string` | 계정 상태 |
| `locked` | `boolean` | 계정 잠김 여부 |
| `avatar_url` | `string` | 아바타 URL |
| `avatar_path` | `string` | 아바타 경로 |
| `custom_attributes` | `array` | 커스텀 속성 목록 (`key` / `value`) |
| `web_url` | `string` | 프로필 URL |
| `access_level` | `string` | 접근 수준 (상속 시 최고 수준) |
| `created_at` | `string` (datetime) | 생성 일시 |
| `created_by` | `object` | 생성자 정보 |
| `expires_at` | `string` (date) | 만료 일시 |
| `group_saml_identity` | `object` | Group SAML ID |
| `group_scim_identity` | `object` | Group SCIM ID |
| `email` | `string` | 이메일 |
| `is_using_seat` | `string` | 시트 사용 여부 |
| `override` | `string` | override 여부 |
| `membership_state` | `string` | 멤버십 상태 |
| `member_role` | `object` | 멤버 역할 상세 |

## Errors

| 상태 코드 | 설명 |
|---:|:---|
| `400 Bad Request` | 요청 파라미터가 잘못됨 |
| `401 Unauthorized` | 인증 실패 또는 토큰 없음 |
| `403 Forbidden` | 권한 부족 (`read_api` 없음) |
| `404 Not Found` | 그룹을 찾을 수 없음 |

---

## 3. List all direct members of a project

## 기본 정보

- **기능:** 지정된 프로젝트의 직접(direct) 멤버 목록을 조회한다. 상위 그룹이나 초대된 그룹으로부터 상속된 멤버는 포함하지 않는다.
- **Endpoint:** `GET /api/v4/projects/{id}/members`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** GET은 멱등

## 설명

인증된 사용자가 볼 수 있는 지정 프로젝트의 직접 멤버만 반환한다. 상속 멤버나 초대된 그룹의 멤버는 제외된다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|:---|
| `id` | `string` | Y | 프로젝트 ID |

### Query parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|:---|
| `query` | `string` | N | 멤버 검색어 |
| `user_ids` | `array` | N | 조회할 사용자 ID 배열 |
| `skip_users` | `array` | N | 건너뛸 사용자 ID 배열 |
| `show_seat_info` | `boolean` | N | 시트 정보 표시 여부 |
| `with_saml_identity` | `boolean` | N | SAML ID 연결된 멤버만 조회 |
| `page` | `integer` | N | 페이지 번호 (기본값: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본값: 20) |

## Response

### `200 OK`

응답 스키마는 "List all direct members of a group"과 동일한 `Member` 객체 배열이다.

| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 멤버 ID |
| `username` | `string` | 사용자명 |
| `public_email` | `string` | 공개 이메일 |
| `name` | `string` | 이름 |
| `state` | `string` | 계정 상태 |
| `locked` | `boolean` | 계정 잠김 여부 |
| `avatar_url` | `string` | 아바타 URL |
| `avatar_path` | `string` | 아바타 경로 |
| `custom_attributes` | `array` | 커스텀 속성 목록 |
| `web_url` | `string` | 프로필 URL |
| `access_level` | `string` | 접근 수준 |
| `created_at` | `string` (datetime) | 생성 일시 |
| `created_by` | `object` | 생성자 정보 |
| `expires_at` | `string` (date) | 만료 일시 |
| `group_saml_identity` | `object` | Group SAML ID |
| `group_scim_identity` | `object` | Group SCIM ID |
| `email` | `string` | 이메일 |
| `is_using_seat` | `string` | 시트 사용 여부 |
| `override` | `string` | override 여부 |
| `membership_state` | `string` | 멤버십 상태 |
| `member_role` | `object` | 멤버 역할 상세 |

## Errors

| 상태 코드 | 설명 |
|---:|:---|
| `400 Bad Request` | 요청 파라미터가 잘못됨 |
| `401 Unauthorized` | 인증 실패 또는 토큰 없음 |
| `403 Forbidden` | 권한 부족 (`read_api` 없음) |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |

---

## 4. List all members of a project

## 기본 정보

- **기능:** 지정된 프로젝트의 모든 멤버 목록을 조회한다. 상위 그룹이나 초대된 그룹으로부터 상속된 멤버도 포함한다.
- **Endpoint:** `GET /api/v4/projects/{id}/members/all`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** GET은 멱등

## 설명

인증된 사용자가 볼 수 있는 프로젝트의 모든 멤버(직접 + 상속)를 반환한다. 사용자가 현재 프로젝트와 하나 이상의 상위 그룹에 모두 속한 경우 가장 높은 `access_level`만 반환한다. 초대된 그룹의 멤버는 초대된 그룹이 공개이거나, 요청자가 해당 그룹의 멤버이거나, 공유된 그룹/프로젝트의 멤버인 경우에만 반환된다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|:---|
| `id` | `string` | Y | 프로젝트 ID |

### Query parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|:---|
| `query` | `string` | N | 멤버 검색어 |
| `user_ids` | `array` | N | 조회할 사용자 ID 배열 |
| `show_seat_info` | `boolean` | N | 시트 정보 표시 여부 |
| `state` | `string` | N | 멤버 상태 필터 |
| `page` | `integer` | N | 페이지 번호 (기본값: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본값: 20) |

## Response

### `200 OK`

응답 스키마는 위 endpoint들과 동일한 `Member` 객체 배열이다.

| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 멤버 ID |
| `username` | `string` | 사용자명 |
| `public_email` | `string` | 공개 이메일 |
| `name` | `string` | 이름 |
| `state` | `string` | 계정 상태 |
| `locked` | `boolean` | 계정 잠김 여부 |
| `avatar_url` | `string` | 아바타 URL |
| `avatar_path` | `string` | 아바타 경로 |
| `custom_attributes` | `array` | 커스텀 속성 목록 |
| `web_url` | `string` | 프로필 URL |
| `access_level` | `string` | 접근 수준 (상속 시 최고 수준) |
| `created_at` | `string` (datetime) | 생성 일시 |
| `created_by` | `object` | 생성자 정보 |
| `expires_at` | `string` (date) | 만료 일시 |
| `group_saml_identity` | `object` | Group SAML ID |
| `group_scim_identity` | `object` | Group SCIM ID |
| `email` | `string` | 이메일 |
| `is_using_seat` | `string` | 시트 사용 여부 |
| `override` | `string` | override 여부 |
| `membership_state` | `string` | 멤버십 상태 |
| `member_role` | `object` | 멤버 역할 상세 |

## Errors

| 상태 코드 | 설명 |
|---:|:---|
| `400 Bad Request` | 요청 파라미터가 잘못됨 |
| `401 Unauthorized` | 인증 실패 또는 토큰 없음 |
| `403 Forbidden` | 권한 부족 (`read_api` 없음) |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |
