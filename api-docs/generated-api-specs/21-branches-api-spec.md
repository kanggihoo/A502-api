# 21 Branches API Spec

---

## 1. List all repository branches [GET]

### 기본 정보
- **기능:** 프로젝트의 모든 저장소 브랜치 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/repository/branches`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트의 모든 저장소 브랜치를 이름 기준 알파벳순으로 반환한다. 이름 검색 또는 정규식을 사용하여 특정 브랜치 패턴을 찾을 수 있다. 보호 상태, 병합 상태, 커밋 상세 정보를 포함한 브랜치 정보를 반환한다.

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
| `page` | `integer` | N | 현재 페이지 번호 (기본값: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본값: 20) |
| `search` | `string` | N | 검색어와 일치하는 브랜치 목록 반환 |
| `regex` | `string` | N | 정규식과 일치하는 브랜치 목록 반환 |
| `sort` | `string` | N | 지정된 필드 기준 정렬 (`name`, `updated`) |
| `page_token` | `string` | N | 페이지네이션 시작할 브랜치 이름 |

### Response
#### `200 OK`
```json
[
  {
    "name": "string",
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
    "merged": "boolean",
    "protected": "boolean",
    "developers_can_push": "boolean",
    "developers_can_merge": "boolean",
    "can_push": "boolean",
    "default": "boolean",
    "web_url": "string"
  }
]
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `name` | `string` | 브랜치 이름 |
| `commit` | `object` | 최신 커밋 정보 |
| `merged` | `boolean` | 병합 여부 |
| `protected` | `boolean` | 보호 브랜치 여부 |
| `developers_can_push` | `boolean` | Developer 권한 push 가능 여부 |
| `developers_can_merge` | `boolean` | Developer 권한 merge 가능 여부 |
| `can_push` | `boolean` | 현재 사용자 push 가능 여부 |
| `default` | `boolean` | 기본 브랜치 여부 |
| `web_url` | `string` | 브랜치 웹 URL |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |

---

## 2. Retrieve a repository branch [GET]

### 기본 정보
- **기능:** 프로젝트의 특정 저장소 브랜치 조회
- **Endpoint:** `GET /api/v4/projects/{id}/repository/branches/{branch}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트에서 특정 브랜치의 상세 정보를 반환한다. 브랜치명으로 단일 브랜치를 조회한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 프로젝트 ID 또는 URL 인코딩된 프로젝트 경로 |
| `branch` | `string` | Y | 조회할 브랜치 이름 |

### Response
#### `200 OK`
```json
{
  "name": "string",
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
  "merged": "boolean",
  "protected": "boolean",
  "developers_can_push": "boolean",
  "developers_can_merge": "boolean",
  "can_push": "boolean",
  "default": "boolean",
  "web_url": "string"
}
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `name` | `string` | 브랜치 이름 |
| `commit` | `object` | 최신 커밋 정보 |
| `merged` | `boolean` | 병합 여부 |
| `protected` | `boolean` | 보호 브랜치 여부 |
| `developers_can_push` | `boolean` | Developer 권한 push 가능 여부 |
| `developers_can_merge` | `boolean` | Developer 권한 merge 가능 여부 |
| `can_push` | `boolean` | 현재 사용자 push 가능 여부 |
| `default` | `boolean` | 기본 브랜치 여부 |
| `web_url` | `string` | 브랜치 웹 URL |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |
