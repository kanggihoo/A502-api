# 1. Get user status

## 기본 정보
- **기능**: 사용자 ID로 사용자의 상태(status)를 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/status`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
서버에서 사용자 ID로 해당 사용자의 상태를 조회하는 API이다. 인증된 사용자라면 누구나 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID |

## Response

### 200 - User status retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| user_id | string | 사용자 ID |
| status | string | 사용자 상태 |
| manual | boolean | 수동 설정 여부 |
| last_activity_at | integer | 마지막 활동 시각 |

```json
{
  "user_id": "string",
  "status": "string",
  "manual": true,
  "last_activity_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |

---

# 2. Update user status

## 기본 정보
- **기능**: 사용자의 상태를 수동으로 설정한다.
- **Endpoint**: `PUT /api/v4/users/{user_id}/status`
- **인증**: Bearer Token 필요
- **권한**: 본인 상태 변경 가능 (문서상 타인 대상은 팀의 `edit_other_users` 권한 필요)

## 설명
사용자의 상태를 수동으로 설정하는 API이다. 설정된 상태는 다시 "online"으로 설정할 때까지 유지되며, "online"으로 설정하면 사용자 활동에 따라 자동으로 갱신되는 상태로 돌아간다. 문서의 Permissions에는 `edit_other_users`만 명시되어 있으나, 이는 타인 상태 변경에 해당하며 본인 상태는 본인 리소스로서 변경 가능하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID |
| status | string | Yes | 사용자 상태. `online`, `away`, `offline`, `dnd` 중 하나 |
| dnd_end_time | integer | No | dnd 상태가 해제될 시각 (epoch 초) |

```json
{
  "user_id": "string",
  "status": "online",
  "dnd_end_time": 0
}
```

## Response

### 200 - User status update successful
| 필드 | 타입 | 설명 |
|---|---|---|
| user_id | string | 사용자 ID |
| status | string | 사용자 상태 |
| manual | boolean | 수동 설정 여부 |
| last_activity_at | integer | 마지막 활동 시각 |

```json
{
  "user_id": "string",
  "status": "string",
  "manual": true,
  "last_activity_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |

## 주의 사항
일반 멤버 계정은 본인(user_id) 상태만 변경 가능하다. 타인 상태 변경에는 `edit_other_users` 권한이 필요하다.

---

# 3. Get user statuses by id

## 기본 정보
- **기능**: 사용자 ID 목록으로 여러 사용자의 상태를 한 번에 조회한다.
- **Endpoint**: `POST /api/v4/users/status/ids`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
사용자 ID 목록을 전달하여 여러 사용자의 상태를 서버에서 한 번에 조회하는 API이다. 인증된 사용자라면 누구나 호출할 수 있다.

## Request

### Body
사용자 ID 문자열 배열을 전송한다.

```json
[
  "string"
]
```

## Response

### 200 - User statuses retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| user_id | string | 사용자 ID |
| status | string | 사용자 상태 |
| manual | boolean | 수동 설정 여부 |
| last_activity_at | integer | 마지막 활동 시각 |

```json
[
  {
    "user_id": "string",
    "status": "string",
    "manual": true,
    "last_activity_at": 0
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |

---

# 4. Update user custom status

## 기본 정보
- **기능**: 사용자의 커스텀 상태(이모지+텍스트)를 설정한다.
- **Endpoint**: `PUT /api/v4/users/{user_id}/status/custom`
- **인증**: Bearer Token 필요
- **권한**: 본인(user_id)으로 로그인 (별도의 이름있는 권한 불요)

## 설명
사용자의 props에 값을 설정하여 커스텀 상태를 갱신하는 API이다. 설정한 커스텀 상태는 사용자의 props에 있는 최근 커스텀 상태(recent custom statuses) 목록에도 저장된다. 커스텀 상태를 변경하려는 본인으로 로그인해야 한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| emoji | string | Yes | 아무 이모지 |
| text | string | Yes | 커스텀 상태 텍스트 |
| duration | string | No | 커스텀 상태 지속 시간. `thirty_minutes`, `one_hour`, `four_hours`, `today`, `this_week`, `date_and_time` 중 하나 |
| expires_at | string | No | 커스텀 상태 만료 시각 (ISO 형식) |

```json
{
  "emoji": "string",
  "text": "string",
  "duration": "today",
  "expires_at": "string"
}
```

## Response

### 200 - User custom status update successful

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |

## 주의 사항
본인(user_id)에 대해서만 호출 가능하다.

---

# 5. Unsets user custom status

## 기본 정보
- **기능**: 사용자의 커스텀 상태를 해제한다.
- **Endpoint**: `DELETE /api/v4/users/{user_id}/status/custom`
- **인증**: Bearer Token 필요
- **권한**: 본인(user_id)으로 로그인 (별도의 이름있는 권한 불요)

## 설명
사용자의 props를 갱신하여 커스텀 상태를 해제하는 API이다. 커스텀 상태를 제거하려는 본인으로 로그인해야 한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID |

## Response

### 200 - User custom status delete successful

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |

## 주의 사항
본인(user_id)에 대해서만 호출 가능하다.

---

# 6. Delete user's recent custom status (DELETE)

## 기본 정보
- **기능**: 사용자의 최근 커스텀 상태 목록에서 특정 상태를 삭제한다.
- **Endpoint**: `DELETE /api/v4/users/{user_id}/status/custom/recent`
- **인증**: Bearer Token 필요
- **권한**: 본인(user_id)으로 로그인 (별도의 이름있는 권한 불요)

## 설명
사용자 props의 recentCustomStatuses에서 지정한 커스텀 상태를 제거하고 사용자를 갱신하는 API이다. 본인으로 로그인해야 한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| emoji | string | Yes | 아무 이모지 |
| text | string | Yes | 커스텀 상태 텍스트 |
| duration | string | Yes | 커스텀 상태 지속 시간. `thirty_minutes`, `one_hour`, `four_hours`, `today`, `this_week`, `date_and_time` 중 하나 |
| expires_at | string | Yes | 커스텀 상태 만료 시각 (ISO 형식) |

```json
{
  "emoji": "string",
  "text": "string",
  "duration": "today",
  "expires_at": "string"
}
```

## Response

### 200 - User recent custom status delete successful

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |

## 주의 사항
본인(user_id)에 대해서만 호출 가능하다.

---

# 7. Delete user's recent custom status (POST)

## 기본 정보
- **기능**: 사용자의 최근 커스텀 상태 목록에서 특정 상태를 삭제한다. (POST 방식)
- **Endpoint**: `POST /api/v4/users/{user_id}/status/custom/recent/delete`
- **인증**: Bearer Token 필요
- **권한**: 본인(user_id)으로 로그인 (별도의 이름있는 권한 불요)

## 설명
6번과 동일하게 사용자 props의 recentCustomStatuses에서 지정한 커스텀 상태를 제거하고 사용자를 갱신하는 API로, POST 방식으로 제공되는 변형이다. 본인으로 로그인해야 한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| emoji | string | Yes | 아무 이모지 |
| text | string | Yes | 커스텀 상태 텍스트 |
| duration | string | Yes | 커스텀 상태 지속 시간. `thirty_minutes`, `one_hour`, `four_hours`, `today`, `this_week`, `date_and_time` 중 하나 |
| expires_at | string | Yes | 커스텀 상태 만료 시각 (ISO 형식) |

```json
{
  "emoji": "string",
  "text": "string",
  "duration": "today",
  "expires_at": "string"
}
```

## Response

### 200 - User recent custom status delete successful

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |

## 주의 사항
본인(user_id)에 대해서만 호출 가능하다.

---
