# 1. Create a channel recap

## 기본 정보
- **기능**: 지정한 채널들의 읽지 않은 메시지를 AI가 요약하는 recap을 생성한다.
- **Endpoint**: `POST /api/v4/recaps`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증 필요, 지정한 모든 채널의 멤버여야 함)

## 설명
선택한 채널들의 읽지 않은 메시지를 요약해 하이라이트와 액션 아이템을 추출하는 AI recap을 생성하는 API이다. recap은 백그라운드 작업으로 비동기 처리되며, 인증된 사용자 본인 소유로 생성된다. 지정한 모든 채널의 멤버여야 한다. 최소 서버 버전은 11.2이다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| title | string | Yes | recap 제목 |
| channel_ids | array(string) | Yes | recap에 포함할 채널 ID 목록 |
| agent_id | string | Yes | recap 생성에 사용할 AI 에이전트 ID |

```json
{
  "title": "string",
  "channel_ids": ["string"],
  "agent_id": "string"
}
```

## Response

### 201 - Recap creation successful (비동기 처리)
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | recap 고유 ID |
| user_id | string | recap을 생성한 사용자 ID |
| title | string | AI가 생성한 recap 제목 (최대 5단어) |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |
| read_at | integer | 읽음 처리된 시각 (밀리초) |
| viewed_at | integer | 확인(viewed) 처리된 시각 (밀리초) |
| total_message_count | integer | 전체 채널에서 요약된 총 메시지 수 |
| status | string | recap 작업 상태 (`pending` \| `processing` \| `completed` \| `failed`) |
| bot_id | string | recap 생성에 사용된 AI 에이전트/봇 ID |
| channels | array | 채널별 요약 목록 (id, recap_id, channel_id, channel_name, highlights, action_items, source_post_ids, create_at) |

