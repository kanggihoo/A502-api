# Markdown API 명세서 (관리자 권한 미필요 API)

본 문서는 `_89-markdown` 디렉토리 내의 GitLab Markdown (마크다운 텍스트를 HTML 렌더링 변환) 관련 API 중 일반 사용자 및 인증된 유저 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 1개)

---

## 01. Render Markdown content [POST]

### 기본 정보

- **기능:** 전달된 마크다운(GitLab Flavored Markdown) 텍스트를 파싱하여 HTML로 렌더링 변환한다.
- **Endpoint:** `POST /api/v4/markdown`
- **인증:** Bearer Token 필요 / 선택 사항
- **권한:** 모든 사용자 (인증 유저 및 공개 렌더링)

### 설명

입력받은 마크다운 문장(`text`)을 GitLab의 사양(GitLab Flavored Markdown: 이슈/MR 링크, 사용자 멘션 `@user`, 이모지 `:thumbsup:`, 코드 하이라이팅 등)에 맞추어 HTML 스트링으로 변환합니다. `gfm: true` 설정 시 프로젝트/그룹 컨텍스트(`project`, `gfm`)를 기반으로 한 하이퍼링크가 자동 생성됩니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters

없음

#### Query parameters

없음

#### Body

| 필드 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `text` | string | Y | - | HTML로 변환할 마크다운 원본 텍스트 | `# Hello World\nSee issue #1` |
| `gfm` | boolean | N | `false` | GitLab Flavored Markdown 연관 링크 활성화 여부 | `true` |
| `project` | string/integer | N | - | GFM 상대 링크 처리를 위한 프로젝트 ID 또는 경로 | `s15p11a502/A502-api` |

```json
{
  "text": "# Feature Proposal\n\nPlease check ~backend label and @kkh_ssafy.",
  "gfm": true,
  "project": "s15p11a502/A502-api"
}
```

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `html` | string | HTML 렌더링 결과 | `<h1>Feature Proposal</h1>...` |

```json
{
  "html": "<h1>Feature Proposal</h1>\n<p>Please check <span class=\"label\">backend</span> label and <a href=\"https://lab.ssafy.com/kkh_ssafy\">@kkh_ssafy</a>.</p>"
}
```
