# 1. Get common teams for members of a Group Message

## 기본 정보
- **기능**: 그룹 메시지(GM) 채널의 모든 활성 멤버가 공통으로 속한 팀 목록을 조회한다.
- **Endpoint**: `GET /api/v4/channels/{channel_id}/common_teams`
- **인증**: Bearer Token 필요
- **권한**: 해당 채널에 대한 `read_channel`

## 설명
그룹 메시지 채널의 모든 활성 멤버가 공통으로 소속된 팀들을 조회하는 API이다. 공통 팀이 없으면 빈 배열을 반환한다. 최소 서버 버전은 9.1이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |

## Response

### 200 - Common teams retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 팀 ID |
| create_at | integer | 팀 생성 시각 (밀리초) |
| update_at | integer | 팀 마지막 수정 시각 (밀리초) |
| delete_at | integer | 팀 삭제 시각 (밀리초) |
| display_name | string | 팀 표시 이름 |
| name | string | 팀 이름 |
| description | string | 팀 설명 |
| email | string | 팀 이메일 |
| type | string | 팀 유형 |
| allowed_domains | string | 허용 도메인 |
| invite_id | string | 초대 ID |
| allow_open_invite | boolean | 공개 초대 허용 여부 |
| policy_id | string | 데이터 보존 정책 ID (정책이 없거나 `sysconsole_read_compliance_data_retention` 권한이 없으면 null) |

```json
[
  {
    "id": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0,
    "display_name": "string",
    "name": "string",
    "description": "string",
    "email": "string",
    "type": "string",
    "allowed_domains": "string",
    "invite_id": "string",
    "allow_open_invite": true,
    "policy_id": "string"
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

---

# 2. Convert group message to private channel

## 기본 정보
- **기능**: 그룹 메시지(GM) 채널을 지정한 팀의 비공개 채널로 변환한다.
- **Endpoint**: `POST /api/v4/channels/{channel_id}/convert_to_channel`
- **인증**: Bearer Token 필요
- **권한**: 대상 팀에서 `create_private_channel`

## 설명
그룹 메시지 채널을 지정한 팀(team_id)의 비공개 채널로 변환하는 API이다. 대상 팀에서 비공개 채널을 생성할 수 있는 권한이 있어야 한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 그룹 메시지 채널 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 변환할 그룹 메시지 채널 ID |
| team_id | string | Yes | 변환 후 소속될 팀 ID |

```json
{
  "channel_id": "string",
  "team_id": "string"
}
```

## Response

### 200 - Conversion successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 채널 ID |
| create_at | integer | 채널 생성 시각 (밀리초) |
| update_at | integer | 채널 마지막 수정 시각 (밀리초) |
| delete_at | integer | 채널 삭제 시각 (밀리초) |
| team_id | string | 소속 팀 ID |
| type | string | 채널 유형 |
| display_name | string | 채널 표시 이름 |
| name | string | 채널 이름 |
| header | string | 채널 헤더 |
| purpose | string | 채널 목적 |
| last_post_at | integer | 채널 마지막 게시글 시각 (밀리초) |
| total_msg_count | integer | 전체 메시지 수 |
| extra_update_at | integer | (Mattermost 5.0에서 deprecated) |
| creator_id | string | 채널 생성자 ID |

```json
{
  "id": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "team_id": "string",
  "type": "string",
  "display_name": "string",
  "name": "string",
  "header": "string",
  "purpose": "string",
  "last_post_at": 0,
  "total_msg_count": 0,
  "extra_update_at": 0,
  "creator_id": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스를 찾을 수 없음 |

---
