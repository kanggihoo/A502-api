




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

## 09. Revoke a personal access token for a project service account [DEL]

### 기본 정보
- **기능:** 프로젝트 서비스 계정에 발급된 특정 개인 액세스 토큰을 폐기한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/service_accounts/{user_id}/personal_access_tokens/{token_id}`
- **인증:** Bearer Token 필요
- **권한:** Project Maintainer 이상 / 서비스 계정 관리 권한

### 설명
프로젝트 서비스 계정이 보유한 특정 액세스 토큰을 즉시 폐기시킵니다. 폐기된 토큰은 더 이상 API 인증에 사용할 수 없습니다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |
| `user_id` | integer | Y | 서비스 계정 ID | `55` |
| `token_id` | integer | Y | 폐기할 토큰 ID | `201` |

#### Query parameters
없음

#### Body
없음

### Response
#### `204 No Content`
응답 본문 없음

### Errors
| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `400` | `BAD_REQUEST` | 폐기 처리 실패 | 대상 토큰 상태 확인 |
| `404` | `NOT_FOUND` | 프로젝트, 서비스 계정 또는 토큰을 찾을 수 없음 | 파라미터 재확인 |

### 주의 사항
- 이미 폐기된 토큰을 다시 폐기 요청하면 오류가 발생할 수 있습니다.

---

## 10. Rotate a personal access token for a project service account [POST]

### 기본 정보
- **기능:** 프로젝트 서비스 계정의 특정 개인 액세스 토큰을 갱신(회전)한다.
- **Endpoint:** `POST /api/v4/projects/{id}/service_accounts/{user_id}/personal_access_tokens/{token_id}/rotate`
- **인증:** Bearer Token 필요
- **권한:** Project Maintainer 이상

### 설명
기존 토큰을 즉시 폐기하고 동일한 이름, 설명, 스코프를 가진 새로운 토큰을 발급합니다. 새 토큰의 만료일은 기본적으로 1주일 후로 설정되며, Body를 통해 만료일을 지정을 변경할 수 있습니다.

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
| `user_id` | integer | Y | 서비스 계정 ID | `55` |
| `token_id` | integer | Y | 회전 대상 토큰 ID | `201` |

#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expires_at` | string | N | YYYY-MM-DD | 신규 토큰 만료일 | `2026-08-30` |

```json
{
  "expires_at": "2026-08-30"
}
```

### Response
#### `201 Created`
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 새로 생성된 토큰 ID | `202` |
| `token` | string | 새로 발급된 평문 토큰 | `glpat-newtoken123` |

```json
{
  "id": 202,
  "name": "sa-token",
  "revoked": false,
  "token": "glpat-newtoken123",
  "active": true,
  "expires_at": "2026-08-30"
}
```

### Errors
| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `400` | `BAD_REQUEST` | 이미 폐기된 토큰이거나 날짜 형식 오류 | 토큰 상태 확인 |
| `404` | `NOT_FOUND` | 리소스 없음 | ID 값 확인 |

### 주의 사항
- 회전 시 이전 토큰은 즉시 무효화되므로 기존 토큰을 사용하는 애플리케이션의 토큰 업데이트가 필요합니다.

---

## 11. List all personal access tokens for a group service account [GET]

