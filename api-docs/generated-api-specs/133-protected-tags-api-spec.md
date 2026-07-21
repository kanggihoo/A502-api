# 133 Protected Tags API Spec

---

## 1. List all protected tags [GET]

### 기본 정보
- **기능:** 프로젝트의 모든 보호 태그 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/protected_tags`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트의 모든 보호 태그 목록을 페이지네이션하여 반환한다.

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

### Response
#### `200 OK`
```json
[
  {
    "name": "string",
    "create_access_levels": [
      {
        "id": "integer",
        "access_level": "integer",
        "access_level_description": "string",
        "deploy_key_id": "integer",
        "user_id": "integer",
        "group_id": "integer",
        "member_role_id": "integer",
        "member_role_name": "string"
      }
    ]
  }
]
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `name` | `string` | 보호 태그 이름 (또는 와일드카드) |
| `create_access_levels` | `object[]` | 태그 생성 권한 레벨 목록 |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `403 Unauthenticated` | 인증 실패 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |

---

## 2. Retrieve a protected tag or wildcard protected tag [GET]

### 기본 정보
- **기능:** 프로젝트의 특정 보호 태그 또는 와일드카드 보호 태그 조회
- **Endpoint:** `GET /api/v4/projects/{id}/protected_tags/{name}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트에서 특정 보호 태그 또는 와일드카드로 설정된 보호 태그의 상세 정보를 반환한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 프로젝트 ID 또는 URL 인코딩된 프로젝트 경로 |
| `name` | `string` | Y | 태그 이름 또는 와일드카드 |

### Response
#### `200 OK`
```json
{
  "name": "string",
  "create_access_levels": [
    {
      "id": "integer",
      "access_level": "integer",
      "access_level_description": "string",
      "deploy_key_id": "integer",
      "user_id": "integer",
      "group_id": "integer",
      "member_role_id": "integer",
      "member_role_name": "string"
    }
  ]
}
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `name` | `string` | 보호 태그 이름 (또는 와일드카드) |
| `create_access_levels` | `object[]` | 태그 생성 권한 레벨 목록 |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `403 Unauthenticated` | 인증 실패 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |
