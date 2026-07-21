# 99-마일스톤(Milestones) API 명세

## 01-List all project milestones

## 기본 정보
- **기능:** 특정 프로젝트의 모든 마일스톤을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/milestones`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트의 모든 마일스톤 목록을 반환한다. 상태, 제목, 검색어, 상위 그룹 포함, 업데이트 일자 등으로 필터링할 수 있다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `state` | string | N | 마일스톤 상태 (`active`, `closed`, `all`) |
| `iids` | array | N | 마일스톤 IID 목록 |
| `title` | string | N | 마일스톤 제목 |
| `search` | string | N | 제목 또는 설명 검색어 |
| `include_parent_milestones` | boolean | N | (Deprecated) `include_ancestors` 사용 |
| `include_ancestors` | boolean | N | 모든 상위 그룹의 마일스톤 포함 |
| `updated_before` | string | N | 지정된 시간 이전에 업데이트된 마일스톤 (ISO 8601) |
| `updated_after` | string | N | 지정된 시간 이후에 업데이트된 마일스톤 (ISO 8601) |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `id` | integer | 마일스톤 ID | `1` |
| `iid` | integer | 프로젝트 내 IID | `1` |
| `project_id` | integer | 프로젝트 ID | `1234` |
| `group_id` | string | 그룹 ID | `null` |
| `title` | string | 마일스톤 제목 | `Sprint 1` |
| `description` | string | 마일스톤 설명 | `First sprint` |
| `state` | string | 상태 (`active`, `closed`) | `active` |
| `created_at` | string | 생성 일시 | `2025-01-01T00:00:00.000+09:00` |
| `updated_at` | string | 업데이트 일시 | `2025-01-02T00:00:00.000+09:00` |
| `due_date` | string | 마감일 | `2025-01-15` |
| `start_date` | string | 시작일 | `2025-01-01` |
| `expired` | boolean | 만료 여부 | `false` |
| `web_url` | string | 웹 UI URL | `https://gitlab.example.com/group/project/-/milestones/1` |

JSON 예시:
```json
[
  {
    "id": 1,
    "iid": 1,
    "project_id": 1234,
    "group_id": null,
    "title": "Sprint 1",
    "description": "First sprint",
    "state": "active",
    "created_at": "2025-01-01T00:00:00.000+09:00",
    "updated_at": "2025-01-02T00:00:00.000+09:00",
    "due_date": "2025-01-15",
    "start_date": "2025-01-01",
    "expired": false,
    "web_url": "https://gitlab.example.com/group/project/-/milestones/1"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 프로젝트를 찾을 수 없음 |

---

## 03-Retrieve a project milestone

## 기본 정보
- **기능:** 특정 프로젝트 마일스톤을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/milestones/{milestone_id}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트에서 특정 마일스톤의 상세 정보를 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |
| `milestone_id` | integer | Y | 마일스톤 ID | `1` |

## Response
### `200 OK`
List project milestones와 동일한 응답 스키마를 사용한다.

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 마일스톤을 찾을 수 없음 |

---

## 06-List all issues for a project milestone

## 기본 정보
- **기능:** 특정 마일스톤에 할당된 모든 이슈를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/milestones/{milestone_id}/issues`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 마일스톤에 할당된 모든 이슈 목록을 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |
| `milestone_id` | integer | Y | 마일스톤 ID | `1` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|---:|
| `id` | integer | 이슈 ID |
| `iid` | integer | 프로젝트 내 IID |
| `project_id` | integer | 프로젝트 ID |
| `title` | string | 이슈 제목 |
| `description` | string | 이슈 설명 |
| `state` | string | 상태 (`opened`, `closed`) |
| `created_at` | string | 생성 일시 |
| `updated_at` | string | 업데이트 일시 |
| `closed_at` | string | 닫힌 일시 |
| `closed_by` | object | 닫은 사용자 정보 |
| `labels` | array[string] | 레이블 목록 |
| `milestone` | object | 마일스톤 정보 |
| `assignees` | object | 담당자 정보 |
| `author` | object | 작성자 정보 |
| `type` | string | 이슈 타입 (`ISSUE`, `INCIDENT`, `TEST_CASE`, `REQUIREMENT`, `TASK`, `TICKET`) |
| `assignee` | object | 담당자 정보 |
| `user_notes_count` | integer | 코멘트 수 |
| `merge_requests_count` | integer | 연결된 MR 수 |
| `upvotes` | integer | 좋아요 수 |
| `downvotes` | integer | 싫어요 수 |
| `start_date` | string | 시작일 |
| `due_date` | string | 마감일 |
| `confidential` | boolean | 비밀 이슈 여부 |
| `discussion_locked` | boolean | 디스커션 잠금 여부 |
| `issue_type` | string | 이슈 타입 |
| `web_url` | string | 웹 UI URL |
| `weight` | integer | 가중치 |
| `blocking_issues_count` | integer | 차단 중인 이슈 수 |

