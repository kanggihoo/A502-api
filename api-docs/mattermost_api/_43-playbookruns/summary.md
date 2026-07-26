# 1. List all playbook runs

## 기본 정보
- **기능**: 팀, 상태, 오너, 이름, 참여자 등으로 필터링된 플레이북 런 목록을 페이지 단위로 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/runs`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
플레이북 런의 페이지 단위 목록을 조회하는 API이다. 팀, 상태, 오너, 이름, 참여자, 채널로 필터링할 수 있고, ID·이름·상태·생성일·종료일·팀·오너 ID로 정렬할 수 있다. `owner_user_id`와 `participant_id`에는 현재 사용자를 뜻하는 "me"를 지정할 수 있다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| team_id | string | Yes | - | 필터링할 팀의 ID |
| page | integer | No | - | 요청할 페이지의 0 기반 인덱스 |
| per_page | integer | No | - | 페이지당 반환할 플레이북 런 수 |
| sort | string | No | - | 정렬 기준 필드 |
| direction | string | No | - | 정렬 방향 (오름차순/내림차순) |
| statuses | array | No | - | 지정한 상태의 플레이북 런만 반환 |
| owner_user_id | string | No | - | 이 사용자가 지휘하는 런만 반환. 현재 사용자는 "me" |
| participant_id | string | No | - | 이 사용자가 참여자인 런만 반환. 현재 사용자는 "me" |
| search_term | string | No | - | 이름에 검색어가 포함된 런만 반환 |
| channel_id | string | No | - | 이 채널 ID에 연결된 런만 반환 |
| omit_ended | boolean | No | - | true면 진행 중인 런(EndAt = 0)만 반환. false 또는 생략 시 종료된 런도 포함 |
| since | integer | No | - | 지정한 타임스탬프(밀리초) 이후 생성/수정된 런만 반환 |

## Response

### 200 - 플레이북 런의 페이지 목록
| 필드 | 타입 | 설명 |
|---|---|---|
| total_count | integer | 페이징과 무관한 전체 플레이북 런 수 |
| page_count | integer | 전체 페이지 수 |
| has_more | boolean | 현재 페이지 뒤에 더 많은 페이지가 있는지 여부 |
| items | array | 이 페이지의 플레이북 런 목록 (플레이북 런 객체 배열) |

각 플레이북 런 객체의 최상위 필드: `id`, `name`, `summary`, `is_active`, `owner_user_id`, `team_id`, `channel_id`, `create_at`, `end_at`, `delete_at`, `active_stage`, `active_stage_title`, `post_id`, `playbook_id`, `checklists`(체크리스트 배열: 각 체크리스트는 `id`, `title`, `items`를 갖고, 아이템은 `id`, `title`, `state`, `state_modified`, `assignee_id`, `assignee_modified`, `command`, `command_last_run`, `description`, `delete_at`, `due_date`, `task_actions`, `update_at`, `condition_id`, `condition_action`, `condition_reason` 필드를 가짐)

```json
{
  "total_count": 0,
  "page_count": 0,
  "has_more": false,
  "items": [
    {
      "id": "string",
      "name": "string",
      "summary": "string",
      "is_active": true,
      "owner_user_id": "string",
      "team_id": "string",
      "channel_id": "string",
      "create_at": 0,
      "end_at": 0,
      "delete_at": 0,
      "active_stage": 0,
      "active_stage_title": "string",
      "post_id": "string",
      "playbook_id": "string",
      "checklists": [
        {
          "id": "string",
          "title": "string",
          "items": [
            { "id": "string", "title": "string", "state": "in_progress", "...": "..." }
          ]
        }
      ]
    }
  ]
}
```
(체크리스트 아이템 상세 필드는 원본 문서 참고, 예시는 축약됨)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---

# 2. Create a new playbook run

## 기본 정보
- **기능**: 플레이북을 템플릿으로 사용하여 특정 팀에 새 플레이북 런을 생성한다.
- **Endpoint**: `POST /plugins/playbooks/api/v0/runs`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
플레이북을 템플릿으로 하여, 지정한 이름과 오너로 팀 내에 새 플레이북 런을 생성하는 API이다. 이름, 오너, 팀, 플레이북 ID가 필수이며, 게시글(post)로부터 런을 생성한 경우 `post_id`를 함께 전달할 수 있다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| name | string | Yes | 플레이북 런의 이름 |
| summary | string | No | 플레이북 런의 요약 |
| owner_user_id | string | Yes | 플레이북 런을 지휘할 사용자의 ID |
| team_id | string | Yes | 플레이북 런의 채널이 속할 팀의 ID |
| post_id | string | No | 게시글로부터 생성된 경우 해당 게시글 ID. 아니면 빈 값 |
| playbook_id | string | Yes | 이 런의 템플릿이 되는 플레이북의 ID |

```json
{
  "name": "string",
  "summary": "string",
  "owner_user_id": "string",
  "team_id": "string",
  "post_id": "string",
  "playbook_id": "string"
}
```

## Response

### 201 - 생성된 플레이북 런
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 플레이북 런의 고유 식별자 (26자 영숫자) |
| name | string | 플레이북 런의 이름 |
| summary | string | 플레이북 런의 요약 |
| is_active | boolean | 진행 중이면 true, 종료되었으면 false |
| owner_user_id | string | 런을 지휘하는 사용자의 ID |
| team_id | string | 런의 채널이 속한 팀의 ID |
| channel_id | string | 런의 채널 ID |
| create_at | integer | 생성 시각 (밀리초) |
| end_at | integer | 종료 시각 (밀리초). 미종료 시 0 |
| delete_at | integer | 삭제 시각 (밀리초). 미삭제 시 0 |
| active_stage | integer | 현재 활성 스테이지의 0 기반 인덱스 |
| active_stage_title | string | 현재 활성 스테이지의 제목 |
| post_id | string | 게시글로부터 생성된 경우 해당 게시글 ID |
| playbook_id | string | 템플릿 플레이북의 ID |
| checklists | array | 체크리스트 목록 (각 체크리스트: id, title, items) |

```json
{
  "id": "string",
  "name": "string",
  "summary": "string",
  "is_active": true,
  "owner_user_id": "string",
  "team_id": "string",
  "channel_id": "string",
  "create_at": 0,
  "end_at": 0,
  "delete_at": 0,
  "active_stage": 0,
  "active_stage_title": "string",
  "post_id": "string",
  "playbook_id": "string",
  "checklists": [
    { "id": "string", "title": "string", "items": [] }
  ]
}
```
(체크리스트 아이템 상세 필드는 원본 문서 참고, 예시는 축약됨)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---

# 3. Get all owners

## 기본 정보
- **기능**: 팀 기준으로 필터링된 모든 플레이북 런의 오너 목록을 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/runs/owners`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 팀의 모든 플레이북 런의 오너(지휘자) 목록을 조회하는 API이다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| team_id | string | Yes | - | 필터링할 팀의 ID |

