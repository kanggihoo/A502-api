# 33 - Code Review Analytics API Specification
Tier: Premium, Ultimate

## 1. List code review information about project

## 기본 정보
- **기능:** 프로젝트의 코드 리뷰 정보를 조회한다.
- **Endpoint:** `GET /api/v4/analytics/code_review`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트의 코드 리뷰 관련 분석 정보를 반환한다. 머지 리퀘스트 단위로 데이터를 제공한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `project_id` | `integer` | Y | 프로젝트 ID |
| `label_name` | `array` | N | 필터링할 라벨 이름 배열 |
| `milestone_title` | `string` | N | 필터링할 마일스톤 제목 |
| `page` | `integer` | N | 페이지 번호 (기본: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본: 20) |
| `not` | `object` | N | 제외 필터를 담은 객체 |
| `not[label_name]` | `array` | N | 제외할 라벨 이름 배열 |
| `not[milestone_title]` | `string` | N | 제외할 마일스톤 제목 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | MR ID |
| `iid` | `integer` | MR 내부 ID |
| `project_id` | `integer` | 프로젝트 ID |
| `title` | `string` | MR 제목 |
| `description` | `string` | MR 설명 |
| `state` | `string` | MR 상태 |
| `created_at` | `string` | 생성일시 |
| `updated_at` | `string` | 업데이트일시 |
| `web_url` | `string` | 웹 URL |
| `milestone` | `object` | 마일스톤 정보 |
| `author` | `object` | 작성자 정보 |
| `approved_by` | `object` | 승인자 정보 |
| `notes_count` | `integer` | 코멘트 수 |
| `review_time` | `integer` | 리뷰 시간 (시간 단위) |
| `diff_stats` | `string` | Diff 통계 |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
