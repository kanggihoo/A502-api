# 1. Get the user's preferences

## 기본 정보
- **기능**: 사용자의 preference 목록을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/preferences`
- **인증**: Bearer Token 필요
- **권한**: 본인(user_id)으로 로그인 (타인 대상은 `edit_other_users` 필요)

## 설명
사용자의 모든 preference 목록을 조회하는 API이다. 본인 계정에 대해서는 별도 권한 없이 호출할 수 있으며, 다른 사용자를 대상으로 하려면 `edit_other_users` 권한이 필요하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 GUID |

## Response

### 200 - User preferences retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| user_id | string | 이 preference를 소유한 사용자 ID |
| category | string | preference 카테고리 |
| name | string | preference 이름 |
| value | string | preference 값 |

```json
[
  {
    "user_id": "string",
    "category": "string",
    "name": "string",
    "value": "string"
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
일반 멤버 계정은 본인(user_id)에 대해서만 호출 가능하다.

---

# 2. Save the user's preferences

## 기본 정보
- **기능**: 사용자의 preference 목록을 저장한다.
- **Endpoint**: `PUT /api/v4/users/{user_id}/preferences`
- **인증**: Bearer Token 필요
- **권한**: 본인(user_id)으로 로그인 (타인 대상은 `edit_other_users` 필요)

## 설명
사용자의 preference 목록을 저장(생성/갱신)하는 API이다. 본인 계정에 대해서는 별도 권한 없이 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 GUID |

### Body
Preference 객체 배열을 전송한다.

| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 이 preference를 소유한 사용자 ID |
| category | string | Yes | preference 카테고리 |
| name | string | Yes | preference 이름 |
| value | string | Yes | preference 값 |

```json
[
  {
    "user_id": "string",
    "category": "string",
    "name": "string",
    "value": "string"
  }
]
```

## Response

### 200 - User preferences saved successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 요청 성공 시 "ok" 반환 |

```json
{ "status": "ok" }
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스 없음 |

## 주의 사항
일반 멤버 계정은 본인(user_id)에 대해서만 호출 가능하다.

---

# 3. Delete user's preferences

## 기본 정보
- **기능**: 사용자의 preference 목록을 삭제한다.
- **Endpoint**: `POST /api/v4/users/{user_id}/preferences/delete`
- **인증**: Bearer Token 필요
- **권한**: 본인(user_id)으로 로그인 (타인 대상은 `edit_other_users` 필요)

## 설명
사용자의 preference 목록을 삭제하는 API이다. 삭제할 preference들을 body에 배열로 전달한다. 본인 계정에 대해서는 별도 권한 없이 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 GUID |

### Body
삭제할 Preference 객체 배열을 전송한다.

| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 이 preference를 소유한 사용자 ID |
| category | string | Yes | preference 카테고리 |
| name | string | Yes | preference 이름 |
| value | string | Yes | preference 값 |

```json
[
  {
    "user_id": "string",
    "category": "string",
    "name": "string",
    "value": "string"
  }
]
```

## Response

### 200 - User preferences saved successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 요청 성공 시 "ok" 반환 |

```json
{ "status": "ok" }
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

## 주의 사항
일반 멤버 계정은 본인(user_id)에 대해서만 호출 가능하다.

---

# 4. List a user's preferences by category

## 기본 정보
- **기능**: 지정한 카테고리에 저장된 사용자의 preference 목록을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/preferences/{category}`
- **인증**: Bearer Token 필요
- **권한**: 본인(user_id)으로 로그인 (타인 대상은 `edit_other_users` 필요)

## 설명
지정한 카테고리에 저장된 현재 사용자의 preference들을 나열하는 API이다. 본인 계정에 대해서는 별도 권한 없이 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 GUID |
| category | string | Yes | preference 그룹의 카테고리 |

## Response

### 200 - A list of all of the current user's preferences in the given category
| 필드 | 타입 | 설명 |
|---|---|---|
| user_id | string | 이 preference를 소유한 사용자 ID |
| category | string | preference 카테고리 |
| name | string | preference 이름 |
| value | string | preference 값 |

```json
[
  {
    "user_id": "string",
    "category": "string",
    "name": "string",
    "value": "string"
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
일반 멤버 계정은 본인(user_id)에 대해서만 호출 가능하다.

---

# 5. Get a specific user preference

## 기본 정보
- **기능**: 카테고리와 이름으로 특정 preference 하나를 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/preferences/{category}/name/{preference_name}`
- **인증**: Bearer Token 필요
- **권한**: 본인(user_id)으로 로그인 (타인 대상은 `edit_other_users` 필요)

## 설명
주어진 카테고리와 이름에 해당하는 현재 사용자의 preference 하나를 조회하는 API이다. 본인 계정에 대해서는 별도 권한 없이 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 GUID |
| category | string | Yes | preference 그룹의 카테고리 |
| preference_name | string | Yes | preference 이름 |

## Response

### 200 - A single preference for the current user in the current category
| 필드 | 타입 | 설명 |
|---|---|---|
| user_id | string | 이 preference를 소유한 사용자 ID |
| category | string | preference 카테고리 |
| name | string | preference 이름 |
| value | string | preference 값 |

```json
{
  "user_id": "string",
  "category": "string",
  "name": "string",
  "value": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |

## 주의 사항
일반 멤버 계정은 본인(user_id)에 대해서만 호출 가능하다.

---
