# Search API 명세서 (관리자 권한 미필요 API)


## 06. Search on GitLab within a project [GET]

### 기본 정보

- **기능:** 특정 단일 프로젝트 범위 내에서 소스코드, 이슈, MR, 커밋 등을 검색한다.
- **Endpoint:** `GET /api/v4/projects/{id}/search`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

단일 프로젝트의 범위 내에서 소스코드 파일(blobs), 이슈, 머지 리퀘스트, 커밋, 댓글(notes), 위키 등을 검색합니다. `ref` 파라미터를 사용하여 특정 브랜치나 태그의 코드를 지정하여 검색할 수 있습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1234` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `search` | string | Y | - | 검색 표현식 키워드 | `getUserById` |
| `scope` | string | Y | - | 검색 범주 (`blobs` \| `issues` \| `merge_requests` \| `commits` \| `notes` \| `wiki_blobs`) | `blobs` |
| `ref` | string | N | default branch | 코드 검색 시 대상 브랜치명 또는 태그 | `main` |
| `state` | string | N | - | 이슈/MR 상태 필터 (`opened` \| `closed` \| `merged`) | `opened` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

```json
[
  {
    "basename": "UserService",
    "filename": "src/main/java/com/ssafy/UserService.java",
    "path": "src/main/java/com/ssafy/UserService.java",
    "ref": "main",
    "startline": 42,
    "data": "public User getUserById(Long id) {\n    return userRepository.findById(id);\n}"
  }
]
```
