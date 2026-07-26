# 3. Create a custom group

## 기본 정보
- **기능**: `custom` 타입의 그룹을 새로 생성한다.
- **Endpoint**: `POST /api/v4/groups`
- **인증**: Bearer Token 필요
- **권한**: `create_custom_group` 권한 필요
- **최소 서버 버전**: 6.3

## 설명
새로운 커스텀 그룹을 생성하는 API이다. `source`는 반드시 `custom`이어야 하며, `allow_reference`는 반드시 `true`여야 한다. 요청 시 그룹의 고유 이름(`name`), 표시 이름(`display_name`), 초기 멤버로 추가할 사용자 ID 목록(`user_ids`)을 함께 전달한다. `source`가 유효하지 않거나 `allow_reference`가 `true`가 아니거나 `remote_id`가 존재하는 경우 501 오류가 발생한다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| name | string | Yes | at-mention에 사용되는 그룹의 고유 이름 |
| display_name | string | Yes | 공백을 포함할 수 있는 그룹의 표시 이름 |
| source | string | Yes | 반드시 `custom`이어야 함 |
| allow_reference | boolean | Yes | 반드시 `true`이어야 함 |
| user_ids | string[] | Yes | 그룹 멤버로 추가할 사용자 ID 목록 |

```json
{
  "name": "string",
  "display_name": "string",
  "source": "custom",
  "allow_reference": true,
  "user_ids": [
    "string"
  ]
}
```

## Response

### 201 - Group creation and memberships successful.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 501 | 그룹의 `source`가 유효하지 않거나, `allow_reference`가 `true`가 아니거나, 그룹에 `remote_id`가 있는 경우 |

---

# 7. Restore a previously deleted group

## 기본 정보
- **기능**: 이전에 삭제된 커스텀 그룹을 복구하여 정상적으로 다시 사용할 수 있게 한다.
- **Endpoint**: `POST /api/v4/groups/{group_id}/restore`
- **인증**: Bearer Token 필요
- **권한**: 해당 그룹에 대한 `restore_custom_group` 권한 필요
- **최소 서버 버전**: 7.7

## 설명
소프트 삭제된 커스텀 그룹을 복구하는 API이다. LDAP 그룹에는 사용할 수 없으며 커스텀 그룹에만 적용된다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| group_id | string | Yes | Group GUID |

## Response

### 200 - Group restored successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 요청이 성공하고 별도로 반환할 내용이 없을 경우 "ok"를 포함 |

```json
{
  "status": "ok"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 501 | 명시되지 않음 |

## 주의 사항
LDAP 그룹에는 사용할 수 없다 (커스텀 그룹 전용).

---

# 26. Get groups by name

## 기본 정보
- **기능**: 제공된 그룹 이름 목록을 기반으로 그룹 목록을 조회한다.
- **Endpoint**: `POST /api/v4/groups/names`
- **인증**: 활성 세션(로그인) 필요
- **권한**: 권한 불요 (활성 세션만 있으면 되고 별도의 이름있는 권한은 필요 없음)
- **최소 서버 버전**: 11.0

## 설명
그룹 이름 문자열 배열을 요청 본문으로 전달하면 해당 이름과 일치하는 그룹들의 목록을 반환하는 API이다. 별도의 이름있는 권한 없이 활성 세션만 있으면 호출할 수 있다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| (root) | string[] | Yes | 조회할 그룹 이름 목록 |

```json
[
  "string"
]
```

## Response

### 200 - Group list retrieval successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 그룹 ID |
| name | string | 그룹 이름 |
| display_name | string | 그룹 표시 이름 |
| description | string | 그룹 설명 |
| source | string | 그룹 소스 (예: custom, ldap 등) |
| remote_id | string | 원격 ID |
| create_at | integer | 생성 시각 (ms) |
| update_at | integer | 수정 시각 (ms) |
| delete_at | integer | 삭제 시각 (ms) |
| has_syncables | boolean | 연동된 syncable 존재 여부 |

```json
[
  {
    "id": "string",
    "name": "string",
    "display_name": "string",
    "description": "string",
    "source": "string",
    "remote_id": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0,
    "has_syncables": false
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 501 | 명시되지 않음 |
