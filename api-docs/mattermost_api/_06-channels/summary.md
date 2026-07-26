# 4. Create a direct message channel

## 기본 정보
- **기능**: 두 사용자 간의 다이렉트 메시지(DM) 채널을 생성한다.
- **Endpoint**: `POST /api/v4/channels/direct`
- **인증**: Bearer Token 필요
- **권한**: 두 사용자 중 한 명이어야 하며 `create_direct_channel` 권한 필요. `manage_system` 권한이 있으면 이 조건은 무시된다.

## 설명
요청 본문으로 전달된 두 사용자 ID 사이에 새로운 다이렉트 메시지 채널을 생성한다. 이미 두 사용자 간의 DM 채널이 존재하면 기존 채널을 반환한다. 호출자는 반드시 두 사용자 중 한 명이어야 하며, `create_direct_channel` 권한을 보유해야 한다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| (array) | string[] | Yes | DM 채널을 생성할 두 사용자의 ID 배열 |

```json
[
  "user_id_1",
  "user_id_2"
]
```

## Response

### 201 - Direct channel creation successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 채널 ID |
| create_at | integer | 채널 생성 시각(ms) |
| update_at | integer | 채널 마지막 수정 시각(ms) |
| delete_at | integer | 채널 삭제 시각(ms) |
| team_id | string | 소속 팀 ID |
| type | string | 채널 타입 |
| display_name | string | UI에 표시되는 이름 |
| name | string | 채널 고유 handle |
| header | string | 채널 헤더 |
| purpose | string | 채널 목적 설명 |
| last_post_at | integer | 마지막 게시물 시각(ms) |
| total_msg_count | integer | 전체 메시지 수 |
| extra_update_at | integer | Deprecated (Mattermost 5.0) |
| creator_id | string | 채널 생성자 ID |

