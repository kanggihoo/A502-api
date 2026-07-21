# 155 Tags API Spec

---

## 1. Get a project repository tags [GET]

### 기본 정보
- **기능:** 프로젝트의 모든 저장소 태그 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/repository/tags`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트의 모든 저장소 태그 목록을 반환한다. 이름, 업데이트일, 버전 순으로 정렬 가능하며, 검색 및 페이지네이션을 지원한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 프로젝트 ID 또는 URL 인코딩된 프로젝트 경로 |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `sort` | `string` | N | 정렬 방향 (`asc` / `desc`) |
| `order_by` | `string` | N | 정렬 기준 (`name` / `updated` / `version`) |
| `search` | `string` | N | 검색어와 일치하는 태그 목록 반환 |
| `page_token` | `string` | N | 페이지네이션 시작할 태그 이름 |
| `page` | `integer` | N | 현재 페이지 번호 (기본값: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본값: 20) |

### Response
#### `200 OK`
```json
[
  {
    "name": "string",
    "message": "string",
    "target": "string",
    "commit": {
      "id": "string",
      "short_id": "string",
      "created_at": "string",
      "parent_ids": ["string"],
      "title": "string",
      "message": "string",
      "author_name": "string",
      "author_email": "string",
      "authored_date": "string",
      "committer_name": "string",
      "committer_email": "string",
      "committed_date": "string",
      "trailers": {},
      "extended_trailers": {},
      "web_url": "string"
    },
    "release": {
      "tag_name": "string",
      "description": "string"
    },
    "protected": "boolean",
    "created_at": "string"
  }
]
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `name` | `string` | 태그 이름 |
| `message` | `string` | 태그 메시지 |
| `target` | `string` | 태그가 가리키는 커밋 SHA |
| `commit` | `object` | 태그가 가리키는 커밋 정보 |
| `release` | `object` | 연결된 릴리스 정보 |
| `protected` | `boolean` | 보호 태그 여부 |
| `created_at` | `string` (datetime) | 태그 생성 일시 |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `403 Unauthenticated` | 인증 실패 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |
| `422 Unprocessable Entity` | 처리할 수 없는 요청 |
| `503 Service Unavailable` | 서비스 일시 불가 |

---

## 2. Get a single repository tag [GET]

### 기본 정보
- **기능:** 프로젝트의 특정 저장소 태그 조회
- **Endpoint:** `GET /api/v4/projects/{id}/repository/tags/{tag_name}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트에서 특정 태그의 상세 정보를 반환한다. 연결된 커밋 및 릴리스 정보를 포함한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 프로젝트 ID 또는 URL 인코딩된 프로젝트 경로 |
| `tag_name` | `string` | Y | 조회할 태그 이름 |

### Response
#### `200 OK`
```json
{
  "name": "string",
  "message": "string",
  "target": "string",
  "commit": {
    "id": "string",
    "short_id": "string",
    "created_at": "string",
    "parent_ids": ["string"],
    "title": "string",
    "message": "string",
    "author_name": "string",
    "author_email": "string",
    "authored_date": "string",
    "committer_name": "string",
    "committer_email": "string",
    "committed_date": "string",
    "trailers": {},
    "extended_trailers": {},
    "web_url": "string"
  },
  "release": {
    "tag_name": "string",
    "description": "string"
  },
  "protected": "boolean",
  "created_at": "string"
}
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `name` | `string` | 태그 이름 |
| `message` | `string` | 태그 메시지 |
| `target` | `string` | 태그가 가리키는 커밋 SHA |
| `commit` | `object` | 태그가 가리키는 커밋 정보 |
| `release` | `object` | 연결된 릴리스 정보 |
| `protected` | `boolean` | 보호 태그 여부 |
| `created_at` | `string` (datetime) | 태그 생성 일시 |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `403 Unauthenticated` | 인증 실패 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |
