# 1. List all playbooks

## 기본 정보
- **기능**: 팀별로 필터링된 플레이북 목록을 페이지 단위로 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/playbooks`
- **인증**: Bearer Token 필요
- **권한**: 플레이북 멤버 기반 접근 (본인이 멤버인 플레이북이 조회됨)

## 설명
지정한 팀의 플레이북 목록을 페이지 단위로 조회하는 API이다. 제목, 스테이지 수, 스텝 수 기준으로 정렬할 수 있으며, 아카이브된 플레이북 포함 여부도 선택할 수 있다. Playbooks 플러그인 API(`/plugins/playbooks/api/v0`)로 제공된다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| team_id | string | Yes | - | 필터링할 팀의 ID |
| page | integer | No | - | 요청할 페이지의 0부터 시작하는 인덱스 |
| per_page | integer | No | - | 페이지당 반환할 플레이북 수 |
| sort | string | No | - | 정렬 기준 필드 (제목, 스테이지 수, 전체 스텝 수) |
| direction | string | No | - | 정렬 방향 (오름차순 또는 내림차순) |
| with_archived | boolean | No | - | 아카이브된 플레이북 포함 여부 |

## Response

### 200 - A paged list of playbooks
| 필드 | 타입 | 설명 |
|---|---|---|
| total_count | integer | 페이징과 무관한 전체 플레이북 수 |
| page_count | integer | 전체 페이지 수 (전체 플레이북 수와 per_page에 따라 결정) |
| has_more | boolean | 현재 반환된 페이지 이후에 더 많은 페이지가 있는지 여부 |
| items | array | 이 페이지의 플레이북 목록 (플레이북 객체 배열) |

items의 각 플레이북 객체 주요 필드: `id`, `title`, `description`, `team_id`, `create_public_playbook_run`, `create_at`, `delete_at`, `num_stages`, `num_steps`, `checklists`(체크리스트/아이템 배열), `member_ids`(멤버 사용자 ID 배열)

```json
{
  "total_count": 0,
  "page_count": 0,
  "has_more": false,
  "items": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "team_id": "string",
      "create_public_playbook_run": true,
      "create_at": 0,
      "delete_at": 0,
      "num_stages": 0,
      "num_steps": 0,
      "checklists": [
        {
          "id": "string",
          "title": "string",
          "items": [
            {
              "id": "string",
              "title": "string",
              "state": "",
              "assignee_id": "string",
              "command": "string",
              "description": "string",
              "due_date": 0
            }
          ]
        }
      ],
      "member_ids": ["string"]
    }
  ]
}
```
(체크리스트 아이템의 `state_modified`, `assignee_modified`, `command_last_run`, `delete_at`, `task_actions`, `update_at`, `condition_id`, `condition_action`, `condition_reason` 필드는 예시에서 생략)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

---

# 2. Create a playbook

## 기본 정보
- **기능**: 새 플레이북을 생성한다.
- **Endpoint**: `POST /plugins/playbooks/api/v0/playbooks`
- **인증**: Bearer Token 필요
- **권한**: `playbook_public_create` / `playbook_private_create` (팀 레벨 권한, 현재 계정 보유)

## 설명
지정한 팀에 새 플레이북을 생성하는 API이다. 제목, 팀 ID, 체크리스트, 멤버 목록 등이 필수이며, 자동 초대·기본 오너·브로드캐스트 채널·웹훅 등 다양한 자동화 옵션을 함께 설정할 수 있다. 무료 티어에서는 `public`을 `true`로 설정해야 한다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| title | string | Yes | 플레이북 제목 |
| description | string | No | 플레이북 설명 |
| team_id | string | Yes | 플레이북이 속한 팀의 식별자 |
| create_public_playbook_run | boolean | Yes | 이 플레이북으로 생성되는 플레이북 런을 공개로 할지 비공개로 할지 여부 |
| public | boolean | No | 플레이북의 공개/비공개 라이선스 여부. 무료 티어에서는 `true` 필수 |
| checklists | array | Yes | 플레이북에 정의된 스테이지 목록. 각 항목: `title`(필수), `items`(필수: `title` 필수, `command`, `description`) |
| member_ids | array of string | Yes | 이 플레이북의 멤버인 모든 사용자의 식별자 |
| broadcast_channel_ids | array of string | No | 모든 상태 업데이트가 브로드캐스트될 채널 ID 목록 (플레이북과 같은 팀이어야 함) |
| invited_user_ids | array of string | No | 플레이북 런 생성 시 채널에 자동 초대될 멤버 ID 목록 |
| invite_users_enabled | boolean | No | invited_user_ids 멤버 자동 초대 여부 |
| default_owner_id | string | No | 플레이북 런 생성 시 자동으로 오너로 지정될 사용자 ID (채널 멤버가 아니거나 invited_user_ids에 없으면 자동 초대됨) |
| default_owner_enabled | string | No | default_owner_id 멤버를 자동으로 오너로 지정할지 여부 |
| announcement_channel_id | string | No | 플레이북 런 생성이 자동으로 공지될 채널 ID |
| announcement_channel_enabled | boolean | No | announcement_channel_id 채널에 자동 공지할지 여부 |
| webhook_on_creation_url | string | No | 플레이북 런 생성 시 POST 요청이 전송될 절대 URL (HTTP/HTTPS만 허용) |
| webhook_on_creation_enabled | boolean | No | webhook_on_creation_url 웹훅 자동 전송 여부 |
| webhook_on_status_update_url | string | No | 플레이북 런 상태 업데이트 시 POST 요청이 전송될 절대 URL (HTTP/HTTPS만 허용) |
| webhook_on_status_update_enabled | boolean | No | webhook_on_status_update_url 웹훅 자동 전송 여부 |

```json
{
  "title": "string",
  "description": "string",
  "team_id": "string",
  "create_public_playbook_run": true,
  "public": true,
  "checklists": [
    {
      "title": "string",
      "items": [
        {
          "title": "string",
          "command": "string",
          "description": "string"
        }
      ]
    }
  ],
  "member_ids": ["string"]
}
```

## Response

### 201 - ID of the created playbook
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 생성된 플레이북의 ID |

```json
{ "id": "string" }
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

## 주의 사항
무료 티어에서는 `public: true`로 생성해야 한다.

---

# 3. Get a playbook

## 기본 정보
- **기능**: 플레이북 하나를 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/playbooks/{id}`
- **인증**: Bearer Token 필요
- **권한**: 플레이북 멤버 기반 접근 (해당 플레이북의 멤버여야 함)

## 설명
플레이북 ID로 단일 플레이북의 상세 정보를 조회하는 API이다. 플레이북의 기본 정보와 체크리스트(스테이지·아이템), 멤버 목록을 반환한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 조회할 플레이북의 ID |

## Response

### 200 - Playbook
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 플레이북의 고유 식별자 (26자 영숫자) |
| title | string | 플레이북 제목 |
| description | string | 플레이북 설명 |
| team_id | string | 플레이북이 속한 팀의 식별자 |
| create_public_playbook_run | boolean | 이 플레이북으로 생성되는 플레이북 런의 공개 여부 |
| create_at | integer | 플레이북 생성 시각 (Unix epoch 밀리초) |
| delete_at | integer | 플레이북 삭제 시각 (밀리초). 삭제되지 않았으면 0 |
| num_stages | integer | 이 플레이북에 정의된 스테이지 수 |
| num_steps | integer | 모든 스테이지의 전체 스텝 수 |
| checklists | array | 플레이북에 정의된 스테이지 목록 (체크리스트/아이템 배열) |
| member_ids | array of string | 이 플레이북의 멤버인 모든 사용자의 식별자 |

```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "team_id": "string",
  "create_public_playbook_run": true,
  "create_at": 0,
  "delete_at": 0,
  "num_stages": 0,
  "num_steps": 0,
  "checklists": [
    {
      "id": "string",
      "title": "string",
      "items": [
        {
          "id": "string",
          "title": "string",
          "state": "",
          "assignee_id": "string",
          "command": "string",
          "description": "string",
          "due_date": 0
        }
      ]
    }
  ],
  "member_ids": ["string"]
}
```
(체크리스트 아이템의 `state_modified`, `assignee_modified`, `command_last_run`, `delete_at`, `task_actions`, `update_at`, `condition_id`, `condition_action`, `condition_reason` 필드는 예시에서 생략)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

---

# 4. Update a playbook

## 기본 정보
- **기능**: 플레이북을 수정한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/playbooks/{id}`
- **인증**: Bearer Token 필요
- **권한**: 플레이북 멤버 기반 접근 (해당 플레이북의 멤버여야 함)

## 설명
플레이북 ID로 기존 플레이북을 수정하는 API이다. Body로 플레이북 객체 전체(제목, 설명, 체크리스트, 멤버 목록 등)를 전달한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 수정할 플레이북의 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | No | 플레이북의 고유 식별자 (26자 영숫자) |
| title | string | No | 플레이북 제목 |
| description | string | No | 플레이북 설명 |
| team_id | string | No | 플레이북이 속한 팀의 식별자 |
| create_public_playbook_run | boolean | No | 이 플레이북으로 생성되는 플레이북 런의 공개 여부 |
| create_at | integer | No | 플레이북 생성 시각 (Unix epoch 밀리초) |
| delete_at | integer | No | 플레이북 삭제 시각 (밀리초). 삭제되지 않았으면 0 |
| num_stages | integer | No | 스테이지 수 |
| num_steps | integer | No | 전체 스텝 수 |
| checklists | array | No | 플레이북에 정의된 스테이지 목록 (체크리스트/아이템 배열) |
| member_ids | array of string | No | 이 플레이북의 멤버인 모든 사용자의 식별자 |

