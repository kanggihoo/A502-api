# 139 Resource Events API 명세

리소스(이슈, 머지 리퀘스트)에 발생한 이벤트(레이블 변경, 상태 변경, 반복 변경, 마일스톤 변경)를 조회하는 API 모음.

---

## 1. State Events (리소스 상태 변경 이벤트)

### 기본 정보
- **기능:** 이슈/MR의 상태(open, closed, reopened 등) 변경 이벤트 목록 조회
- **Endpoint:**
  - `GET /api/v4/projects/{id}/issues/{eventable_id}/resource_state_events`
  - `GET /api/v4/projects/{id}/merge_requests/{eventable_id}/resource_state_events`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
이슈 또는 머지 리퀘스트에 발생한 상태 변경 이벤트 목록을 반환한다. 각 이벤트는 변경을 수행한 사용자, 변경된 상태, 연결된 커밋/MR 정보를 포함한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | string | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |
| `eventable_id` | integer | Y | 이슈 IID (Issue) 또는 MR IID (Merge Request) |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---|---|
| `page` | integer | N | 현재 페이지 번호 (기본값: 1) | `1` |
| `per_page` | integer | N | 페이지당 항목 수 (기본값: 20) | `20` |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---|
| `id` | integer | 이벤트 ID | `1` |
| `user` | object | 이벤트를 발생시킨 사용자 | `{ id: 1, username: "root", name: "Administrator" }` |
| `user.id` | integer | 사용자 ID | `1` |
| `user.username` | string | 사용자명 | `"root"` |
| `user.public_email` | string | 공개 이메일 | `"admin@example.com"` |
| `user.name` | string | 이름 | `"Administrator"` |
| `user.state` | string | 사용자 상태 | `"active"` |
| `user.locked` | boolean | 계정 잠금 여부 | `false` |
| `user.avatar_url` | string | 아바타 URL | `"https://www.gravatar.com/avatar/..."` |
| `user.avatar_path` | string | 아바타 경로 | `null` |
| `user.custom_attributes` | array | 사용자 정의 속성 목록 | `[{ key: "department", value: "engineering" }]` |
| `user.web_url` | string | 사용자 프로필 URL | `"https://gitlab.example.com/root"` |
| `created_at` | string (datetime) | 이벤트 생성 시간 | `"2024-01-01T00:00:00.000Z"` |
| `resource_type` | string | 리소스 타입 | `"Issue"` |
| `resource_id` | integer | 리소스 ID | `10` |
| `source_commit` | string | 상태 변경을 트리거한 커밋 SHA | `"a1b2c3d4..."` |
| `source_merge_request_id` | integer | 상태 변경을 트리거한 MR ID | `5` |
| `state` | string | 변경된 상태 | `"closed"` |

## Errors
| HTTP 상태 | 코드 | 설명 | 처리 방법 |
|---:|---|---|---|
| `400` | `BAD_REQUEST` | 잘못된 요청 | 요청 파라미터 확인 |
| `401` | `UNAUTHENTICATED` | 토큰 없음 또는 만료 | 토큰 갱신 |
| `403` | `FORBIDDEN` | 권한 없음 | 권한 요청 |
| `404` | `NOT_FOUND` | 리소스 없음 | ID 확인 |

---

## 2. Label Events (리소스 레이블 변경 이벤트)

### 기본 정보
- **기능:** 이슈/MR에 부착된 레이블 변경(add/remove) 이벤트 목록 조회
- **Endpoint:**
  - `GET /api/v4/projects/{id}/issues/{eventable_id}/resource_label_events`
  - `GET /api/v4/projects/{id}/merge_requests/{eventable_id}/resource_label_events`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
