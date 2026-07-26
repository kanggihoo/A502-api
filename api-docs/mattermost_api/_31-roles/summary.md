# 2. Get a role (by ID)

## 기본 정보
- **기능**: 역할(role) ID로 역할 정보를 조회한다.
- **Endpoint**: `GET /api/v4/roles/{role_id}`
- **인증**: 로그인 필요
- **권한**: 없음 (활성 세션만 있으면 호출 가능)

## 설명
역할 GUID로 해당 역할의 이름, 표시명, 설명, 그리고 그 역할이 부여하는 권한 목록을 조회하는 API이다. 활성 세션 외 별도 권한이 필요 없다. 최소 서버 버전 4.9.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| role_id | string | Yes | 역할 GUID |

## Response

### 200 - Role retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 역할의 고유 식별자 |
| name | string | 역할의 고유 이름 (사용자/그룹에 역할을 할당할 때 사용) |
| display_name | string | 사람이 읽을 수 있는 역할 이름 |
| description | string | 역할에 대한 설명 |
| permissions | string[] | 이 역할이 부여하는 권한 이름 목록 |
| scheme_managed | boolean | scheme이 관리하는 역할(true)인지 커스텀 독립 역할(false)인지 |

```json
{
  "id": "string",
  "name": "string",
  "display_name": "string",
  "description": "string",
  "permissions": ["string"],
  "scheme_managed": true
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 404 | 역할을 찾을 수 없음 |

---

# 3. Get a role (by name)

## 기본 정보
- **기능**: 역할 이름으로 역할 정보를 조회한다.
- **Endpoint**: `GET /api/v4/roles/name/{role_name}`
- **인증**: 로그인 필요
- **권한**: 없음 (활성 세션만 있으면 호출 가능)

## 설명
역할 이름(예: `system_user`, `team_user`, `channel_user`)으로 해당 역할의 권한 목록 등을 조회하는 API이다. 현재 계정으로 실제 호출에 성공한 것이 확인되었다. 최소 서버 버전 4.9.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| role_name | string | Yes | 역할 이름 |

## Response

### 200 - Role retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 역할의 고유 식별자 |
| name | string | 역할의 고유 이름 |
| display_name | string | 사람이 읽을 수 있는 역할 이름 |
| description | string | 역할에 대한 설명 |
| permissions | string[] | 이 역할이 부여하는 권한 이름 목록 |
| scheme_managed | boolean | scheme이 관리하는 역할(true)인지 커스텀 독립 역할(false)인지 |

```json
{
  "id": "string",
  "name": "string",
  "display_name": "string",
  "description": "string",
  "permissions": ["string"],
  "scheme_managed": true
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 404 | 역할을 찾을 수 없음 |

---

# 5. Get a list of roles by name

## 기본 정보
- **기능**: 역할 이름 목록으로 여러 역할 정보를 한 번에 조회한다.
- **Endpoint**: `POST /api/v4/roles/names`
- **인증**: 로그인 필요
- **권한**: 없음 (활성 세션만 있으면 호출 가능)

## 설명
역할 이름들의 배열을 본문으로 전달해 해당 역할들의 정보를 일괄 조회하는 API이다. 활성 세션 외 별도 권한이 필요 없다. 최소 서버 버전 4.9.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| (root) | string[] | Yes | 조회할 역할 이름 배열 |

```json
["system_user", "team_user"]
```

## Response

### 200 - Role list retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 역할의 고유 식별자 |
| name | string | 역할의 고유 이름 |
| display_name | string | 사람이 읽을 수 있는 역할 이름 |
| description | string | 역할에 대한 설명 |
| permissions | string[] | 이 역할이 부여하는 권한 이름 목록 |
| scheme_managed | boolean | scheme이 관리하는 역할(true)인지 커스텀 독립 역할(false)인지 |

```json
[
  {
    "id": "string",
    "name": "string",
    "display_name": "string",
    "description": "string",
    "permissions": ["string"],
    "scheme_managed": true
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 역할을 찾을 수 없음 |

---

## 제외된 API
- **01-Get a list of all the roles**: `manage_system` 권한이 필요해 제외됨.
- **04-Patch a role**: `sysconsole_write_user_management_permissions` 또는 `manage_system` 권한이 필요해 제외됨.
