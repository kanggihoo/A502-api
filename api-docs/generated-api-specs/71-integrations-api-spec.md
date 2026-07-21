# 71-integrations — 통합(Integration) API

GitLab 프로젝트와 외부 서비스(Jenkins, Jira, Mattermost 등)의 통합 설정을 다룬다.

---

## 04 — List all active integrations [GET]

### 기본 정보
- **기능:** 프로젝트에 활성화된 모든 통합 서비스 목록을 조회한다
- **Endpoint:** `GET /api/v4/projects/{id}/services`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트에 등록된 모든 활성 통합 서비스 목록을 반환한다. 각 서비스의 slug, 활성화 여부, 이벤트 구독 설정을 확인할 수 있다.

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

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | integer | 통합 서비스 ID | `1` |
| `title` | string | 통합 서비스 표시 이름 | `Jenkins` |
| `slug` | string | 통합 서비스 식별자 | `jenkins` |
| `created_at` | string | 생성 일시 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `updated_at` | string | 수정 일시 (ISO 8601) | `2024-01-02T00:00:00Z` |
| `active` | boolean | 활성화 여부 | `true` |
| `commit_events` | boolean | 커밋 이벤트 구독 여부 | `false` |
| `push_events` | boolean | push 이벤트 구독 여부 | `true` |
| `issues_events` | boolean | 이슈 이벤트 구독 여부 | `false` |
| `incident_events` | boolean | 인시던트 이벤트 구독 여부 | `false` |
| `alert_events` | boolean | 알림 이벤트 구독 여부 | `false` |
| `confidential_issues_events` | boolean | 기밀 이슈 이벤트 구독 여부 | `false` |
| `merge_requests_events` | boolean | MR 이벤트 구독 여부 | `true` |
| `tag_push_events` | boolean | tag push 이벤트 구독 여부 | `false` |
| `deployment_events` | boolean | 배포 이벤트 구독 여부 | `false` |
| `note_events` | boolean | 노트(댓글) 이벤트 구독 여부 | `false` |
| `confidential_note_events` | boolean | 기밀 노트 이벤트 구독 여부 | `false` |
| `pipeline_events` | boolean | 파이프라인 이벤트 구독 여부 | `true` |
| `wiki_page_events` | boolean | Wiki 이벤트 구독 여부 | `false` |
| `job_events` | boolean | Job 이벤트 구독 여부 | `false` |
| `comment_on_event_enabled` | boolean | 이벤트 시 댓글 작성 여부 | `true` |
| `inherited` | boolean | 그룹에서 상속된 설정인지 여부 | `false` |
| `vulnerability_events` | boolean | 취약점 이벤트 구독 여부 | `false` |

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 401 | 인증 실패 |
| 404 | 프로젝트를 찾을 수 없음 |

---

## 57 — Get an integration settings [GET]

### 기본 정보
- **기능:** 특정 통합 서비스의 상세 설정을 조회한다
- **Endpoint:** `GET /api/v4/projects/{id}/services/{slug}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트와 slug에 해당하는 통합 서비스의 상세 설정을 반환한다. `properties` 필드에 각 서비스별 고유 설정이 포함된다 (예: Jenkins URL, Jira URL 등).

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
| `slug` | string | Y | 통합 서비스 이름 (예: `jenkins`, `jira`, `mattermost`) |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | integer | 통합 서비스 ID | `1` |
| `title` | string | 통합 서비스 표시 이름 | `Jenkins` |
| `slug` | string | 통합 서비스 식별자 | `jenkins` |
| `created_at` | string | 생성 일시 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `updated_at` | string | 수정 일시 (ISO 8601) | `2024-01-02T00:00:00Z` |
| `active` | boolean | 활성화 여부 | `true` |
| `commit_events` | boolean | 커밋 이벤트 구독 여부 | `false` |
| `push_events` | boolean | push 이벤트 구독 여부 | `true` |
| `issues_events` | boolean | 이슈 이벤트 구독 여부 | `false` |
| `incident_events` | boolean | 인시던트 이벤트 구독 여부 | `false` |
| `alert_events` | boolean | 알림 이벤트 구독 여부 | `false` |
| `confidential_issues_events` | boolean | 기밀 이슈 이벤트 구독 여부 | `false` |
| `merge_requests_events` | boolean | MR 이벤트 구독 여부 | `true` |
| `tag_push_events` | boolean | tag push 이벤트 구독 여부 | `false` |
| `deployment_events` | boolean | 배포 이벤트 구독 여부 | `false` |
| `note_events` | boolean | 노트(댓글) 이벤트 구독 여부 | `false` |
| `confidential_note_events` | boolean | 기밀 노트 이벤트 구독 여부 | `false` |
| `pipeline_events` | boolean | 파이프라인 이벤트 구독 여부 | `true` |
| `wiki_page_events` | boolean | Wiki 이벤트 구독 여부 | `false` |
| `job_events` | boolean | Job 이벤트 구독 여부 | `false` |
| `comment_on_event_enabled` | boolean | 이벤트 시 댓글 작성 여부 | `true` |
| `inherited` | boolean | 그룹에서 상속된 설정인지 여부 | `false` |
| `vulnerability_events` | boolean | 취약점 이벤트 구독 여부 | `false` |
| `properties` | object | 서비스별 상세 설정 (키-값 쌍) | `{"jenkins_url": "..."}` |

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 400 | 잘못된 요청 |
| 401 | 인증 실패 |
| 404 | 통합 서비스를 찾을 수 없음 |

---

## 연동 참고사항

- `GET /projects/{id}/services`로 활성 통합 목록을 조회한 후, 각 slug로 개별 설정을 상세 조회하는 흐름이 기본이다.
- 주요 통합 서비스 slug: `jenkins`, `jira`, `mattermost`, `mattermost_slash_commands`, `discord`, `slack`, `microsoft_teams`
- 통합 서비스 생성/수정은 PUT 메서드를 사용한다 (예: `PUT /projects/{id}/services/jenkins`).
- 각 통합 서비스는 서로 다른 `properties` 필드를 가지므로, slug별 응답 구조를 개별 확인해야 한다.
- 통합 비활성화는 `DELETE /projects/{id}/services/{slug}`로 가능하다.
