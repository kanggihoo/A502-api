# 1. List all the Custom Profile Attributes fields

## 기본 정보
- **기능**: 커스텀 프로필 속성(CPA) 필드 목록을 조회한다.
- **Endpoint**: `GET /api/v4/custom_profile_attributes/fields`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
서버에 정의된 모든 커스텀 프로필 속성 필드(이름, 타입, 옵션 등)를 조회하는 API이다. 인증된 사용자라면 누구나 호출할 수 있으며, 결과는 비어 있을 수 있다. 최소 서버 버전은 10.5이다.

## Response

### 200 - Custom Profile Attributes fetch successful. Result may be empty.
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 속성 필드의 고유 식별자 (26자 영숫자) |
| type | enum | 필드 타입 (`text` \| `select` \| `multiselect`) |
| name | string | 필드 이름 |
| description | string | 필드 설명 |
| create_at | integer | 필드 생성 시각 (밀리초) |
| update_at | integer | 필드 수정 시각 (밀리초) |
| delete_at | integer | 필드 삭제 시각 (밀리초), 미삭제 시 0 |
| attrs | object | 추가 속성 (select 필드의 옵션, 노출 설정 등) |

```json
[
  {
    "id": "string",
    "type": "text",
    "name": "string",
    "description": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0,
    "attrs": {}
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |

---

# 5. Patch Custom Profile Attribute values

## 기본 정보
- **기능**: 요청자 본인의 커스텀 프로필 속성 값을 부분 업데이트한다.
- **Endpoint**: `PATCH /api/v4/custom_profile_attributes/values`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요, 본인 값 대상)

## 설명
요청자 본인의 CPA 필드 값들 중 원하는 것만 골라 부분 업데이트하는 API이다. 요청에 포함하지 않은 필드는 변경되지 않는다. `attrs.protected = true`인 필드의 값은 업데이트할 수 없으며 에러를 반환한다. 최소 서버 버전은 10.5이다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | No | 대상 속성 필드 ID |
| value | any | No | 설정할 값 |

```json
[
  {
    "id": "string",
    "value": "any"
  }
]
```

## Response

### 200 - Custom Profile Attribute values patch successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 속성 필드 ID |
| value | any | 저장된 값 |

```json
[
  {
    "id": "string",
    "value": "any"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

## 주의 사항
`attrs.protected = true`인 필드 값은 수정할 수 없다.

---

# 6. Get Custom Profile Attribute property group data

## 기본 정보
- **기능**: 커스텀 프로필 속성에 사용되는 property group 정보를 조회한다.
- **Endpoint**: `GET /api/v4/custom_profile_attributes/group`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
CPA가 소속된 property group의 데이터를 조회하는 API이다. properties API(`/api/v4/properties/...`)와 연동할 때 그룹 ID를 얻는 용도로 사용된다. 최소 서버 버전은 10.8이다.

## Response

### 200 - Group fetch successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 커스텀 프로필 속성 그룹의 ID |

```json
{
  "id": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

---

# 7. List Custom Profile Attribute values

## 기본 정보
- **기능**: 특정 사용자의 커스텀 프로필 속성 값 목록을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/custom_profile_attributes`
- **인증**: Bearer Token 필요
- **권한**: `view_members`

## 설명
지정한 사용자의 모든 CPA 값을 조회하는 API이다. `view members` 권한이 필요하며, 일반 멤버 계정(system_user)에 부여되어 있다. 결과는 비어 있을 수 있다. 최소 서버 버전은 10.5이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 GUID |

## Response

### 200 - Custom Profile Attribute values fetch successful. Result may be empty.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

---

# 8. Update custom profile attribute values for a user

## 기본 정보
- **기능**: 특정 사용자의 커스텀 프로필 속성 값을 업데이트한다.
- **Endpoint**: `PATCH /api/v4/users/{user_id}/custom_profile_attributes`
- **인증**: Bearer Token 필요
- **권한**: 대상 사용자 편집 권한 필요 — 일반 사용자는 본인(user_id) 값만 수정 가능 (시스템 관리자는 타인도 가능)

## 설명
지정한 사용자의 CPA 필드 값을 업데이트하는 API이다. 일반 사용자는 본인의 값만 수정할 수 있다. `attrs.protected = true`인 필드의 값은 업데이트할 수 없으며 에러를 반환한다. 최소 서버 버전은 11이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | No | 대상 속성 필드 ID |
| value | any | No | 설정할 값 |

```json
[
  {
    "id": "string",
    "value": "any"
  }
]
```

## Response

### 200 - Custom profile attribute values updated successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 속성 필드 ID |
| value | any | 저장된 값 |

```json
[
  {
    "id": "string",
    "value": "any"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 (본인이 아닌 경우) |
| 404 | 사용자를 찾을 수 없음 |

## 주의 사항
일반 사용자는 본인(user_id)의 값만 수정할 수 있으며, `attrs.protected = true` 필드는 수정 불가하다.

---

## 제외된 API
- **02-Create a custom profile attribute field**: `manage_system` 권한 필요로 제외됨.
- **03-Patch a custom profile attribute field**: `manage_system` 권한 필요로 제외됨.
- **04-Delete a custom profile attribute field**: `manage_system` 권한 필요로 제외됨.
