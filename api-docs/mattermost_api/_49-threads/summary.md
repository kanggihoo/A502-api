# 1. Get all threads that user is following

## 기본 정보
- **기능**: 사용자가 팔로우 중인 모든 스레드를 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/teams/{team_id}/threads`
- **인증**: 로그인 필요
- **권한**: 본인(user_id) 계정에 대해서만 가능 (타 사용자는 `edit_other_users` 필요)

## 설명
특정 팀에서 사용자가 팔로우하고 있는 스레드 목록을 조회하는 API이다. `user_id`에 "me"를 사용하면 현재 사용자를 가리킨다. `since`, `deleted`, `extended` 등 다양한 쿼리 파라미터로 결과를 필터링하거나 참가자 상세 정보를 포함시킬 수 있다. 최소 서버 버전은 5.29이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID. "me"를 사용하면 현재 사용자를 가리킴 |
| team_id | string | Yes | 스레드가 속한 팀의 ID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| since | integer | No | - | LastUpdateAt 타임스탬프 기준으로 스레드를 필터링 |
| deleted | boolean | No | - | true이면 삭제된 스레드도 반환 (모바일 동기화용) |
| extended | boolean | No | - | true이면 참가자 상세 정보를 응답에 포함 |
| page | integer | No | - | per_page 단위로 반환할 결과 페이지 지정 |
| per_page | integer | No | - | 반환할 결과 묶음의 크기 |
| totalsOnly | boolean | No | - | true이면 전체 개수만 반환 |
| threadsOnly | boolean | No | - | true이면 스레드만 반환 |

## Response

### 200 - User's thread retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| total | integer | 전체 스레드 수 (페이징에 사용) |
| threads | array | 스레드 배열 |
| threads[].id | string | 스레드의 루트가 되는 게시글의 ID |
| threads[].reply_count | integer | 스레드의 답글 수 |
| threads[].last_reply_at | integer | 스레드에 마지막 게시글이 작성된 시각 |
| threads[].last_viewed_at | integer | 사용자가 스레드를 마지막으로 본 시각 |
| threads[].participants | array | 스레드 참가자 목록 (extended가 true가 아니면 ID만 포함) |
| threads[].post | object | 스레드 루트 게시글 정보 (id, create_at, update_at, delete_at, edit_at, user_id, channel_id, root_id, original_id, message, type, props, hashtag, file_ids, pending_post_id, metadata 등) |

```json
{
  "total": 0,
  "threads": [
    {
      "id": "string",
      "reply_count": 0,
      "last_reply_at": 0,
      "last_viewed_at": 0,
      "participants": [
        { "id": "string", "username": "string" }
      ],
      "post": {
        "id": "string",
        "create_at": 0,
        "user_id": "string",
        "channel_id": "string",
        "root_id": "string",
        "message": "string"
      }
    }
  ]
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인(user_id) 스레드에 대해서만 조회 가능하다 (타 사용자 대상은 `edit_other_users` 권한 필요). 최소 서버 버전 5.29.

---

# 2. Mark all threads that user is following as read

## 기본 정보
- **기능**: 사용자가 팔로우 중인 모든 스레드를 읽음 처리한다.
- **Endpoint**: `PUT /api/v4/users/{user_id}/teams/{team_id}/threads/read`
- **인증**: 로그인 필요
- **권한**: 본인(user_id) 계정에 대해서만 가능 (타 사용자는 `edit_other_users` 필요)

## 설명
특정 팀에서 사용자가 팔로우하고 있는 모든 스레드를 읽음 상태로 표시하는 API이다. `user_id`에 "me"를 사용하면 현재 사용자를 가리킨다. 최소 서버 버전은 5.29이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID. "me"를 사용하면 현재 사용자를 가리킴 |
| team_id | string | Yes | 스레드가 속한 팀의 ID |

## Response

### 200 - User's thread update successful

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인(user_id)에 대해서만 호출 가능하다 (타 사용자 대상은 `edit_other_users` 권한 필요). 최소 서버 버전 5.29.

---

# 3. Mark a thread that user is following read state to the timestamp

## 기본 정보
- **기능**: 사용자가 팔로우 중인 특정 스레드의 읽음 상태를 지정한 타임스탬프로 설정한다.
- **Endpoint**: `PUT /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/read/{timestamp}`
- **인증**: 로그인 필요
- **권한**: 본인(user_id) 계정에 대해서만 가능 (타 사용자는 `edit_other_users` 필요)

## 설명
팔로우 중인 특정 스레드의 "마지막 읽음(last read)" 상태를 지정한 타임스탬프로 재설정하는 API이다. `user_id`에 "me"를 사용하면 현재 사용자를 가리킨다. 최소 서버 버전은 5.29이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID. "me"를 사용하면 현재 사용자를 가리킴 |
| team_id | string | Yes | 스레드가 속한 팀의 ID |
| thread_id | string | Yes | 갱신할 스레드의 ID |
| timestamp | string | Yes | 스레드의 "마지막 읽음" 상태를 재설정할 타임스탬프 |

## Response

### 200 - User's thread update successful

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인(user_id)에 대해서만 호출 가능하다 (타 사용자 대상은 `edit_other_users` 권한 필요). 최소 서버 버전 5.29.

---

# 4. Mark a thread that user is following as unread based on a post id

## 기본 정보
- **기능**: 특정 post를 기준으로, 사용자가 팔로우 중인 스레드를 읽지 않음(unread) 상태로 표시한다.
- **Endpoint**: `POST /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/set_unread/{post_id}`
- **인증**: 로그인 필요
- **권한**: 스레드가 속한 채널의 `read_channel` 권한 필요 (보유). 공개 채널인 경우 팀의 `read_public_channels` 권한으로도 가능. 본인 계정에 대해서만 가능 (타 사용자는 `edit_other_users` 필요)

## 설명
스레드에 속한 특정 게시글(post_id)을 기준으로 해당 스레드를 읽지 않음 상태로 표시하는 API이다. 스레드가 속한 채널에 대한 `read_channel` 권한(현재 계정 보유)이 필요하며, 공개 채널이면 팀의 `read_public_channels` 권한으로도 가능하다. 본인이 아닌 사용자를 대상으로 표시하려면 `edit_other_users` 권한이 필요하므로 본인에 대해서만 사용 가능하다. 최소 서버 버전은 6.7이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID. "me"를 사용하면 현재 사용자를 가리킴 |
| team_id | string | Yes | 스레드가 속한 팀의 ID |
| thread_id | string | Yes | 갱신할 스레드의 ID |
| post_id | string | Yes | 읽지 않음으로 표시할, 스레드에 속한 게시글의 ID |

## Response

### 200 - User's thread update successful

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인(user_id)에 대해서만 호출 가능하다 (타 사용자 대상은 `edit_other_users` 권한 필요). 최소 서버 버전 6.7.

---

# 5. Start following a thread

## 기본 정보
- **기능**: 특정 스레드의 팔로우를 시작한다.
- **Endpoint**: `PUT /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/following`
- **인증**: 로그인 필요
- **권한**: 본인(user_id) 계정에 대해서만 가능 (타 사용자는 `edit_other_users` 필요)

## 설명
사용자가 특정 스레드를 팔로우하도록 설정하는 API이다. `user_id`에 "me"를 사용하면 현재 사용자를 가리킨다. 최소 서버 버전은 5.29이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID. "me"를 사용하면 현재 사용자를 가리킴 |
| team_id | string | Yes | 스레드가 속한 팀의 ID |
| thread_id | string | Yes | 팔로우할 스레드의 ID |

## Response

### 200 - User's thread update successful

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인(user_id)에 대해서만 호출 가능하다 (타 사용자 대상은 `edit_other_users` 권한 필요). 최소 서버 버전 5.29.

---

# 6. Stop following a thread

## 기본 정보
- **기능**: 특정 스레드의 팔로우를 중단한다.
- **Endpoint**: `DELETE /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/following`
- **인증**: 로그인 필요
- **권한**: 본인(user_id) 계정에 대해서만 가능 (타 사용자는 `edit_other_users` 필요)

## 설명
사용자가 팔로우하고 있는 특정 스레드의 팔로우를 해제하는 API이다. `user_id`에 "me"를 사용하면 현재 사용자를 가리킨다. 최소 서버 버전은 5.29이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID. "me"를 사용하면 현재 사용자를 가리킴 |
| team_id | string | Yes | 스레드가 속한 팀의 ID |
| thread_id | string | Yes | 갱신할(팔로우 해제할) 스레드의 ID |

## Response

### 200 - User's thread update successful

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인(user_id)에 대해서만 호출 가능하다 (타 사용자 대상은 `edit_other_users` 권한 필요). 최소 서버 버전 5.29.

---

# 7. Get a thread followed by the user

## 기본 정보
- **기능**: 사용자가 팔로우 중인 특정 스레드 하나를 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}`
- **인증**: 로그인 필요
- **권한**: 본인(user_id) 계정에 대해서만 가능 (타 사용자는 `edit_other_users` 필요)

## 설명
사용자가 팔로우하고 있는 특정 스레드의 정보를 조회하는 API이다. `user_id`에 "me"를 사용하면 현재 사용자를 가리킨다. 최소 서버 버전은 5.29이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID. "me"를 사용하면 현재 사용자를 가리킴 |
| team_id | string | Yes | 스레드가 속한 팀의 ID |
| thread_id | string | Yes | 조회할 스레드의 ID |

## Response

### 200 - Get was successful

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 리소스를 찾을 수 없음 |

## 주의 사항
본인(user_id)에 대해서만 조회 가능하다 (타 사용자 대상은 `edit_other_users` 권한 필요). 최소 서버 버전 5.29.

---