## Response

### 200 - 오너 목록
| 필드 | 타입 | 설명 |
|---|---|---|
| user_id | string | 오너의 고유 식별자 (26자 영숫자) |
| username | string | 오너의 사용자명 |

```json
[
  {
    "user_id": "string",
    "username": "string"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---

# 4. Get playbook run channels

## 기본 정보
- **기능**: 플레이북 런에 연결된 채널들을 팀, 상태, 오너, 이름, 참여자 등으로 필터링하여 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/runs/channels`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
플레이북 런에 연결된 채널 ID 목록을 조회하는 API이다. 팀, 상태, 오너, 이름, 참여자로 필터링할 수 있고, 연결된 플레이북 런 기준으로 ID·이름·상태·생성일·종료일·팀·오너 ID로 정렬할 수 있다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| team_id | string | Yes | - | 필터링할 팀의 ID |
| sort | string | No | - | 연결된 플레이북 런 기준의 정렬 필드 |
| direction | string | No | - | 정렬 방향 (오름차순/내림차순) |
| status | string | No | - | 이 상태의 플레이북 런에 연결된 채널만 반환 |
| owner_user_id | string | No | - | 이 사용자가 지휘하는 런의 채널만 반환 |
| search_term | string | No | - | 런 이름에 검색어가 포함된 채널만 반환 |
| participant_id | string | No | - | 이 사용자가 참여자인 런의 채널만 반환 |

## Response

### 200 - 채널 ID 목록
채널 ID 문자열 배열을 반환한다.

```json
[
  "string"
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---

# 5. Find playbook run by channel ID

## 기본 정보
- **기능**: 채널 ID로 해당 채널에 연결된 플레이북 런을 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/runs/channel/{channel_id}`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 채널에 연결된 플레이북 런을 조회하는 API이다. 채널에 연결된 런이 없으면 404를 반환한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 조회할 플레이북 런에 연결된 채널의 ID |

## Response

### 200 - 채널에 연결된 플레이북 런
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 플레이북 런의 고유 식별자 (26자 영숫자) |
| name | string | 플레이북 런의 이름 |
| summary | string | 플레이북 런의 요약 |
| is_active | boolean | 진행 중이면 true, 종료되었으면 false |
| owner_user_id | string | 런을 지휘하는 사용자의 ID |
| team_id | string | 런의 채널이 속한 팀의 ID |
| channel_id | string | 런의 채널 ID |
| create_at | integer | 생성 시각 (밀리초) |
| end_at | integer | 종료 시각 (밀리초). 미종료 시 0 |
| delete_at | integer | 삭제 시각 (밀리초). 미삭제 시 0 |
| active_stage | integer | 현재 활성 스테이지의 0 기반 인덱스 |
| active_stage_title | string | 현재 활성 스테이지의 제목 |
| post_id | string | 게시글로부터 생성된 경우 해당 게시글 ID |
| playbook_id | string | 템플릿 플레이북의 ID |
| checklists | array | 체크리스트 목록 (각 체크리스트: id, title, items) |

```json
{
  "id": "string",
  "name": "string",
  "is_active": true,
  "owner_user_id": "string",
  "team_id": "string",
  "channel_id": "string",
  "create_at": 0,
  "end_at": 0,
  "playbook_id": "string",
  "checklists": []
}
```
(체크리스트 아이템 상세 필드는 원본 문서 참고, 예시는 축약됨)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 404 | 채널에 연결된 플레이북 런이 없음 |
| 500 | 서버 오류 |

---

# 6. Get a playbook run

## 기본 정보
- **기능**: 플레이북 런 하나를 ID로 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/runs/{id}`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 ID의 플레이북 런 상세 정보(체크리스트 포함)를 조회하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 조회할 플레이북 런의 ID |

## Response

### 200 - 플레이북 런
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 플레이북 런의 고유 식별자 (26자 영숫자) |
| name | string | 플레이북 런의 이름 |
| summary | string | 플레이북 런의 요약 |
| is_active | boolean | 진행 중이면 true, 종료되었으면 false |
| owner_user_id | string | 런을 지휘하는 사용자의 ID |
| team_id | string | 런의 채널이 속한 팀의 ID |
| channel_id | string | 런의 채널 ID |
| create_at | integer | 생성 시각 (밀리초) |
| end_at | integer | 종료 시각 (밀리초). 미종료 시 0 |
| delete_at | integer | 삭제 시각 (밀리초). 미삭제 시 0 |
| active_stage | integer | 현재 활성 스테이지의 0 기반 인덱스 |
| active_stage_title | string | 현재 활성 스테이지의 제목 |
| post_id | string | 게시글로부터 생성된 경우 해당 게시글 ID |
| playbook_id | string | 템플릿 플레이북의 ID |
| checklists | array | 체크리스트 목록 (각 체크리스트: id, title, items) |

```json
{
  "id": "string",
  "name": "string",
  "is_active": true,
  "owner_user_id": "string",
  "team_id": "string",
  "channel_id": "string",
  "create_at": 0,
  "end_at": 0,
  "playbook_id": "string",
  "checklists": []
}
```
(체크리스트 아이템 상세 필드는 원본 문서 참고, 예시는 축약됨)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---

# 7. Update a playbook run

## 기본 정보
- **기능**: 플레이북 런의 이름과 요약을 수정한다.
- **Endpoint**: `PATCH /plugins/playbooks/api/v0/runs/{id}`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
플레이북 런의 이름(`name`)과 요약(`summary`)을 수정하는 API이다. 이름은 비워둘 수 없고, 요약은 빈 값으로 보내 초기화할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 수정할 플레이북 런의 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| name | string | No | 플레이북 런의 새 이름. 비워둘 수 없음 |
| summary | string | No | 플레이북 런의 새 요약. 빈 값으로 요약을 지울 수 있음 |

```json
{
  "name": "string",
  "summary": "string"
}
```

## Response

### 200 - Playbook run successfully updated
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 500 | 서버 오류 |

---

# 8. Get playbook run metadata

## 기본 정보
- **기능**: 플레이북 런의 메타데이터(채널명, 팀명, 멤버 수, 게시글 수)를 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/runs/{id}/metadata`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 플레이북 런의 연결 채널 이름, 팀 이름, 멤버 수, 채널 게시글 수 등의 메타데이터를 조회하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 메타데이터를 조회할 플레이북 런의 ID |

## Response

### 200 - 플레이북 런 메타데이터
| 필드 | 타입 | 설명 |
|---|---|---|
| channel_name | string | 런에 연결된 채널의 이름 |
| channel_display_name | string | 런에 연결된 채널의 표시 이름 |
| team_name | string | 런이 속한 팀의 이름 |
| num_members | integer | 어느 시점에든 런의 멤버였던 사용자 수 |
| total_posts | integer | 런에 연결된 채널의 게시글 수 |

```json
{
  "channel_name": "string",
  "channel_display_name": "string",
  "team_name": "string",
  "num_members": 0,
  "total_posts": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---

# 9. End a playbook run

## 기본 정보
- **기능**: 플레이북 런을 종료한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/runs/{id}/end`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 플레이북 런을 종료 상태로 전환하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 종료할 플레이북 런의 ID |

## Response

### 200 - Playbook run ended
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 500 | 서버 오류 |

---

# 10. Restart a playbook run

## 기본 정보
- **기능**: 종료된 플레이북 런을 재시작한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/runs/{id}/restart`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 플레이북 런을 다시 시작(재개)하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 재시작할 플레이북 런의 ID |

## Response

### 200 - Playbook run restarted
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 500 | 서버 오류 |

---

# 11. Update a playbook run's status

## 기본 정보
- **기능**: 플레이북 런의 상태 업데이트(status update) 메시지를 게시한다.
- **Endpoint**: `POST /plugins/playbooks/api/v0/runs/{id}/status`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
플레이북 런의 상태 업데이트 메시지를 등록하는 API이다. `reminder`로 오너에게 다음 상태 업데이트 리마인더를 보낼 시간을 초 단위로 지정할 수 있으며, 0이거나 생략하면 리마인더가 예약되지 않는다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 상태를 업데이트할 플레이북 런의 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| message | string | Yes | 상태 업데이트 메시지 |
| reminder | number | No | 오너에게 상태 업데이트 리마인더를 보내기까지의 초 수. 0 또는 생략 시 리마인더 없음 |

```json
{
  "message": "string",
  "reminder": 0
}
```

## Response

### 200 - Playbook run updated
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---

# 12. Finish a playbook

## 기본 정보
- **기능**: 플레이북 런을 완료(finish) 처리한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/runs/{id}/finish`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 플레이북 런을 완료 상태로 전환하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 완료 처리할 플레이북 런의 ID |

## Response

### 200 - Playbook run finished
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 500 | 서버 오류 |

---

# 13. Update playbook run owner

## 기본 정보
- **기능**: 플레이북 런의 오너(지휘자)를 변경한다.
- **Endpoint**: `POST /plugins/playbooks/api/v0/runs/{id}/owner`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 플레이북 런의 오너를 새 사용자로 변경하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 오너를 변경할 플레이북 런의 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| owner_id | string | Yes | 새 오너의 사용자 ID |

```json
{
  "owner_id": "string"
}
```

## Response

### 200 - Owner successfully changed
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---

# 14. Add an item to a playbook run's checklist

## 기본 정보
- **기능**: 플레이북 런의 체크리스트에 새 아이템을 추가한다.
- **Endpoint**: `POST /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/add`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
플레이북 런의 특정 체크리스트에 아이템을 추가하는 API이다. 가장 일반적인 사용 방식은 제목(`title`)만 보내는 것이며, 이 경우 기본적으로 담당자와 슬래시 커맨드가 없는 미완료(open) 아이템이 생성된다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 체크리스트를 수정할 플레이북 런의 ID |
| checklist | integer | Yes | 수정할 체크리스트의 0 기반 인덱스 |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| title | string | Yes | 체크리스트 아이템의 제목 |
| state | string | No | 아이템의 상태 (`""` \| `in_progress` \| `closed`). 빈 문자열은 미완료 |
| state_modified | integer | No | 상태의 최종 수정 시각 (밀리초). 수정된 적 없으면 0 |
| assignee_id | string | No | 아이템 담당자의 사용자 ID. 담당자가 없으면 빈 문자열 |
| assignee_modified | integer | No | 담당자의 최종 수정 시각 (밀리초). 담당자가 지정된 적 없으면 0 |
| command | string | No | 아이템에 연결된 슬래시 커맨드. 없으면 빈 문자열 |
| command_last_run | integer | No | 커맨드의 최종 실행 시각 (밀리초). 실행된 적 없으면 0 |
| description | string | No | 아이템의 상세 설명 (Markdown 지원) |

```json
{
  "title": "string",
  "state": "",
  "assignee_id": "string",
  "command": "string",
  "description": "string"
}
```

## Response

### 200 - Item successfully added
응답 본문 없음.

### default - 에러 응답
| 필드 | 타입 | 설명 |
|---|---|---|
| error | string | 에러 설명 메시지 |
| details | string | 에러 발생 위치와 원인에 대한 상세 정보 |

```json
{
  "error": "string",
  "details": "string"
}
```

---

# 15. Reorder an item in a playbook run's checklist

## 기본 정보
- **기능**: 플레이북 런 체크리스트 내 아이템의 순서를 변경한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/reorder`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
체크리스트 내에서 지정한 아이템을 새 위치로 이동하는 API이다. 아이템 인덱스와 이동할 위치 모두 0 기반 인덱스이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 체크리스트를 수정할 플레이북 런의 ID |
| checklist | integer | Yes | 수정할 체크리스트의 0 기반 인덱스 |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| item_num | integer | Yes | 이동할 아이템의 0 기반 인덱스 |
| new_location | integer | Yes | 아이템을 이동시킬 새 위치의 0 기반 인덱스 |

```json
{
  "item_num": 0,
  "new_location": 1
}
```

## Response

### 200 - Item successfully reordered
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 500 | 서버 오류 |

---

# 16. Update an item of a playbook run's checklist

## 기본 정보
- **기능**: 플레이북 런 체크리스트 아이템의 제목, 슬래시 커맨드, 설명을 수정한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
플레이북 런의 특정 체크리스트 아이템의 제목, 슬래시 커맨드, 설명을 수정하는 API이다. 제목과 커맨드는 필수 필드이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 체크리스트를 수정할 플레이북 런의 ID |
| checklist | integer | Yes | 수정할 체크리스트의 0 기반 인덱스 |
| item | integer | Yes | 수정할 아이템의 0 기반 인덱스 |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| title | string | Yes | 아이템의 새 제목 |
| command | string | Yes | 아이템의 새 슬래시 커맨드 |
| description | string | No | 아이템의 새 설명 (Markdown 지원) |

```json
{
  "title": "string",
  "command": "string",
  "description": "string"
}
```

## Response

### 200 - Item updated
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 500 | 서버 오류 |

---

# 17. Delete an item of a playbook run's checklist

## 기본 정보
- **기능**: 플레이북 런 체크리스트의 아이템을 삭제한다.
- **Endpoint**: `DELETE /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
플레이북 런의 특정 체크리스트에서 지정한 아이템을 삭제하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 체크리스트를 수정할 플레이북 런의 ID |
| checklist | integer | Yes | 수정할 체크리스트의 0 기반 인덱스 |
| item | integer | Yes | 삭제할 아이템의 0 기반 인덱스 |

## Response

### 204 - Item successfully deleted
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 500 | 서버 오류 |

---

# 18. Update the state of an item

## 기본 정보
- **기능**: 플레이북 런 체크리스트 아이템의 상태를 변경한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}/state`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
체크리스트 아이템의 상태를 변경하는 API이다. 상태는 빈 문자열(미완료), `in_progress`, `closed` 중 하나이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 체크리스트를 수정할 플레이북 런의 ID |
| checklist | integer | Yes | 수정할 체크리스트의 0 기반 인덱스 |
| item | integer | Yes | 수정할 아이템의 0 기반 인덱스 |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| new_state | string | Yes | 아이템의 새 상태 (`""` \| `in_progress` \| `closed`) |

```json
{
  "new_state": "closed"
}
```

## Response

### 200 - Item's state successfully updated
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 500 | 서버 오류 |

---

# 19. Update the assignee of an item

## 기본 정보
- **기능**: 플레이북 런 체크리스트 아이템의 담당자를 변경한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}/assignee`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
체크리스트 아이템에 새 담당자(assignee)를 지정하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 아이템의 담당자를 변경할 플레이북 런의 ID |
| checklist | integer | Yes | 대상 체크리스트의 0 기반 인덱스 |
| item | integer | Yes | 담당자를 변경할 아이템의 0 기반 인덱스 |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| assignee_id | string | Yes | 아이템의 새 담당자 사용자 ID |

