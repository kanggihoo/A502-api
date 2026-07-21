# Environments API Spec

## 01-List all environments [GET]

## 기본 정보
- **기능:** 지정된 프로젝트의 모든 환경(Environment) 목록을 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/environments`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트에 속한 모든 환경을 반환합니다. 이름 검색, 상태 필터, 페이지네이션을 지원합니다.

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
| `name` | `string` | N | 특정 이름의 환경 반환. `search`와 상호 배타적 |
| `search` | `string` | N | 검색어와 일치하는 환경 목록 반환. 최소 3자. `name`과 상호 배타적 |
| `states` | `string` | N | 특정 상태(`available`, `stopping`, `stopped`)의 환경 필터. 미지정 시 전체 반환 |

## Response
### `200 OK`

```json
{
  "id": integer,
  "name": string,
  "slug": string,
  "external_url": string,
  "created_at": string,
  "updated_at": string,
  "tier": string,
  "project": {
    "id": integer,
    "description": string,
    "name": string,
    "name_with_namespace": string,
    "path": string,
    "path_with_namespace": string,
    "created_at": string,
    "default_branch": string,
    "tag_list": [string],
    "topics": [string],
    "ssh_url_to_repo": string,
    "http_url_to_repo": string,
    "web_url": string,
    "readme_url": string,
    "forks_count": integer,
    "license_url": string,
    "license": { "key": string, "name": string, "nickname": string, "html_url": string, "source_url": string },
    "avatar_url": string,
    "star_count": integer,
    "last_activity_at": string,
    "visibility": string,
    "namespace": { "id": integer, "name": string, "path": string, "kind": string, "full_path": string, "parent_id": integer, "avatar_url": string, "web_url": string },
    "custom_attributes": { "key": string, "value": string },
    "repository_storage": string
  },
  "last_deployment": {
    "id": integer,
    "iid": integer,
    "ref": string,
    "sha": string,
    "created_at": string,
    "updated_at": string,
    "user": { "id": integer, "username": string, "public_email": string, "name": string, "state": string, "locked": boolean, "avatar_url": string, "avatar_path": string, "custom_attributes": [{ "key": string, "value": string }], "web_url": string },
    "environment": { "id": integer, "name": string, "slug": string, "external_url": string, "created_at": string, "updated_at": string },
    "deployable": { "id": integer, "status": string, "stage": string, "name": string, "ref": string, "tag": boolean, "coverage": number, "allow_failure": boolean, "created_at": string, "started_at": string, "finished_at": string, "erased_at": string, "duration": number, "queued_duration": number, "user": { ... }, "commit": { ... }, "pipeline": { "id": integer, "iid": integer, "project_id": integer, "sha": string, "ref": string, "status": string, "source": string, "created_at": string, "updated_at": string, "web_url": string }, "failure_reason": string, "web_url": string, "project": string, "artifacts_file": { "filename": string, "size": integer }, "artifacts": [{ "file_type": string, "size": integer, "filename": string, "file_format": string }], "runner": { ... }, "runner_manager": { ... }, "artifacts_expire_at": string, "archived": boolean, "tag_list": [string] },
    "status": string
  },
  "state": string,
  "auto_stop_at": string,
  "cluster_agent": { "id": integer, "name": string, "config_project": { ... }, "created_at": string, "created_by_user_id": integer, "is_receptive": boolean },
  "kubernetes_namespace": string,
  "flux_resource_path": string,
  "description": string,
  "auto_stop_setting": string
}
```

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not found |

---

## 05-Retrieve an environment [GET]

## 기본 정보
- **기능:** 지정된 프로젝트의 특정 환경 상세 정보를 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/environments/{environment_id}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
프로젝트 ID와 환경 ID를 기준으로 특정 환경의 상세 정보를 반환합니다.

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
| `environment_id` | `integer` | Y | 환경 ID |

## Response
### `200 OK`

`01-List all environments`와 동일한 스키마.

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not found |