### 기본 정보
- **기능:** 특정 그룹 서비스 계정의 개인 액세스 토큰 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/service_accounts/{user_id}/personal_access_tokens`
- **인증:** Bearer Token 필요
- **권한:** Group Owner 이상

### 설명
지정된 그룹에 속한 서비스 계정에 발급된 개인 액세스 토큰 목록을 조회합니다.


## 12. Create a personal access token for a group service account [POST]

### 기본 정보
- **기능:** 그룹 서비스 계정에 대한 개인 액세스 토큰을 발급한다.
- **Endpoint:** `POST /api/v4/groups/{id}/service_accounts/{user_id}/personal_access_tokens`
- **인증:** Bearer Token 필요
- **권한:** Group Owner 권한 필요 (GitLab 16.1+)

### 설명
그룹 소유자(Owner)가 그룹 서비스 계정을 위한 액세스 토큰을 생성합니다. 자동화 및 외부 서비스 통합에 사용됩니다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID | `g-567` |
| `user_id` | integer | Y | 서비스 계정 ID | `88` |

#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | Y | - | 토큰 이름 | `ci-bot-token` |
| `scopes` | array | Y | - | 권한 범위 | `["api"]` |
| `expires_at` | string | N | YYYY-MM-DD | 만료일 | `2026-12-31` |

```json
{
  "name": "ci-bot-token",
  "scopes": ["api"],
  "expires_at": "2026-12-31"
}
```

### Response
#### `201 Created`
```json
{
  "id": 302,
  "name": "ci-bot-token",
  "token": "glpat-groupsa123456",
  "active": true,
  "expires_at": "2026-12-31"
}
```

### Errors
| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `400` | `BAD_REQUEST` | 파라미터 오류 | 파라미터 확인 |
| `403` | `FORBIDDEN` | Group Owner 권한 부족 | 권한 요청 |

---

## 13. Revoke a personal access token for a group service account [DEL]

### 기본 정보
- **기능:** 그룹 서비스 계정의 개인 액세스 토큰을 폐기한다.
- **Endpoint:** `DELETE /api/v4/groups/{id}/service_accounts/{user_id}/personal_access_tokens/{token_id}`
- **인증:** Bearer Token 필요
- **권한:** Group Owner

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID | `g-567` |
| `user_id` | integer | Y | 서비스 계정 ID | `88` |
| `token_id` | integer | Y | 토큰 ID | `302` |

### Response
#### `204 No Content`

---

## 14. Rotate a personal access token for a group service account [POST]

### 기본 정보
- **기능:** 그룹 서비스 계정의 개인 액세스 토큰을 회전(갱신)한다.
- **Endpoint:** `POST /api/v4/groups/{id}/service_accounts/{user_id}/personal_access_tokens/{token_id}/rotate`
- **인증:** Bearer Token 필요
- **권한:** Group Owner

### Request
#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expires_at` | string | N | YYYY-MM-DD | 만료일 | `2026-10-15` |

### Response
#### `201 Created`
```json
{
  "id": 303,
  "name": "ci-bot-token",
  "token": "glpat-rotatedtoken789",
  "expires_at": "2026-10-15"
}
```

---

## 15. Rotate a project access token (Self) [POST]

### 기본 정보
- **기능:** 프로젝트 액세스 토큰 자체를 사용하여 자기 자신을 갱신한다.
- **Endpoint:** `POST /api/v4/projects/{id}/access_tokens/self/rotate`
- **인증:** Bearer Token (자기 자신 프로젝트 액세스 토큰)
- **권한:** 토큰 소유권 (`self_rotate` 스코프)

### 설명
프로젝트 액세스 토큰을 헤더에 전달하여 자기 자신의 만료일을 연장하고 새 토큰 값을 받아옵니다. 기존 토큰은 즉시 무효화됩니다.

### Response
#### `200 OK`
```json
{
  "id": 401,
  "name": "project-bot",
  "token": "glpat-selfrotated123",
  "active": true
}
```

---

## 16. Rotate a group access token (Self) [POST]

### 기본 정보
- **기능:** 그룹 액세스 토큰 자체를 사용하여 자기 자신을 갱신한다.
- **Endpoint:** `POST /api/v4/groups/{id}/access_tokens/self/rotate`
- **인증:** Bearer Token (자기 자신 그룹 액세스 토큰)
- **권한:** 토큰 소유권

### Response
#### `200 OK`
```json
{
  "id": 501,
  "name": "group-bot",
  "token": "glpat-groupselfrotated456"
}
```

---

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

## 22. List all group access tokens [GET]