JSON 예시:
```json
[
  {
    "id": 42,
    "iid": 1,
    "project_id": 1234,
    "title": "Fix login bug",
    "description": "Users cannot log in",
    "state": "opened",
    "created_at": "2025-01-01T00:00:00.000+09:00",
    "updated_at": "2025-01-02T00:00:00.000+09:00",
    "labels": ["bug"],
    "milestone": {
      "id": 1,
      "iid": 1,
      "title": "Sprint 1",
      "state": "active",
      "web_url": "https://gitlab.example.com/group/project/-/milestones/1"
    },
    "author": {
      "id": 1,
      "username": "john",
      "name": "John Doe"
    },
    "issue_type": "ISSUE",
    "confidential": false,
    "web_url": "https://gitlab.example.com/group/project/-/issues/1",
    "weight": 3
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 마일스톤을 찾을 수 없음 |

---

## 07-List all merge requests for a project milestone

## 기본 정보
- **기능:** 특정 마일스톤에 할당된 모든 Merge Request를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/milestones/{milestone_id}/merge_requests`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 마일스톤에 할당된 모든 Merge Request 목록을 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |
| `milestone_id` | integer | Y | 마일스톤 ID | `1` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|---:|
| `id` | integer | MR ID |
| `iid` | integer | 프로젝트 내 IID |
| `project_id` | integer | 프로젝트 ID |
| `title` | string | MR 제목 |
| `description` | string | MR 설명 |
| `state` | string | 상태 |
| `created_at` | string | 생성 일시 |
| `updated_at` | string | 업데이트 일시 |
| `merged_by` | object | 병합한 사용자 |
| `merged_at` | string | 병합 일시 |
| `closed_by` | object | 닫은 사용자 |
| `closed_at` | string | 닫힌 일시 |
| `target_branch` | string | 대상 브랜치 |
| `source_branch` | string | 소스 브랜치 |
| `author` | object | 작성자 |
| `assignees` | object | 담당자 |
| `reviewers` | object | 리뷰어 |
| `labels` | array[string] | 레이블 목록 |
| `draft` | boolean | 초안 여부 |
| `milestone` | object | 마일스톤 정보 |
| `merge_status` | string | 병합 상태 |
| `sha` | string | MR SHA |
| `web_url` | string | 웹 UI URL |
| `has_conflicts` | boolean | 충돌 여부 |
| `blocking_discussions_resolved` | boolean | 차단 디스커션 해결 여부 |
| `approvals_before_merge` | integer | 필요한 승인 수 |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 마일스톤을 찾을 수 없음 |

---

## 10-List all group milestones

## 기본 정보
- **기능:** 특정 그룹의 모든 마일스톤을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/milestones`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 그룹의 모든 마일스톤 목록을 반환한다. 하위 그룹/프로젝트의 마일스톤도 포함할 수 있다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | string | Y | 그룹 ID | `6789` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `state` | string | N | 상태 (`active`, `closed`, `all`) |
| `iids` | array | N | 마일스톤 IID 목록 |
| `title` | string | N | 마일스톤 제목 |
| `search` | string | N | 검색어 |
| `include_parent_milestones` | boolean | N | (Deprecated) |
| `include_ancestors` | boolean | N | 상위 그룹 마일스톤 포함 |
| `updated_before` | string | N | 업데이트 시간 이전 필터 |
| `updated_after` | string | N | 업데이트 시간 이후 필터 |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |
| `include_descendants` | boolean | N | 모든 하위 그룹/프로젝트 마일스톤 포함 |

## Response
### `200 OK`
Project milestones와 동일한 응답 스키마를 사용한다.

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 그룹을 찾을 수 없음 |
