# 15. Get access control attributes for a channel

## 기본 정보
- **기능**: 특정 채널에 적용 중인 접근 제어 정책(access control policy) 속성을 조회한다.
- **Endpoint**: `GET /api/v4/channels/{channel_id}/access_control/attributes`
- **인증**: Bearer Token 필요
- **권한**: `read_channel` (해당 채널에 대해)

## 설명
지정한 채널에 대해 접근 제어 시스템이 현재 적용하고 있는 유효(effective) 정책 속성을 조회하는 API이다. 채널에 어떤 속성 기반 접근 제어가 걸려 있는지 파악하는 용도로 사용한다. 해당 채널의 `read_channel` 권한만 있으면 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 ID |

## Response

### 200 - Access control attributes retrieved successfully.

```json
{}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 채널을 찾을 수 없음 |
| 500 | 서버 내부 오류 |

---

## 제외된 API
- **01, 02, 04, 06~14, 16**: `manage_system` 권한 필요로 제외됨.
- **03-Validate if the current user matches a CEL expression**: `manage_system` 또는 채널 관리자(channel admin) 필요 — 일반 멤버 권한에 없어 제외됨.
- **05-Simulate an access control policy decision**: `manage_system` 또는 `manage_team_access_rules`/`manage_channel_access_rules` 위임 관리자 권한 필요로 제외됨.
- **17-Activate or deactivate access control policies**: `manage_system` 또는 채널 관리자의 `manage_channel_access_rules` 필요로 제외됨.
