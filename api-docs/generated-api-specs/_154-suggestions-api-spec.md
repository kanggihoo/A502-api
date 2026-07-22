# Suggestions API Spec
**타인 프로젝트에 봇이 들어가는 2가지 방법:**


### 방법 A: CodeRabbit 방식 (OAuth2 활용 자동 멤버 추가)

1. 내가 만든 서비스 전용 **글로벌 봇 계정**(`my-ai-bot`) 생성.
2. 타인이 내 서비스 사이트에서 **"GitLab 프로젝트 연결" (OAuth2 승인)** 클릭.
3. 내 백엔드가 타인의 승인 토큰을 써서 **타인 프로젝트 멤버 목록에 `my-ai-bot`을 Developer로 추가** (`POST /projects/{id}/members`).
4. 이제 `my-ai-bot` 계정이 타인 프로젝트 멤버가 되었으므로 **타인 프로젝트 MR에 봇 이름으로 리뷰 작성 가능.**

---

### 방법 B: BYOK 방식 (토큰 직접 입력받기)

1. 타인(프로젝트 주인)에게 *"네 프로젝트에서 Project Access Token 하나 만들어서 우리 서비스 설정창에 등록해 줘"* 라고 안내.
2. 타인이 발급해 준 토큰으로 내 백엔드가 타인 프로젝트 API 호출.

---

### 요약
- **OAuth2**: 타인이 버튼 누르면 봇 계정을 **타인 프로젝트 멤버로 자동 침투/추가**.
- **BYOK**: 타인이 봇 역할을 할 **토큰을 내 서비스에 등록**.
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
