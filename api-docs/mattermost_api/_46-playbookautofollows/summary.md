# 1. Get the list of followers' user IDs of a playbook

## 기본 정보
- **기능**: 특정 플레이북을 자동 팔로우(auto-follow)로 설정한 사용자들의 ID 목록을 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/playbooks/{id}/autofollows`
- **인증**: 로그인 필요
- **권한**: 플레이북 멤버 기반 접근 (별도의 이름있는 권한 불요)

## 설명
지정한 플레이북의 런(run)을 자동으로 팔로우하도록 설정한 사용자들의 user ID 목록과 총 인원 수를 조회하는 API이다. Playbooks 플러그인이 제공하는 API로, 해당 플레이북에 접근할 수 있는 멤버가 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 팔로워를 조회할 플레이북의 ID |

## Response

### 200 - List of the user IDs who follow the playbook
| 필드 | 타입 | 설명 |
|---|---|---|
| total_count | integer | 이 플레이북을 자동 팔로우로 설정한 사용자의 총 수 |
| items | string[] | 자동 팔로우로 설정한 사용자들의 user ID 목록 |

```json
{
  "total_count": 0,
  "items": ["string"]
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

## 주의 사항
Playbooks 플러그인이 설치·활성화되어 있어야 사용할 수 있다.

---
