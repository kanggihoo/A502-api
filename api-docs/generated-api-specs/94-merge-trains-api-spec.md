# Merge Trains API Spec
Tier: Premium, Ultimate
## 01-List all merge trains for a project [GET]

## 기본 정보
- **기능:** 프로젝트의 모든 merge train 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/merge_trains`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트의 모든 merge train을 반환합니다. merge train은 병합 대기열에 있는 MR들을 순서대로 관리하는 기능입니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `scope` | string | N | 조회 범위 |
| `sort` | string | N | 정렬 방향 (`asc`, `desc`) |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | integer | merge train ID |
| `merge_request` | object | 연결된 MR 정보 |
| `merge_request.id` | integer | MR ID |
| `merge_request.iid` | integer | MR IID |
| `merge_request.project_id` | integer | 프로젝트 ID |
| `merge_request.title` | string | MR 제목 |
| `merge_request.description` | string | MR 설명 |
| `merge_request.state` | string | MR 상태 |
| `merge_request.created_at` | string | 생성 일시 |
| `merge_request.updated_at` | string | 수정 일시 |
| `merge_request.web_url` | string | MR URL |
| `user` | object | 트레인에 추가한 사용자 |
| `user.id` | integer | 사용자 ID |
| `user.username` | string | 사용자명 |
| `user.name` | string | 이름 |
| `user.avatar_url` | string | 아바타 URL |
| `user.web_url` | string | 프로필 URL |
| `pipeline` | object | 연결된 CI 파이프라인 |
| `pipeline.id` | integer | 파이프라인 ID |
| `pipeline.iid` | integer | 파이프라인 IID |
| `pipeline.project_id` | integer | 프로젝트 ID |
| `pipeline.sha` | string | SHA |
| `pipeline.ref` | string | 브랜치 참조 |
| `pipeline.status` | string | 파이프라인 상태 |
| `pipeline.source` | string | 파이프라인 소스 |
| `pipeline.created_at` | string | 생성 일시 |
| `pipeline.web_url` | string | 파이프라인 URL |
| `created_at` | string | 트레인 추가 일시 |
| `updated_at` | string | 트레인 수정 일시 |
| `target_branch` | string | 대상 브랜치 |
| `status` | string | 트레인 상태 |
| `merged_at` | string | 병합 일시 |
| `duration` | integer | 소요 시간 (초) |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |

---

## 03-Retrieve merge train status [GET]

## 기본 정보
- **기능:** 특정 MR의 merge train 상태 조회
- **Endpoint:** `GET /api/v4/projects/{id}/merge_trains/merge_requests/{merge_request_iid}`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 merge request의 merge train 상태를 반환합니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `merge_request_iid` | any | Y | MR의 IID |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | integer | merge train ID |
| `merge_request` | object | 연결된 MR 정보 |
| `merge_request.id` | integer | MR ID |
| `merge_request.iid` | integer | MR IID |
| `merge_request.project_id` | integer | 프로젝트 ID |
| `merge_request.title` | string | MR 제목 |
| `merge_request.description` | string | MR 설명 |
| `merge_request.state` | string | MR 상태 |
| `merge_request.created_at` | string | 생성 일시 |
| `merge_request.updated_at` | string | 수정 일시 |
| `merge_request.web_url` | string | MR URL |
| `user` | object | 트레인에 추가한 사용자 |
| `pipeline` | object | 연결된 CI 파이프라인 |
| `pipeline.id` | integer | 파이프라인 ID |
| `pipeline.iid` | integer | 파이프라인 IID |
| `pipeline.project_id` | integer | 프로젝트 ID |
| `pipeline.sha` | string | SHA |
| `pipeline.ref` | string | 브랜치 참조 |
| `pipeline.status` | string | 파이프라인 상태 |
| `pipeline.source` | string | 파이프라인 소스 |
| `pipeline.created_at` | string | 생성 일시 |
| `pipeline.web_url` | string | 파이프라인 URL |
| `created_at` | string | 트레인 추가 일시 |
| `updated_at` | string | 트레인 수정 일시 |
| `target_branch` | string | 대상 브랜치 |
| `status` | string | 트레인 상태 |
| `merged_at` | string | 병합 일시 |
| `duration` | integer | 소요 시간 (초) |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