### 기본 정보
- **기능:** 그룹에 생성된 그룹 액세스 토큰(Group Access Token) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/access_tokens`
- **인증:** Bearer Token 필요
- **권한:** Group Owner / Maintainer

### Response
#### `200 OK`
```json
[
  {
    "id": 701,
    "name": "group-all-repo-bot",
    "access_level": 40
  }
]
```

---

## 23. Create a group access token [POST]

### 기본 정보
- **기능:** 그룹 및 하위 모든 프로젝트에 적용되는 그룹 액세스 토큰을 생성한다.
- **Endpoint:** `POST /api/v4/groups/{id}/access_tokens`
- **인증:** Bearer Token 필요
- **권한:** Group Owner / Maintainer

### 설명
GitLab 권한 상속 규칙에 따라, 상위 그룹 토큰 1개 생성 시 하위 모든 프로젝트(백엔드, 프론트엔드, AI 등)에 동일한 접근 권한이 상속 적용되어 통합 서비스 운영에 매우 용이합니다.

### Request
#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | Y | - | 토큰 이름 | `team-group-bot` |
| `scopes` | array | Y | - | 권한 범위 | `["api"]` |
| `access_level` | integer | N | 10~50 | 역할 권한 레벨 | `40` |

```json
{
  "name": "team-group-bot",
  "scopes": ["api"],
  "access_level": 40
}
```

### Response
#### `201 Created`
```json
{
  "id": 702,
  "name": "team-group-bot",
  "token": "glpat-grouptoken999",
  "access_level": 40,
  "resource_type": "group"
}
```

---

## 24. Retrieve details on a group access token [GET]

### 기본 정보
- **기능:** 특정 그룹 액세스 토큰의 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/access_tokens/{token_id}`
- **인증:** Bearer Token 필요
- **권한:** Group Owner / Maintainer

### Response
#### `200 OK`
```json
{
  "id": 702,
  "name": "team-group-bot",
  "revoked": false
}
```

---

## 25. Revoke a group access token [DEL]

### 기본 정보
- **기능:** 특정 그룹 액세스 토큰을 폐기한다.
- **Endpoint:** `DELETE /api/v4/groups/{id}/access_tokens/{token_id}`
- **인증:** Bearer Token 필요
- **권한:** Group Owner / Maintainer

### Response
#### `204 No Content`

---

## 26. Rotate a group access token [POST]

### 기본 정보
- **기능:** 그룹 액세스 토큰을 회전(갱신)한다.
- **Endpoint:** `POST /api/v4/groups/{id}/access_tokens/{token_id}/rotate`
- **인증:** Bearer Token 필요
- **권한:** Group Owner / Maintainer

### Response
#### `200 OK`
```json
{
  "id": 703,
  "name": "team-group-bot",
  "token": "glpat-rotatedgroup888"
}
```

---

## 27. Rotate a personal access token (Self) [POST]

### 기본 정보
- **기능:** 요청 시 전달한 사용자 자신의 개인 액세스 토큰을 갱신한다.
- **Endpoint:** `POST /api/v4/personal_access_tokens/self/rotate`
- **인증:** Bearer Token (자기 자신 PAT)
- **권한:** 사용자 본인

### Response
#### `200 OK`
```json
{
  "id": 801,
  "name": "my-pat",
  "token": "glpat-selfrotatedpat111",
  "expires_at": "2026-08-01"
}
```

---

## 28. Retrieve a personal access token (Self) [GET]

### 기본 정보
- **기능:** 요청 헤더에 사용된 자기 자신의 개인 액세스 토큰 정보를 조회한다.
- **Endpoint:** `GET /api/v4/personal_access_tokens/self`
- **인증:** Bearer Token (자기 자신 PAT)
- **권한:** 사용자 본인

### Response
#### `200 OK`
```json
{
  "id": 801,
  "name": "my-pat",
  "revoked": false,
  "active": true
}
```

---

## 29. Revoke a personal access token (Self) [DEL]

### 기본 정보
- **기능:** 요청 헤더에 사용된 자기 자신의 개인 액세스 토큰을 폐기한다.
- **Endpoint:** `DELETE /api/v4/personal_access_tokens/self`
- **인증:** Bearer Token (자기 자신 PAT)
- **권한:** 사용자 본인

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
