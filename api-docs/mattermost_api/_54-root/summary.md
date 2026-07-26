# 1. Acknowledge receiving of a notification

## 기본 정보
- **기능**: 푸시 알림 수신을 서버에 확인(acknowledge) 처리한다.
- **Endpoint**: `POST /api/v4/notifications/ack`
- **인증**: Bearer Token 필요 (로그인 필요)
- **권한**: 없음 (인증만 필요)

## 설명
클라이언트(주로 모바일)가 푸시 알림을 수신했음을 서버에 알리는 API이다. 로그인한 사용자라면 호출할 수 있다. 최소 서버 버전은 3.10이다.

## Response

### 200 - Status of the system
| 필드 | 타입 | 설명 |
|---|---|---|
| ack_id | string | 확인(ack) ID |
| platform | string | 플랫폼 |
| server_id | string | 서버 ID |
| device_id | string | 디바이스 ID |
| post_id | string | 게시글 ID |
| category | string | 알림 카테고리 |
| sound | string | 알림 사운드 |
| message | string | 알림 메시지 |
| badge | number | 배지 수 |
| cont_ava | number | - |
| team_id | string | 팀 ID |
| channel_id | string | 채널 ID |
| root_id | string | 루트 게시글 ID |
| channel_name | string | 채널 이름 |
| type | string | 알림 유형 |
| sub_type | string | 모바일 클라이언트용 추가 메시지 유형 (Calls 플러그인 알림은 "calls") |
| transport | string | 푸시 프록시 전달 경로 (`""` 또는 `"voip"`, VoIP(CallKit) 알림은 "voip") |
| sender_id | string | 발신자 ID |
| sender_name | string | 발신자 이름 |
| override_username | string | 대체 사용자명 |
| override_icon_url | string | 대체 아이콘 URL |
| from_webhook | string | 웹훅 발신 여부 |
| version | string | 버전 |
| is_crt_enabled | boolean | 수신자의 Collapsed Reply Threads 활성화 여부 |
| is_id_loaded | boolean | ID 로드 여부 |
| signature | string | 서명 |

```json
{
  "ack_id": "string",
  "platform": "string",
  "server_id": "string",
  "device_id": "string",
  "post_id": "string",
  "category": "string",
  "sound": "string",
  "message": "string",
  "badge": 0,
  "cont_ava": 0,
  "team_id": "string",
  "channel_id": "string",
  "root_id": "string",
  "channel_name": "string",
  "type": "string",
  "sub_type": "string",
  "transport": "voip",
  "sender_id": "string",
  "sender_name": "string",
  "override_username": "string",
  "override_icon_url": "string",
  "from_webhook": "string",
  "version": "string",
  "is_crt_enabled": true,
  "is_id_loaded": true,
  "signature": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 404 | 리소스를 찾을 수 없음 |

---
