# To-Do Items API 명세

GitLab REST API의 To-Do Items 기능을 제공합니다. 사용자에게 할당된 이슈, Merge Request 등의 할일 항목을 조회, 생성, 완료 처리할 수 있습니다.

---

## 1. Create a to-do item for an issuable

### 기본 정보

- **기능:** 특정 issuable(현재는 Merge Request)에 대해 현재 사용자의 to-do item을 생성합니다. 이미 존재하는 경우 `304`를 반환합니다.
- **Endpoint:** `POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/todo`
- **인증:** Personal Access Token 필요
- **권한:** `read_api` 또는 `api`
- **멱등성:** 미지원 (중복 요청 시 304)

### 설명

지정한 프로젝트의 Merge Request에 대해 현재 사용자의 to-do item을 생성합니다. 동일한 issuable에 대한 to-do item이 이미 존재하면 `304`를 반환하며 새로 생성하지 않습니다.

### Request

**Headers**

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | Personal Access Token | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

**Path Parameters**

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `string` | Y | 프로젝트의 ID 또는 URL-encoded 경로 |
| `merge_request_iid` | `integer` | Y | Merge Request의 내부 ID (IID) |

### Response

**`201 Created`**

| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | To-do item 고유 ID |
| `project` | `object` | 프로젝트 정보 (`id`, `description`, `name`, `name_with_namespace`, `path`, `path_with_namespace`, `created_at`) |
| `group` | `object` | 그룹 정보 (`id`, `name`, `path`, `kind`, `full_path`, `parent_id`, `avatar_url`, `web_url`) |
| `author` | `object` | 작성자 정보 (`id`, `username`, `public_email`, `name`, `state`, `locked`, `avatar_url`, `avatar_path`, `custom_attributes`, `web_url`) |
| `action_name` | `string` | to-do action 이름 |
| `target_type` | `string` | 대상 객체 타입 (예: `MergeRequest`) |
| `target` | `object` | 대상 객체 상세 |
| `target_url` | `string` | 대상 객체 URL |
| `body` | `string` | 본문 내용 |
| `state` | `string` | 상태 (`pending` 또는 `done`) |
| `created_at` | `string` | 생성 시간 (ISO 8601) |
| `updated_at` | `string` | 수정 시간 (ISO 8601) |

**`304 Not Modified`** — 동일한 to-do item이 이미 존재할 때 반환 (본문 없음)

### Errors

| 상태 코드 | 의미 |
|---:|---|
| `400` | Bad Request — 요청 파라미터가 유효하지 않음 |
| `404` | Not Found — 프로젝트 또는 Merge Request를 찾을 수 없음 |
| `401` | Unauthorized — 인증 정보가 유효하지 않음 |
| `403` | Forbidden — 권한 부족 |

---

## 2. List all to-do items

### 기본 정보

- **기능:** 현재 사용자의 모든 to-do item을 페이징하여 조회합니다. 필터를 적용하여 특정 조건의 항목만 조회할 수 있습니다.
- **Endpoint:** `GET /api/v4/todos`
- **인증:** Personal Access Token 필요
- **권한:** `read_api` 또는 `api`
- **멱등성:** GET이므로 멱등

### 설명

필터를 적용하지 않으면 현재 사용자의 모든 pending to-do item을 반환합니다. `action`, `author_id`, `project_id`, `group_id`, `state`, `type` 등의 필터로 결과를 좁힐 수 있습니다.

### Request

**Headers**

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | Personal Access Token | `Bearer {accessToken}` |

**Query Parameters**

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `page` | `integer` | N | 현재 페이지 번호 (기본값: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본값: 20) |
| `action` | `string` | N | 필터링할 action (예: `assigned`, `mentioned`) |
| `author_id` | `integer` | N | 작성자 ID로 필터링 |
| `project_id` | `integer` | N | 프로젝트 ID로 필터링 |
| `group_id` | `integer` | N | 그룹 ID로 필터링 |
| `state` | `string` | N | 상태로 필터링 (`pending` 또는 `done`) |
| `type` | `string` | N | to-do 타입으로 필터링 (예: `MergeRequest`, `Issue`) |