```json
{
  "id": "string",
  "user_id": "string",
  "title": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "read_at": 0,
  "viewed_at": 0,
  "total_message_count": 0,
  "status": "pending",
  "bot_id": "string",
  "channels": [
    {
      "id": "string",
      "recap_id": "string",
      "channel_id": "string",
      "channel_name": "string",
      "highlights": ["string"],
      "action_items": ["string"],
      "source_post_ids": ["string"],
      "create_at": 0
    }
  ]
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

---

# 2. Get current user's recaps

## 기본 정보
- **기능**: 현재 사용자가 생성한 recap 목록을 페이지네이션으로 조회한다.
- **Endpoint**: `GET /api/v4/recaps`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요, 본인 recap만 조회)

## 설명
인증된 사용자가 생성한 recap들의 페이지네이션된 목록을 조회하는 API이다. 최소 서버 버전은 11.2이다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| page | integer | No | - | 조회할 페이지 |
| per_page | integer | No | - | 페이지당 recap 수 |

## Response

### 200 - Recaps retrieval successful
recap 객체 배열을 반환한다. 필드 구성은 "Create a channel recap"의 201 응답과 동일하다.

```json
[
  {
    "id": "string",
    "user_id": "string",
    "title": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0,
    "read_at": 0,
    "viewed_at": 0,
    "total_message_count": 0,
    "status": "completed",
    "bot_id": "string",
    "channels": []
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |

---

# 3. Mark all of the authenticated user's finished recaps as viewed

## 기본 정보
- **기능**: 본인의 완료(completed)/실패(failed) 상태 recap 중 아직 확인하지 않은 것들을 일괄 확인(viewed) 처리한다.
- **Endpoint**: `POST /api/v4/recaps/mark_viewed`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요, 본인 recap에만 동작)

## 설명
아직 확인하지 않은 완료 또는 실패 상태의 본인 recap을 현재 시각으로 일괄 확인 처리하는 API이다. pending/processing 상태 recap은 영향을 받지 않는다. 갱신된 recap ID 목록을 반환하며, 영향받은 각 recap에 대해 `recap_updated` WebSocket 이벤트가 브로드캐스트된다. 보통 recaps 페이지를 열 때 한 번 호출해 사이드바 미확인 배지를 일괄 제거하는 용도이다. 최소 서버 버전은 11.2이다.

## Response

### 200 - Recaps marked as viewed successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| recap_ids | array(string) | 갱신된 recap ID 목록 |

```json
{
  "recap_ids": ["string"]
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 501 | AI Recaps feature flag 비활성화 |

---

# 4. Get a specific recap

## 기본 정보
- **기능**: recap ID로 특정 recap을 채널별 요약과 함께 조회한다.
- **Endpoint**: `GET /api/v4/recaps/{recap_id}`
- **인증**: Bearer Token 필요
- **권한**: 없음 (본인이 생성한 recap만 조회 가능)

## 설명
recap ID로 모든 채널 요약을 포함한 recap을 조회하는 API이다. recap을 생성한 사용자 본인만 조회할 수 있다. 최소 서버 버전은 11.2이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| recap_id | string | Yes | Recap GUID |

## Response

### 200 - Recap retrieval successful
recap 객체를 반환한다. 필드 구성은 "Create a channel recap"의 201 응답과 동일하다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 403 | 권한 없음 (본인 recap이 아닌 경우) |
| 404 | recap을 찾을 수 없음 |

---

# 5. Delete a recap

## 기본 정보
- **기능**: recap ID로 recap을 삭제한다.
- **Endpoint**: `DELETE /api/v4/recaps/{recap_id}`
- **인증**: Bearer Token 필요
- **권한**: 없음 (본인이 생성한 recap만 삭제 가능)

## 설명
recap ID로 recap을 삭제하는 API이다. recap을 생성한 사용자 본인만 삭제할 수 있다. 최소 서버 버전은 11.2이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| recap_id | string | Yes | Recap GUID |

## Response

### 200 - Recap deletion successful
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
| 403 | 권한 없음 (본인 recap이 아닌 경우) |
| 404 | recap을 찾을 수 없음 |

---

# 6. Mark a recap as read

## 기본 정보
- **기능**: recap을 읽음 처리한다.
- **Endpoint**: `POST /api/v4/recaps/{recap_id}/read`
- **인증**: Bearer Token 필요
- **권한**: 없음 (본인이 생성한 recap만 가능)

## 설명
recap을 읽음 처리해 read 상태와 타임스탬프를 갱신하는 API이다. recap을 생성한 사용자 본인만 가능하다. 최소 서버 버전은 11.2이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| recap_id | string | Yes | Recap GUID |

## Response

### 200 - Recap marked as read successfully
갱신된 recap 객체를 반환한다. 필드 구성은 "Create a channel recap"의 201 응답과 동일하다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 403 | 권한 없음 (본인 recap이 아닌 경우) |
| 404 | recap을 찾을 수 없음 |

---

# 7. Regenerate a recap

## 기본 정보
- **기능**: recap을 최신 메시지 기준으로 다시 생성한다.
- **Endpoint**: `POST /api/v4/recaps/{recap_id}/regenerate`
- **인증**: Bearer Token 필요
- **권한**: 없음 (본인이 생성한 recap만 가능)

## 설명
recap ID로 recap을 재생성하는 API이다. 지정된 채널들의 최신 메시지로 AI recap을 다시 생성하는 백그라운드 작업이 새로 만들어진다. recap을 생성한 사용자 본인만 가능하다. 최소 서버 버전은 11.2이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| recap_id | string | Yes | Recap GUID |

## Response

### 200 - Recap regeneration initiated successfully
recap 객체를 반환한다. 필드 구성은 "Create a channel recap"의 201 응답과 동일하다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 403 | 권한 없음 (본인 recap이 아닌 경우) |
| 404 | recap을 찾을 수 없음 |

## 주의 사항
AI Recaps 기능은 서버의 feature flag와 AI 에이전트 구성이 활성화되어 있어야 동작한다 (비활성 시 501 반환 가능).

---
