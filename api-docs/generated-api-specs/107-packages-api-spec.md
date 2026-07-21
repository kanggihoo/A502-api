# Packages API Spec

## 01-List all packages for a project [GET]

## 기본 정보
- **기능:** 프로젝트의 모든 패키지 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/packages`
- **인증:** Bearer Token 필요 (public 프로젝트는 인증 없이 가능)
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트의 모든 패키지를 반환합니다. 모든 패키지 유형이 결과에 포함됩니다. 기본적으로 `default`, `deprecated`, `error` 상태의 패키지를 반환하며, `status` 파라미터로 다른 상태를 조회할 수 있습니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | 액세스 토큰 (public 프로젝트는 선택) | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |
| `order_by` | string | N | 정렬 필드 (`created_at`, `name`, `version`, `type`) |
| `sort` | string | N | 정렬 방향 (`asc`, `desc`) |
| `package_type` | string | N | 패키지 유형 필터 |
| `package_name` | string | N | 패키지 이름 필터 |
| `package_version` | string | N | 패키지 버전 필터 |
| `include_versionless` | boolean | N | 버전 없는 패키지 포함 여부 |
| `status` | string | N | 패키지 상태 필터 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | integer | 패키지 ID |
| `name` | string | 패키지 이름 |
| `conan_package_name` | string | Conan 패키지 이름 |
| `version` | string | 패키지 버전 |
| `package_type` | string | 패키지 유형 |
| `status` | string | 패키지 상태 |
| `_links` | string | 관련 링크 |
| `created_at` | string | 생성 일시 |
| `last_downloaded_at` | string | 마지막 다운로드 일시 |
| `creator_id` | integer | 생성자 ID |
| `project_id` | integer | 프로젝트 ID |
| `project_path` | string | 프로젝트 경로 |
| `tags` | string | 태그 |
| `pipeline` | object | 연결된 파이프라인 |
| `pipeline.id` | integer | 파이프라인 ID |
| `pipeline.sha` | string | SHA |
| `pipeline.ref` | string | 브랜치 참조 |
| `pipeline.status` | string | 파이프라인 상태 |
| `pipeline.web_url` | string | 파이프라인 URL |
| `versions[]` | array | 버전 목록 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 403 | Forbidden |
| 404 | Project Not Found |

---

## 08-List all packages for a group [GET]

## 기본 정보
- **기능:** 그룹의 모든 패키지 목록 조회
- **Endpoint:** `GET /api/v4/groups/{id}/packages`
- **인증:** Bearer Token 필요 (public 그룹은 인증 없이 가능)
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 그룹의 모든 패키지를 반환합니다. 기본적으로 `default`, `deprecated`, `error` 상태의 패키지를 반환하며, `status` 파라미터로 다른 상태를 조회할 수 있습니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | 액세스 토큰 (public 그룹은 선택) | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 그룹 ID 또는 URL-인코딩된 경로 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `exclude_subgroups` | boolean | N | 서브그룹 제외 여부 |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |
| `order_by` | string | N | 정렬 필드 (`created_at`, `name`, `version`, `type`) |
| `sort` | string | N | 정렬 방향 (`asc`, `desc`) |
| `package_type` | string | N | 패키지 유형 필터 |
| `package_name` | string | N | 패키지 이름 필터 |
| `package_version` | string | N | 패키지 버전 필터 |
| `include_versionless` | boolean | N | 버전 없는 패키지 포함 여부 |
| `status` | string | N | 패키지 상태 필터 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | integer | 패키지 ID |
| `name` | string | 패키지 이름 |
| `conan_package_name` | string | Conan 패키지 이름 |
| `version` | string | 패키지 버전 |
| `package_type` | string | 패키지 유형 |
| `status` | string | 패키지 상태 |
| `_links` | string | 관련 링크 |
| `created_at` | string | 생성 일시 |
| `last_downloaded_at` | string | 마지막 다운로드 일시 |
| `creator_id` | integer | 생성자 ID |
| `project_id` | integer | 프로젝트 ID |
| `project_path` | string | 프로젝트 경로 |
| `tags` | string | 태그 |
| `pipeline` | object | 연결된 파이프라인 |
| `versions[]` | array | 버전 목록 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Group Not Found |
