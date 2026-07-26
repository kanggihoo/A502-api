# 1. Create a board channel

## 기본 정보
- **기능**: 새 board 채널(칸반 view 기반 채널)을 생성한다.
- **Endpoint**: `POST /api/v4/boards`
- **인증**: Bearer Token 필요
- **권한**: type `BO`(open board)는 `create_public_channel`, type `BP`(private board)는 `create_private_channel` (대상 팀)

## 설명
새 board 채널을 생성하는 API이다. Board는 연결된 속성(기본값: status, assignee)을 기반으로 한 칸반 view를 가진 채널로, 일반 채널과 함께 존재하지만 `/api/v4/channels` endpoint로는 생성/수정할 수 없다. Request body는 `type`이 `BO`(open board) 또는 `BP`(private board)인 Channel 객체이며 `team_id`와 `display_name`이 필수이다. `IntegratedBoards` feature flag 뒤에 있는 기능으로, flag가 꺼져 있으면 라우트가 등록되지 않아 404를 반환한다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| team_id | string | Yes | board가 속할 팀 ID |
| type | enum("BO" \| "BP") | Yes | board 채널 타입. `BO`: open board (모든 팀 멤버에게 보임), `BP`: private board (초대된 멤버에게만 보임) |
| display_name | string | Yes | UI에 표시되는 이름. 비어 있으면 안 됨 |
| name | string | No | URL-safe 채널 이름. 생략 시 자동 생성 |
| header | string | No | 채널 헤더 |
| purpose | string | No | 채널 목적 |

```json
{
  "team_id": "string",
  "type": "BO",
  "display_name": "string",
  "name": "string",
  "header": "string",
  "purpose": "string"
}
```

## Response

### 201 - Board channel creation successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 채널 ID |
| create_at | integer | 채널 생성 시각 (밀리초) |
| update_at | integer | 채널 마지막 수정 시각 (밀리초) |
| delete_at | integer | 채널 삭제 시각 (밀리초) |
| team_id | string | 팀 ID |
| type | string | 채널 타입 |
| display_name | string | 표시 이름 |
| name | string | 채널 이름 |
| header | string | 채널 헤더 |
| purpose | string | 채널 목적 |
| last_post_at | integer | 채널의 마지막 게시물 시각 (밀리초) |
| total_msg_count | integer | 총 메시지 수 |
| extra_update_at | integer | Mattermost 5.0에서 deprecated |
| creator_id | string | 생성자 ID |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | `IntegratedBoards` feature flag가 꺼져 있어 라우트가 없음 |
| 500 | 서버 오류 |

## 주의 사항
Experimental endpoint이며 `IntegratedBoards` feature flag가 켜져 있어야 사용할 수 있다. flag가 꺼져 있으면 404를 반환한다.

---