이슈 또는 머지 리퀘스트에 발생한 레이블 추가/제거 이벤트 목록을 반환한다. 각 이벤트는 변경을 수행한 사용자, 변경된 레이블 정보, 수행된 액션(add/remove)을 포함한다. GitLab 11.3에서 도입되었다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | string | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |
| `eventable_id` | any | Y | 이슈 IID (Issue) 또는 MR IID (Merge Request) |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---|---|
| `page` | integer | N | 현재 페이지 번호 (기본값: 1) | `1` |
| `per_page` | integer | N | 페이지당 항목 수 (기본값: 20) | `20` |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---|
| `id` | integer | 이벤트 ID | `1` |
| `user` | object | 이벤트를 발생시킨 사용자 | `{ id: 1, username: "root" }` |
| `user.id` | integer | 사용자 ID | `1` |
| `user.username` | string | 사용자명 | `"root"` |
| `user.public_email` | string | 공개 이메일 | `"admin@example.com"` |
| `user.name` | string | 이름 | `"Administrator"` |
| `user.state` | string | 사용자 상태 | `"active"` |
| `user.locked` | boolean | 계정 잠금 여부 | `false` |
| `user.avatar_url` | string | 아바타 URL | `"https://www.gravatar.com/avatar/..."` |
| `user.avatar_path` | string | 아바타 경로 | `null` |
| `user.custom_attributes` | array | 사용자 정의 속성 목록 | `[{ key: "department", value: "engineering" }]` |
| `user.web_url` | string | 사용자 프로필 URL | `"https://gitlab.example.com/root"` |
| `created_at` | string (datetime) | 이벤트 생성 시간 | `"2024-01-01T00:00:00.000Z"` |
| `resource_type` | string | 리소스 타입 | `"Issue"` |
| `resource_id` | integer | 리소스 ID | `10` |
| `label` | object | 추가/제거된 레이블 정보 | `{ id: 1, name: "bug", color: "#FF0000" }` |
| `label.id` | integer | 레이블 ID | `1` |
| `label.name` | string | 레이블 이름 | `"bug"` |
| `label.description` | string | 레이블 설명 | `"Bug report"` |
| `label.text_color` | string | 텍스트 색상 | `"#FFFFFF"` |
| `label.description_html` | string | HTML 렌더링된 설명 | `"<p>Bug report</p>"` |
| `label.color` | string | 배경 색상 | `"#FF0000"` |
| `label.archived` | boolean | 보관 여부 | `false` |
| `action` | string | 수행된 액션 | `"add"` |

## Errors
| HTTP 상태 | 코드 | 설명 | 처리 방법 |
|---:|---|---|---|
| `400` | `BAD_REQUEST` | 잘못된 요청 | 요청 파라미터 확인 |
| `401` | `UNAUTHENTICATED` | 토큰 없음 또는 만료 | 토큰 갱신 |
| `403` | `FORBIDDEN` | 권한 없음 | 권한 요청 |
| `404` | `NOT_FOUND` | 리소스 없음 | ID 확인 |

---

## 3. Iteration Events (리소스 반복 변경 이벤트)

