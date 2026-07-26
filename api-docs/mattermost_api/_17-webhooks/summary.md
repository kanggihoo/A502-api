# 1. Create an incoming webhook

## 기본 정보
- **기능**: 채널에 메시지를 게시할 수 있는 incoming webhook을 생성한다.
- **Endpoint**: `POST /api/v4/hooks/incoming`
- **인증**: Bearer Token 필요
- **권한**: `manage_own_incoming_webhooks` (팀 레벨, 본인 소유 webhook 한정. 문서상 표기는 `manage_webhooks` for the team)

## 설명
지정한 공개 채널 또는 비공개 그룹에 페이로드를 전달하는 incoming webhook을 생성하는 API이다. webhook 소유자를 요청자와 다른 사용자로 지정하려면 `manage_others_incoming_webhooks` 권한이 추가로 필요하다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | webhook 페이로드를 수신할 공개 채널 또는 비공개 그룹의 ID |
| user_id | string | No | 요청자와 다른 경우 webhook 소유자의 ID (local mode에서 필수) |
| display_name | string | No | incoming webhook의 표시 이름 |
| description | string | No | incoming webhook의 설명 |
| username | string | No | webhook이 게시할 때 사용할 사용자 이름 |
| icon_url | string | No | webhook이 게시할 때 사용할 프로필 사진 |
| channel_locked | boolean | No | webhook을 채널에 고정할지 여부 |

```json
{
  "channel_id": "string",
  "display_name": "string",
  "description": "string",
  "username": "string",
  "icon_url": "string",
  "channel_locked": false
}
```

## Response

### 201 - Incoming webhook creation successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | incoming webhook의 고유 식별자 |
| create_at | integer | incoming webhook이 생성된 시각 (밀리초) |
| update_at | integer | incoming webhook이 마지막으로 수정된 시각 (밀리초) |
| delete_at | integer | incoming webhook이 삭제된 시각 (밀리초) |
| last_used | integer | 이 webhook으로 마지막으로 메시지가 게시된 시각 (밀리초) |
| channel_id | string | webhook 페이로드를 수신하는 공개 채널 또는 비공개 그룹의 ID |
| description | string | incoming webhook의 설명 |
| display_name | string | incoming webhook의 표시 이름 |

