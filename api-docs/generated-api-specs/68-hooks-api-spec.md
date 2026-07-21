# 68-hooks — Webhook API

프로젝트 이벤트를 외부 HTTP 엔드포인트로 전달하는 webhook을 관리한다.

---

## 27 — List all webhooks for a project [GET]

### 기본 정보
- **기능:** 프로젝트에 등록된 모든 webhook 목록을 조회한다
- **Endpoint:** `GET /api/v4/projects/{id}/hooks`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트의 webhook 목록을 반환한다. push, merge request, pipeline 등 각 이벤트 유형별 구독 여부를 확인할 수 있다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | integer | webhook ID | `1` |
| `url` | string | webhook URL | `https://example.com/webhook` |
| `name` | string | webhook 이름 | `My Webhook` |
| `description` | string | webhook 설명 | `Notifies CI status` |
| `created_at` | string | 생성 일시 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `push_events` | boolean | push 이벤트 구독 여부 | `true` |
| `tag_push_events` | boolean | tag push 이벤트 구독 여부 | `false` |
| `merge_requests_events` | boolean | MR 이벤트 구독 여부 | `true` |
| `repository_update_events` | boolean | 저장소 업데이트 이벤트 구독 여부 | `false` |
| `enable_ssl_verification` | boolean | SSL 검증 사용 여부 | `true` |
| `alert_status` | string | webhook 상태 | `executable` |
| `disabled_until` | string | 비활성화 만료 시간 | `null` |
| `push_events_branch_filter` | string | 브랜치 필터 | `main` |
| `branch_filter_strategy` | string | 브랜치 필터 전략 | `wildcard` |
| `custom_webhook_template` | string | 커스텀 템플릿 | `null` |
| `token_present` | boolean | 시크릿 토큰 설정 여부 | `true` |
| `signing_token_present` | boolean | HMAC 서명 토큰 설정 여부 | `false` |
| `project_id` | integer | 프로젝트 ID | `1` |
| `issues_events` | boolean | 이슈 이벤트 구독 여부 | `true` |
| `confidential_issues_events` | boolean | 기밀 이슈 이벤트 구독 여부 | `false` |
| `note_events` | boolean | 노트(댓글) 이벤트 구독 여부 | `false` |
| `confidential_note_events` | boolean | 기밀 노트 이벤트 구독 여부 | `false` |
| `pipeline_events` | boolean | 파이프라인 이벤트 구독 여부 | `true` |
| `wiki_page_events` | boolean | Wiki 이벤트 구독 여부 | `false` |
| `deployment_events` | boolean | 배포 이벤트 구독 여부 | `false` |
| `feature_flag_events` | boolean | 기능 플래그 이벤트 구독 여부 | `false` |
| `job_events` | boolean | Job 이벤트 구독 여부 | `false` |
| `releases_events` | boolean | 릴리스 이벤트 구독 여부 | `false` |
| `milestone_events` | boolean | 마일스톤 이벤트 구독 여부 | `false` |
| `emoji_events` | boolean | 이모지 이벤트 구독 여부 | `false` |
| `resource_access_token_events` | boolean | 액세스 토큰 만료 이벤트 구독 여부 | `false` |
| `resource_deploy_token_events` | boolean | 배포 토큰 만료 이벤트 구독 여부 | `false` |
| `vulnerability_events` | boolean | 취약점 이벤트 구독 여부 | `false` |

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 400 | 잘못된 요청 |
| 404 | 프로젝트를 찾을 수 없음 |

---

## 28 — Add a webhook to a project [POST]

### 기본 정보
- **기능:** 프로젝트에 새 webhook을 등록한다
- **Endpoint:** `POST /api/v4/projects/{id}/hooks`
- **인증:** Bearer Token 필요
- **권한:** `api`
- **멱등성:** 미지원

### 설명
지정된 프로젝트에 URL과 이벤트 구독 설정을 포함한 webhook을 생성한다. 응답에서 `token`과 `signing_token` 필드는 반환되지 않는다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |

