# Notes API 명세서 (관리자 권한 미필요 API)

본 문서는 `_101-notes` 디렉토리 내의 GitLab Notes(댓글 및 토론 노트) 관련 API 중 일반 사용자/프로젝트 멤버/그룹 멤버 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 35개)

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
m `Content-Type` | Y | 요청 형식 | `application/json` |

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

