# 1. Create a command

## 기본 정보
- **기능**: 팀에 슬래시 명령어(slash command)를 생성한다.
- **Endpoint**: `POST /api/v4/commands`
- **인증**: Bearer Token 필요
- **권한**: 문서상 `manage_slash_commands` (해당 팀). 일반 멤버 계정은 실측 권한 `manage_own_slash_commands`로 본인 명령어 생성 가능

## 설명
팀에 슬래시 명령어를 생성하는 API이다. 문서에는 팀의 `manage_slash_commands` 권한이 명시되어 있으나, 현재 계정이 보유한 `manage_own_slash_commands` 권한으로 본인 소유 명령어의 생성·관리가 가능하다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| team_id | string | Yes | 명령어를 생성할 팀 ID |
| method | string | Yes | `'P'`: POST 요청, `'G'`: GET 요청 |
| trigger | string | Yes | 명령어를 발동시키는 활성화 단어 |
| url | string | Yes | 명령어가 요청을 보낼 URL |

```json
{
  "team_id": "string",
  "method": "P",
  "trigger": "string",
  "url": "string"
}
```

## Response

### 201 - Command creation successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 슬래시 명령어 ID |
| token | string | payload 출처 검증에 사용하는 토큰 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초, 미삭제 시 0) |
| creator_id | string | 명령어 생성자의 사용자 ID |
| team_id | string | 명령어가 설정된 팀 ID |
| trigger | string | 명령어를 발동시키는 문자열 |
| method | string | HTTP Get('G') 또는 HTTP Post('P') |
| username | string | 응답 게시물에 사용할 사용자 이름 |
| icon_url | string | 아바타 아이콘 URL |
| auto_complete | boolean | 자동완성 사용 여부 |
| auto_complete_desc | string | 명령어 선택 시 표시되는 설명 |
| auto_complete_hint | string | 명령어 힌트 |
| display_name | string | 명령어 표시 이름 |
| description | string | 명령어 설명 |
| url | string | 트리거되는 URL |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 501 | 기능 미구현/비활성화 |

## 주의 사항
일반 멤버 계정은 본인 소유 명령어에 한해 관리 가능하다 (`manage_own_slash_commands`).

---

# 2. List commands for a team

## 기본 정보
- **기능**: 팀의 명령어 목록을 조회한다.
- **Endpoint**: `GET /api/v4/commands`
- **인증**: Bearer Token 필요
- **권한**: 커스텀 명령어만 조회할 때(`custom_only=true`) `manage_slash_commands` 필요. 그 외에는 접근 가능한 커스텀 명령어 + 시스템 명령어 조회 가능

## 설명
팀의 명령어 목록을 조회하는 API이다. `custom_only=false`이면 사용자가 접근 가능한 커스텀 명령어와 시스템 명령어를 함께 조회하며, `custom_only=true`로 커스텀 명령어만 조회하려면 `manage_slash_commands` 권한이 필요하다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| team_id | string | No | - | 팀 ID |
| custom_only | boolean | No | false | true면 커스텀 명령어만 조회. false면 접근 가능한 커스텀 명령어 + 시스템 명령어 조회 |

## Response

### 200 - List Commands retrieve successful
Command 객체 배열이 반환된다.

| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 슬래시 명령어 ID |
| token | string | payload 출처 검증에 사용하는 토큰 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초, 미삭제 시 0) |
| creator_id | string | 명령어 생성자의 사용자 ID |
| team_id | string | 명령어가 설정된 팀 ID |
| trigger | string | 명령어를 발동시키는 문자열 |
| method | string | HTTP Get('G') 또는 HTTP Post('P') |
| username | string | 응답 게시물에 사용할 사용자 이름 |
| icon_url | string | 아바타 아이콘 URL |
| auto_complete | boolean | 자동완성 사용 여부 |
| auto_complete_desc | string | 명령어 선택 시 표시되는 설명 |
| auto_complete_hint | string | 명령어 힌트 |
| display_name | string | 명령어 표시 이름 |
| description | string | 명령어 설명 |
| url | string | 트리거되는 URL |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 501 | 기능 미구현/비활성화 |

## 주의 사항
`custom_only=true`로 팀 전체 커스텀 명령어를 조회하는 것은 `manage_slash_commands` 권한이 필요해 일반 멤버 계정으로는 불가하다.

---

# 3. List autocomplete commands