#### Body (application/json)
| 필드 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `url` | string | Y | webhook 전송 대상 URL |
| `name` | string | N | webhook 이름 |
| `description` | string | N | webhook 설명 |
| `push_events` | boolean | N | push 이벤트 트리거 |
| `issues_events` | boolean | N | 이슈 이벤트 트리거 |
| `confidential_issues_events` | boolean | N | 기밀 이슈 이벤트 트리거 |
| `merge_requests_events` | boolean | N | MR 이벤트 트리거 |
| `tag_push_events` | boolean | N | tag push 이벤트 트리거 |
| `note_events` | boolean | N | 노트(댓글) 이벤트 트리거 |
| `confidential_note_events` | boolean | N | 기밀 노트 이벤트 트리거 |
| `job_events` | boolean | N | Job 이벤트 트리거 |
| `pipeline_events` | boolean | N | 파이프라인 이벤트 트리거 |
| `wiki_page_events` | boolean | N | Wiki 이벤트 트리거 |
| `deployment_events` | boolean | N | 배포 이벤트 트리거 |
| `feature_flag_events` | boolean | N | 기능 플래그 이벤트 트리거 |
| `releases_events` | boolean | N | 릴리스 이벤트 트리거 |
| `milestone_events` | boolean | N | 마일스톤 이벤트 트리거 |
| `emoji_events` | boolean | N | 이모지 이벤트 트리거 |
| `resource_access_token_events` | boolean | N | 액세스 토큰 만료 이벤트 트리거 |
| `resource_deploy_token_events` | boolean | N | 배포 토큰 만료 이벤트 트리거 |
| `enable_ssl_verification` | boolean | N | SSL 검증 사용 여부 |
| `token` | string | N | payload 검증용 시크릿 토큰 (응답 미포함) |
| `signing_token` | string | N | HMAC 서명 토큰 (`whsec_<base64>` 형식, 응답 미포함) |
| `push_events_branch_filter` | string | N | 특정 브랜치만 트리거 |
| `custom_webhook_template` | string | N | 요청 payload 커스텀 템플릿 |
| `branch_filter_strategy` | enum | N | 브랜치 필터 전략 (`wildcard`/`regex`/`all_branches`) |
| `vulnerability_events` | boolean | N | 취약점 이벤트 트리거 |
| `url_variables` | array | N | URL 변수 목록 (`key`, `value`) |
| `custom_headers` | array | N | 커스텀 헤더 목록 (`key`, `value`) |

### Response
#### `201 Created`
27번 List all webhooks 응답과 동일한 스키마를 반환한다 (단, `token`/`signing_token` 제외).

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 400 | 유효성 검증 오류 |
| 404 | 프로젝트를 찾을 수 없음 |
| 422 | 처리 불가능한 엔티티 |

---

## 29 — Retrieve a project webhook [GET]

### 기본 정보
- **기능:** 프로젝트의 특정 webhook 상세 정보를 조회한다
- **Endpoint:** `GET /api/v4/projects/{id}/hooks/{hook_id}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트와 hook_id에 해당하는 webhook 설정을 반환한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |
| `hook_id` | integer | Y | webhook ID |

### Response
#### `200 OK`
27번 List all webhooks 응답과 동일한 단일 객체 스키마.

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 400 | 잘못된 요청 |
| 404 | webhook 또는 프로젝트를 찾을 수 없음 |

---

## 31 — Delete a project webhook [DEL]

### 기본 정보
- **기능:** 프로젝트의 특정 webhook을 삭제한다
- **Endpoint:** `DELETE /api/v4/projects/{id}/hooks/{hook_id}`
- **인증:** Bearer Token 필요
- **권한:** `api`
- **멱등성:** 미지원

### 설명
지정된 프로젝트와 hook_id에 해당하는 webhook을 삭제한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |
| `hook_id` | integer | Y | 삭제할 webhook ID |

### Response
#### `204 No Content`
본문 없이 성공 응답을 반환한다.

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 400 | 잘못된 요청 |
| 404 | webhook 또는 프로젝트를 찾을 수 없음 |

---

## 연동 참고사항

- webhook 이벤트를 수신하려면 공개적으로 접근 가능한 HTTP 엔드포인트가 필요하다. SSAFY EC2 인스턴스에 수신 서버를 구축하여 사용할 수 있다.
- 시크릿 토큰(`token`) 또는 HMAC 서명(`signing_token`)을 설정하여 payload 변조를 방지할 수 있다.
- `push_events_branch_filter`와 `branch_filter_strategy`를 조합하여 특정 브랜치의 push 이벤트만 필터링할 수 있다.
- webhook 생성 후 30일 동안 5번 연속 실패하면 자동 비활성화된다 (`alert_status`, `disabled_until` 필드로 확인 가능).
