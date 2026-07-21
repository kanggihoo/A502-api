# Container Registry API Spec

## 01-List all registry repositories for a project [GET]

## 기본 정보
- **기능:** 프로젝트의 모든 컨테이너 레지스트리 저장소 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/registry/repositories`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트의 모든 컨테이너 레지스트리 저장소를 반환합니다. 페이지네이션 지원 (기본 20개).

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
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |
| `tags` | boolean | N | 태그 포함 여부 |
| `tags_count` | boolean | N | 태그 개수 포함 여부 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | integer | 저장소 ID |
| `name` | string | 저장소 이름 |
| `path` | string | 저장소 경로 |
| `project_id` | integer | 프로젝트 ID |
| `location` | string | 레지스트리 위치 |
| `created_at` | string | 생성 일시 |
| `cleanup_policy_started_at` | string | 정리 정책 마지막 실행 일시 |
| `tags_count` | integer | 태그 개수 |
| `tags[]` | array | 태그 목록 |
| `tags[].name` | string | 태그 이름 |
| `tags[].path` | string | 태그 경로 |
| `tags[].location` | string | 태그 위치 |
| `delete_api_path` | string | 삭제 API 경로 |
| `size` | integer | 저장소 크기 |
| `status` | string | 저장소 상태 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |

---

## 03-List all registry repository tags for a project [GET]

## 기본 정보
- **기능:** 특정 레지스트리 저장소의 모든 태그 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/registry/repositories/{repository_id}/tags`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 컨테이너 레지스트리 저장소의 모든 태그를 반환합니다. 페이지네이션 지원 (기본 20개).

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `repository_id` | integer | Y | 저장소 ID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `name` | string | 태그 이름 |
| `path` | string | 태그 경로 |
| `location` | string | 태그 위치 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 405 | Method Not Allowed |

---

## 07-List all registry repositories for a group [GET]

## 기본 정보
- **기능:** 그룹의 모든 컨테이너 레지스트리 저장소 목록 조회
- **Endpoint:** `GET /api/v4/groups/{id}/registry/repositories`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 그룹의 모든 컨테이너 레지스트리 저장소를 반환합니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 그룹 ID 또는 URL-인코딩된 경로 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | integer | 저장소 ID |
| `name` | string | 저장소 이름 |
| `path` | string | 저장소 경로 |
| `project_id` | integer | 프로젝트 ID |
| `location` | string | 레지스트리 위치 |
| `created_at` | string | 생성 일시 |
| `cleanup_policy_started_at` | string | 정리 정책 마지막 실행 일시 |
| `tags_count` | integer | 태그 개수 |
| `tags[]` | array | 태그 목록 |
| `delete_api_path` | string | 삭제 API 경로 |
| `size` | integer | 저장소 크기 |
| `status` | string | 저장소 상태 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Group Not Found |
