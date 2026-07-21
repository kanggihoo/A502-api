# 131 Protected Branches API Spec

---

## 1. List all protected branches [GET]

### 기본 정보
- **기능:** 그룹의 모든 보호 브랜치 목록 조회
- **Endpoint:** `GET /api/v4/groups/{id}/protected_branches`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 그룹의 모든 보호 브랜치 목록을 반환한다. 와일드카드가 설정된 경우, 해당 와일드카드와 일치하는 브랜치의 실제 이름 대신 와일드카드가 반환된다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `string` | Y | 그룹 ID 또는 URL 인코딩된 그룹 경로 |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `page` | `integer` | N | 현재 페이지 번호 (기본값: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본값: 20) |
| `search` | `string` | N | 보호 브랜치 이름 검색 |

### Response
#### `200 OK`
```json
[
  {
    "id": "integer",
    "name": "string",
    "push_access_levels": [
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
    ],
    "merge_access_levels": [
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
    ],
    "allow_force_push": "boolean",
    "unprotect_access_levels": [
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
    ],
    "code_owner_approval_required": "boolean"
  }
]
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | `integer` | 보호 브랜치 ID |
| `name` | `string` | 브랜치 이름 (또는 와일드카드) |
| `push_access_levels` | `object[]` | Push 권한 레벨 목록 |
| `merge_access_levels` | `object[]` | Merge 권한 레벨 목록 |
| `allow_force_push` | `boolean` | Force push 허용 여부 |
| `unprotect_access_levels` | `object[]` | 보호 해제 권한 레벨 목록 |
| `code_owner_approval_required` | `boolean` | Code Owner 승인 필요 여부 |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `401 Unauthorized` | 인증 실패 |
| `404 Not Found` | 그룹을 찾을 수 없음 |

---

## 2. Retrieve a protected branch [GET]

### 기본 정보
- **기능:** 그룹의 특정 보호 브랜치 조회
- **Endpoint:** `GET /api/v4/groups/{id}/protected_branches/{name}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 그룹에서 특정 보호 브랜치의 상세 정보를 반환한다. `name`에 와일드카드를 사용하여 여러 브랜치를 조회할 수 있다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `string` | Y | 그룹 ID 또는 URL 인코딩된 그룹 경로 |
| `name` | `string` | Y | 브랜치 이름 또는 와일드카드 |

### Response
#### `200 OK`
```json
{
  "id": "integer",
  "name": "string",
  "push_access_levels": [
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
  ],
  "merge_access_levels": [
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
  ],
  "allow_force_push": "boolean",
  "unprotect_access_levels": [
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
  ],
  "code_owner_approval_required": "boolean"
}
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | `integer` | 보호 브랜치 ID |
| `name` | `string` | 브랜치 이름 (또는 와일드카드) |
| `push_access_levels` | `object[]` | Push 권한 레벨 목록 |
| `merge_access_levels` | `object[]` | Merge 권한 레벨 목록 |
| `allow_force_push` | `boolean` | Force push 허용 여부 |
| `unprotect_access_levels` | `object[]` | 보호 해제 권한 레벨 목록 |
| `code_owner_approval_required` | `boolean` | Code Owner 승인 필요 여부 |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `401 Unauthorized` | 인증 실패 |
| `404 Not Found` | 보호 브랜치를 찾을 수 없음 |
