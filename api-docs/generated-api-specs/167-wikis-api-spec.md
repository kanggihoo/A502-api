# 167 - Wikis API Specification

---

## 1. List all wiki pages for a group

## 기본 정보
- **기능:** 특정 그룹의 모든 위키 페이지 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/wikis`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 그룹의 모든 위키 페이지 목록을 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 그룹의 ID 또는 URL 인코딩된 경로 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `with_content` | `boolean` | N | 페이지 내용 포함 여부 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `format` | `string` | 위키 페이지 포맷 |
| `slug` | `string` | 위키 페이지 slug |
| `title` | `string` | 제목 |
| `wiki_page_meta_id` | `integer` | 위키 페이지 메타 ID |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `404 Not Found` | 그룹을 찾을 수 없음 |

---

## 2. List all wiki pages for a project

## 기본 정보
- **기능:** 특정 프로젝트의 모든 위키 페이지 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/wikis`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트의 모든 위키 페이지 목록을 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 프로젝트의 ID 또는 URL 인코딩된 경로 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `with_content` | `boolean` | N | 페이지 내용 포함 여부 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `format` | `string` | 위키 페이지 포맷 |
| `slug` | `string` | 위키 페이지 slug |
| `title` | `string` | 제목 |
| `wiki_page_meta_id` | `integer` | 위키 페이지 메타 ID |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |

---

## 3. Retrieve a wiki page for a project

## 기본 정보
- **기능:** 특정 프로젝트의 단일 위키 페이지 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/wikis/{slug}`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트의 특정 위키 페이지를 slug로 조회한다. 내용(content) 포함 여부를 선택할 수 있다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 프로젝트의 ID 또는 URL 인코딩된 경로 |
| `slug` | `string` | Y | 위키 페이지의 slug |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `version` | `string` | N | 위키 페이지의 버전 해시 |
| `render_html` | `boolean` | N | 내용을 HTML로 렌더링 여부 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `format` | `string` | 위키 페이지 포맷 |
| `slug` | `string` | 위키 페이지 slug |
| `title` | `string` | 제목 |
| `wiki_page_meta_id` | `integer` | 위키 페이지 메타 ID |
| `content` | `string` | 페이지 내용 |
| `encoding` | `string` | 인코딩 방식 |
| `front_matter` | `object` | Front matter 데이터 |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `404 Not Found` | 위키 페이지 또는 프로젝트를 찾을 수 없음 |
