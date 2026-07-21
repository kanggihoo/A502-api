# 40 - DORA Metrics API Specification

---

## 1. Retrieve project-level DORA metrics

## 기본 정보
- **기능:** 지정된 프로젝트의 DORA 메트릭을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/dora/metrics`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
DORA(Diagnostics Outcomes and Research for Accelerate) 메트릭을 프로젝트 수준에서 조회한다. 측정 가능한 메트릭: `deployment_frequency`, `lead_time_for_changes`, `time_to_restore_service`, `change_failure_rate`.

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
| `metric` | `string` | Y | 측정할 메트릭 (`deployment_frequency`, `lead_time_for_changes`, `time_to_restore_service`, `change_failure_rate`) |
| `start_date` | `string` | N | 시작일 (ISO 8601, 예: `2021-03-01`, 기본: 3개월 전) |
| `end_date` | `string` | N | 종료일 (ISO 8601, 기본: 현재 날짜) |
| `interval` | `string` | N | 버킷 간격 (`all`, `monthly`, `daily`, 기본: `daily`) |
| `environment_tiers` | `array` | N | 환경 티어 목록 (기본: `production`) |

## Response
### `200 OK`
응답 본문은 요청한 `metric`과 `interval` 파라미터에 따라 달라진다. 일반적으로 시간 범위별 메트릭 값 배열을 반환한다.

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `401 Unauthorized` | 인증 실패 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |
