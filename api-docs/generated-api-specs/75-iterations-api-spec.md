# 75-이터레이션(Iterations) API 명세

## 01-List all project iterations

## 기본 정보
- **기능:** 특정 프로젝트의 모든 이터레이션을 조회한다. (GitLab 13.5+)
- **Endpoint:** `GET /api/v4/projects/{id}/iterations`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트의 모든 이터레이션 목록을 반환한다. Iteration cadence의 **Enable automatic scheduling**으로 생성된 이터레이션은 `title`과 `description`이 `null`로 반환된다.

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
| `state` | string | N | 상태 필터 (`opened`, `upcoming`, `current`, `closed`, `all`). `started`는 14.1부터 deprecated |
| `search` | string | N | 이터레이션 제목 검색어 |
| `in` | array | N | 퍼지 검색 대상 필드 (`title`, `cadence_title`). 기본값 `[title]` |
| `include_ancestors` | boolean | N | 상위 그룹 및 그 상위 그룹의 이터레이션 포함 |
| `include_descendants` | boolean | N | 하위 그룹 이터레이션 포함 |
| `updated_before` | string | N | 업데이트 시간 이전 필터 (ISO 8601) |
| `updated_after` | string | N | 업데이트 시간 이후 필터 (ISO 8601) |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `id` | integer | 이터레이션 ID | `1` |
| `iid` | integer | 그룹 내 IID | `1` |
| `sequence` | integer | 시퀀스 번호 | `1` |
| `group_id` | integer | 그룹 ID | `6789` |
| `title` | string | 이터레이션 제목 (자동 스케줄링 시 `null`) | `Sprint 1` |
| `description` | string | 이터레이션 설명 (자동 스케줄링 시 `null`) | `First sprint` |
| `state` | integer | 상태 (`1`: opened, `2`: current, `3`: closed) | `1` |
| `created_at` | string | 생성 일시 | `2025-01-01T00:00:00.000+09:00` |
| `updated_at` | string | 업데이트 일시 | `2025-01-02T00:00:00.000+09:00` |
| `start_date` | string | 시작일 | `2025-01-01` |
| `due_date` | string | 마감일 | `2025-01-14` |
| `web_url` | string | 웹 UI URL | `https://gitlab.example.com/groups/group/-/iterations/1` |

JSON 예시:
```json
[
  {
    "id": 1,
    "iid": 1,
    "sequence": 1,
    "group_id": 6789,
    "title": "Sprint 1",
    "description": "First sprint",
    "state": 1,
    "created_at": "2025-01-01T00:00:00.000+09:00",
    "updated_at": "2025-01-02T00:00:00.000+09:00",
    "start_date": "2025-01-01",
    "due_date": "2025-01-14",
    "web_url": "https://gitlab.example.com/groups/group/-/iterations/1"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 프로젝트를 찾을 수 없음 |

---

## 02-List all group iterations

## 기본 정보
- **기능:** 특정 그룹의 모든 이터레이션을 조회한다. (GitLab 13.5+)
- **Endpoint:** `GET /api/v4/groups/{id}/iterations`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 그룹의 모든 이터레이션 목록을 반환한다.

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
| `state` | string | N | 상태 필터 (`opened`, `upcoming`, `current`, `closed`, `all`) |
| `search` | string | N | 이터레이션 제목 검색어 |
| `in` | array | N | 퍼지 검색 대상 필드 (`title`, `cadence_title`). 기본값 `[title]` |
| `include_ancestors` | boolean | N | 상위 그룹 이터레이션 포함 |
| `include_descendants` | boolean | N | 하위 그룹 이터레이션 포함 |
| `updated_before` | string | N | 업데이트 시간 이전 필터 (ISO 8601) |
| `updated_after` | string | N | 업데이트 시간 이후 필터 (ISO 8601) |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
Project iterations와 동일한 응답 스키마를 사용한다.

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 그룹을 찾을 수 없음 |
