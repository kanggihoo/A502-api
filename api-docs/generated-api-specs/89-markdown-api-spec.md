# Markdown API Spec

## 01-Render Markdown content [POST]

## 기본 정보
- **기능:** Markdown 콘텐츠를 HTML로 렌더링합니다.
- **Endpoint:** `POST /api/v4/markdown`
- **인증:** Bearer Token 필요
- **권한:** `api`
- **멱등성:** 미지원

## 설명
제공된 Markdown 텍스트를 HTML로 변환하여 반환합니다. GitLab Flavored Markdown(GFM) 렌더링 및 프로젝트 컨텍스트 내 참조 생성을 지원합니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Body
```json
{
  "text": string,
  "gfm": boolean,
  "project": string
}
```

| 필드 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `text` | `string` | Y | 렌더링할 Markdown 텍스트 |
| `gfm` | `boolean` | N | GitLab Flavored Markdown 사용 여부. 기본값 `false` |
| `project` | `string` | N | GFM 참조 생성 시 컨텍스트로 사용할 프로젝트 경로 |

## Response
### `201 Created`

```json
{
  "html": string
}
```

## Errors
| 상태 | 의미 |
|---|---:|
| 400 | Bad request |
| 401 | Unauthorized |