```json
{
  "id": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "last_used": 0,
  "channel_id": "string",
  "description": "string",
  "display_name": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

## 주의 사항
현재 계정은 `manage_own_incoming_webhooks` 권한만 보유하므로 본인 소유 webhook 생성만 가능하다. `user_id`를 타인으로 지정하려면 `manage_others_incoming_webhooks` 권한이 필요하다.

---

# 2. List incoming webhooks

## 기본 정보
- **기능**: incoming webhook 목록을 페이지 단위로 조회한다.
- **Endpoint**: `GET /api/v4/hooks/incoming`
- **인증**: Bearer Token 필요
- **권한**: `manage_own_incoming_webhooks` (팀 레벨, 본인 소유 webhook 범위. 문서상 표기는 시스템 또는 팀의 `manage_webhooks`)

## 설명
incoming webhook 목록을 페이지 단위로 조회하는 API이다. 쿼리 파라미터로 특정 팀의 webhook만 필터링할 수 있다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| page | integer | No | - | 조회할 페이지 |
| per_page | integer | No | - | 페이지당 hook 수 |
| team_id | string | No | - | hook을 조회할 팀의 ID |
| include_total_count | boolean | No | - | 응답 객체에 전체 hook 수를 포함 (예: `{ "incoming_webhooks": [], "total_count": 0 }`) |

## Response

### 200 - Incoming webhooks retrieval successful
incoming webhook 객체의 배열을 반환한다.

| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | incoming webhook의 고유 식별자 |
| create_at | integer | incoming webhook이 생성된 시각 (밀리초) |
| update_at | integer | incoming webhook이 마지막으로 수정된 시각 (밀리초) |
| delete_at | integer | incoming webhook이 삭제된 시각 (밀리초) |
| last_used | integer | 이 webhook으로 마지막으로 메시지가 게시된 시각 (밀리초) |
| channel_id | string | webhook 페이로드를 수신하는 공개 채널 또는 비공개 그룹의 ID |
| description | string | incoming webhook의 설명 |
| display_name | string | incoming webhook의 표시 이름 |

```json
[
  {
    "id": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0,
    "last_used": 0,
    "channel_id": "string",
    "description": "string",
    "display_name": "string"
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
본인 소유 webhook 범위로 조회된다. 시스템 전체 webhook 조회는 시스템 레벨 `manage_webhooks` 권한이 필요하다.

---

# 3. Get an incoming webhook

## 기본 정보
- **기능**: hook ID로 incoming webhook 하나를 조회한다.
- **Endpoint**: `GET /api/v4/hooks/incoming/{hook_id}`
- **인증**: Bearer Token 필요
- **권한**: `manage_own_incoming_webhooks` (팀 레벨, 본인 소유 webhook 한정. 문서상 표기는 시스템/팀/채널의 `manage_webhooks`)

## 설명
hook ID를 지정하여 incoming webhook 하나의 정보를 조회하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| hook_id | string | Yes | Incoming Webhook GUID |

## Response

### 200 - Webhook retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | incoming webhook의 고유 식별자 |
| create_at | integer | incoming webhook이 생성된 시각 (밀리초) |
| update_at | integer | incoming webhook이 마지막으로 수정된 시각 (밀리초) |
| delete_at | integer | incoming webhook이 삭제된 시각 (밀리초) |
| last_used | integer | 이 webhook으로 마지막으로 메시지가 게시된 시각 (밀리초) |
| channel_id | string | webhook 페이로드를 수신하는 공개 채널 또는 비공개 그룹의 ID |
| description | string | incoming webhook의 설명 |
| display_name | string | incoming webhook의 표시 이름 |

```json
{
  "id": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "last_used": 0,
  "channel_id": "string",
  "description": "string",
  "display_name": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인 소유 webhook만 조회 가능하다. 타인 소유 webhook 조회는 `manage_others_incoming_webhooks` 계열 권한이 필요하다.

---

# 4. Delete an incoming webhook

## 기본 정보
- **기능**: hook ID로 incoming webhook을 삭제한다.
- **Endpoint**: `DELETE /api/v4/hooks/incoming/{hook_id}`
- **인증**: Bearer Token 필요
- **권한**: `manage_own_incoming_webhooks` (팀 레벨, 본인 소유 webhook 한정. 문서상 표기는 시스템/팀/채널의 `manage_webhooks`)

## 설명
hook ID를 지정하여 incoming webhook을 삭제하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| hook_id | string | Yes | Incoming webhook GUID |

## Response

### 200 - Webhook deletion successful
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
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인 소유 webhook만 삭제 가능하다. 타인 소유 webhook 삭제는 `manage_others_incoming_webhooks` 계열 권한이 필요하다.

---

# 5. Update an incoming webhook

## 기본 정보
- **기능**: hook ID로 incoming webhook 정보를 수정한다.
- **Endpoint**: `PUT /api/v4/hooks/incoming/{hook_id}`
- **인증**: Bearer Token 필요
- **권한**: `manage_own_incoming_webhooks` (팀 레벨, 본인 소유 webhook 한정. 문서상 표기는 시스템/팀/채널의 `manage_webhooks`)

## 설명
hook ID를 지정하여 incoming webhook의 대상 채널, 표시 이름, 설명 등을 수정하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| hook_id | string | Yes | Incoming Webhook GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | Incoming webhook GUID |
| channel_id | string | Yes | webhook 페이로드를 수신할 공개 채널 또는 비공개 그룹의 ID |
| display_name | string | Yes | incoming webhook의 표시 이름 |
| description | string | Yes | incoming webhook의 설명 |
| username | string | No | webhook이 게시할 때 사용할 사용자 이름 |
| icon_url | string | No | webhook이 게시할 때 사용할 프로필 사진 |
| channel_locked | boolean | No | webhook을 채널에 고정할지 여부 |

```json
{
  "id": "string",
  "channel_id": "string",
  "display_name": "string",
  "description": "string",
  "username": "string",
  "icon_url": "string",
  "channel_locked": false
}
```

## Response

### 200 - Webhook update successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | incoming webhook의 고유 식별자 |
| create_at | integer | incoming webhook이 생성된 시각 (밀리초) |
| update_at | integer | incoming webhook이 마지막으로 수정된 시각 (밀리초) |
| delete_at | integer | incoming webhook이 삭제된 시각 (밀리초) |
| last_used | integer | 이 webhook으로 마지막으로 메시지가 게시된 시각 (밀리초) |
| channel_id | string | webhook 페이로드를 수신하는 공개 채널 또는 비공개 그룹의 ID |
| description | string | incoming webhook의 설명 |
| display_name | string | incoming webhook의 표시 이름 |

```json
{
  "id": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "last_used": 0,
  "channel_id": "string",
  "description": "string",
  "display_name": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인 소유 webhook만 수정 가능하다. 타인 소유 webhook 수정은 `manage_others_incoming_webhooks` 계열 권한이 필요하다.

---

# 6. Create an outgoing webhook

## 기본 정보
- **기능**: 팀에 대한 outgoing webhook을 생성한다.
- **Endpoint**: `POST /api/v4/hooks/outgoing`
- **인증**: Bearer Token 필요
- **권한**: `manage_own_outgoing_webhooks` (팀 레벨, 본인 소유 webhook 한정. 문서상 표기는 `manage_webhooks` for the team)

## 설명
지정한 팀/채널에서 트리거 단어를 감시하다가 매칭되는 메시지가 게시되면 콜백 URL로 페이로드를 전송하는 outgoing webhook을 생성하는 API이다. webhook 소유자를 요청자와 다른 사용자로 지정하려면 `manage_others_outgoing_webhooks` 권한이 추가로 필요하다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| team_id | string | Yes | webhook이 감시하는 팀의 ID |
| channel_id | string | No | webhook이 감시하는 공개 채널의 ID |
| creator_id | string | No | 요청자와 다른 경우 webhook 소유자의 ID (local mode에서 필수) |
| description | string | No | outgoing webhook의 설명 |
| display_name | string | Yes | outgoing webhook의 표시 이름 |
| trigger_words | array of string | Yes | webhook을 트리거할 단어 목록 |
| trigger_when | integer | No | 트리거 시점. `0`: 트리거 단어가 포함될 때, `1`: 메시지가 트리거 단어로 시작할 때 |
| callback_urls | array of string | Yes | webhook 트리거 시 페이로드를 POST할 URL 목록 |
| content_type | string | No | 데이터 POST 형식. `application/json` 또는 `application/x-www-form-urlencoded` |

```json
{
  "team_id": "string",
  "channel_id": "string",
  "display_name": "string",
  "description": "string",
  "trigger_words": ["string"],
  "trigger_when": 0,
  "callback_urls": ["string"],
  "content_type": "application/json"
}
```

## Response

### 201 - Outgoing webhook creation successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | outgoing webhook의 고유 식별자 |
| create_at | integer | outgoing webhook이 생성된 시각 (밀리초) |
| update_at | integer | outgoing webhook이 마지막으로 수정된 시각 (밀리초) |
| delete_at | integer | outgoing webhook이 삭제된 시각 (밀리초) |
| creator_id | string | webhook을 생성한 사용자의 ID |
| team_id | string | webhook이 감시하는 팀의 ID |
| channel_id | string | webhook이 감시하는 공개 채널의 ID |
| description | string | outgoing webhook의 설명 |
| display_name | string | outgoing webhook의 표시 이름 |
| trigger_words | array of string | webhook을 트리거할 단어 목록 |
| trigger_when | integer | 트리거 시점 (`0` 포함 시, `1` 시작 시) |
| callback_urls | array of string | 트리거 시 페이로드를 POST할 URL 목록 |
| content_type | string | 데이터 POST 형식 |

```json
{
  "id": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "creator_id": "string",
  "team_id": "string",
  "channel_id": "string",
  "description": "string",
  "display_name": "string",
  "trigger_words": ["string"],
  "trigger_when": 0,
  "callback_urls": ["string"],
  "content_type": "application/json"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
현재 계정은 `manage_own_outgoing_webhooks` 권한만 보유하므로 본인 소유 webhook 생성만 가능하다. `creator_id`를 타인으로 지정하려면 `manage_others_outgoing_webhooks` 권한이 필요하다.

---

# 7. List outgoing webhooks

## 기본 정보
- **기능**: outgoing webhook 목록을 페이지 단위로 조회한다.
- **Endpoint**: `GET /api/v4/hooks/outgoing`
- **인증**: Bearer Token 필요
- **권한**: `manage_own_outgoing_webhooks` (팀 레벨, 본인 소유 webhook 범위. 문서상 표기는 시스템 또는 팀/채널의 `manage_webhooks`)

## 설명
outgoing webhook 목록을 페이지 단위로 조회하는 API이다. 쿼리 파라미터로 특정 팀 또는 채널의 webhook만 필터링할 수 있다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| page | integer | No | - | 조회할 페이지 |
| per_page | integer | No | - | 페이지당 hook 수 |
| team_id | string | No | - | hook을 조회할 팀의 ID |
| channel_id | string | No | - | hook을 조회할 채널의 ID |

## Response

### 200 - Outgoing webhooks retrieval successful
outgoing webhook 객체의 배열을 반환한다.

| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | outgoing webhook의 고유 식별자 |
| create_at | integer | outgoing webhook이 생성된 시각 (밀리초) |
| update_at | integer | outgoing webhook이 마지막으로 수정된 시각 (밀리초) |
| delete_at | integer | outgoing webhook이 삭제된 시각 (밀리초) |
| creator_id | string | webhook을 생성한 사용자의 ID |
| team_id | string | webhook이 감시하는 팀의 ID |
| channel_id | string | webhook이 감시하는 공개 채널의 ID |
| description | string | outgoing webhook의 설명 |
| display_name | string | outgoing webhook의 표시 이름 |
| trigger_words | array of string | webhook을 트리거할 단어 목록 |
| trigger_when | integer | 트리거 시점 (`0` 포함 시, `1` 시작 시) |
| callback_urls | array of string | 트리거 시 페이로드를 POST할 URL 목록 |
| content_type | string | 데이터 POST 형식 |

```json
[
  {
    "id": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0,
    "creator_id": "string",
    "team_id": "string",
    "channel_id": "string",
    "description": "string",
    "display_name": "string",
    "trigger_words": ["string"],
    "trigger_when": 0,
    "callback_urls": ["string"],
    "content_type": "application/json"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인 소유 webhook 범위로 조회된다. 시스템 전체 webhook 조회는 시스템 레벨 `manage_webhooks` 권한이 필요하다.

---

# 8. Get an outgoing webhook

## 기본 정보
- **기능**: hook ID로 outgoing webhook 하나를 조회한다.
- **Endpoint**: `GET /api/v4/hooks/outgoing/{hook_id}`
- **인증**: Bearer Token 필요
- **권한**: `manage_own_outgoing_webhooks` (팀 레벨, 본인 소유 webhook 한정. 문서상 표기는 시스템/팀/채널의 `manage_webhooks`)

## 설명
hook ID를 지정하여 outgoing webhook 하나의 정보를 조회하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| hook_id | string | Yes | Outgoing webhook GUID |

## Response

### 200 - Outgoing webhook retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | outgoing webhook의 고유 식별자 |
| create_at | integer | outgoing webhook이 생성된 시각 (밀리초) |
| update_at | integer | outgoing webhook이 마지막으로 수정된 시각 (밀리초) |
| delete_at | integer | outgoing webhook이 삭제된 시각 (밀리초) |
| creator_id | string | webhook을 생성한 사용자의 ID |
| team_id | string | webhook이 감시하는 팀의 ID |
| channel_id | string | webhook이 감시하는 공개 채널의 ID |
| description | string | outgoing webhook의 설명 |
| display_name | string | outgoing webhook의 표시 이름 |
| trigger_words | array of string | webhook을 트리거할 단어 목록 |
| trigger_when | integer | 트리거 시점 (`0` 포함 시, `1` 시작 시) |
| callback_urls | array of string | 트리거 시 페이로드를 POST할 URL 목록 |
| content_type | string | 데이터 POST 형식 |

```json
{
  "id": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "creator_id": "string",
  "team_id": "string",
  "channel_id": "string",
  "description": "string",
  "display_name": "string",
  "trigger_words": ["string"],
  "trigger_when": 0,
  "callback_urls": ["string"],
  "content_type": "application/json"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인 소유 webhook만 조회 가능하다. 타인 소유 webhook 조회는 `manage_others_outgoing_webhooks` 계열 권한이 필요하다.

---

# 9. Delete an outgoing webhook

## 기본 정보
- **기능**: hook ID로 outgoing webhook을 삭제한다.
- **Endpoint**: `DELETE /api/v4/hooks/outgoing/{hook_id}`
- **인증**: Bearer Token 필요
- **권한**: `manage_own_outgoing_webhooks` (팀 레벨, 본인 소유 webhook 한정. 문서상 표기는 시스템/팀/채널의 `manage_webhooks`)

## 설명
hook ID를 지정하여 outgoing webhook을 삭제하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| hook_id | string | Yes | Outgoing webhook GUID |

## Response

### 200 - Webhook deletion successful
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
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인 소유 webhook만 삭제 가능하다. 타인 소유 webhook 삭제는 `manage_others_outgoing_webhooks` 계열 권한이 필요하다.

---

# 10. Update an outgoing webhook

## 기본 정보
- **기능**: hook ID로 outgoing webhook 정보를 수정한다.
- **Endpoint**: `PUT /api/v4/hooks/outgoing/{hook_id}`
- **인증**: Bearer Token 필요
- **권한**: `manage_own_outgoing_webhooks` (팀 레벨, 본인 소유 webhook 한정. 문서상 표기는 시스템/팀/채널의 `manage_webhooks`)

## 설명
hook ID를 지정하여 outgoing webhook의 대상 채널, 표시 이름, 설명을 수정하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| hook_id | string | Yes | Outgoing Webhook GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | Outgoing webhook GUID |
| channel_id | string | Yes | webhook 페이로드를 수신할 공개 채널 또는 비공개 그룹의 ID |
| display_name | string | Yes | webhook의 표시 이름 |
| description | string | Yes | webhook의 설명 |

```json
{
  "id": "string",
  "channel_id": "string",
  "display_name": "string",
  "description": "string"
}
```

## Response

### 200 - Webhook update successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | outgoing webhook의 고유 식별자 |
| create_at | integer | outgoing webhook이 생성된 시각 (밀리초) |
| update_at | integer | outgoing webhook이 마지막으로 수정된 시각 (밀리초) |
| delete_at | integer | outgoing webhook이 삭제된 시각 (밀리초) |
| creator_id | string | webhook을 생성한 사용자의 ID |
| team_id | string | webhook이 감시하는 팀의 ID |
| channel_id | string | webhook이 감시하는 공개 채널의 ID |
| description | string | outgoing webhook의 설명 |
| display_name | string | outgoing webhook의 표시 이름 |
| trigger_words | array of string | webhook을 트리거할 단어 목록 |
| trigger_when | integer | 트리거 시점 (`0` 포함 시, `1` 시작 시) |
| callback_urls | array of string | 트리거 시 페이로드를 POST할 URL 목록 |
| content_type | string | 데이터 POST 형식 |

```json
{
  "id": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "creator_id": "string",
  "team_id": "string",
  "channel_id": "string",
  "description": "string",
  "display_name": "string",
  "trigger_words": ["string"],
  "trigger_when": 0,
  "callback_urls": ["string"],
  "content_type": "application/json"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인 소유 webhook만 수정 가능하다. 타인 소유 webhook 수정은 `manage_others_outgoing_webhooks` 계열 권한이 필요하다.

---

# 11. Regenerate the token for the outgoing webhook

## 기본 정보
- **기능**: outgoing webhook의 토큰을 재발급한다.
- **Endpoint**: `POST /api/v4/hooks/outgoing/{hook_id}/regen_token`
- **인증**: Bearer Token 필요
- **권한**: `manage_own_outgoing_webhooks` (팀 레벨, 본인 소유 webhook 한정. 문서상 표기는 시스템/팀/채널의 `manage_webhooks`)

## 설명
hook ID를 지정하여 outgoing webhook의 토큰을 재발급하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| hook_id | string | Yes | Outgoing webhook GUID |

## Response

### 200 - Webhook token regenerate successful
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
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인 소유 webhook에 대해서만 토큰 재발급이 가능하다. 타인 소유 webhook 대상 시 `manage_others_outgoing_webhooks` 계열 권한이 필요하다.

---
