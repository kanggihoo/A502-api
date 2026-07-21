# 78 - Jira Forge Subscriptions API Specification

---

## 1. List GitLab for Jira (Forge) namespace subscriptions

## 기본 정보
- **기능:** Forge 설치에 구독된 GitLab 네임스페이스 목록을 조회한다.
- **Endpoint:** `GET /api/v4/integrations/jira_forge/subscriptions`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
Jira Forge 통합을 위해 구독된 GitLab 네임스페이스 목록을 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `created_at` | `string` | 구독 생성일시 |
| `unlink_path` | `string` | 연결 해제 경로 |
| `group.name` | `string` | 그룹 이름 |
| `group.avatar_url` | `string` | 그룹 아바타 URL |
| `group.full_name` | `string` | 그룹 전체 이름 |
| `group.description` | `string` | 그룹 설명 |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `401 Unauthorized` | 인증 실패 |
