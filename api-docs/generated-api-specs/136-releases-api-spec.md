# Releases API Spec

## 06-List all releases in a group [GET]

## 기본 정보
- **기능:** 지정된 그룹에 속한 모든 프로젝트의 릴리즈 목록을 조회합니다.
- **Endpoint:** `GET /api/v4/groups/{id}/releases`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 그룹 ID 또는 URL-인코딩된 경로에 속한 모든 프로젝트의 릴리즈를 목록으로 반환합니다. `sort`, `simple` 모드, 페이지네이션을 지원합니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | `any` | Y | 그룹의 ID 또는 URL-인코딩된 경로 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `sort` | `string` | N | 정렬 방향. `desc`(기본) 또는 `asc` |
| `simple` | `boolean` | N | `true`로 설정 시 각 릴리즈의 제한된 필드만 반환 |
| `page` | `integer` | N | 현재 페이지 번호 |
| `per_page` | `integer` | N | 페이지당 항목 수 |

## Response
### `200 OK`

```json
{
  "name": string,
  "tag_name": string,
  "description": string,
  "created_at": string,
  "released_at": string,
  "upcoming_release": boolean,
  "description_html": string,
  "author": {
    "id": integer,
    "username": string,
    "public_email": string,
    "name": string,
    "state": string,
    "locked": boolean,
    "avatar_url": string,
    "avatar_path": string,
    "custom_attributes": [{ "key": string, "value": string }],
    "web_url": string
  },
  "commit": {
    "id": string,
    "short_id": string,
    "created_at": string,
    "parent_ids": [string],
    "title": string,
    "message": string,
    "author_name": string,
    "author_email": string,
    "authored_date": string,
    "committer_name": string,
    "committer_email": string,
    "committed_date": string,
    "trailers": {},
    "extended_trailers": {},
    "web_url": string
  },
  "milestones": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "group_id": string,
    "title": string,
    "description": string,
    "state": string,
    "created_at": string,
    "updated_at": string,
    "due_date": string,
    "start_date": string,
    "expired": boolean,
    "web_url": string,
    "issue_stats": {}
  },
  "commit_path": string,
  "tag_path": string,
  "assets": string,
  "evidences": { "sha": string, "filepath": string, "collected_at": string },
  "_links": string
}
```

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad request |
| 403 | Forbidden |
| 404 | Not found |

---

## 07-List all releases in a project [GET]

## 기본 정보
- **기능:** 지정된 프로젝트의 모든 릴리즈를 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/releases`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트의 모든 릴리즈를 `released_at` 기준 정렬로 반환합니다. 페이지네이션, 정렬, HTML 설명 포함 여부, 업데이트 시간 필터를 지원합니다.

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
| `order_by` | `string` | N | 정렬 기준 필드. `released_at`(기본) 또는 `created_at` |
| `sort` | `string` | N | 정렬 방향. `desc`(기본) 또는 `asc` |
| `include_html_description` | `boolean` | N | `true`면 HTML 렌더링된 릴리즈 설명을 포함 |
| `updated_before` | `string` | N | 지정된 ISO 8601 시간 이전에 업데이트된 릴리즈 필터 |
| `updated_after` | `string` | N | 지정된 ISO 8601 시간 이후에 업데이트된 릴리즈 필터 |

## Response
### `200 OK`

`06-List all releases in a group`과 동일한 스키마.

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 404 | Not Found |

---

## 09-Retrieve a release by tag name [GET]

## 기본 정보
- **기능:** 지정된 태그 이름에 해당하는 릴리즈를 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/releases/{tag_name}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트에서 특정 Git 태그와 연결된 릴리즈 상세 정보를 반환합니다.

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
| `tag_name` | `string` | Y | 릴리즈와 연결된 Git 태그 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `include_html_description` | `boolean` | N | `true`면 HTML 렌더링된 릴리즈 설명을 포함 |

## Response
### `200 OK`

`06-List all releases in a group`과 동일한 스키마.

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not found |