### 기본 정보
- **기능:** 이슈의 iteration(반복/스프린트) 변경 이벤트 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/issues/{eventable_id}/resource_iteration_events`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
이슈에 할당된 iteration이 변경될 때 발생하는 이벤트 목록을 반환한다. 각 이벤트는 변경을 수행한 사용자, 변경된 iteration 정보, 수행된 액션(add/remove)을 포함한다. GitLab 13.4에서 도입되었다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |
| `eventable_id` | any | Y | 이슈 IID |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---|---|
| `page` | integer | N | 현재 페이지 번호 (기본값: 1) | `1` |
| `per_page` | integer | N | 페이지당 항목 수 (기본값: 20) | `20` |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---|
| `id` | integer | 이벤트 ID | `1` |
| `user` | object | 이벤트를 발생시킨 사용자 | `{ id: 1, username: "root" }` |
| `user.id` | integer | 사용자 ID | `1` |
| `user.username` | string | 사용자명 | `"root"` |
| `user.public_email` | string | 공개 이메일 | `"admin@example.com"` |
| `user.name` | string | 이름 | `"Administrator"` |
| `user.state` | string | 사용자 상태 | `"active"` |
| `user.locked` | boolean | 계정 잠금 여부 | `false` |
| `user.avatar_url` | string | 아바타 URL | `"https://www.gravatar.com/avatar/..."` |
| `user.avatar_path` | string | 아바타 경로 | `null` |
| `user.custom_attributes` | array | 사용자 정의 속성 목록 | `[{ key: "department", value: "engineering" }]` |
| `user.web_url` | string | 사용자 프로필 URL | `"https://gitlab.example.com/root"` |
| `created_at` | string (datetime) | 이벤트 생성 시간 | `"2024-01-01T00:00:00.000Z"` |
| `resource_type` | string | 리소스 타입 | `"Issue"` |
| `resource_id` | integer | 리소스 ID | `10` |
| `iteration` | object | 변경된 iteration 정보 | `{ id: 1, title: "Sprint 1", start_date: "2024-01-01" }` |
| `iteration.id` | integer | iteration ID | `1` |
| `iteration.iid` | integer | iteration IID | `1` |
| `iteration.sequence` | integer | iteration 순서 번호 | `3` |
| `iteration.group_id` | integer | 그룹 ID | `1` |
| `iteration.title` | string | iteration 제목 | `"Sprint 1"` |
| `iteration.description` | string | iteration 설명 | `"First sprint"` |
| `iteration.state` | integer | iteration 상태 | `1` |
| `iteration.created_at` | string (datetime) | iteration 생성 시간 | `"2024-01-01T00:00:00.000Z"` |
| `iteration.updated_at` | string (datetime) | iteration 수정 시간 | `"2024-01-10T00:00:00.000Z"` |
| `iteration.start_date` | string (date) | iteration 시작일 | `"2024-01-01"` |
| `iteration.due_date` | string (date) | iteration 마감일 | `"2024-01-14"` |
| `iteration.web_url` | string | iteration 웹 URL | `"https://gitlab.example.com/groups/my-group/-/iterations/1"` |
| `action` | string | 수행된 액션 | `"add"` |

## Errors
| HTTP 상태 | 코드 | 설명 | 처리 방법 |
|---:|---|---|---|
| `400` | `BAD_REQUEST` | 잘못된 요청 | 요청 파라미터 확인 |
| `401` | `UNAUTHENTICATED` | 토큰 없음 또는 만료 | 토큰 갱신 |
| `403` | `FORBIDDEN` | 권한 없음 | 권한 요청 |
| `404` | `NOT_FOUND` | 리소스 없음 | ID 확인 |

---

## 4. Milestone Events (리소스 마일스톤 변경 이벤트)

### 기본 정보
- **기능:** 이슈/MR에 연결된 마일스톤 변경 이벤트 목록 조회
- **Endpoint:**
  - `GET /api/v4/projects/{id}/issues/{eventable_id}/resource_milestone_events`
  - `GET /api/v4/projects/{id}/merge_requests/{eventable_id}/resource_milestone_events`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
이슈 또는 머지 리퀘스트에 발생한 마일스톤 변경 이벤트 목록을 반환한다. 각 이벤트는 변경을 수행한 사용자, 변경된 마일스톤 정보, 수행된 액션(add/remove), 그리고 변경 후 상태를 포함한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |
| `eventable_id` | any | Y | 이슈 IID (Issue) 또는 MR IID (Merge Request) |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---|---|
| `page` | integer | N | 현재 페이지 번호 (기본값: 1) | `1` |
| `per_page` | integer | N | 페이지당 항목 수 (기본값: 20) | `20` |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---|
| `id` | integer | 이벤트 ID | `1` |
| `user` | object | 이벤트를 발생시킨 사용자 | `{ id: 1, username: "root" }` |
| `user.id` | integer | 사용자 ID | `1` |
| `user.username` | string | 사용자명 | `"root"` |
| `user.public_email` | string | 공개 이메일 | `"admin@example.com"` |
| `user.name` | string | 이름 | `"Administrator"` |
| `user.state` | string | 사용자 상태 | `"active"` |
| `user.locked` | boolean | 계정 잠금 여부 | `false` |
| `user.avatar_url` | string | 아바타 URL | `"https://www.gravatar.com/avatar/..."` |
| `user.avatar_path` | string | 아바타 경로 | `null` |
| `user.custom_attributes` | array | 사용자 정의 속성 목록 | `[{ key: "department", value: "engineering" }]` |
| `user.web_url` | string | 사용자 프로필 URL | `"https://gitlab.example.com/root"` |
| `created_at` | string (datetime) | 이벤트 생성 시간 | `"2024-01-01T00:00:00.000Z"` |
| `resource_type` | string | 리소스 타입 | `"Issue"` |
| `resource_id` | integer | 리소스 ID | `10` |
| `milestone` | object | 변경된 마일스톤 정보 | `{ id: 1, title: "v1.0", state: "active" }` |
| `milestone.id` | integer | 마일스톤 ID | `1` |
| `milestone.iid` | integer | 마일스톤 IID | `1` |
| `milestone.project_id` | integer | 프로젝트 ID | `1` |
| `milestone.group_id` | string | 그룹 ID | `"null"` |
| `milestone.title` | string | 마일스톤 제목 | `"v1.0"` |
| `milestone.description` | string | 마일스톤 설명 | `"First release"` |
| `milestone.state` | string | 마일스톤 상태 | `"active"` |
| `milestone.created_at` | string (datetime) | 마일스톤 생성 시간 | `"2024-01-01T00:00:00.000Z"` |
| `milestone.updated_at` | string (datetime) | 마일스톤 수정 시간 | `"2024-01-10T00:00:00.000Z"` |
| `milestone.due_date` | string (date) | 마일스톤 마감일 | `"2024-03-31"` |
| `milestone.start_date` | string (date) | 마일스톤 시작일 | `"2024-01-01"` |
| `milestone.expired` | boolean | 마감일 경과 여부 | `false` |
| `milestone.web_url` | string | 마일스톤 웹 URL | `"https://gitlab.example.com/groups/my-group/-/milestones/1"` |
| `action` | string | 수행된 액션 | `"add"` |
| `state` | string | 이슈/MR의 현재 상태 | `"opened"` |

## Errors
| HTTP 상태 | 코드 | 설명 | 처리 방법 |
|---:|---|---|---|
| `400` | `BAD_REQUEST` | 잘못된 요청 | 요청 파라미터 확인 |
| `401` | `UNAUTHENTICATED` | 토큰 없음 또는 만료 | 토큰 갱신 |
| `403` | `FORBIDDEN` | 권한 없음 | 권한 요청 |
| `404` | `NOT_FOUND` | 리소스 없음 | ID 확인 |
