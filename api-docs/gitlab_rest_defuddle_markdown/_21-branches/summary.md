# Branches API 명세서 (관리자 권한 미필요 API)

본 문서는 `_21-branches` 디렉토리 내의 GitLab Branches (저장소 브랜치 목록 조회, 생성, 삭제, 보호 설정 및 병합 완료 브랜치 정리) 관련 API 중 일반 사용자 및 프로젝트 멤버(Developer, Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 8개)

---

## 01. List all repository branches [GET]

### 기본 정보

- **기능:** 프로젝트 저장소의 모든 브랜치 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/branches`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

프로젝트 저장소에 존재하며 사전순으로 정렬된 브랜치 목록을 조회합니다. 각 브랜치의 최신 커밋 정보, 머지 여부(`merged`), 보호 여부(`protected`), 푸시 가능 여부(`can_push`) 등을 포함하여 가져오며, `search` 또는 `regex` 파라미터로 정규식/키워드 검색을 지원합니다.

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
| `search` | string | N | - | 브랜치 이름 검색어 | `feature` |
| `regex` | string | N | - | 브랜치 이름 정규식 패턴 | `^feature/.*` |
| `sort` | string | N | - | 정렬 기준 (`name_asc` \| `updated_asc` \| `updated_desc`) | `updated_desc` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `name` | string | 브랜치 이름 | `main` |
| `merged` | boolean | 기본 브랜치에 병합 완료 여부 | `false` |
| `protected` | boolean | 보호 브랜치 여부 | `true` |
| `default` | boolean | 기본 브랜치 여부 | `true` |
| `commit` | object | 브랜치 Head 커밋 상세 객체 | `{ "id": "a1b2c3...", "title": "feat: init" }` |

```json
[
  {
    "name": "main",
    "commit": {
      "id": "a1b2c3d4e5f6...",
      "short_id": "a1b2c3d4",
      "title": "feat: init project structure",
      "author_name": "홍길동",
      "created_at": "2026-07-23T10:00:00Z"
    },
    "merged": false,
    "protected": true,
    "developers_can_push": false,
    "developers_can_merge": true,
    "can_push": true,
    "default": true,
    "web_url": "https://lab.ssafy.com/my-org/my-project/-/tree/main"
  }
]
```

---


## 04. Retrieve a repository branch [GET]

### 기본 정보

- **기능:** 단일 브랜치의 상세 정보 및 최신 Head 커밋 내역을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/branches/{branch}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### Response

#### `200 OK`

```json
{
  "name": "main",
  "commit": {
    "id": "a1b2c3d4e5f6...",
    "title": "latest commit"
  },
  "merged": false,
  "protected": true,
  "default": true
}
```

---


---

## 06. Protect a single branch [PUT]

### 기본 정보

- **기능:** 단일 브랜치에 대해 기본적인 보호(Protection) 설정을 적용한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/repository/branches/{branch}/protect`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

### Request

#### Body

| 필드 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `developers_can_push` | boolean | N | `false` | Developer 역할 유저의 푸시 허용 여부 | `false` |
| `developers_can_merge` | boolean | N | `false` | Developer 역할 유저의 머지 허용 여부 | `true` |

```json
{
  "developers_can_push": false,
  "developers_can_merge": true
}
```

### Response

#### `200 OK`

```json
{
  "name": "main",
  "protected": true,
  "developers_can_push": false,
  "developers_can_merge": true
}
```

---

## 07. Unprotect a single branch [PUT]

### 기본 정보

- **기능:** 단일 브랜치의 기본 보호 설정을 해제한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/repository/branches/{branch}/unprotect`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

### Response

#### `200 OK`

```json
{
  "name": "main",
  "protected": false
}
```

---

