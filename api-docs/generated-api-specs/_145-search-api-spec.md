# Search API Spec

## 04-Search an instance [GET]

## 기본 정보
- **기능:** 전체 GitLab 인스턴스 범위에서 검색을 수행합니다.
- **Endpoint:** `GET /api/v4/search`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
전체 GitLab 인스턴스를 대상으로 검색어를 조회합니다. 응답 형식은 요청한 `scope` 값에 따라 달라집니다. 고급 검색, 정규식 코드 검색 등을 지원합니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `search` | `string` | Y | 검색어 |
| `scope` | `string` | Y | 검색 범위 |
| `state` | `string` | N | 상태별 필터 |
| `confidential` | `boolean` | N | 기밀 여부 필터 |
| `type` | `array` | N | 작업 항목 타입 필터 (work_items scope 전용) |
| `include_archived` | `boolean` | N | 보관된 프로젝트 포함 (GitLab 18.9+) |
| `fields` | `array` | N | 검색 대상 필드 배열 (고급 검색) |
| `exclude_forks` | `boolean` | N | 포크 제외 (정확한 코드 검색, GitLab 18.9+) |
| `num_context_lines` | `integer` | N | 일치 항목 주변 컨텍스트 라인 수 (GitLab 18.11+) |
| `regex` | `boolean` | N | 정규식 코드 검색 (GitLab 18.9+) |
| `page` | `integer` | N | 현재 페이지 번호 |
| `per_page` | `integer` | N | 페이지당 항목 수 |

## Response
### `200 OK`

응답은 `scope` 값에 따라 달라집니다.

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |

---

## 05-Search on GitLab within a group [GET]

## 기본 정보
- **기능:** 특정 그룹 범위 내에서 검색을 수행합니다.
- **Endpoint:** `GET /api/v4/groups/{id}/(-/)search`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
GitLab 10.5에서 도입되었습니다. 지정된 그룹 내에서 검색어를 조회합니다. `scope`에 따라 결과 형식이 결정됩니다.

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
| `search` | `string` | Y | 검색어 |
| `scope` | `string` | Y | 검색 범위 |
| `state` | `string` | N | 상태별 필터 |
| `confidential` | `boolean` | N | 기밀 여부 필터 |
| `type` | `array` | N | 작업 항목 타입 필터 |
| `include_archived` | `boolean` | N | 보관된 프로젝트 포함 (GitLab 18.9+) |
| `fields` | `array` | N | 검색 대상 필드 배열 (고급 검색) |
| `exclude_forks` | `boolean` | N | 포크 제외 (GitLab 18.9+) |
| `num_context_lines` | `integer` | N | 컨텍스트 라인 수 (GitLab 18.11+) |
| `regex` | `boolean` | N | 정규식 코드 검색 (GitLab 18.9+) |
| `page` | `integer` | N | 현재 페이지 번호 |
| `per_page` | `integer` | N | 페이지당 항목 수 |

## Response
### `200 OK`

`scope` 값에 따라 응답이 달라집니다.

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 404 | Not Found |

---

## 06-Search on GitLab within a project [GET]

## 기본 정보
- **기능:** 특정 프로젝트 범위 내에서 검색을 수행합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/(-/)search`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
GitLab 10.5에서 도입되었습니다. 지정된 프로젝트 내에서 검색어를 조회합니다. 브랜치/태그 지정이 가능하며 `scope`에 따라 결과 형식이 결정됩니다.

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
| `search` | `string` | Y | 검색어 |
| `scope` | `string` | Y | 검색 범위 |
| `ref` | `string` | N | 검색 대상 브랜치 또는 태그. 미지정 시 기본 브랜치 사용 |
| `state` | `string` | N | 상태별 필터 |
| `confidential` | `boolean` | N | 기밀 여부 필터 |
| `type` | `array` | N | 작업 항목 타입 필터 |
| `fields` | `array` | N | 검색 대상 필드 배열 (고급 검색) |
| `num_context_lines` | `integer` | N | 컨텍스트 라인 수 (GitLab 18.11+) |
| `regex` | `boolean` | N | 정규식 코드 검색 (GitLab 18.9+) |
| `page` | `integer` | N | 현재 페이지 번호 |
| `per_page` | `integer` | N | 페이지당 항목 수 |

## Response
### `200 OK`

`scope` 값에 따라 응답이 달라집니다.

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 404 | Not Found |
