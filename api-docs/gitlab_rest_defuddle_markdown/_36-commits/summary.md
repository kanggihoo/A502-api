# Commits API 명세서 (관리자 권한 미필요 API)

본 문서는 `_36-commits` 디렉토리 내의 GitLab Commits (저장소 커밋 목록 조회, 직접 커밋 생성, Diff 변경사항 조회, 커밋 댓글 작성, 체리픽, 리버트 및 연관 MR/GPG 서명 조회) 관련 API 중 일반 사용자 및 프로젝트 멤버(Developer, Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 12개)

---

## 01. List all repository commits [GET]

### 기본 정보

- **기능:** 프로젝트 저장소의 커밋 이력 목록을 필터링 및 정렬하여 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

프로젝트 저장소의 특정 브랜치(`ref_name`)나 파일 경로(`path`), 특정 작성자(`author`), 날짜 범위(`since`, `until`) 조건을 지정하여 커밋 로그 이력을 조회합니다. `with_stats=true` 옵션을 적용하면 커밋별 변경 라인 수(additions, deletions, total) 통계 정보를 함께 수집합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `ref_name` | string | N | default branch | 대상 브랜치명 또는 태그명 | `main` |
| `path` | string | N | - | 특정 파일 또는 디렉토리 상대 경로 | `src/main/App.java` |
| `author` | string | N | - | 커밋 작성자 이름 또는 이메일 | `kkh` |
| `since` | string | N | - | 조회 시작 날짜 (ISO 8601) | `2026-07-01T00:00:00Z` |
| `until` | string | N | - | 조회 종료 날짜 (ISO 8601) | `2026-07-23T23:59:59Z` |
| `with_stats` | boolean | N | `false` | 커밋별 코드 변경 통계 포함 여부 | `true` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | Full 커밋 해시 (40자리) | `a1b2c3d4e5f67890...` |
| `short_id` | string | 8자리 커밋 SHA | `a1b2c3d4` |
| `title` | string | 커밋 메시지 첫 줄 제목 | `feat: add user login API` |
| `message` | string | 커밋 메시지 전체 | `feat: add user login API\n\nImplement JWT token issue` |
| `author_name` | string | 작성자 이름 | `강기후` |
| `author_email` | string | 작성자 이메일 | `kkh@ssafy.com` |
| `created_at` | string | 커밋 작성 시각 | `2026-07-23T10:00:00Z` |

```json
[
  {
    "id": "a1b2c3d4e5f67890123456789abcdef012345678",
    "short_id": "a1b2c3d4",
    "title": "feat: add user login API",
    "message": "feat: add user login API\n\nImplement JWT token issue",
    "author_name": "강기후",
    "author_email": "kkh@ssafy.com",
    "authored_date": "2026-07-23T10:00:00Z",
    "committer_name": "강기후",
    "committer_email": "kkh@ssafy.com",
    "committed_date": "2026-07-23T10:00:00Z",
    "web_url": "https://lab.ssafy.com/my-org/my-project/-/commit/a1b2c3d4e5f67890123456789abcdef012345678"
  }
]
```

---

## 02. Create a commit [POST]

### 기본 정보

- **기능:** 여러 파일의 생성/수정/삭제 액션을 묶어 원격 브랜치에 직접 커밋을 생성한다.
- **Endpoint:** `POST /api/v4/projects/{id}/repository/commits`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### 설명

Git CLI 클라이언트 통신 없이 REST API를 통해 하나 이상의 파일 생성(`create`), 수정(`update`), 삭제(`delete`), 이동(`move`) 동작(`actions` 배열)을 지정하여 단일 커밋으로 원격 저장소 브랜치(`branch`)에 직접 반영합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `branch` | string | Y | - | 커밋을 등록할 대상 브랜치명 | `main` |
| `commit_message` | string | Y | - | 커밋 메시지 | `docs: update README.md` |
| `actions` | array[object] | Y | 1개 이상 | 파일 변경 액션 배열 | `[ { "action": "update", "file_path": "README.md", "content": "# Hello" } ]` |
| `start_branch` | string | N | - | 신규 브랜치 자동 생성 시 기준 분기 브랜치 | `main` |

```json
{
  "branch": "main",
  "commit_message": "docs: update README.md via API",
  "actions": [
    {
      "action": "update",
      "file_path": "README.md",
      "content": "# A502 API Integration Project\n\nSSAFY Workspace API Document"
    }
  ]
}
```

### Response

#### `201 Created`

```json
{
  "id": "b2c3d4e5f6...",
  "short_id": "b2c3d4e5",
  "title": "docs: update README.md via API",
  "author_name": "강기후",
  "created_at": "2026-07-23T10:05:00Z"
}
```

---

## 03. Retrieve a commit [GET]

### 기본 정보

- **기능:** 특정 커밋 SHA의 상세 메타데이터 및 작성 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{sha}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `sha` | string | Y | 커밋 해시 (SHA 또는 브랜치/태그 이름) | `a1b2c3d4e5f6...` |

### Response

#### `200 OK`

```json
{
  "id": "a1b2c3d4e5f6...",
  "short_id": "a1b2c3d4",
  "title": "feat: add user login API",
  "stats": {
    "additions": 45,
    "deletions": 10,
    "total": 55
  }
}
```

---

## 04. Retrieve a commit diff [GET]

### 기본 정보

- **기능:** 특정 커밋에서 변경된 파일들의 패치 Diff(차이점) 내용을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{sha}/diff`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

해당 커밋에서 변경된 각 파일의 구 파일 경로(`old_path`), 신규 파일 경로(`new_path`), 신규/삭제 파일 여부(`new_file`, `deleted_file`), 그리고 git diff 텍스트 패치 내용(`diff`)을 가져옵니다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `sha` | string | Y | 커밋 해시 | `a1b2c3d4e5f6...` |

### Response

#### `200 OK`

```json
[
  {
    "diff": "@@ -1,3 +1,5 @@\n # Title\n+New line added\n",
    "new_path": "README.md",
    "old_path": "README.md",
    "a_mode": "100644",
    "b_mode": "100644",
    "new_file": false,
    "renamed_file": false,
    "deleted_file": false
  }
]
```

-
## 07. Retrieve a commit sequence [GET]

### 기본 정보

- **기능:** 특정 커밋의 시퀀스 순서 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{sha}/sequence`
- **인증:** Bearer Token 필요


## 10. List all references a commit is pushed to [GET]

### 기본 정보

- **기능:** 특정 커밋 해시가 포함되어 있는 브랜치 및 태그 레퍼런스 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{sha}/refs`
- **인증:** Bearer Token 필요

### Request

#### Query parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `type` | string | N | 레퍼런스 범주 (`branch` \| `tag` \| `all`) | `branch` |

### Response

#### `200 OK`

```json
[
  { "type": "branch", "name": "main" },
  { "type": "branch", "name": "feature/login" }
]
```

---

## 11. List all merge requests for a commit [GET]

### 기본 정보

- **기능:** 특정 커밋이 포함되어 병합되었거나 연결된 Merge Request 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{sha}/merge_requests`
- **인증:** Bearer Token 필요

### Response

#### `200 OK`

```json
[
  {
    "id": 102,
    "iid": 15,
    "project_id": 1234,
    "title": "Resolve user login API issue",
    "state": "merged"
  }
]
```


