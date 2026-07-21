# Remote Mirrors API Spec

## 01-List the project's remote mirrors [GET]

## 기본 정보
- **기능:** 프로젝트의 원격 미러 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/remote_mirrors`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트에 설정된 원격 미러(푸시 미러) 목록을 반환합니다.

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
| `id` | integer | 미러 ID |
| `enabled` | boolean | 미러 활성화 여부 |
| `url` | string | 원격 미러 URL |
| `update_status` | string | 업데이트 상태 (none, updating, failed 등) |
| `last_update_at` | string | 마지막 업데이트 일시 |
| `last_update_started_at` | string | 마지막 업데이트 시작 일시 |
| `last_successful_update_at` | string | 마지막 성공 업데이트 일시 |
| `last_error` | string | 마지막 오류 메시지 |
| `only_protected_branches` | boolean | 보호 브랜치만 미러링 여부 |
| `keep_divergent_refs` | boolean | 분기된 참조 유지 여부 |
| `auth_method` | string | 인증 방법 (ssh_public_key, password 등) |
| `host_keys[]` | array | 호스트 키 목록 |
| `host_keys[].fingerprint_sha256` | string | SHA256 지문 |
| `mirror_branch_regex` | string | 미러링할 브랜치 정규식 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
