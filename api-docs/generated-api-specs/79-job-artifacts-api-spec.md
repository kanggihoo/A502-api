# Job Artifacts API Spec

## 01-Retrieve job artifacts [GET]

## 기본 정보
- **기능:** 최신 성공한 Job의 아티팩트 아카이브를 다운로드합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/jobs/artifacts/{ref_name}/download`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 브랜치나 태그의 최신 성공한 Job에서 아티팩트 아카이브를 다운로드합니다. `HEAD`나 SHA 참조는 지원되지 않습니다.

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
| `ref_name` | `string` | Y | 브랜치 또는 태그 이름. `HEAD`/SHA 참조 미지원 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `job` | `string` | Y | Job 이름 |
| `job_token` | `string` | N | 멀티-프로젝트 파이프라인 트리거용 (Premium/Ultimate) |
| `search_recent_successful_pipelines` | `boolean` | N | 최신 파이프라인 외에 최근 성공한 파이프라인까지 검색 범위 확장 |

## Response
### `200 OK`

아티팩트 아카이브 파일 바이너리.

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not found |

---

## 02-Download the artifacts archive from a job [GET]

## 기본 정보
- **기능:** 특정 Job의 아티팩트 아카이브를 다운로드합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/jobs/{job_id}/artifacts`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
GitLab 8.5에서 도입되었습니다. Job ID를 기준으로 특정 Job의 아티팩트 아카이브를 다운로드합니다.

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
| `job_id` | `integer` | Y | Job ID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `job_token` | `string` | N | 멀티-프로젝트 파이프라인 트리거용 (Premium/Ultimate) |

## Response
### `200 OK`

아티팩트 아카이브 파일 바이너리.

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not found |

---

## 04-List all files in an artifacts archive [GET]

## 기본 정보
- **기능:** 아티팩트 아카이브 내의 모든 파일 목록을 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/jobs/{job_id}/artifacts/tree`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
아티팩트 아카이브를 추출하지 않고 내부 파일 목록을 조회합니다. 특정 경로 탐색, 재귀 조회, 페이지네이션을 지원합니다.

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
| `job_id` | `integer` | Y | Job ID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `path` | `string` | N | 아카이브 내 탐색 경로. 기본값은 루트 |
| `recursive` | `boolean` | N | `true`면 모든 항목을 재귀적으로 반환 |
| `job_token` | `string` | N | CI/CD Job Token (Premium/Ultimate) |
| `page` | `integer` | N | 현재 페이지 번호 |
| `per_page` | `integer` | N | 페이지당 항목 수 |

## Response
### `200 OK`

```json
{
  "name": string,
  "path": string,
  "type": string,
  "size": integer,
  "mode": string
}
```

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not found |