```json
{
  "id": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "team_id": "string",
  "type": "string",
  "display_name": "string",
  "name": "string",
  "header": "string",
  "purpose": "string",
  "last_post_at": 0,
  "total_msg_count": 0,
  "extra_update_at": 0,
  "creator_id": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

## 주의 사항
호출자가 두 사용자 중 한 명이 아니면서 `manage_system` 권한도 없으면 403이 발생한다.

---

# 5. Create a group message channel

## 기본 정보
- **기능**: 여러 사용자를 대상으로 하는 그룹 메시지(GM) 채널을 생성한다.
- **Endpoint**: `POST /api/v4/channels/group`
- **인증**: Bearer Token 필요
- **권한**: `create_group_channel` 권한 필요

## 설명
요청 본문에 전달된 사용자 ID 목록을 대상으로 새로운 그룹 메시지 채널을 생성한다. 로그인한 사용자의 ID가 목록에 포함되어 있지 않으면 자동으로 목록 끝에 추가된다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| (array) | string[] | Yes | 그룹 메시지 채널에 포함할 사용자 ID 배열 |

```json
[
  "user_id_1",
  "user_id_2",
  "user_id_3"
]
```

## Response

### 201 - Group channel creation successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 채널 ID |
| create_at | integer | 채널 생성 시각(ms) |
| update_at | integer | 채널 마지막 수정 시각(ms) |
| delete_at | integer | 채널 삭제 시각(ms) |
| team_id | string | 소속 팀 ID |
| type | string | 채널 타입 |
| display_name | string | UI에 표시되는 이름 |
| name | string | 채널 고유 handle |
| header | string | 채널 헤더 |
| purpose | string | 채널 목적 설명 |
| last_post_at | integer | 마지막 게시물 시각(ms) |
| total_msg_count | integer | 전체 메시지 수 |
| extra_update_at | integer | Deprecated (Mattermost 5.0) |
| creator_id | string | 채널 생성자 ID |

```json
{
  "id": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "team_id": "string",
  "type": "string",
  "display_name": "string",
  "name": "string",
  "header": "string",
  "purpose": "string",
  "last_post_at": 0,
  "total_msg_count": 0,
  "extra_update_at": 0,
  "creator_id": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

## 주의 사항
호출자에게 `create_group_channel` 권한이 없으면 403이 발생한다.

---

# 37. Update channel notifications

## 기본 정보
- **기능**: 특정 채널에 대한 사용자의 알림 설정(notify_props)을 수정한다.
- **Endpoint**: `PUT /api/v4/channels/{channel_id}/members/{user_id}/notify_props`
- **인증**: Bearer Token 필요
- **권한**: 본인(self)으로 로그인했거나 `edit_other_users` 권한 필요

## 설명
채널 멤버의 알림 설정 중 전달된 필드만 갱신한다. 이메일, 푸시, 데스크톱 알림, 읽지 않음 표시 방식 등을 개별적으로 설정할 수 있다. 호출자가 대상 `user_id`와 동일한 본인일 경우 별도의 권한 없이 호출 가능하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |
| user_id | string | Yes | 사용자 GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| email | string | No | "true"/"false"/"default" 중 하나로 이메일 알림 설정 |
| push | string | No | "all"/"mention"/"none"/"default" 중 하나로 푸시 알림 설정 |
| desktop | string | No | "all"/"mention"/"none"/"default" 중 하나로 데스크톱 알림 설정 |
| mark_unread | string | No | "all"/"mention" 중 하나로 읽지 않음 표시 방식 설정 (기본값 "all") |

```json
{
  "email": "default",
  "push": "mention",
  "desktop": "all",
  "mark_unread": "all"
}
```

## Response

### 200 - Channel notification properties update successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

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
| 404 | 명시되지 않음 |

## 주의 사항
본인의 알림 설정을 변경하는 경우에는 별도의 이름있는 권한이 요구되지 않는다(로그인한 사용자 본인이면 충분).

---

# 38. Update channel member autotranslation setting

## 기본 정보
- **기능**: 채널 멤버 개인의 자동 번역(autotranslation) 사용 여부를 설정한다.
- **Endpoint**: `PUT /api/v4/channels/{channel_id}/members/{user_id}/autotranslation`
- **인증**: Bearer Token 필요
- **권한**: 본인(self)으로 로그인했거나 `edit_other_users` 권한 필요

## 설명
채널이 자동 번역 기능을 지원하는 경우, 사용자별로 자동 번역 메시지 수신 여부를 제어한다. 기본적으로 채널이 자동 번역을 지원하면 모든 사용자에게 자동 번역이 활성화되어 있다. 대상 `user_id`가 호출자 본인이면 별도 권한 없이 호출 가능하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |
| user_id | string | Yes | 사용자 GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| autotranslation_disabled | boolean | Yes | 해당 사용자에 대해 채널 내 자동 번역을 비활성화할지 여부 |

```json
{
  "autotranslation_disabled": true
}
```

## Response

### 200 - Channel member autotranslation setting update successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

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

## 주의 사항
본인의 설정을 변경하는 경우에는 별도의 이름있는 권한이 요구되지 않는다(로그인한 사용자 본인이면 충분).

---

# 39. Mark multiple channels as read

## 기본 정보
- **기능**: 특정 사용자를 기준으로 여러 채널을 한 번에 읽음 처리한다.
- **Endpoint**: `POST /api/v4/channels/members/{user_id}/mark_read`
- **인증**: Bearer Token 필요
- **권한**: 본인(self)으로 로그인했거나 `edit_other_users` 권한 필요

## 설명
요청 본문으로 전달된 채널 ID 목록을 대상으로 지정된 사용자의 읽음 상태(viewed)를 갱신한다. 대상 `user_id`가 호출자 본인이면 별도의 이름있는 권한 없이 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 채널을 읽음 처리할 대상 사용자 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| (array) | string[] | Yes | 읽음 처리할 채널 ID 배열 |

```json
[
  "channel_id_1",
  "channel_id_2"
]
```

## Response

### 200 - Channels marked as read
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 처리 결과 상태 |
| last_viewed_at_times | object | 채널 ID를 키로 하는 마지막 조회 시각 매핑 |

```json
{
  "status": "OK",
  "last_viewed_at_times": {
    "channel_id_1": 1690000000000
  }
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

## 주의 사항
본인의 채널을 읽음 처리하는 경우에는 별도의 이름있는 권한이 요구되지 않는다(로그인한 사용자 본인이면 충분).

---

# 41. View channel

## 기본 정보
- **기능**: 채널을 조회(view)할 때 발생하는 일련의 동작(읽음 처리, 푸시 알림 해제, 활성 채널 갱신)을 수행한다.
- **Endpoint**: `POST /api/v4/channels/members/{user_id}/view`
- **인증**: Bearer Token 필요
- **권한**: 본인(self)으로 로그인했거나 `edit_other_users` 권한 필요

## 설명
채널을 읽음 처리하고, 해당 채널의 푸시 알림을 지우며, 사용자의 활성(active) 채널 상태를 갱신하는 등 "채널 보기"에 수반되는 모든 동작을 한 번에 수행한다. `prev_channel_id`를 함께 전달하면 이전 채널로 전환할 때 해당 채널의 푸시 알림도 함께 해제된다. Mattermost 서버 4.3 이상부터 응답에 `last_viewed_at_times`가 포함된다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | view 동작을 수행할 대상 사용자 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 조회 중인 채널 ID. 모든 채널이 포커스를 잃었음을 나타내려면 빈 문자열 사용 |
| prev_channel_id | string | No | 채널 전환 시 이전 채널 ID. 지정 시 전환 대상 채널의 푸시 알림이 해제됨 |

```json
{
  "channel_id": "channel_id_1",
  "prev_channel_id": "channel_id_0"
}
```

## Response

### 200 - Channel view successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "OK" |
| last_viewed_at_times | object | 채널 ID를 키로 하는 조회 시각 매핑 |

```json
{
  "status": "OK",
  "last_viewed_at_times": {
    "channel_id_1": 1690000000000
  }
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

## 주의 사항
본인이 자신의 view 동작을 수행하는 경우 별도의 이름있는 권한이 요구되지 않는다(로그인한 사용자 본인이면 충분).

---

# 42. Mark all direct and group messages as read

## 기본 정보
- **기능**: 특정 사용자의 모든 다이렉트 메시지 및 그룹 메시지 채널을 읽음 처리한다.
- **Endpoint**: `PUT /api/v4/channels/members/{user_id}/direct/read`
- **인증**: Bearer Token 필요
- **권한**: 본인(self)으로 로그인했거나 `edit_other_users` 권한 필요

## 설명
지정된 사용자의 모든 DM 및 GM 채널을 한 번에 읽음 처리한다. 대상 `user_id`가 호출자 본인이면 별도의 이름있는 권한 없이 호출 가능하다. 서버 버전 11.3 이상에서 지원된다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 메시지를 읽음 처리할 대상 사용자 ID |

## Response

### 200 - Direct messages marked as read successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "OK" |
| last_viewed_at_times | object | 채널 ID를 키로 하는 마지막 조회 시각 매핑 |

```json
{
  "status": "OK",
  "last_viewed_at_times": {
    "channel_id_1": 1690000000000
  }
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
본인의 DM/GM 채널을 읽음 처리하는 경우에는 별도의 이름있는 권한이 요구되지 않는다(로그인한 사용자 본인이면 충분).