## 기본 정보
- **기능**: 팀의 자동완성(autocomplete) 명령어 목록을 조회한다.
- **Endpoint**: `GET /api/v4/teams/{team_id}/commands/autocomplete`
- **인증**: Bearer Token 필요
- **권한**: `view_team` (해당 팀)

## 설명
팀 내 자동완성 명령어 목록을 조회하는 API이다. 해당 팀에 대한 `view_team` 권한만 있으면 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| team_id | string | Yes | 팀 GUID |

## Response

### 200 - Autocomplete commands retrieval successful
Command 객체 배열이 반환된다. (필드 구성은 2번 응답과 동일)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

---

# 4. List commands' autocomplete data

## 기본 정보
- **기능**: 팀 명령어들의 자동완성 데이터(제안 목록)를 조회한다.
- **Endpoint**: `GET /api/v4/teams/{team_id}/commands/autocomplete_suggestions`
- **인증**: Bearer Token 필요
- **권한**: `view_team` (해당 팀)

## 설명
사용자가 입력 중인 문자열을 기반으로 팀 명령어들의 자동완성 데이터를 조회하는 API이다. 최소 서버 버전은 5.24이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| team_id | string | Yes | 팀 GUID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| user_input | string | Yes | - | 사용자가 입력한 문자열 |

## Response

### 200 - Commands' autocomplete data retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| Complete | string | 완성된 제안 |
| Suggestion | string | 사용자가 입력하려는 것으로 예측되는 텍스트 |
| Hint | string | 제안 입력에 대한 힌트 |
| Description | string | 제안된 명령어 설명 |
| IconData | string | Base64로 인코딩된 svg 이미지 |

```json
[
  {
    "Complete": "string",
    "Suggestion": "string",
    "Hint": "string",
    "Description": "string",
    "IconData": "string"
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

# 5. Get a command

## 기본 정보
- **기능**: 명령어 ID로 명령어 정의를 조회한다.
- **Endpoint**: `GET /api/v4/commands/{command_id}`
- **인증**: Bearer Token 필요
- **권한**: 문서상 `manage_slash_commands` (해당 팀). 일반 멤버 계정은 `manage_own_slash_commands`로 본인 명령어에 한해 가능

## 설명
명령어 ID 문자열로 명령어 정의를 조회하는 API이다. 최소 서버 버전은 5.22이다. 문서에는 `manage_slash_commands`가 명시되어 있으나, 현재 계정이 보유한 `manage_own_slash_commands`로 본인이 생성한 명령어에 대해 사용 가능하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| command_id | string | Yes | 조회할 명령어 ID |

## Response

### 200 - Command get successful
Command 객체가 반환된다. (필드 구성은 1번 응답과 동일)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 명령어 없음 |

## 주의 사항
일반 멤버 계정은 본인이 생성한 명령어에 한해 조회 가능하다.

---

# 6. Update a command

## 기본 정보
- **기능**: 명령어를 수정한다.
- **Endpoint**: `PUT /api/v4/commands/{command_id}`
- **인증**: Bearer Token 필요
- **권한**: 문서상 `manage_slash_commands` (해당 팀). 일반 멤버 계정은 `manage_own_slash_commands`로 본인 명령어에 한해 가능

## 설명
명령어 ID와 Command 구조체를 기반으로 단일 명령어를 수정하는 API이다. 문서에는 `manage_slash_commands`가 명시되어 있으나, 현재 계정이 보유한 `manage_own_slash_commands`로 본인이 생성한 명령어에 대해 사용 가능하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| command_id | string | Yes | 수정할 명령어 ID |

### Body
Command 객체를 전송한다.

| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | No | 슬래시 명령어 ID |
| token | string | No | payload 출처 검증에 사용하는 토큰 |
| create_at | integer | No | 생성 시각 (밀리초) |
| update_at | integer | No | 마지막 수정 시각 (밀리초) |
| delete_at | integer | No | 삭제 시각 (밀리초, 미삭제 시 0) |
| creator_id | string | No | 명령어 생성자의 사용자 ID |
| team_id | string | No | 명령어가 설정된 팀 ID |
| trigger | string | No | 명령어를 발동시키는 문자열 |
| method | string | No | HTTP Get('G') 또는 HTTP Post('P') |
| username | string | No | 응답 게시물에 사용할 사용자 이름 |
| icon_url | string | No | 아바타 아이콘 URL |
| auto_complete | boolean | No | 자동완성 사용 여부 |
| auto_complete_desc | string | No | 명령어 선택 시 표시되는 설명 |
| auto_complete_hint | string | No | 명령어 힌트 |
| display_name | string | No | 명령어 표시 이름 |
| description | string | No | 명령어 설명 |
| url | string | No | 트리거되는 URL |

## Response

### 200 - Command updated successful
수정된 Command 객체가 반환된다. (필드 구성은 위 Body와 동일)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

## 주의 사항
일반 멤버 계정은 본인이 생성한 명령어에 한해 수정 가능하다.

---

# 7. Delete a command

## 기본 정보
- **기능**: 명령어를 삭제한다.
- **Endpoint**: `DELETE /api/v4/commands/{command_id}`
- **인증**: Bearer Token 필요
- **권한**: 문서상 `manage_slash_commands` (해당 팀). 일반 멤버 계정은 `manage_own_slash_commands`로 본인 명령어에 한해 가능

## 설명
명령어 ID 문자열을 기반으로 명령어를 삭제하는 API이다. 문서에는 `manage_slash_commands`가 명시되어 있으나, 현재 계정이 보유한 `manage_own_slash_commands`로 본인이 생성한 명령어에 대해 사용 가능하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| command_id | string | Yes | 삭제할 명령어 ID |

## Response

### 200 - Command deletion successful
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
| 404 | 명령어 없음 |

## 주의 사항
일반 멤버 계정은 본인이 생성한 명령어에 한해 삭제 가능하다.

---

# 9. Generate a new token

## 기본 정보
- **기능**: 명령어의 토큰을 재발급한다.
- **Endpoint**: `PUT /api/v4/commands/{command_id}/regen_token`
- **인증**: Bearer Token 필요
- **권한**: 문서상 `manage_slash_commands` (해당 팀). 일반 멤버 계정은 `manage_own_slash_commands`로 본인 명령어에 한해 가능

## 설명
명령어 ID 문자열을 기반으로 해당 명령어의 새 토큰을 생성하는 API이다. 문서에는 `manage_slash_commands`가 명시되어 있으나, 현재 계정이 보유한 `manage_own_slash_commands`로 본인이 생성한 명령어에 대해 사용 가능하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| command_id | string | Yes | 새 토큰을 발급할 명령어 ID |

## Response

### 200 - Token generation successful
| 필드 | 타입 | 설명 |
|---|---|---|
| token | string | 새 토큰 |

```json
{ "token": "string" }
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

