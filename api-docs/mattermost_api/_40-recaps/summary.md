# 1. Create a channel recap

## 기본 정보
- **기능**: 지정한 채널들에 대해 AI 기반 recap(요약)을 생성한다.
- **Endpoint**: `POST /api/v4/recaps`
- **인증**: 로그인 필요
- **권한**: 없음 (인증 필요, 지정한 모든 채널의 멤버여야 함)

## 설명
선택한 채널들의 읽지 않은 메시지를 요약하고 핵심 내용(highlights)과 액션 아이템을 추출하는 AI recap을 생성하는 API이다. 백그라운드 잡으로 비동기 처리되며, recap은 인증된 사용자 본인 소유로 생성된다. 지정한 모든 채널의 멤버여야 한다. 최소 서버 버전 11.2.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| title | string | Yes | recap 제목 |
| channel_ids | string[] | Yes | recap에 포함할 채널 ID 목록 |
| agent_id | string | Yes | recap 생성에 사용할 AI 에이전트 ID |

```json
{
  "title": "string",
  "channel_ids": ["string"],
  "agent_id": "string"
}
```

## Response

### 201 - Recap creation successful. The recap will be processed asynchronously.
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | recap 고유 식별자 |
| user_id | string | recap을 생성한 사용자 ID |
| title | string | AI가 생성한 recap 제목 (최대 5단어) |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 갱신 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |
| read_at | integer | 읽음 처리된 시각 (밀리초) |
| viewed_at | integer | 조회 처리된 시각 (밀리초, recaps 페이지 열람 시 일괄 설정) |
| total_message_count | integer | 전체 채널에서 요약된 총 메시지 수 |
| status | enum | recap 잡 상태 ("pending" \| "processing" \| "completed" \| "failed") |
| bot_id | string | recap 생성에 사용된 AI 에이전트/봇 ID |
| channels | object[] | 이 recap에 포함된 채널별 요약 목록 |
| channels[].id | string | recap 채널 고유 식별자 |
| channels[].recap_id | string | 상위 recap ID |
| channels[].channel_id | string | 요약된 채널 ID |
| channels[].channel_name | string | 채널 표시명 |
| channels[].highlights | string[] | 채널의 핵심 논의 사항과 중요 정보 |
| channels[].action_items | string[] | 채널에서 언급된 할 일·액션 아이템 |
| channels[].source_post_ids | string[] | 요약 생성에 사용된 게시물 ID 목록 |
| channels[].create_at | integer | recap 채널 생성 시각 (밀리초) |

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
| 403 | 권한 없음 (채널 멤버가 아닌 경우 등) |

## 주의 사항
recap은 비동기(백그라운드 잡)로 처리되므로 응답 시점의 status는 "pending"일 수 있다.

---

# 2. Get current user's recaps

## 기본 정보
- **기능**: 현재 사용자가 생성한 recap 목록을 페이지 단위로 조회한다.
- **Endpoint**: `GET /api/v4/recaps`
- **인증**: 로그인 필요
- **권한**: 없음 (인증만 필요, 본인 recap만 조회)

## 설명
인증된 사용자가 생성한 recap들의 페이지네이션 목록을 조회하는 API이다. 최소 서버 버전 11.2.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| page | integer | No | - | 조회할 페이지 |
| per_page | integer | No | - | 페이지당 recap 수 |

## Response

### 200 - Recaps retrieval successful
recap 객체 배열을 반환한다. 각 recap 객체의 필드는 1번(Create a channel recap)의 응답 스키마와 동일하다.

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
- **기능**: 본인의 완료(completed/failed)된 미열람 recap을 모두 viewed 처리한다.
- **Endpoint**: `POST /api/v4/recaps/mark_viewed`
- **인증**: 로그인 필요
- **권한**: 없음 (본인 recap에만 동작)

## 설명
인증된 사용자의 아직 열람되지 않은 completed 또는 failed 상태 recap 전부를 현재 시각으로 viewed 처리하는 API이다. pending/processing 상태의 recap은 영향을 받지 않는다. 갱신된 recap ID 목록을 반환하며, 영향을 받은 recap마다 `recap_updated` WebSocket 이벤트가 브로드캐스트된다. 보통 recaps 페이지를 열 때 한 번 호출해 사이드바 unread 배지를 일괄 해제하는 용도이다. 최소 서버 버전 11.2.

## Response

### 200 - Recaps marked as viewed successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| recap_ids | string[] | 갱신된 recap ID 목록 |

```json
{ "recap_ids": ["string"] }
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 501 | AI Recaps feature flag 비활성화 |

---

# 4. Get a specific recap

## 기본 정보
- **기능**: recap ID로 특정 recap을 채널별 요약 포함해 조회한다.
- **Endpoint**: `GET /api/v4/recaps/{recap_id}`
- **인증**: 로그인 필요
- **권한**: 없음 (본인이 생성한 recap만 조회 가능)

## 설명
recap ID로 모든 채널 요약을 포함한 recap을 조회하는 API이다. recap을 생성한 본인만 조회할 수 있다. 최소 서버 버전 11.2.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| recap_id | string | Yes | Recap GUID |

## Response

### 200 - Recap retrieval successful
recap 객체를 반환한다. 필드는 1번(Create a channel recap)의 응답 스키마와 동일하다.

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
- **인증**: 로그인 필요
- **권한**: 없음 (본인이 생성한 recap만 삭제 가능)

## 설명
recap ID로 recap을 삭제하는 API이다. recap을 생성한 본인만 삭제할 수 있다. 최소 서버 버전 11.2.

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
- **인증**: 로그인 필요
- **권한**: 없음 (본인이 생성한 recap만 가능)

## 설명
인증된 사용자가 recap을 읽음 처리하는 API이다. recap의 읽음 상태와 타임스탬프(read_at)가 갱신된다. 본인이 생성한 recap만 가능하다. 최소 서버 버전 11.2.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| recap_id | string | Yes | Recap GUID |

## Response

### 200 - Recap marked as read successfully
갱신된 recap 객체를 반환한다. 필드는 1번(Create a channel recap)의 응답 스키마와 동일하다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 403 | 권한 없음 (본인 recap이 아닌 경우) |
| 404 | recap을 찾을 수 없음 |

---

# 7. Regenerate a recap

## 기본 정보
- **기능**: recap을 최신 메시지로 다시 생성한다.
- **Endpoint**: `POST /api/v4/recaps/{recap_id}/regenerate`
- **인증**: 로그인 필요
- **권한**: 없음 (본인이 생성한 recap만 가능)

## 설명
recap ID로 recap을 재생성하는 API이다. 지정된 채널들의 최신 메시지로 AI recap을 다시 생성하는 새 백그라운드 잡을 만든다. 본인이 생성한 recap만 가능하다. 최소 서버 버전 11.2.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| recap_id | string | Yes | Recap GUID |

## Response

### 200 - Recap regeneration initiated successfully
recap 객체를 반환한다. 필드는 1번(Create a channel recap)의 응답 스키마와 동일하다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 403 | 권한 없음 (본인 recap이 아닌 경우) |
| 404 | recap을 찾을 수 없음 |

---
