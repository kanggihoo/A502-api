# 29-ci-triggers — CI/CD Trigger API

외부에서 파이프라인을 트리거하는 토큰을 관리한다.

---

## 01 — Trigger a pipeline with a token [POST]

### 기본 정보
- **기능:** 트리거 토큰을 사용해 파이프라인을 실행한다
- **Endpoint:** `POST /api/v4/projects/{id}/(ref/{ref}/)trigger/pipeline`
- **인증:** Bearer Token 또는 trigger token
- **권한:** `api` (Bearer Token 사용 시)
- **멱등성:** 미지원

### 설명
트리거 토큰을 사용하여 지정된 프로젝트에서 파이프라인을 실행한다. CI/CD job token을 사용하면 multi-project pipeline이 생성된다. Trigger token을 사용하면 upstream pipeline과 연결되지 않는다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N (token body 필드로 대체 가능) | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |
| `ref` | string | Y | 커밋 SHA, 브랜치 또는 태그 이름 |

#### Body (application/json)
| 필드 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `token` | string | Y | 트리거 토큰 또는 job token |
| `variables` | object | N | 파이프라인에 주입할 변수 (키-값 쌍) |
| `inputs` | object | N | 파이프라인 생성에 사용할 입력 값 |

### Response
#### `201 Created`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | integer | 파이프라인 ID | `1` |
| `iid` | integer | 프로젝트 내 파이프라인 IID | `1` |
| `project_id` | integer | 프로젝트 ID | `1` |
| `sha` | string | 커밋 SHA | `abc123` |
| `ref` | string | 브랜치/태그 이름 | `main` |
| `status` | string | 파이프라인 상태 | `pending` |
| `source` | string | 트리거 소스 | `trigger` |
| `created_at` | string | 생성 일시 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `updated_at` | string | 수정 일시 (ISO 8601) | `2024-01-01T00:00:01Z` |
| `web_url` | string | GitLab UI 파이프라인 페이지 URL | `https://gitlab.com/...` |
| `before_sha` | string | 이전 커밋 SHA | `000...` |
| `tag` | boolean | 태그 파이프라인 여부 | `false` |
| `yaml_errors` | string | YAML 오류 메시지 (없으면 null) | `null` |
| `user` | object | 트리거한 사용자 정보 | `{id: 1, username: "user", ...}` |
| `started_at` | string | 시작 일시 | `2024-01-01T00:00:02Z` |
| `finished_at` | string | 완료 일시 | `null` |
| `committed_at` | string | 커밋 일시 | `2024-01-01T00:00:00Z` |
| `duration` | integer | 실행 시간 (초) | `null` |
| `queued_duration` | integer | 대기 시간 (초) | `null` |
| `coverage` | number | 코드 커버리지 | `null` |
| `detailed_status` | object | 상세 상태 정보 | `{icon: "status_pending", ...}` |
| `archived` | boolean | 아카이브 여부 | `false` |

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 400 | 잘못된 요청 |
| 401 | 인증 실패 |
| 403 | 금지됨 (권한 부족) |
| 404 | 프로젝트를 찾을 수 없음 |

---

## 02 — List all project trigger tokens [GET]

### 기본 정보
- **기능:** 프로젝트의 모든 파이프라인 트리거 토큰 목록을 조회한다
- **Endpoint:** `GET /api/v4/projects/{id}/triggers`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트에 등록된 모든 트리거 토큰을 반환한다. 각 토큰의 설명, 소유자, 마지막 사용일, 만료일을 확인할 수 있다.

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

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | integer | 트리거 ID | `1` |
| `token` | string | 트리거 토큰 값 | `abc123...` |
| `description` | string | 트리거 설명 | `Deploy trigger` |
| `created_at` | string | 생성 일시 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `updated_at` | string | 수정 일시 (ISO 8601) | `2024-01-02T00:00:00Z` |
| `last_used` | string | 마지막 사용 일시 | `2024-01-03T00:00:00Z` |
| `expires_at` | string | 만료 일시 | `2025-01-01T00:00:00Z` |
| `owner` | object | 트리거 소유자 사용자 정보 | `{id: 1, username: "admin", ...}` |

`owner` 객체 상세:
| 필드 | 타입 | 설명 |
|---|---:|---:|---|
| `id` | integer | 사용자 ID |
| `username` | string | 사용자명 |
| `public_email` | string | 공개 이메일 |
| `name` | string | 표시 이름 |
| `state` | string | 계정 상태 (`active`, `blocked`) |
| `locked` | boolean | 계정 잠금 여부 |
| `avatar_url` | string | 아바타 URL |
| `web_url` | string | 사용자 프로필 URL |

### Errors
| 상태 코드 | 설명 |
|---|---:|---:|
| 400 | 잘못된 요청 |
| 401 | 인증 실패 |
| 403 | 금지됨 (권한 부족) |
| 404 | 프로젝트를 찾을 수 없음 |

---

## 연동 참고사항

- Trigger token은 외부 CI/CD 파이프라인 트리거에 사용된다. Jenkins 등 외부 도구에서 GitLab 파이프라인을 실행할 때 유용하다.
- Trigger token은 API 응답에 포함되므로 저장 시 보안에 주의해야 한다.
- Bearer Token을 사용하는 경우 `api` 권한이 필요하지만, trigger token만 body에 전달하면 별도 인증 없이 사용 가능하다.
- 프로젝트당 여러 개의 trigger token을 생성할 수 있으며, 용도별로 분리하여 관리할 수 있다.
- 토큰에 만료일(`expires_at`)을 설정할 수 있다.
