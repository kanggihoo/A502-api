# Deploy Keys & Deployments API Spec

## 02-List all project deployments [GET]

## 기본 정보
- **기능:** 프로젝트의 모든 배포(Deployment) 목록을 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/deployments`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트의 모든 배포를 목록으로 반환합니다. 정렬, 시간 범위 필터, 환경명 및 상태 필터, 페이지네이션을 지원합니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | `any` | Y | 프로젝트의 ID 또는 URL-인코딩된 경로 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `page` | `integer` | N | 현재 페이지 번호 |
| `per_page` | `integer` | N | 페이지당 항목 수 |
| `order_by` | `string` | N | 정렬 기준 필드. `id`, `iid`, `created_at`, `updated_at`, `ref` 중 하나. 기본값 `id` |
| `sort` | `string` | N | 정렬 방향. `asc`(기본) 또는 `desc` |
| `updated_after` | `string` | N | ISO 8601 형식으로 지정된 시간 이후 업데이트된 배포 필터 |
| `updated_before` | `string` | N | ISO 8601 형식으로 지정된 시간 이전 업데이트된 배포 필터 |
| `finished_after` | `string` | N | ISO 8601 형식으로 지정된 시간 이후 완료된 배포 필터 |
| `finished_before` | `string` | N | ISO 8601 형식으로 지정된 시간 이전 완료된 배포 필터 |
| `environment` | `string` | N | 환경 이름으로 배포 필터 |
| `status` | `string` | N | 상태로 배포 필터. `created`, `running`, `success`, `failed`, `canceled`, `blocked` 중 하나 |

## Response
### `200 OK`

```json
{
  "id": integer,
  "iid": integer,
  "ref": string,
  "sha": string,
  "created_at": string,
  "updated_at": string,
  "user": { "id": integer, "username": string, "public_email": string, "name": string, "state": string, "locked": boolean, "avatar_url": string, "avatar_path": string, "custom_attributes": [{ "key": string, "value": string }], "web_url": string },
  "environment": { "id": integer, "name": string, "slug": string, "external_url": string, "created_at": string, "updated_at": string },
  "deployable": { "id": integer, "status": string, "stage": string, "name": string, "ref": string, "tag": boolean, "coverage": number, "allow_failure": boolean, "created_at": string, "started_at": string, "finished_at": string, "erased_at": string, "duration": number, "queued_duration": number, "user": { ... }, "commit": { ... }, "pipeline": { ... }, "failure_reason": string, "web_url": string, "project": string, "artifacts_file": { ... }, "artifacts": [{ ... }], "runner": { ... }, "runner_manager": { ... }, "artifacts_expire_at": string, "archived": boolean, "tag_list": [string] },
  "status": string
}
```

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad request |
| 401 | Unauthorized |
| 404 | Not found |

---

## 04-Retrieve a deployment [GET]

## 기본 정보
- **기능:** 특정 배포의 상세 정보를 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/deployments/{deployment_id}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
프로젝트 ID와 배포 ID를 기준으로 단일 배포의 상세 정보를 반환합니다. 승인(Approval) 관련 정보를 포함합니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | `any` | Y | 프로젝트의 ID 또는 URL-인코딩된 경로 |
| `deployment_id` | `integer` | Y | 배포 ID |

## Response
### `200 OK`

`02-List all project deployments`와 동일한 기본 스키마 + 추가 필드:
- `pending_approval_count`: integer
- `approvals`: `{ user: { ... }, status: string, created_at: string, comment: string }`
- `approval_summary`: `{ rules: { id, user_id, group_id, access_level, access_level_description, required_approvals, group_inheritance_type, deployment_approvals: { ... } } }`

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not found |

---

## 07-List all merge requests associated with a deployment [GET]

## 기본 정보
- **기능:** 특정 배포와 함께 출시된 모든 Merge Request 목록을 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/deployments/{deployment_id}/merge_requests`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 배포에 포함된 모든 Merge Request를 반환합니다. 작성자, 담당자, 리뷰어, 레이블, 마일스톤, 상태, 정렬 등 다양한 필터를 지원합니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | `any` | Y | 프로젝트의 ID 또는 URL-인코딩된 경로 |
| `deployment_id` | `integer` | Y | 배포 ID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `page` | `integer` | N | 현재 페이지 번호 |
| `per_page` | `integer` | N | 페이지당 항목 수 |
| `author_id` | `integer` | N | 특정 사용자 ID가 생성한 MR 필터. `author_username`과 상호 배타적 |
| `author_username` | `string` | N | 특정 사용자명이 생성한 MR 필터. `author_id`와 상호 배타적 |
| `assignee_id` | `any` | N | 특정 사용자 ID에 할당된 MR 필터. `None`/`Any` 지원 |
| `assignee_username` | `array` | N | 특정 사용자명에 할당된 MR 필터 |
| `reviewer_username` | `string` | N | 특정 사용자명이 리뷰어인 MR 필터 |
| `labels` | `array` | N | 라벨로 MR 필터 (쉼표 구분) |
| `milestone` | `string` | N | 마일스톤으로 MR 필터 |
| `state` | `string` | N | MR 상태 필터. `all`, `opened`, `closed`, `locked`, `merged` |
| `order_by` | `string` | N | 정렬 기준 필드 |
| `sort` | `string` | N | 정렬 방향. `asc` 또는 `desc` |
| `search` | `string` | N | 제목과 설명에서 검색 |
| `source_branch` | `string` | N | 소스 브랜치 필터 |
| `target_branch` | `string` | N | 타겟 브랜치 필터 |
| `draft` | `boolean` | N | Draft 상태 필터 |
| `created_after` / `created_before` | `string` | N | 생성 시간 범위 필터 (ISO 8601) |
| `updated_after` / `updated_before` | `string` | N | 업데이트 시간 범위 필터 (ISO 8601) |
| `deployed_before` / `deployed_after` | `string` | N | 배포 시간 범위 필터 (ISO 8601) |
| `environment` | `string` | N | 배포된 환경 필터 |
| `scope` | `string` | N | `created_by_me`, `assigned_to_me`, `all` 등 |

## Response
### `200 OK`

```json
{
  "id": integer,
  "iid": integer,
  "project_id": integer,
  "title": string,
  "description": string,
  "state": string,
  "created_at": string,
  "updated_at": string,
  "merged_by": { ... },
  "merge_user": { ... },
  "merged_at": string,
  "closed_by": { ... },
  "closed_at": string,
  "title_html": string,
  "description_html": string,
  "target_branch": string,
  "source_branch": string,
  "user_notes_count": integer,
  "upvotes": integer,
  "downvotes": integer,
  "author": { ... },
  "assignees": { ... },
  "assignee": { ... },
  "reviewers": { ... },
  "source_project_id": integer,
  "target_project_id": integer,
  "labels": [string],
  "draft": boolean,
  "milestone": { ... },
  "merge_when_pipeline_succeeds": boolean,
  "merge_status": string,
  "detailed_merge_status": string,
  "sha": string,
  "merge_commit_sha": string,
  "squash_commit_sha": string,
  "discussion_locked": boolean,
  "web_url": string,
  "time_stats": { "time_estimate": integer, "total_time_spent": integer, "human_time_estimate": string, "human_total_time_spent": string },
  "squash": boolean,
  "squash_on_merge": boolean,
  "task_completion_status": { "count": integer, "completed_count": integer },
  "has_conflicts": boolean,
  "blocking_discussions_resolved": boolean,
  "approvals_before_merge": integer
}
```

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not found |
