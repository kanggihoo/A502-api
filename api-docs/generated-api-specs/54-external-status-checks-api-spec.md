# External Status Checks API Spec

## 02-Retrieve project external status check services [GET]

## 기본 정보
- **기능:** 프로젝트의 외부 상태 검사 서비스 조회
- **Endpoint:** `GET /api/v4/projects/{id}/external_status_checks`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트에 등록된 외부 상태 검사(External Status Check) 서비스 정보를 반환합니다.

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

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | integer | 상태 검사 ID |
| `name` | string | 서비스 이름 |
| `project_id` | integer | 프로젝트 ID |
| `external_url` | string | 외부 서비스 URL |
| `protected_branches[]` | array | 적용되는 보호 브랜치 목록 |
| `protected_branches[].id` | integer | 브랜치 ID |
| `protected_branches[].name` | string | 브랜치 이름 |
| `protected_branches[].push_access_levels[]` | array | 푸시 접근 레벨 |
| `protected_branches[].merge_access_levels[]` | array | 병합 접근 레벨 |
| `protected_branches[].allow_force_push` | boolean | 강제 푸시 허용 여부 |
| `protected_branches[].code_owner_approval_required` | boolean | code owner 승인 필요 여부 |
| `hmac` | boolean | HMAC 서명 사용 여부 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 404 | Not Found |

---

## 06-List all status checks for a merge request [GET]

## 기본 정보
- **기능:** MR의 외부 상태 검사 목록 및 상태 조회
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/status_checks`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 merge request에 적용된 외부 상태 검사 서비스와 각각의 상태를 반환합니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `merge_request_iid` | integer | Y | MR의 IID |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | integer | 상태 검사 ID |
| `name` | string | 상태 검사 이름 |
| `external_url` | string | 외부 서비스 URL |
| `status` | string | 상태 (passed, failed, pending 등) |

## Errors
| 상태 | 설명 |
|---|---:|
| 404 | Not Found |
