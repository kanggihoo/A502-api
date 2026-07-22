# 162 - Users API Specification

---

## 1. List all users

### 기본 정보

- **기능:** GitLab 인스턴스에 등록된 모든 사용자 목록을 조회한다.
- **Endpoint:** `GET /api/v4/users`
- **인증:** Bearer Token 필요
- **권한:** `read_api` 또는 `read_user`
- **멱등성:** GET은 멱등

### 설명

인스턴스의 모든 사용자를 페이징하여 반환한다. GitLab 17.0부터 기본적으로 keyset pagination을 사용한다. 특정 username, public_email, 외부 인증 제공자 UID로 단일 사용자를 조회하거나, `search`, `active`, `blocked`, `external` 등 다양한 필터로 목록을 좁힐 수 있다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Query parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `username` | `string` | N | 특정 username으로 단일 사용자 조회 |
| `extern_uid` | `string` | N | 외부 인증 제공자 UID로 단일 사용자 조회 |
| `public_email` | `string` | N | 특정 public email로 단일 사용자 조회 |
| `provider` | `string` | N | 외부 제공자명 |
| `search` | `string` | N | username 검색 |
| `active` | `boolean` | N | 활성 사용자만 필터 |
| `humans` | `boolean` | N | 사람 사용자만 필터 |
| `external` | `boolean` | N | 외부 사용자만 필터 |
| `blocked` | `boolean` | N | 차단된 사용자만 필터 |
| `created_after` | `string` | N | 지정 시간 이후 생성된 사용자 |
| `created_before` | `string` | N | 지정 시간 이전 생성된 사용자 |
| `without_projects` | `boolean` | N | 프로젝트가 없는 사용자만 필터 |
| `without_project_bots` | `boolean` | N | 프로젝트 봇 제외 |
| `admins` | `boolean` | N | 관리자만 필터 |
| `two_factor` | `string` | N | 2FA 사용 여부로 필터 |
| `exclude_active` | `boolean` | N | 비활성 사용자만 필터 |
| `exclude_external` | `boolean` | N | 내부 사용자만 필터 |
| `exclude_humans` | `boolean` | N | 비사람 사용자만 필터 |
| `exclude_internal` | `boolean` | N | 내부 사용자 제외 |
| `order_by` | `string` | N | 정렬 기준 필드 |
| `sort` | `string` | N | 오름차순/내림차순 정렬 |
| `page` | `integer` | N | 페이지 번호 |
| `per_page` | `integer` | N | 페이지당 항목 수 |
| `with_custom_attributes` | `boolean` | N | 응답에 custom attributes 포함 |
| `custom_attributes` | `object` | N | custom attributes로 필터 |
| `skip_ldap` | `boolean` | N | LDAP 사용자 제외 |
| `auditors` | `boolean` | N | 감사자(auditor) 사용자만 필터 |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 사용자 ID |
| `username` | `string` | 사용자명 |
| `public_email` | `string` | 공개 이메일 |
| `name` | `string` | 표시 이름 |
| `state` | `string` | 계정 상태 (active, blocked 등) |
| `locked` | `boolean` | 계정 잠금 여부 |
| `avatar_url` | `string` | 아바타 URL |
| `avatar_path` | `string` | 아바타 경로 |
| `custom_attributes` | `array` | 커스텀 속성 목록 (`key`, `value`) |
| `web_url` | `string` | 사용자 프로필 URL |

### Errors

| 상태 코드 | 설명 |
|---:|---|
| `400 Bad Request` | 요청 파라미터가 잘못됨 |

---

## 2. Retrieve a user as a regular user

### 기본 정보

- **기능:** 특정 사용자의 공개 프로필 정보를 일반 사용자 권한으로 조회한다.
- **Endpoint:** `GET /api/v4/users/{id}`
- **인증:** Bearer Token 필요
- **권한:** `read_api` 또는 `read_user`
- **멱등성:** GET은 멱등

### 설명

지정된 `id`의 사용자 상세 정보를 반환한다. list all users API보다 더 많은 필드(bio, location, linkedin, twitter, discord, github, job_title, followers 등)를 포함한다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `integer` | Y | 조회할 사용자 ID |

#### Query parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `with_custom_attributes` | `boolean` | N | 응답에 custom attributes 포함 |
| `custom_attributes` | `object` | N | custom attributes로 필터 |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 사용자 ID |
| `username` | `string` | 사용자명 |
| `public_email` | `string` | 공개 이메일 |
| `name` | `string` | 표시 이름 |
| `state` | `string` | 계정 상태 |
| `locked` | `boolean` | 계정 잠금 여부 |
| `avatar_url` | `string` | 아바타 URL |
| `avatar_path` | `string` | 아바타 경로 |
| `custom_attributes` | `array` | 커스텀 속성 목록 (`key`, `value`) |
| `web_url` | `string` | 사용자 프로필 URL |
| `created_at` | `string` | 계정 생성일 |
| `bio` | `string` | 자기소개 |
| `location` | `string` | 위치 |
| `linkedin` | `string` | LinkedIn 사용자명 |
| `twitter` | `string` | Twitter 사용자명 |
| `discord` | `string` | Discord 사용자명 |
| `website_url` | `string` | 웹사이트 URL |
| `github` | `string` | GitHub 사용자명 |
| `job_title` | `string` | 직함 |
| `pronouns` | `string` | 대명사 |
| `organization` | `string` | 소속 조직 |
| `bot` | `boolean` | 봇 계정 여부 |
| `work_information` | `string` | 업무 정보 |
| `followers` | `string` | 팔로워 수 |
| `following` | `string` | 팔로잉 수 |
| `is_followed` | `string` | 현재 사용자의 팔로우 여부 |
| `local_time` | `string` | 사용자 현지 시간 |

