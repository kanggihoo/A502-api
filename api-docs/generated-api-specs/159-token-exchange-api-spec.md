# Token Exchange API Spec

## 01-Issue a short-lived JWT for a single modular-service audience [POST]

## 기본 정보
- **기능:** 단일 모듈형 서비스 대상의 단기 RS256 JWT를 발급합니다.
- **Endpoint:** `POST /api/v4/token_exchange`
- **인증:** Bearer Token 필요
- **권한:** `api`
- **멱등성:** 미지원

## 설명
단일 모듈형 서비스 (예: Artifact Registry)로 범위가 지정된 단기 RS256 JWT를 발급합니다. 클레임에는 요청 사용자 ID(sub), 조직 ID, 배포 영역(saas/self-managed)이 포함됩니다. 해당 백엔드에 제시되며 인스턴스 JWKS에 대해 검증됩니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Body
```json
{
  "audience": "gitlab-artifact-registry",
  "expires_in": 300
}
```

| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---:|---|
| `audience` | `enum` | Y | 대상 서비스. 현재 `gitlab-artifact-registry`만 지원 |
| `expires_in` | `integer` | N | 요청 토큰 수명(초). 기본값 300, 최대 43200 |

## Response
### `201 Created`

JWT 토큰 문자열.

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
