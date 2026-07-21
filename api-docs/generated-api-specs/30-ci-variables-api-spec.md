# 30 CI Variables API Spec

---

## 1. List all group variables [GET]

### 기본 정보
- **기능:** 지정된 그룹의 모든 CI/CD 변수 목록 조회
- **Endpoint:** `GET /api/v4/groups/{id}/variables`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 그룹에 속한 모든 CI/CD 변수를 페이지네이션하여 반환한다. `page`와 `per_page` 파라미터로 결과를 제어할 수 있다.

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

### Response
#### `200 OK`
```json
[
  {
    "variable_type": "string",
    "key": "string",
    "value": "string",
    "hidden": "boolean",
    "protected": "boolean",
    "masked": "boolean",
    "raw": "boolean",
    "environment_scope": "string",
    "description": "string"
  }
]
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `variable_type` | `string` | 변수 타입 (`env_var` / `file`) |
| `key` | `string` | 변수 키 |
| `value` | `string` | 변수 값 |
| `hidden` | `boolean` | 숨김 여부 |
| `protected` | `boolean` | 보호된 브랜치에서만 노출 여부 |
| `masked` | `boolean` | CI/CD 로그에서 마스킹 여부 |
| `raw` | `boolean` | raw 여부 |
| `environment_scope` | `string` | 적용 환경 범위 |
| `description` | `string` | 변수 설명 |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `404 Not Found` | 그룹을 찾을 수 없음 |

---

## 2. List all project variables [GET]

### 기본 정보
- **기능:** 지정된 프로젝트의 모든 CI/CD 변수 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/variables`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트에 속한 모든 CI/CD 변수를 페이지네이션하여 반환한다. `page`와 `per_page` 파라미터로 결과를 제어할 수 있다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 프로젝트 ID 또는 URL 인코딩된 `NAMESPACE/PROJECT_NAME` |

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
    "variable_type": "string",
    "key": "string",
    "value": "string",
    "hidden": "boolean",
    "protected": "boolean",
    "masked": "boolean",
    "raw": "boolean",
    "environment_scope": "string",
    "description": "string"
  }
]
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `variable_type` | `string` | 변수 타입 (`env_var` / `file`) |
| `key` | `string` | 변수 키 |
| `value` | `string` | 변수 값 |
| `hidden` | `boolean` | 숨김 여부 |
| `protected` | `boolean` | 보호된 브랜치에서만 노출 여부 |
| `masked` | `boolean` | CI/CD 로그에서 마스킹 여부 |
| `raw` | `boolean` | raw 여부 |
| `environment_scope` | `string` | 적용 환경 범위 |
| `description` | `string` | 변수 설명 |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |
