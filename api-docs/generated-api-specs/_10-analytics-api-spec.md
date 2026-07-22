# 10 - Analytics API Specification

---

## 1. List deployment frequencies for the project

## 기본 정보
- **기능:** 프로젝트의 배포 빈도(deployment frequency)를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/analytics/deployment_frequency`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트의 배포 빈도 데이터를 반환한다. 특정 환경과 시간 범위를 지정할 수 있다.

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
| `environment` | `string` | Y | 필터링할 환경 이름 |
| `from` | `string` | Y | 시작 일시 (포함) |
| `to` | `string` | N | 종료 일시 (제외) |
| `interval` | `string` | N | 데이터 롤업 간격 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `value` | `string` | 배포 빈도 값 |
| `from` | `string` | 시작 시간 |
| `to` | `string` | 종료 시간 |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |

---

## 2. Retrieve count of recently created issues for a group

## 기본 정보
- **기능:** 특정 그룹에서 최근 생성된 이슈 수를 조회한다.
- **Endpoint:** `GET /api/v4/analytics/group_activity/issues_count`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 그룹의 최근 이슈 생성 수를 반환한다. 최대 1000개까지 집계된다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `group_path` | `string` | Y | 그룹 경로 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `issues_count` | `integer` | 최근 생성된 이슈 수 (최대 1000) |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |

---

## 3. Retrieve count of recently created merge requests for a group

## 기본 정보
- **기능:** 특정 그룹에서 최근 생성된 머지 리퀘스트 수를 조회한다.
- **Endpoint:** `GET /api/v4/analytics/group_activity/merge_requests_count`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 그룹의 최근 MR 생성 수를 반환한다. 최대 1000개까지 집계된다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `group_path` | `string` | Y | 그룹 경로 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `merge_requests_count` | `integer` | 최근 생성된 MR 수 (최대 1000) |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |

---

## 4. Retrieve count of members recently added to a group

## 기본 정보
- **기능:** 특정 그룹에 최근 추가된 멤버 수를 조회한다.
- **Endpoint:** `GET /api/v4/analytics/group_activity/new_members_count`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 그룹의 최근 신규 멤버 수를 반환한다. 최대 1000명까지 집계된다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `group_path` | `string` | Y | 그룹 경로 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `new_members_count` | `integer` | 최근 추가된 멤버 수 (최대 1000) |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
