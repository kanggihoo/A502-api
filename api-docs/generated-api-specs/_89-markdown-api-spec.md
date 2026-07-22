# Markdown API Spec
**마크다운 텍스트를 HTML로 변환(렌더링)할 때 사용하는 API.**

---

### 주요 특장점
- **GFM (GitLab Flavored Markdown) 변환**:
  - 일반 마크다운 파서와 달리, **GitLab 특화 태그 자동 링크 파싱**:
    - `#123` → 해당 이슈 페이지 링크 (`<a href="...">#123</a>`)
    - `!45` → 해당 MR 페이지 링크
    - `@username` → 사용자 프로필 링크

---

### 언제 쓰나?
1. **에디터 실시간 미리보기 (Live Preview)**:
   - 통합 대시보드 웹 앱에서 댓글/이슈 작성 중 **"미리보기" 탭** 눌렀을 때 HTML 반환.
2. **README / 코멘트 본문 출력**:
   - 웹 화면에 GitLab 스타일 그대로 예쁘게 렌더링해서 보여줄 때.

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
