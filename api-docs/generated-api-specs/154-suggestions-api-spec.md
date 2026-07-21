# Suggestions API Spec

## 01-Apply a suggestion to a merge request [PUT]

## 기본 정보
- **기능:** Merge Request에 제안된 패치를 적용합니다.
- **Endpoint:** `PUT /api/v4/suggestions/{id}/apply`
- **인증:** Bearer Token 필요
- **권한:** `api`
- **멱등성:** 미지원

## 설명
Merge Request에서 제안된 패치를 적용합니다. Developer, Maintainer 또는 Owner 역할이 필요합니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | `integer` | Y | Suggestion ID |

### Body
```json
{
  "commit_message": string
}
```

| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---:|---|
| `commit_message` | `string` | N | 기본 메시지 대신 사용할 커스텀 커밋 메시지 |

## Response
### `200 OK`

```json
{
  "id": integer,
  "from_line": integer,
  "to_line": integer,
  "appliable": boolean,
  "applied": boolean,
  "from_content": string,
  "to_content": string
}
```

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 404 | Not Found |
