




## 07. List all personal access tokens for a project service account [GET]

### 기본 정보
- **기능:** 특정 프로젝트 서비스 계정의 개인 액세스 토큰 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/service_accounts/{user_id}/personal_access_tokens`
- **인증:** Bearer Token 필요
- **권한:** Project Maintainer 이상 / 서비스 계정 소유자

### 설명
지정된 프로젝트의 서비스 계정에 발급된 개인 액세스 토큰 목록을 조회합니다. 파라미터를 통해 폐기(revoked) 상태에 따른 필터링 조회가 가능합니다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |
| `user_id` | integer | Y | 서비스 계정의 사용자 ID | `55` |

#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `revoked` | boolean | N | - | 토큰 폐기 여부 필터링 | `false` |

#### Body
없음

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 토큰 ID | `201` |
| `name` | string | 토큰 이름 | `sa-token` |


## 17. List all project access tokens [GET]

### 기본 정보
- **기능:** 프로젝트에 발급된 프로젝트 액세스 토큰(Project Access Token) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/access_tokens`
- **인증:** Bearer Token 필요
- **권한:** Project Maintainer 이상

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |

### Response
#### `200 OK`
```json
[
  {
    "id": 601,
    "name": "deploy-bot",
    "revoked": false,
    "access_level": 40,
    "scopes": ["api"]
  }
]
```

---

## 18. Create a project access token [POST]

### 기본 정보
- **기능:** 특정 프로젝트 전용 봇 토큰(Project Access Token)을 생성한다.
- **Endpoint:** `POST /api/v4/projects/{id}/access_tokens`
- **인증:** Bearer Token 필요 (사용자의 개인/OAuth 토큰)
- **권한:** Project Maintainer 이상

### 설명
팀장(Maintainer)이 특정 프로젝트에 대한 24시간 자동화/알림/봇 연동용 전용 토큰을 발급받아 DB에 저장할 때 사용합니다. 호출자의 권한 수준(access_level)을 초과하는 토큰은 생성할 수 없습니다.

### Request
#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | Y | - | 봇 토큰 이름 | `a502-bot` |
| `scopes` | array | Y | `api`, `read_repository` 등 | 권한 목록 | `["api"]` |
| `access_level` | integer | N | 10, 20, 30, 40, 50 | 역할 수준 (40=Maintainer) | `40` |
| `expires_at` | string | N | YYYY-MM-DD | 만료일 | `2027-01-01` |

```json
{
  "name": "a502-bot",
  "scopes": ["api"],
  "access_level": 40,
  "expires_at": "2027-01-01"
}
```

### Response
#### `201 Created`
```json
{
  "id": 602,
  "name": "a502-bot",
  "token": "glpat-projectbottoken789",
  "access_level": 40,
  "resource_type": "project",
  "resource_id": 1234
}
```

---

## 19. Retrieve details on a project access token [GET]

### 기본 정보
- **기능:** 특정 프로젝트 액세스 토큰의 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/access_tokens/{token_id}`
- **인증:** Bearer Token 필요
- **권한:** Project Maintainer 이상

### Response
#### `200 OK`
```json
{
  "id": 602,
  "name": "a502-bot",
  "revoked": false,
  "access_level": 40,
  "scopes": ["api"]
}
```

---

## 20. Revoke a project access token [DEL]

### 기본 정보
- **기능:** 지정된 프로젝트 액세스 토큰을 폐기한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/access_tokens/{token_id}`
- **인증:** Bearer Token 필요
- **권한:** Project Maintainer 이상

### Response
#### `204 No Content`

---

## 21. Rotate a project access token [POST]

### 기본 정보
- **기능:** 프로젝트 액세스 토큰을 회전(갱신)한다.
- **Endpoint:** `POST /api/v4/projects/{id}/access_tokens/{token_id}/rotate`
- **인증:** Bearer Token 필요 (PAT 또는 프로젝트 액세스 토큰)
- **권한:** Project Maintainer 이상

### Response
#### `200 OK`
```json
{
  "id": 603,
  "name": "a502-bot",
  "token": "glpat-rotatedproj123",
  "active": true
}
```

---
### Response
#### `204 No Content`

---

## 30. List all token associations [GET]

### 기본 정보
- **기능:** 해당 개인 액세스 토큰으로 접근 가능한 프로젝트 및 그룹 연관 목록을 조회한다.
- **Endpoint:** `GET /api/v4/personal_access_tokens/self/associations`
- **인증:** Bearer Token 필요
- **권한:** 사용자 본인

### Response
#### `200 OK`
```json
{
  "projects": [
    {
      "id": 1234,
      "name": "A502-Backend"
    }
  ],
  "groups": [
    {
      "id": 567,
      "name": "A502-Team"
    }
  ]
}
```

---

## 31. List all personal access tokens [GET]

### 기본 정보
- **기능:** 사용자가 접근 권한을 가진 개인 액세스 토큰 목록을 조회한다. (일반 사용자는 본인 토큰만, 관리자는 전역 토큰 목록 반환)
- **Endpoint:** `GET /api/v4/personal_access_tokens`
- **인증:** Bearer Token 필요
- **권한:** 일반 사용자 (본인 토큰 조회) / Administrator (전역 조회)

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `user_id` | integer | N | - | 특정 사용자 토큰 필터링 (관리자 전용) | `42` |
| `revoked` | boolean | N | - | 폐기 여부 필터 | `false` |
| `state` | string | N | - | 토큰 상태 (`active`, `inactive`) | `active` |

### Response
#### `200 OK`
```json
[
  {
    "id": 801,
    "name": "my-pat",
    "revoked": false,
    "user_id": 42,
    "active": true
  }
]
```

---

## 32. Retrieve a personal access token [GET]

### 기본 정보
- **기능:** ID 지정 개인 액세스 토큰의 상세 정보를 조회한다. (일반 사용자는 본인 토큰만 조회 가능)
- **Endpoint:** `GET /api/v4/personal_access_tokens/{id}`
- **인증:** Bearer Token 필요
- **권한:** 토큰 소유자 / Administrator

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer | Y | 토큰 ID | `801` |

### Response
#### `200 OK`
```json
{
  "id": 801,
  "name": "my-pat",
  "revoked": false,
  "user_id": 42,
  "scopes": ["api"],
  "active": true
}
```

---

## 33. Revoke a personal access token [DEL]

### 기본 정보
- **기능:** ID로 지정된 개인 액세스 토큰을 폐기한다. (일반 사용자는 본인 토큰만 폐기 가능)
- **Endpoint:** `DELETE /api/v4/personal_access_tokens/{id}`
- **인증:** Bearer Token 필요
- **권한:** 토큰 소유자 / Administrator

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer | Y | 토큰 ID | `801` |

### Response
#### `204 No Content`

---

## 34. Rotate a personal access token [POST]

### 기본 정보
- **기능:** ID로 지정된 개인 액세스 토큰을 갱신(회전)한다. (일반 사용자는 본인 토큰만 가능)
- **Endpoint:** `POST /api/v4/personal_access_tokens/{id}/rotate`
- **인증:** Bearer Token 필요
- **권한:** 토큰 소유자 / Administrator

### Request
#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expires_at` | string | N | YYYY-MM-DD | 갱신 후 만료일 | `2026-11-30` |

### Response
#### `201 Created`
```json
{
  "id": 802,
  "name": "my-pat",
  "token": "glpat-rotatedpat9999",
  "expires_at": "2026-11-30"
}
```