```json
{
  "assignee_id": "string"
}
```

## Response

### 200 - Item's assignee successfully updated
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 500 | 서버 오류 |

---

# 20. Run an item's slash command

## 기본 정보
- **기능**: 플레이북 런 체크리스트 아이템에 연결된 슬래시 커맨드를 실행한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}/run`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
체크리스트 아이템에 연결된 슬래시 커맨드를 실행하는 API이다. 성공 시 슬래시 커맨드가 반환한 `trigger_id`를 응답한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 아이템을 실행할 플레이북 런의 ID |
| checklist | integer | Yes | 대상 체크리스트의 0 기반 인덱스 |
| item | integer | Yes | 슬래시 커맨드를 실행할 아이템의 0 기반 인덱스 |

## Response

### 200 - 슬래시 커맨드 실행 성공
| 필드 | 타입 | 설명 |
|---|---|---|
| trigger_id | string | 슬래시 커맨드가 반환한 trigger_id |

```json
{
  "trigger_id": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 500 | 서버 오류 |

---

# 21. Get property fields for a playbook run

## 기본 정보
- **기능**: 플레이북 런의 속성 필드(property field) 목록을 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/runs/{id}/property_fields`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 플레이북 런의 속성 필드 목록을 조회하는 API이다. `updated_since` 파라미터로 특정 시각 이후에 수정된 필드만 필터링할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 속성 필드를 조회할 플레이북 런의 ID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| updated_since | integer | No | - | 이 타임스탬프(밀리초) 이후에 수정된 속성 필드만 반환 |

## Response

### 200 - 플레이북 런의 속성 필드 목록
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 속성 필드의 고유 식별자 (26자 영숫자) |
| type | string | 속성 필드의 타입 (`text` \| `select` \| `multiselect`) |
| name | string | 속성 필드의 이름 |
| description | string | 속성 필드의 설명 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초). 미삭제 시 0 |
| attrs | object | 속성 필드의 추가 속성 (select 필드의 옵션, 표시 여부 등) |

```json
[
  {
    "id": "string",
    "type": "text",
    "name": "string",
    "description": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0,
    "attrs": {}
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---

# 22. Get property values for a playbook run

## 기본 정보
- **기능**: 플레이북 런의 속성 값(property value) 목록을 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/runs/{id}/property_values`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 플레이북 런의 속성 값 목록을 조회하는 API이다. `updated_since` 파라미터로 특정 시각 이후에 수정된 값만 필터링할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 속성 값을 조회할 플레이북 런의 ID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| updated_since | integer | No | - | 이 타임스탬프(밀리초) 이후에 수정된 속성 값만 반환 |

## Response

### 200 - 플레이북 런의 속성 값 목록
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 속성 값의 고유 식별자 (26자 영숫자) |
| field_id | string | 이 값이 속한 속성 필드의 식별자 |
| value | string | JSON으로 인코딩된 속성 값 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초). 미삭제 시 0 |

```json
[
  {
    "id": "string",
    "field_id": "string",
    "value": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---

# 23. Set a property value for a playbook run

## 기본 정보
- **기능**: 플레이북 런의 특정 속성 필드에 값을 설정한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/runs/{id}/property_fields/{field_id}/value`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 플레이북 런의 특정 속성 필드에 값을 설정하는 API이다. 값은 JSON으로 인코딩된 문자열로 전달한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 속성 값을 설정할 플레이북 런의 ID |
| field_id | string | Yes | 값을 설정할 속성 필드의 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| value | string | Yes | 설정할 JSON 인코딩 값 |

```json
{
  "value": "string"
}
```

## Response

### 200 - 속성 값 설정 성공
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 속성 값의 고유 식별자 (26자 영숫자) |
| field_id | string | 이 값이 속한 속성 필드의 식별자 |
| value | string | JSON으로 인코딩된 속성 값 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초). 미삭제 시 0 |

```json
{
  "id": "string",
  "field_id": "string",
  "value": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---
