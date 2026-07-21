# 118-pipeline-schedules — 파이프라인 일정 API

정기 파이프라인 실행 일정을 관리한다.

---

## 01 — List all pipeline schedules [GET]

### 기본 정보
- **기능:** 프로젝트의 모든 파이프라인 일정 목록을 조회한다
- **Endpoint:** `GET /api/v4/projects/{id}/pipeline_schedules`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트에 등록된 모든 파이프라인 일정을 반환한다. 각 일정의 cron 표현식, 시간대, 활성화 여부, 다음 실행 시간을 확인할 수 있다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |
| `scope` | string | N | 파이프라인 일정 범위 필터 |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | integer | 일정 ID | `1` |
| `description` | string | 일정 설명 | `Nightly build` |
| `ref` | string | 대상 브랜치/태그 | `main` |
| `cron` | string | cron 표현식 | `0 2 * * *` |
| `cron_timezone` | string | cron 시간대 | `Asia/Seoul` |
| `next_run_at` | string | 다음 실행 예정 일시 (ISO 8601) | `2024-01-02T02:00:00Z` |
| `active` | boolean | 일정 활성화 여부 | `true` |
| `created_at` | string | 생성 일시 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `updated_at` | string | 수정 일시 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `owner` | object | 일정 소유자 사용자 정보 | `{id: 1, username: "admin", ...}` |
| `inputs` | object | 파이프라인 입력 변수 | `{"name": "value"}` |

`owner` 객체 상세:
| 필드 | 타입 | 설명 |
|---|---:|---:|---|
| `id` | integer | 사용자 ID |
| `username` | string | 사용자명 |
| `public_email` | string | 공개 이메일 |
| `name` | string | 표시 이름 |
| `state` | string | 계정 상태 |
| `locked` | boolean | 계정 잠금 여부 |
| `avatar_url` | string | 아바타 URL |
| `web_url` | string | 사용자 프로필 URL |

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 400 | 잘못된 요청 |
| 401 | 인증 실패 |
| 403 | 금지됨 (권한 부족) |
| 404 | 프로젝트를 찾을 수 없음 |

---

## 08 — Run a pipeline schedule [POST]

### 기본 정보
- **기능:** 파이프라인 일정을 즉시 실행한다
- **Endpoint:** `POST /api/v4/projects/{id}/pipeline_schedules/{pipeline_schedule_id}/play`
- **인증:** Bearer Token 필요
- **권한:** `api`
- **멱등성:** 미지원

### 설명
지정된 파이프라인 일정을 즉시 실행한다. 이 실행은 다음 정기 실행 일정에 영향을 주지 않는다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |
| `pipeline_schedule_id` | integer | Y | 실행할 파이프라인 일정 ID |

### Response
#### `201 Created`
본문 없이 생성 성공 응답을 반환한다.

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 400 | 잘못된 요청 |
| 401 | 인증 실패 |
| 403 | 금지됨 (권한 부족) |
| 404 | 일정 또는 프로젝트를 찾을 수 없음 |

---

## 연동 참고사항

- 파이프라인 일정은 cron 표현식을 기반으로 정기적으로 CI/CD 파이프라인을 실행한다.
- `scope` 파라미터로 `active` 또는 `inactive` 상태의 일정만 필터링할 수 있다. (`scope` 지원 여부는 GitLab 버전에 따라 다를 수 있음)
- 수동 실행(`POST .../play`)은 1회성 실행이며 cron 일정에 영향을 주지 않으므로, 테스트나 긴급 실행에 유용하다.
- 각 일정은 특정 브랜치/태그(`ref`)에 대해 실행되며, 입력 변수(`inputs`)를 통해 동적 값을 전달할 수 있다.
- 일정 생성, 수정, 삭제는 각각 POST/PUT/DELETE 메서드로 가능하다.