### Errors

| 상태 코드 | 설명 |
|---:|---|
| `400 Bad Request` | 요청 파라미터가 잘못됨 |
| `404 Not Found` | 지정한 ID의 사용자가 존재하지 않음 |

---

## 3. Retrieve current user details

### 기본 정보

- **기능:** 현재 인증된 사용자 자신의 계정 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/user`
- **인증:** Bearer Token 필요
- **권한:** `read_api` 또는 `read_user`
- **멱등성:** GET은 멱등

### 설명

현재 액세스 토큰에 연결된 사용자의 전체 계정 정보를 반환한다. 일반 사용자 조회 API보다 더 많은 필드(email, confirmed_at, last_sign_in_at, theme_id, projects_limit, can_create_group, two_factor_enabled, private_profile, preferred_language, shared_runners_minutes_limit, identities, scim_identities 등)를 포함한다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 사용자 ID |
| `username` | `string` | 사용자명 |
| `public_email` | `string` | 공개 이메일 |
| `name` | `string` | 표시 이름 |
| `state` | `string` | 계정 상태 |
| `locked` | `boolean` | 계정 잠금 여부 |
| `avatar_url` | `string` | 아바타 URL |
| `avatar_path` | `string` | 아바타 경로 |
| `custom_attributes` | `array` | 커스텀 속성 목록 (`key`, `value`) |
| `web_url` | `string` | 사용자 프로필 URL |
| `created_at` | `string` | 계정 생성일 |
| `bio` | `string` | 자기소개 |
| `location` | `string` | 위치 |
| `linkedin` | `string` | LinkedIn 사용자명 |
| `twitter` | `string` | Twitter 사용자명 |
| `discord` | `string` | Discord 사용자명 |
| `website_url` | `string` | 웹사이트 URL |
| `github` | `string` | GitHub 사용자명 |
| `job_title` | `string` | 직함 |
| `pronouns` | `string` | 대명사 |
| `organization` | `string` | 소속 조직 |
| `bot` | `boolean` | 봇 계정 여부 |
| `work_information` | `string` | 업무 정보 |
| `followers` | `string` | 팔로워 수 |
| `following` | `string` | 팔로잉 수 |
| `is_followed` | `string` | 현재 사용자의 팔로우 여부 |
| `local_time` | `string` | 사용자 현지 시간 |
| `last_sign_in_at` | `string` | 마지막 로그인 시간 |
| `confirmed_at` | `string` | 이메일 확인 시간 |
| `last_activity_on` | `string` | 마지막 활동일 |
| `email` | `string` | 이메일 주소 |
| `theme_id` | `integer` | 테마 ID |
| `color_scheme_id` | `integer` | 컬러 스킴 ID |
| `projects_limit` | `integer` | 생성 가능한 최대 프로젝트 수 |
| `current_sign_in_at` | `string` | 현재 로그인 시간 |
| `identities` | `object` | 연결된 외부 인증 정보 (`provider`, `extern_uid`, `saml_provider_id`) |
| `can_create_group` | `boolean` | 그룹 생성 권한 여부 |
| `can_create_project` | `boolean` | 프로젝트 생성 권한 여부 |
| `two_factor_enabled` | `boolean` | 2FA 활성화 여부 |
| `external` | `boolean` | 외부 사용자 여부 |
| `private_profile` | `boolean` | 프로필 비공개 여부 |
| `commit_email` | `string` | 커밋에 사용되는 이메일 |
| `preferred_language` | `string` | 선호 언어 |
| `shared_runners_minutes_limit` | `string` | 공유 러너 분 제한 |
| `extra_shared_runners_minutes_limit` | `string` | 추가 공유 러너 분 제한 |
| `scim_identities` | `object` | SCIM 연결 정보 (`extern_uid`, `group_id`, `active`) |

### Errors

| 상태 코드 | 설명 |
|---:|---|
| `401 Unauthorized` | 유효하지 않거나 누락된 액세스 토큰 |
| `403 Forbidden` | 토큰에 충분한 권한이 없음 |

---

## 4. Retrieve your user status

### 기본 정보

- **기능:** 현재 인증된 사용자의 상태(emoji, 메시지, 가용성)를 조회한다.
- **Endpoint:** `GET /api/v4/user/status`
- **인증:** Bearer Token 필요
- **권한:** `read_api` 또는 `read_user`
- **멱등성:** GET은 멱등

### 설명

현재 사용자의 상태 정보를 반환한다. 설정된 emoji, 상태 메시지, 가용성(availability), 메시지 HTML 렌더링 결과, 자동 상태 초기화 시간을 포함한다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 |
|---|---:|---|
| `emoji` | `string` | 상태에 표시할 emoji 이름 |
| `message` | `string` | 상태 메시지 |
| `availability` | `string` | 가용성 상태 (busy 등) |
| `message_html` | `string` | 상태 메시지 HTML 렌더링 |
| `clear_status_at` | `string` | 상태가 자동 초기화되는 시간 |

### Errors

| 상태 코드 | 설명 |
|---:|---|
| `401 Unauthorized` | 유효하지 않거나 누락된 액세스 토큰 |
| `403 Forbidden` | 토큰에 충분한 권한이 없음 |
