# 1. Creates a scheduled post

## 기본 정보
- **기능**: 지정한 시각에 전송될 예약 게시물(scheduled post)을 생성한다.
- **Endpoint**: `POST /api/v4/posts/schedule`
- **인증**: Bearer Token 필요
- **권한**: `create_post` (게시물을 작성할 채널에 대해 필요, 채널 레벨 보유 권한)

## 설명
지정한 채널에 특정 시각(UNIX timestamp, 밀리초)에 전송될 예약 게시물을 생성하는 API이다. 게시물을 작성할 채널에 대한 `create_post` 권한이 필요하다. 최소 서버 버전은 10.3이다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| scheduled_at | integer | Yes | 예약 게시물이 전송될 시각의 UNIX timestamp (밀리초) |
| channel_id | string | Yes | 게시할 채널의 ID |
| message | string | Yes | 메시지 내용 (Markdown 형식 지원) |
| root_id | string | No | 댓글을 달 게시물의 ID |
| file_ids | array | No | 게시물에 첨부할 파일 ID 목록. 게시물당 최대 5개 파일로 제한되며, 더 많은 파일은 추가 게시물을 사용해야 함 |
| props | object | No | 게시물에 첨부할 범용 JSON 속성 객체 |

```json
{
  "scheduled_at": 0,
  "channel_id": "string",
  "message": "string",
  "root_id": "string",
  "file_ids": [],
  "props": {}
}
```

## Response

### 200 - Created scheduled post

```json
{}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

## 주의 사항
파일 첨부는 게시물당 최대 5개로 제한된다. 최소 서버 버전 10.3 이상에서만 사용 가능하다.

---

# 2. Gets all scheduled posts for a user for the specified team

## 기본 정보
- **기능**: 지정한 팀에 대한 본인(사용자)의 예약 게시물 전체를 조회한다.
- **Endpoint**: `GET /api/v4/posts/scheduled/team/{team_id}`
- **인증**: Bearer Token 필요
- **권한**: `view_team` (예약 게시물을 조회할 팀에 대해 필요, 팀 레벨 보유 권한)

## 설명
지정한 팀에서 사용자의 예약 게시물 목록을 조회하는 API이다. 쿼리 파라미터로 DM/GM 채널의 예약 게시물 포함 여부를 지정할 수 있다. 최소 서버 버전은 10.3이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| team_id | string | Yes | 예약 게시물을 조회할 팀의 ID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| includeDirectChannels | boolean | No | false | DM/GM의 예약 게시물 포함 여부 |

## Response

### 200 - Created scheduled post

```json
{}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

## 주의 사항
본인의 예약 게시물이 조회 대상이며, 해당 팀에 대한 `view_team` 권한이 필요하다.

---

# 3. Update a scheduled post

## 기본 정보
- **기능**: 기존 예약 게시물의 내용과 예약 시각을 수정한다.
- **Endpoint**: `PUT /api/v4/posts/schedule/{scheduled_post_id}`
- **인증**: Bearer Token 필요
- **권한**: `create_post` (예약 게시물이 속한 채널에 대해 필요, 채널 레벨 보유 권한)

## 설명
예약 게시물 ID를 지정하여 예약 게시물의 메시지, 채널, 예약 시각을 수정하는 API이다. 예약 게시물이 속한 채널에 대한 `create_post` 권한이 필요하다. 최소 서버 버전은 10.3이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| scheduled_post_id | string | Yes | 수정할 예약 게시물의 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 수정할 예약 게시물의 ID |
| channel_id | string | Yes | 게시할 채널의 ID |
| user_id | string | Yes | 현재 사용자의 ID |
| scheduled_at | integer | Yes | 예약 게시물이 전송될 시각의 UNIX timestamp (밀리초) |
| message | string | Yes | 메시지 내용 (Markdown 형식 지원) |

```json
{
  "id": "string",
  "channel_id": "string",
  "user_id": "string",
  "scheduled_at": 0,
  "message": "string"
}
```

## Response

### 200 - Updated scheduled post

```json
{}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

## 주의 사항
`user_id`에는 현재 사용자의 ID를 지정한다 (본인 리소스 대상). 최소 서버 버전 10.3 이상에서만 사용 가능하다.

---

# 4. Delete a scheduled post

## 기본 정보
- **기능**: 예약 게시물을 삭제한다.
- **Endpoint**: `DELETE /api/v4/posts/schedule/{scheduled_post_id}`
- **인증**: Bearer Token 필요
- **권한**: 문서에 별도의 이름있는 권한 서술 없음 (본인 예약 게시물 대상)

## 설명
예약 게시물 ID를 지정하여 예약 게시물을 삭제하는 API이다. 최소 서버 버전은 10.3이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| scheduled_post_id | string | Yes | 삭제할 예약 게시물의 ID |

## Response

### 200 - Deleted scheduled post

```json
{}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

## 주의 사항
최소 서버 버전 10.3 이상에서만 사용 가능하다.

---
