# 1. Upsert synced draft

## 기본 정보
- **기능**: 현재 사용자의 동기화 초안(synced draft)을 생성하거나 갱신한다.
- **Endpoint**: `POST /api/v4/drafts`
- **인증**: 로그인 필요
- **권한**: 해당 채널의 `create_post`

## 설명
현재 사용자의 초안을 생성하거나(없으면) 갱신하는(있으면) API이다. 대상 채널에서 게시글을 작성할 수 있는 권한(`create_post`)이 있어야 하며, 서버에서 synced drafts 기능이 활성화되어 있어야 한다. `message`를 빈 문자열로 보내면 초안이 삭제된다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 초안 대상 채널 ID |
| root_id | string | No | 스레드 초안일 경우 루트 게시글 ID |
| message | string | Yes | 초안 메시지. 빈 문자열이면 초안이 삭제된다 |
| type | string | No | 초안 타입 |
| props | object | No | 추가 속성 |
| file_ids | string[] | No | 첨부 파일 ID 목록 |
| priority | object | No | 우선순위 정보 (priority: "" \| "important" \| "urgent", requested_ack: boolean, persistent_notifications: boolean) |

```json
{
  "channel_id": "string",
  "root_id": "string",
  "message": "string",
  "type": "string",
  "props": {},
  "file_ids": ["string"],
  "priority": {
    "priority": "important",
    "requested_ack": false,
    "persistent_notifications": false
  }
}
```

## Response

### 201 - Draft upsert successful
업서트된 초안을 반환한다. 빈 메시지로 초안을 삭제한 경우 `null`을 반환한다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 501 | 기능이 활성화되지 않음 |

## 주의 사항
서버에서 synced drafts 기능이 활성화되어 있어야 한다.

---

# 2. Get synced drafts for a team

## 기본 정보
- **기능**: 특정 팀에서 현재 사용자의 동기화 초안 목록을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/teams/{team_id}/drafts`
- **인증**: 로그인 필요
- **권한**: 해당 팀의 `view_team`

## 설명
지정한 팀 내에서 현재 사용자가 작성해 둔 초안 목록을 조회하는 API이다. 해당 팀에 대한 `view_team` 권한이 있어야 하며, 서버에서 synced drafts 기능이 활성화되어 있어야 한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID |
| team_id | string | Yes | 팀 ID |

## Response

### 200 - Drafts retrieval successful
초안 객체의 배열을 반환한다.

| 필드 | 타입 | 설명 |
|---|---|---|
| create_at | integer | 초안 생성 시각 |
| update_at | integer | 초안 갱신 시각 |
| delete_at | integer | Deprecated. 초안은 hard-delete 된다 |
| user_id | string | 사용자 ID |
| channel_id | string | 채널 ID |
| root_id | string | 스레드 초안일 경우 루트 게시글 ID |
| message | string | 초안 메시지 |
| type | string | 초안 타입 |
| props | object | 추가 속성 |
| file_ids | string[] | 첨부 파일 ID 목록 |
| metadata | object | 임베드, 이모지, 파일, 이미지, 리액션, 우선순위, 확인(acknowledgements) 등 부가 정보 |
| priority | object | 우선순위 정보 (priority: "" \| "important" \| "urgent", requested_ack: boolean, persistent_notifications: boolean) |

```json
[
  {
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0,
    "user_id": "string",
    "channel_id": "string",
    "root_id": "string",
    "message": "string",
    "type": "string",
    "props": {},
    "file_ids": ["string"],
    "metadata": {},
    "priority": {
      "priority": "",
      "requested_ack": false,
      "persistent_notifications": false
    }
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 501 | 기능이 활성화되지 않음 |

## 주의 사항
서버에서 synced drafts 기능이 활성화되어 있어야 한다.

---

# 3. Delete synced draft

## 기본 정보
- **기능**: 특정 채널에 대한 동기화 초안을 삭제한다.
- **Endpoint**: `DELETE /api/v4/users/{user_id}/channels/{channel_id}/drafts`
- **인증**: 로그인 필요
- **권한**: 초안 소유자 본인만 가능 (별도의 이름있는 권한 불요)

## 설명
지정한 채널에 저장된 초안을 삭제하는 API이다. 초안의 소유자로 인증된 경우에만 호출할 수 있으며, 서버에서 synced drafts 기능이 활성화되어 있어야 한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID |
| channel_id | string | Yes | 채널 ID |

## Response

### 200 - Draft deletion successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 요청 성공 시 "ok" 반환 |

```json
{ "status": "ok" }
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 403 | 권한 없음 (초안 소유자가 아닌 경우) |
| 501 | 기능이 활성화되지 않음 |

## 주의 사항
초안 소유자 본인만 삭제할 수 있으며, 서버에서 synced drafts 기능이 활성화되어 있어야 한다.

---

# 4. Delete synced thread draft

## 기본 정보
- **기능**: 특정 채널의 스레드에 대한 동기화 초안을 삭제한다.
- **Endpoint**: `DELETE /api/v4/users/{user_id}/channels/{channel_id}/drafts/{thread_id}`
- **인증**: 로그인 필요
- **권한**: 초안 소유자 본인만 가능 (별도의 이름있는 권한 불요)

## 설명
지정한 채널의 특정 스레드에 저장된 초안을 삭제하는 API이다. 초안의 소유자로 인증된 경우에만 호출할 수 있으며, 서버에서 synced drafts 기능이 활성화되어 있어야 한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID |
| channel_id | string | Yes | 채널 ID |
| thread_id | string | Yes | 스레드의 루트 게시글 ID |

## Response

### 200 - Thread draft deletion successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 요청 성공 시 "ok" 반환 |

```json
{ "status": "ok" }
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 403 | 권한 없음 (초안 소유자가 아닌 경우) |
| 501 | 기능이 활성화되지 않음 |

## 주의 사항
초안 소유자 본인만 삭제할 수 있으며, 서버에서 synced drafts 기능이 활성화되어 있어야 한다.

---