## 주의 사항
일반 멤버 계정은 본인이 생성한 명령어에 한해 토큰 재발급 가능하다.

---

# 10. Execute a command

## 기본 정보
- **기능**: 팀에서 슬래시 명령어를 실행한다.
- **Endpoint**: `POST /api/v4/commands/execute`
- **인증**: Bearer Token 필요
- **권한**: `use_slash_commands` (명령어가 있는 팀)

## 설명
팀에서 슬래시 명령어를 실행하는 API이다. 명령어가 속한 팀에 대한 `use_slash_commands` 권한이 있어야 한다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 명령어가 실행될 채널 ID |
| command | string | Yes | 파라미터를 포함한 실행할 슬래시 명령어. 예: `'/echo bounces around the room'` |

```json
{
  "channel_id": "string",
  "command": "/echo bounces around the room"
}
```

## Response

### 200 - Command execution successful
| 필드 | 타입 | 설명 |
|---|---|---|
| ResponseType | string | 응답 타입 (in_channel 또는 ephemeral) |
| Text | string | 응답 텍스트 |
| Username | string | 사용자 이름 |
| IconURL | string | 아이콘 URL |
| GotoLocation | string | 이동 위치 |
| Attachments | array | 메시지 첨부 배열 (Id, Fallback, Color, Pretext, AuthorName, AuthorLink, AuthorIcon, Title, TitleLink, Text, Fields, ImageURL, ThumbURL, Footer, FooterIcon, Timestamp) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 501 | 기능 미구현/비활성화 |

---

## 제외된 API
- **08-Move a command**: 명령어를 다른 팀으로 이동하는 팀 단위 관리 기능으로, 현재 팀과 대상 팀 모두에 `manage_slash_commands` 권한이 필요하나 보유 권한 목록에 없어 제외됨.
