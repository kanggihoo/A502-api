# 1. Create a reaction

## 기본 정보
- **기능**: 게시물에 리액션(이모지 반응)을 추가한다.
- **Endpoint**: `POST /api/v4/reactions`
- **인증**: Bearer Token 필요
- **권한**: `read_channel` (게시물이 있는 채널)

## 설명
게시물에 리액션을 생성하는 API이다. 게시물이 속한 채널에 대한 `read_channel` 권한이 있어야 한다. (실측 권한으로 `read_channel`, `add_reaction` 보유)

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | No | 리액션을 남긴 사용자 ID |
| post_id | string | No | 리액션 대상 게시물 ID |
| emoji_name | string | No | 리액션에 사용한 이모지 이름 |
| create_at | integer | No | 리액션 생성 시각 (밀리초) |

```json
{
  "user_id": "string",
  "post_id": "string",
  "emoji_name": "string",
  "create_at": 0
}
```

## Response

### 201 - Reaction creation successful
| 필드 | 타입 | 설명 |
|---|---|---|
| user_id | string | 리액션을 남긴 사용자 ID |
| post_id | string | 리액션 대상 게시물 ID |
| emoji_name | string | 리액션에 사용한 이모지 이름 |
| create_at | integer | 리액션 생성 시각 (밀리초) |

```json
{
  "user_id": "string",
  "post_id": "string",
  "emoji_name": "string",
  "create_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |

---

# 2. Get a list of reactions to a post

## 기본 정보
- **기능**: 게시물에 달린 모든 사용자의 리액션 목록을 조회한다.
- **Endpoint**: `GET /api/v4/posts/{post_id}/reactions`
- **인증**: Bearer Token 필요
- **권한**: `read_channel` (게시물이 있는 채널)

## 설명
특정 게시물에 모든 사용자가 남긴 리액션 목록을 조회하는 API이다. 게시물이 속한 채널에 대한 `read_channel` 권한이 있어야 한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| post_id | string | Yes | 게시물 ID |

## Response

### 200 - List reactions retrieve successful
| 필드 | 타입 | 설명 |
|---|---|---|
| user_id | string | 리액션을 남긴 사용자 ID |
| post_id | string | 리액션 대상 게시물 ID |
| emoji_name | string | 리액션에 사용한 이모지 이름 |
| create_at | integer | 리액션 생성 시각 (밀리초) |

```json
[
  {
    "user_id": "string",
    "post_id": "string",
    "emoji_name": "string",
    "create_at": 0
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

---

# 3. Remove a reaction from a post

## 기본 정보
- **기능**: 사용자가 게시물에 남긴 리액션을 삭제한다.
- **Endpoint**: `DELETE /api/v4/users/{user_id}/posts/{post_id}/reactions/{emoji_name}`
- **인증**: Bearer Token 필요
- **권한**: 본인(user_id)이어야 함 (또는 `manage_system` — 미보유)

## 설명
지정한 사용자가 게시물에 남긴 리액션을 삭제하는 API이다. 해당 사용자 본인이거나 `manage_system` 권한이 있어야 한다. 일반 멤버 계정은 본인 리액션만 삭제할 수 있다 (실측 권한 `remove_reaction` 보유).

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID |
| post_id | string | Yes | 게시물 ID |
| emoji_name | string | Yes | 이모지 이름 |

## Response

### 200 - Reaction deletion successful
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
일반 멤버 계정은 본인이 남긴 리액션만 삭제 가능하다.

---

# 4. Bulk get the reaction for posts

## 기본 정보
- **기능**: 여러 게시물의 리액션을 한 번에 조회한다.
- **Endpoint**: `POST /api/v4/posts/ids/reactions`
- **인증**: Bearer Token 필요
- **권한**: `read_channel` (게시물이 있는 채널)

## 설명
게시물 ID 목록을 전달하여 각 게시물에 모든 사용자가 남긴 리액션을 한 번에 조회하는 API이다. 게시물이 속한 채널에 대한 `read_channel` 권한이 있어야 한다. 최소 서버 버전은 5.8이다.

## Request

### Body
게시물 ID 문자열 배열을 전송한다.

```json
[
  "string"
]
```

## Response

### 200 - Reactions retrieval successful
게시물 ID를 key로 하는 객체가 반환된다.

```json
{}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

---
