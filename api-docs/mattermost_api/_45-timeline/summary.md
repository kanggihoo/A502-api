# 1. Remove a timeline event from the playbook run

## 기본 정보
- **기능**: 플레이북 런(playbook run)의 타임라인에서 특정 이벤트를 삭제한다.
- **Endpoint**: `DELETE /plugins/playbooks/api/v0/runs/{id}/timeline/{event_id}`
- **인증**: 로그인 필요
- **권한**: 플레이북 런 멤버(참여자) 기반 접근 (별도의 이름있는 권한 불요)

## 설명
플레이북 런의 타임라인에 기록된 이벤트 중 지정한 이벤트를 삭제하는 API이다. Playbooks 플러그인이 제공하는 API로, 해당 플레이북 런에 접근할 수 있는 멤버(참여자)가 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 타임라인 이벤트를 수정할 플레이북 런의 ID |
| event_id | string | Yes | 삭제할 타임라인 이벤트의 ID |

## Response

### 204 - Item successfully deleted
응답 본문 없음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 500 | 서버 내부 오류 |

## 주의 사항
Playbooks 플러그인이 설치·활성화되어 있어야 사용할 수 있다.

---
