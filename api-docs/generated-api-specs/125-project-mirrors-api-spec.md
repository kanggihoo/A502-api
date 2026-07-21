# 125 - Project Mirrors API Specification

---

## 1. Retrieve project pull mirror details

## 기본 정보
- **기능:** 특정 프로젝트의 풀 미러(pull mirror) 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/mirror/pull`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트의 풀 미러링 설정과 상태 정보를 반환한다. 프로젝트가 미러링 대상이 아닌 경우 400 오류가 발생한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 프로젝트의 ID 또는 URL 인코딩된 경로 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 미러 ID |
| `update_status` | `string` | 업데이트 상태 |
| `url` | `string` | 미러 소스 URL |
| `last_error` | `string` | 마지막 오류 메시지 |
| `last_update_at` | `string` | 마지막 업데이트 시간 |
| `last_update_started_at` | `string` | 마지막 업데이트 시작 시간 |
| `last_successful_update_at` | `string` | 마지막 성공적 업데이트 시간 |
| `enabled` | `boolean` | 미러 활성화 여부 |
| `mirror_trigger_builds` | `boolean` | 미러 시 빌드 트리거 여부 |
| `only_mirror_protected_branches` | `boolean` | 보호된 브랜치만 미러 여부 |
| `mirror_overwrites_diverged_branches` | `boolean` | 분기된 브랜치 덮어쓰기 여부 |
| `mirror_branch_regex` | `string` | 미러할 브랜치 정규식 |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 프로젝트가 미러링 대상이 아님 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |
