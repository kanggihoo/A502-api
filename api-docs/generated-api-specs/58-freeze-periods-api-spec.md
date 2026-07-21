# 58 - Freeze Periods API Specification

---

## 1. List all freeze periods

## 기본 정보
- **기능:** 특정 프로젝트의 모든 프리즈 기간(freeze period) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/freeze_periods`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트에 설정된 모든 배포 프리즈 기간을 반환한다. 프리즈 기간 동안에는 배포가 제한된다.

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
| `page` | `integer` | N | 페이지 번호 (기본: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본: 20) |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 프리즈 기간 ID |
| `freeze_start` | `string` | 프리즈 시작 시간 (cron 표현식) |
| `freeze_end` | `string` | 프리즈 종료 시간 (cron 표현식) |
| `cron_timezone` | `string` | cron 시간대 |
| `created_at` | `string` | 생성일시 |
| `updated_at` | `string` | 업데이트일시 |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `401 Unauthorized` | 인증 실패 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |
