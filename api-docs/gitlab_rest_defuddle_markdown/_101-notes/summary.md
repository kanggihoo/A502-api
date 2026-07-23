# Notes API 명세서 (관리자 권한 미필요 API)

본 문서는 `_101-notes` 디렉토리 내의 GitLab Notes(댓글 및 토론 노트) 관련 API 중 일반 사용자/프로젝트 멤버/그룹 멤버 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 35개)

---

## 01. Get a list of issue notes [GET]

### 기본 정보

- **기능:** 특정 이슈(Issue)에 작성된 댓글(Note) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/issues/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

프로젝트의 특정 이슈에 등록된 전체 댓글 목록을 조회합니다. 정렬 순서(`order_by`, `sort`), 활동 필터링(`activity_filter`), 페이지네이션 옵션을 사용하여 결과를 가져올 수 있습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1234` |
| `noteable_id` | integer | Y | 대상 이슈의 ID (IID가 아님에 유의) | `567` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `order_by` | string | N | `created_at` | 정렬 기준 필드 (`created_at` 또는 `updated_at`) | `created_at` |
| `sort` | string | N | `desc` | 정렬 방식 (`asc` 또는 `desc`) | `asc` |
| `activity_filter` | string | N | - | 반환할 활동 타입 필터 | `all` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 댓글 ID | `1001` |
| `body` | string | 댓글 본문 내용 | `이슈 확인하였습니다. 수정 진행할게요.` |
| `author` | object | 작성자 정보 객체 | `{ "id": 12, "username": "user1" }` |
| `created_at` | string | 작성 시각 (ISO 8601) | `2026-07-23T10:00:00Z` |
| `system` | boolean | 시스템 자동 생성 여부 | `false` |
| `internal` | boolean | 내부 비공개 댓글 여부 | `false` |

```json
[
  {
    "id": 1001,
    "body": "이슈 확인하였습니다. 수정 진행할게요.",
    "author": {
      "id": 12,
      "username": "user1",
      "name": "홍길동"
    },
    "created_at": "2026-07-23T10:00:00Z",
    "system": false,
    "internal": false
  }
]
```

---

## 02. Create a new issue note [POST]

### 기본 정보

- **기능:** 특정 이슈(Issue)에 새로운 댓글(Note)을 등록한다.
- **Endpoint:** `POST /api/v4/projects/{id}/issues/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Reporter 이상)

### 설명

프로젝트 이슈에 새 댓글을 추가합니다. 댓글 본문(`body`)은 필수 항목이며, 필요에 따라 내부 비공개 댓글 여부(`internal`)나 생성 시각(`created_at`)을 지정할 수 있습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | 대상 이슈 ID | `567` |

#### Query parameters

없음

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `body` | string | Y | - | 댓글 본문 텍스트 | `수정 완료되었습니다.` |
| `internal` | boolean | N | 기본값 `false` | 내부용 댓글 설정 | `false` |
| `created_at` | string | N | ISO 8601 | 댓글 작성 시각 지정 | `2026-07-23T10:00:00Z` |

```json
{
  "body": "수정 완료되었습니다.",
  "internal": false
}
```

### Response

#### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 생성된 댓글 ID | `1002` |
| `body` | string | 댓글 본문 | `수정 완료되었습니다.` |
| `noteable_id` | integer | 이슈 ID | `567` |
| `created_at` | string | 생성 시각 | `2026-07-23T10:05:00Z` |

```json
{
  "id": 1002,
  "body": "수정 완료되었습니다.",
  "noteable_id": 567,
  "created_at": "2026-07-23T10:05:00Z"
}
```

---

## 03. Get a single issue note [GET]

### 기본 정보

- **기능:** 특정 이슈의 단일 댓글(Note) 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/issues/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

댓글 ID(`note_id`)를 지정하여 해당 이슈 댓글의 전체 상세 데이터(작성자, 본문, 작성 시각, 수정 시각 등)를 조회합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | 이슈 ID | `567` |
| `note_id` | integer | Y | 조회할 댓글 ID | `1001` |

#### Query parameters

없음

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 댓글 ID | `1001` |
| `body` | string | 댓글 내용 | `이슈 확인하였습니다.` |
| `author` | object | 작성자 정보 | `{ "id": 12 }` |

```json
{
  "id": 1001,
  "body": "이슈 확인하였습니다.",
  "author": {
    "id": 12,
    "username": "user1"
  }
}
```

---

## 04. Update an existing issue note [PUT]

### 기본 정보

- **기능:** 특정 이슈 댓글(Note)의 본문을 수정한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/issues/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요
- **권한:** 댓글 작성자 또는 프로젝트 Maintainer 이상

### 설명

기존에 작성된 이슈 댓글의 본문 내용을 수정합니다. 작성자 본인이거나 수정 권한을 가진 사용자만 호출 가능합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | 이슈 ID | `567` |
| `note_id` | integer | Y | 수정할 댓글 ID | `1001` |

#### Query parameters

없음

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `body` | string | Y | - | 수정할 댓글 본문 | `수정된 댓글 내용입니다.` |

```json
{
  "body": "수정된 댓글 내용입니다."
}
```

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 댓글 ID | `1001` |
| `body` | string | 수정된 본문 | `수정된 댓글 내용입니다.` |
| `updated_at` | string | 수정 시각 | `2026-07-23T10:10:00Z` |

```json
{
  "id": 1001,
  "body": "수정된 댓글 내용입니다.",
  "updated_at": "2026-07-23T10:10:00Z"
}
```

---

## 05. Delete a issue note [DEL]

### 기본 정보

- **기능:** 특정 이슈 댓글(Note)을 삭제한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/issues/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요
- **권한:** 댓글 작성자 또는 프로젝트 Owner/Maintainer

### 설명

지정한 이슈 댓글을 완전히 삭제합니다. 삭제 후에는 복구할 수 없습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | 이슈 ID | `567` |
| `note_id` | integer | Y | 삭제할 댓글 ID | `1001` |

#### Query parameters

없음

#### Body

없음

### Response

#### `204 No Content`

성공 시 본문 없이 `204 No Content` 응답을 반환합니다.

---

## 06. Get a list of merge request notes [GET]

### 기본 정보

- **기능:** 특정 머지 리퀘스트(MR)에 작성된 댓글 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### 설명

지정한 Merge Request에 등록된 일반 댓글 및 코드 리뷰 댓글 목록을 조회합니다. 정렬 및 페이지네이션을 지원합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | 대상 Merge Request ID | `89` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `order_by` | string | N | `created_at` | 정렬 기준 | `created_at` |
| `sort` | string | N | `desc` | 정렬 순서 | `asc` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 댓글 ID | `2001` |
| `body` | string | MR 댓글 내용 | `코드 리뷰 반영 요청드립니다.` |
| `author` | object | 작성자 정보 | `{ "username": "reviewer1" }` |

```json
[
  {
    "id": 2001,
    "body": "코드 리뷰 반영 요청드립니다.",
    "author": {
      "id": 15,
      "username": "reviewer1"
    }
  }
]
```

---

## 07. Create a new merge request note [POST]

### 기본 정보

- **기능:** 특정 머지 리퀘스트(MR)에 새 댓글을 추가한다.
- **Endpoint:** `POST /api/v4/projects/{id}/merge_requests/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### 설명

Merge Request에 리뷰 댓글이나 의견을 작성합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | Merge Request ID | `89` |

#### Query parameters

없음

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `body` | string | Y | - | 댓글 본문 내용 | `LGTM! 승인합니다.` |
| `internal` | boolean | N | 기본값 `false` | 내부 전용 댓글 여부 | `false` |

```json
{
  "body": "LGTM! 승인합니다."
}
```

### Response

#### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 생성된 댓글 ID | `2002` |
| `body` | string | 댓글 본문 | `LGTM! 승인합니다.` |

```json
{
  "id": 2002,
  "body": "LGTM! 승인합니다."
}
```

---

## 08. Get a single merge request note [GET]

### 기본 정보

- **기능:** 머지 리퀘스트(MR)의 단일 댓글 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | Merge Request ID | `89` |
| `note_id` | integer | Y | 댓글 ID | `2001` |

### Response

#### `200 OK`

```json
{
  "id": 2001,
  "body": "코드 리뷰 반영 요청드립니다."
}
```

---

## 09. Update an existing merge request note [PUT]

### 기본 정보

- **기능:** 기존 머지 리퀘스트(MR) 댓글을 수정한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요
- **권한:** 작성자 본인 또는 Maintainer 이상

### Request

#### Body

| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `body` | string | Y | 수정할 댓글 내용 | `내용 수정되었습니다.` |

```json
{
  "body": "내용 수정되었습니다."
}
```

### Response

#### `200 OK`

```json
{
  "id": 2001,
  "body": "내용 수정되었습니다."
}
```

---

## 10. Delete a merge request note [DEL]

### 기본 정보

- **기능:** 머지 리퀘스트(MR) 댓글을 삭제한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요
- **권한:** 작성자 본인 또는 Maintainer 이상

### Response

#### `204 No Content`

---

## 11. Get a list of snippet notes [GET]

### 기본 정보

- **기능:** 프로젝트 스니펫(Snippet)에 등록된 댓글 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/snippets/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 스니펫 접근 권한이 있는 사용자

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | 스니펫 ID | `45` |

### Response

#### `200 OK`

```json
[
  {
    "id": 3001,
    "body": "유용한 스니펫이네요!"
  }
]
```

---

## 12. Create a new snippet note [POST]

### 기본 정보

- **기능:** 프로젝트 스니펫(Snippet)에 새 댓글을 추가한다.
- **Endpoint:** `POST /api/v4/projects/{id}/snippets/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 스니펫 접근 및 작성 권한이 있는 사용자

### Request

#### Body

| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `body` | string | Y | 댓글 본문 | `감사합니다. 잘 쓰겠습니다.` |

```json
{
  "body": "감사합니다. 잘 쓰겠습니다."
}
```

### Response

#### `201 Created`

```json
{
  "id": 3002,
  "body": "감사합니다. 잘 쓰겠습니다."
}
```

---

## 13. Get a single snippet note [GET]

### 기본 정보

- **기능:** 단일 스니펫 댓글 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/snippets/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요
- **권한:** 스니펫 접근 권한 사용자

### Response

#### `200 OK`

---

## 14. Update an existing snippet note [PUT]

### 기본 정보

- **기능:** 스니펫 댓글을 수정한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/snippets/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요
- **권한:** 작성자 본인 또는 관리 권한자

### Request

#### Body

| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `body` | string | Y | 수정할 댓글 | `댓글 수정본입니다.` |

### Response

#### `200 OK`

---

## 15. Delete a snippet note [DEL]

### 기본 정보

- **기능:** 스니펫 댓글을 삭제한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/snippets/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요
- **권한:** 작성자 본인 또는 관리 권한자

### Response

#### `204 No Content`

---

## 16. Get a list of wiki page meta notes [GET]

### 기본 정보

- **기능:** 프로젝트 위키 페이지 메타(Wiki Page Meta)에 등록된 노트/댓글 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/wiki_pages/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 위키 접근 권한 사용자

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | 위키 페이지 메타 ID | `78` |

### Response

#### `200 OK`

---

## 17. Create a new wiki page meta note [POST]

### 기본 정보

- **기능:** 프로젝트 위키 페이지에 새 댓글/노트를 등록한다.
- **Endpoint:** `POST /api/v4/projects/{id}/wiki_pages/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 위키 편집 권한 사용자

### Request

#### Body

| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `body` | string | Y | 위키 노트 본문 | `위키 내용 검토 바랍니다.` |

### Response

#### `201 Created`

---

## 18. Get a single wiki page meta note [GET]

### 기본 정보

- **기능:** 단일 프로젝트 위키 노트를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/wiki_pages/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `200 OK`

---

## 19. Update an existing wiki page meta note [PUT]

### 기본 정보

- **기능:** 프로젝트 위키 노트를 수정한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/wiki_pages/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `200 OK`

---

## 20. Delete a wiki page meta note [DEL]

### 기본 정보

- **기능:** 프로젝트 위키 노트를 삭제한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/wiki_pages/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `204 No Content`

---

## 21. Get a list of epic notes [GET]

### 기본 정보

- **기능:** 그룹 에픽(Epic)에 등록된 댓글 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/epics/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 그룹 에픽 접근 권한 사용자 (Premium / Ultimate)

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID 또는 경로 | `my-group` |
| `noteable_id` | integer | Y | 에픽 ID | `12` |

### Response

#### `200 OK`

---

## 22. Create a new epic note [POST]

### 기본 정보

- **기능:** 그룹 에픽(Epic)에 새 댓글을 추가한다.
- **Endpoint:** `POST /api/v4/groups/{id}/epics/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 그룹 에픽 편집 권한 사용자

### Request

#### Body

| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `body` | string | Y | 에픽 댓글 내용 | `에픽 일정을 조정합니다.` |

### Response

#### `201 Created`

---

## 23. Get a single epic note [GET]

### 기본 정보

- **기능:** 단일 에픽 댓글을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/epics/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `200 OK`

---

## 24. Update an existing epic note [PUT]

### 기본 정보

- **기능:** 에픽 댓글을 수정한다.
- **Endpoint:** `PUT /api/v4/groups/{id}/epics/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `200 OK`

---

## 25. Delete a epic note [DEL]

### 기본 정보

- **기능:** 에픽 댓글을 삭제한다.
- **Endpoint:** `DELETE /api/v4/groups/{id}/epics/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `204 No Content`

---

## 26. Get a list of vulnerability notes [GET]

### 기본 정보

- **기능:** 프로젝트 취약점(Vulnerability) 항목에 등록된 노트 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/vulnerabilities/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 보안 취약점 접근 권한 사용자 (Ultimate)

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | 취약점 항목 ID | `99` |

### Response

#### `200 OK`

---

## 27. Create a new vulnerability note [POST]

### 기본 정보

- **기능:** 보안 취약점 항목에 새 조치 노트를 추가한다.
- **Endpoint:** `POST /api/v4/projects/{id}/vulnerabilities/{noteable_id}/notes`
- **인증:** Bearer Token 필요

### Request

#### Body

| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `body` | string | Y | 취약점 조치 메모 | `패치 적용 준비 중입니다.` |

### Response

#### `201 Created`

---

## 28. Get a single vulnerability note [GET]

### 기본 정보

- **기능:** 단일 취약점 노트를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/vulnerabilities/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `200 OK`

---

## 29. Update an existing vulnerability note [PUT]

### 기본 정보

- **기능:** 취약점 노트를 수정한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/vulnerabilities/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `200 OK`

---

## 30. Delete a vulnerability note [DEL]

### 기본 정보

- **기능:** 취약점 노트를 삭제한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/vulnerabilities/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `204 No Content`

---

## 31. Get a list of group wiki page meta notes [GET]

### 기본 정보

- **기능:** 그룹 위키 페이지(Group Wiki Page)에 등록된 노트 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/wiki_pages/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** 그룹 위키 접근 권한 사용자

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID 또는 경로 | `my-group` |
| `noteable_id` | integer | Y | 위키 페이지 메타 ID | `88` |

### Response

#### `200 OK`

---

## 32. Create a new group wiki page meta note [POST]

### 기본 정보

- **기능:** 그룹 위키 페이지에 새 노트를 추가한다.
- **Endpoint:** `POST /api/v4/groups/{id}/wiki_pages/{noteable_id}/notes`
- **인증:** Bearer Token 필요

### Request

#### Body

| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `body` | string | Y | 노트 본문 | `그룹 문서 업데이트 진행` |

### Response

#### `201 Created`

---

## 33. Get a single group wiki page meta note [GET]

### 기본 정보

- **기능:** 단일 그룹 위키 노트를 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/wiki_pages/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `200 OK`

---

## 34. Update an existing group wiki page meta note [PUT]

### 기본 정보

- **기능:** 그룹 위키 노트를 수정한다.
- **Endpoint:** `PUT /api/v4/groups/{id}/wiki_pages/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `200 OK`

---

## 35. Delete a group wiki page meta note [DEL]

### 기본 정보

- **기능:** 그룹 위키 노트를 삭제한다.
- **Endpoint:** `DELETE /api/v4/groups/{id}/wiki_pages/{noteable_id}/notes/{note_id}`
- **인증:** Bearer Token 필요

### Response

#### `204 No Content`