```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "team_id": "string",
  "create_public_playbook_run": true,
  "checklists": [
    {
      "id": "string",
      "title": "string",
      "items": [
        {
          "id": "string",
          "title": "string",
          "state": "",
          "command": "string",
          "description": "string"
        }
      ]
    }
  ],
  "member_ids": ["string"]
}
```
(체크리스트 아이템의 기타 필드는 예시에서 생략)

## Response

### 200 - Playbook succesfully updated
(본문 스키마 없음)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

---

# 5. Delete a playbook

## 기본 정보
- **기능**: 플레이북을 삭제한다.
- **Endpoint**: `DELETE /plugins/playbooks/api/v0/playbooks/{id}`
- **인증**: Bearer Token 필요
- **권한**: 플레이북 멤버 기반 접근 (해당 플레이북의 멤버여야 함)

## 설명
플레이북 ID로 플레이북을 삭제하는 API이다. 성공 시 204(본문 없음)를 반환한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 삭제할 플레이북의 ID |

## Response

### 204 - Playbook successfully deleted
(본문 없음)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

---

# 6. Get property fields for a playbook

## 기본 정보
- **기능**: 플레이북의 프로퍼티 필드 목록을 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/playbooks/{id}/property_fields`
- **인증**: Bearer Token 필요
- **권한**: 플레이북 멤버 기반 접근 (해당 플레이북의 멤버여야 함)

## 설명
플레이북에 정의된 프로퍼티 필드 목록을 조회하는 API이다. `updated_since` 쿼리 파라미터로 특정 시각 이후에 갱신된 필드만 필터링할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 프로퍼티 필드를 조회할 플레이북의 ID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| updated_since | integer | No | - | 이 타임스탬프(Unix time, 밀리초) 이후에 갱신된 프로퍼티 필드만 포함 |

## Response

### 200 - List of property fields for the playbook
프로퍼티 필드 객체의 배열을 반환한다.
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 프로퍼티 필드의 고유 식별자 (26자 영숫자) |
| type | enum | 프로퍼티 필드 타입 (text / select / multiselect) |
| name | string | 프로퍼티 필드 이름 |
| description | string | 프로퍼티 필드 설명 |
| create_at | integer | 생성 시각 (Unix epoch 밀리초) |
| update_at | integer | 갱신 시각 (Unix epoch 밀리초) |
| delete_at | integer | 삭제 시각 (밀리초). 삭제되지 않았으면 0 |
| attrs | object | 추가 속성 (select 필드의 옵션, 표시 설정 등) |

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
| 500 | 서버 내부 오류 |

---

# 7. Create a property field for a playbook

## 기본 정보
- **기능**: 플레이북에 프로퍼티 필드를 생성한다.
- **Endpoint**: `POST /plugins/playbooks/api/v0/playbooks/{id}/property_fields`
- **인증**: Bearer Token 필요
- **권한**: 플레이북 멤버 기반 접근 (해당 플레이북의 멤버여야 함)

## 설명
플레이북에 새 프로퍼티 필드를 생성하는 API이다. 필드 이름과 타입(text/select/multiselect)이 필수이며, select 계열 필드는 attrs.options로 선택지를 정의할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 프로퍼티 필드를 생성할 플레이북의 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| name | string | Yes | 프로퍼티 필드 이름 |
| type | enum | Yes | 프로퍼티 필드 타입 (text / select / multiselect) |
| attrs | object | No | 추가 속성. visibility(hidden / when_set / always: 표시 시점), sortOrder(number: 표시 순서), options(select/multiselect의 선택지 배열: id, name(필수), color), parentID(계층형 필드의 부모 필드 ID) |

```json
{
  "name": "string",
  "type": "select",
  "attrs": {
    "visibility": "always",
    "sortOrder": 0,
    "options": [
      { "id": "string", "name": "string", "color": "string" }
    ],
    "parentID": "string"
  }
}
```

## Response

### 201 - Property field created successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 프로퍼티 필드의 고유 식별자 (26자 영숫자) |
| type | enum | 프로퍼티 필드 타입 (text / select / multiselect) |
| name | string | 프로퍼티 필드 이름 |
| description | string | 프로퍼티 필드 설명 |
| create_at | integer | 생성 시각 (Unix epoch 밀리초) |
| update_at | integer | 갱신 시각 (Unix epoch 밀리초) |
| delete_at | integer | 삭제 시각 (밀리초). 삭제되지 않았으면 0 |
| attrs | object | 추가 속성 (select 필드의 옵션, 표시 설정 등) |

```json
{
  "id": "string",
  "type": "select",
  "name": "string",
  "description": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "attrs": {}
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

---

# 8. Update a property field for a playbook

## 기본 정보
- **기능**: 플레이북의 프로퍼티 필드를 수정한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/playbooks/{id}/property_fields/{field_id}`
- **인증**: Bearer Token 필요
- **권한**: 플레이북 멤버 기반 접근 (해당 플레이북의 멤버여야 함)

## 설명
플레이북의 기존 프로퍼티 필드를 수정하는 API이다. Body 구조는 생성 API와 동일하며, 이름과 타입이 필수이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 프로퍼티 필드가 속한 플레이북의 ID |
| field_id | string | Yes | 수정할 프로퍼티 필드의 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| name | string | Yes | 프로퍼티 필드 이름 |
| type | enum | Yes | 프로퍼티 필드 타입 (text / select / multiselect) |
| attrs | object | No | 추가 속성. visibility(hidden / when_set / always: 표시 시점), sortOrder(number: 표시 순서), options(select/multiselect의 선택지 배열: id, name(필수), color), parentID(계층형 필드의 부모 필드 ID) |

```json
{
  "name": "string",
  "type": "select",
  "attrs": {
    "visibility": "always",
    "sortOrder": 0,
    "options": [
      { "id": "string", "name": "string", "color": "string" }
    ],
    "parentID": "string"
  }
}
```

## Response

### 200 - Property field updated successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 프로퍼티 필드의 고유 식별자 (26자 영숫자) |
| type | enum | 프로퍼티 필드 타입 (text / select / multiselect) |
| name | string | 프로퍼티 필드 이름 |
| description | string | 프로퍼티 필드 설명 |
| create_at | integer | 생성 시각 (Unix epoch 밀리초) |
| update_at | integer | 갱신 시각 (Unix epoch 밀리초) |
| delete_at | integer | 삭제 시각 (밀리초). 삭제되지 않았으면 0 |
| attrs | object | 추가 속성 (select 필드의 옵션, 표시 설정 등) |

```json
{
  "id": "string",
  "type": "select",
  "name": "string",
  "description": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "attrs": {}
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

---

# 9. Delete a property field for a playbook

## 기본 정보
- **기능**: 플레이북의 프로퍼티 필드를 삭제한다.
- **Endpoint**: `DELETE /plugins/playbooks/api/v0/playbooks/{id}/property_fields/{field_id}`
- **인증**: Bearer Token 필요
- **권한**: 플레이북 멤버 기반 접근 (해당 플레이북의 멤버여야 함)

## 설명
플레이북에서 프로퍼티 필드를 삭제하는 API이다. 성공 시 204(본문 없음)를 반환한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 프로퍼티 필드가 속한 플레이북의 ID |
| field_id | string | Yes | 삭제할 프로퍼티 필드의 ID |

## Response

### 204 - Property field deleted successfully
(본문 없음)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

---

# 10. Reorder property fields for a playbook

## 기본 정보
- **기능**: 플레이북의 프로퍼티 필드 표시 순서를 변경한다.
- **Endpoint**: `POST /plugins/playbooks/api/v0/playbooks/{id}/property_fields/reorder`
- **인증**: Bearer Token 필요
- **권한**: 플레이북 멤버 기반 접근 (해당 플레이북의 멤버여야 함)

## 설명
지정한 프로퍼티 필드를 목표 위치(0부터 시작하는 인덱스)로 이동시켜 필드 순서를 재정렬하는 API이다. 성공 시 재정렬된 전체 프로퍼티 필드 목록을 반환한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 플레이북의 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| field_id | string | Yes | 이동할 프로퍼티 필드의 ID |
| target_position | integer | Yes | 필드가 이동할 목표 위치 인덱스 (0부터 시작) |

```json
{
  "field_id": "string",
  "target_position": 0
}
```

## Response

### 200 - Property fields reordered successfully
프로퍼티 필드 객체의 배열을 반환한다.
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 프로퍼티 필드의 고유 식별자 (26자 영숫자) |
| type | enum | 프로퍼티 필드 타입 (text / select / multiselect) |
| name | string | 프로퍼티 필드 이름 |
| description | string | 프로퍼티 필드 설명 |
| create_at | integer | 생성 시각 (Unix epoch 밀리초) |
| update_at | integer | 갱신 시각 (Unix epoch 밀리초) |
| delete_at | integer | 삭제 시각 (밀리초). 삭제되지 않았으면 0 |
| attrs | object | 추가 속성 (select 필드의 옵션, 표시 설정 등) |

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
| 404 | 찾을 수 없음 |
| 500 | 서버 내부 오류 |

---