### Response

**`200 OK`**

응답 본문은 to-do item 객체의 배열입니다. 각 객체의 스키마는 Create endpoint와 동일합니다.

| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | To-do item 고유 ID |
| `project` | `object` | 프로젝트 정보 |
| `group` | `object` | 그룹 정보 |
| `author` | `object` | 작성자 정보 |
| `action_name` | `string` | to-do action 이름 |
| `target_type` | `string` | 대상 객체 타입 |
| `target` | `object` | 대상 객체 상세 |
| `target_url` | `string` | 대상 객체 URL |
| `body` | `string` | 본문 내용 |
| `state` | `string` | 상태 (`pending` 또는 `done`) |
| `created_at` | `string` | 생성 시간 (ISO 8601) |
| `updated_at` | `string` | 수정 시간 (ISO 8601) |

### Errors

| 상태 코드 | 의미 |
|---:|---|
| `400` | Bad Request — 쿼리 파라미터가 유효하지 않음 |
| `401` | Unauthorized — 인증 정보가 유효하지 않음 |
| `403` | Forbidden — 권한 부족 |

---

## 3. Mark a to-do item as done

### 기본 정보

- **기능:** 특정 to-do item을 완료(done) 상태로 변경합니다.
- **Endpoint:** `POST /api/v4/todos/{id}/mark_as_done`
- **인증:** Personal Access Token 필요
- **권한:** `read_api` 또는 `api`
- **멱등성:** 미지원

### 설명

지정한 ID의 to-do item을 현재 사용자에 대해 완료 처리합니다.

### Request

**Headers**

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | Personal Access Token | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

**Path Parameters**

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `integer` | Y | 완료 처리할 to-do item의 ID |

### Response

**`201 Created`**

응답 스키마는 완료 처리된 to-do item 객체입니다. (Create endpoint와 동일한 스키마)

| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | To-do item 고유 ID |
| `project` | `object` | 프로젝트 정보 |
| `group` | `object` | 그룹 정보 |
| `author` | `object` | 작성자 정보 |
| `action_name` | `string` | to-do action 이름 |
| `target_type` | `string` | 대상 객체 타입 |
| `target` | `object` | 대상 객체 상세 |
| `target_url` | `string` | 대상 객체 URL |
| `body` | `string` | 본문 내용 |
| `state` | `string` | 상태 (`done`) |
| `created_at` | `string` | 생성 시간 (ISO 8601) |
| `updated_at` | `string` | 수정 시간 (ISO 8601) |

### Errors

| 상태 코드 | 의미 |
|---:|---|
| `400` | Bad Request — 요청이 유효하지 않음 |
| `404` | Not Found — to-do item을 찾을 수 없음 |
| `401` | Unauthorized — 인증 정보가 유효하지 않음 |
| `403` | Forbidden — 권한 부족 |

---

## 4. Mark all to-do items as done

### 기본 정보

- **기능:** 현재 사용자의 모든 pending to-do item을 일괄 완료(done) 처리합니다.
- **Endpoint:** `POST /api/v4/todos/mark_as_done`
- **인증:** Personal Access Token 필요
- **권한:** `read_api` 또는 `api`
- **멱등성:** 미지원

### 설명

현재 사용자의 모든 pending to-do item을 한 번에 완료 처리합니다. 성공 시 본문 없이 `204 No Content`를 반환합니다.

### Request

**Headers**

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | Personal Access Token | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Response

**`204 No Content`** — 성공적으로 모든 to-do item을 완료 처리함 (응답 본문 없음)

### Errors

| 상태 코드 | 의미 |
|---:|---|
| `400` | Bad Request — 요청이 유효하지 않음 |
| `401` | Unauthorized — 인증 정보가 유효하지 않음 |
| `403` | Forbidden — 권한 부족 |
