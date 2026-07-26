# 1. Retrieve a list of supported timezones

## 기본 정보
- **기능**: 서버가 지원하는 타임존 목록을 조회한다.
- **Endpoint**: `GET /api/v4/system/timezones`
- **인증**: Bearer Token 필요
- **권한**: 없음 (로그인만 필요)

## 설명
서버에서 지원하는 타임존의 전체 목록을 문자열 배열로 반환한다. 최소 서버 버전은 3.10이다.

## Request

파라미터 없음.

## Response

### 200 - List of timezones retrieval successful
문자열 배열로 타임존 목록이 반환된다.

```json
[
  "string"
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 500 | 명시되지 않음 |

---

# 2. Check system health

## 기본 정보
- **기능**: 서버가 정상 동작 중인지 확인한다 (ping).
- **Endpoint**: `GET /api/v4/system/ping`
- **인증**: Bearer Token 불필요
- **권한**: 없음 (인증 자체가 불필요)

## 설명
`GoRoutineHealthThreshold` 설정을 기준으로 서버가 정상인지 확인한다. 해당 설정이 없거나 고루틴 수가 임계값 이하이면 정상으로 판단한다. `device_id`를 쿼리로 전달하면 해당 기기가 푸시 알림을 받을 수 있는지 Push Notification Proxy를 테스트하며, 응답에 `CanReceiveNotifications`(true/false/unknown)가 포함된다. `get_server_status=true`이면 `database_status`, `filestore_status`가 추가로 반환된다 (`manage_system` 권한이 있으면 `root_status`도 반환되지만 일반 계정에는 해당 없음).

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| get_server_status | boolean | No | - | 데이터베이스·파일 스토리지 상태도 함께 확인. true이면 응답에 `database_status`, `filestore_status` 추가 |
| device_id | string | No | - | 해당 device id가 푸시 알림을 받을 수 있는지 확인 |
| use_rest_semantics | boolean | No | - | 서버 상태가 비정상이어도 200 상태 코드를 반환 |

## Response

### 200 - Status of the system
| 필드 | 타입 | 설명 |
|---|---|---|
| AndroidLatestVersion | string | 지원되는 최신 Android 버전 |
| AndroidMinVersion | string | 지원되는 최소 Android 버전 |
| DesktopLatestVersion | string | 지원되는 최신 데스크톱 버전 |
| DesktopMinVersion | string | 지원되는 최소 데스크톱 버전 |
| IosLatestVersion | string | 지원되는 최신 iOS 버전 |
| IosMinVersion | string | 지원되는 최소 iOS 버전 |
| database_status | string | 데이터베이스 상태 ("OK" 또는 "UNHEALTHY"). get_server_status 지정 시 포함 |
| filestore_status | string | 파일 스토리지 상태 ("OK" 또는 "UNHEALTHY"). get_server_status 지정 시 포함 |
| status | string | 서버 상태 ("OK" 또는 "UNHEALTHY") |
| CanReceiveNotifications | string | 해당 기기의 알림 수신 가능 여부 ("true", "false", "unknown"). device_id 지정 시 포함 |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 500 | 명시되지 않음 |

---

# 3. Open a WebSocket connection

## 기본 정보
- **기능**: 실시간 이벤트 수신용 WebSocket 연결을 연다.
- **Endpoint**: `GET /api/v4/websocket`
- **인증**: 연결 자체에는 불필요 (연결 후 인증 가능)
- **권한**: 없음 (연결에 권한 불요)

## 설명
HTTP 연결을 WebSocket 연결로 업그레이드하여 실시간 이벤트와 websocket 액션에 사용한다. 인증은 표준 API 인증(쿠키/헤더)으로 하거나, 연결 후 `authentication_challenge` 액션을 전송하는 방식으로 수행할 수 있다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| connection_id | string | No | - | 재연결 시 사용할 기존 연결 식별자 |
| sequence_number | string | No | - | 재연결 시 마지막으로 수신한 시퀀스 번호 |
| posted_ack | boolean | No | - | 이 연결에서 post 수신 확인 이벤트 활성화 여부 |
| disconnect_err_code | string | No | - | 클라이언트가 연결 종료 사유를 나타내는 close 코드 (선택) |

## Response

### 101 - Switching Protocols
WebSocket으로 프로토콜이 전환된다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |

---

# 5. Get notices for logged in user in specified team

## 기본 정보
- **기능**: 지정한 팀에서 현재 사용자에게 표시할 제품 공지(product notices)를 조회한다.
- **Endpoint**: `GET /api/v4/system/notices/{team_id}`
- **인증**: Bearer Token 필요
- **권한**: 없음 (로그인만 필요)

## 설명
team_id로 지정한 팀에서 현재 사용자에게 적합한 제품 공지 목록을 반환한다. 클라이언트 종류와 버전을 쿼리로 전달해야 한다. 최소 서버 버전은 5.26이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| team_id | string | Yes | 팀 ID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| clientVersion | string | Yes | - | 요청을 보내는 클라이언트(desktop/mobile/web)의 버전 |
| locale | string | No | - | 클라이언트 로케일 |
| client | string | Yes | - | 클라이언트 타입 (web/mobile-ios/mobile-android/desktop) |

## Response

### 200 - List notices retrieve successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 공지 ID |
| sysAdminOnly | boolean | 시스템 관리자에게만 적용되는 공지 여부 |
| teamAdminOnly | boolean | 팀 관리자에게만 적용되는 공지 여부 |
| action | string | 액션 버튼 클릭 시 수행할 액션 (기본: 공지 닫기) |
| actionParam | string | 액션 파라미터. 예: {"action": "url", "actionParam": "/console/some-page"} |
| actionText | string | 액션 버튼 텍스트 재정의 (기본: OK) |
| description | string | 공지 내용 (Markdown 지원) |
| image | string | 표시할 이미지 URL |
| title | string | 공지 제목 (Markdown 지원) |

```json
[
  {
    "id": "string",
    "sysAdminOnly": true,
    "teamAdminOnly": true,
    "action": "string",
    "actionParam": "string",
    "actionText": "string",
    "description": "string",
    "image": "string",
    "title": "string"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 500 | 명시되지 않음 |

---

# 6. Update notices as 'viewed'

## 기본 정보
- **기능**: 지정한 공지들을 현재 사용자가 '읽음' 처리한다.
- **Endpoint**: `PUT /api/v4/system/notices/view`
- **인증**: Bearer Token 필요
- **권한**: 없음 (로그인만 필요)

## 설명
지정한 공지 ID들을 로그인한 사용자 기준으로 'viewed' 상태로 표시한다. 최소 서버 버전은 5.26이다.

## Request

### Body
공지 ID 문자열 배열.

```json
[
  "string"
]
```

## Response

### 200 - Update successfull
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

```json
{
  "status": "ok"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 500 | 명시되지 않음 |

---

# 14. Send a test notification

## 기본 정보
- **기능**: 알림 설정이 올바른지 확인하기 위한 테스트 알림을 자신에게 보낸다.
- **Endpoint**: `POST /api/v4/notifications/test`
- **인증**: Bearer Token 필요
- **권한**: 없음 (로그인만 필요)

## 설명
자신의 알림 설정이 제대로 구성되어 있는지 확인할 수 있도록 테스트 알림을 발송한다.

## Request

파라미터 없음.

## Response

### 200 - Notification successfully sent
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

```json
{
  "status": "ok"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 403 | 명시되지 않음 |
| 500 | 명시되지 않음 |

---

# 22. Get client configuration

## 기본 정보
- **기능**: 클라이언트에 필요한 서버 설정의 일부를 조회한다.
- **Endpoint**: `GET /api/v4/config/client`
- **인증**: Bearer Token 불필요
- **권한**: 없음

## 설명
클라이언트가 필요로 하는 서버 설정의 하위 집합을 반환한다. 권한이 전혀 필요하지 않다.

## Request

파라미터 없음.

## Response

### 200 - Configuration retrieval successful
응답 스키마는 문서에 명시되지 않음.

---

# 28. Get client license

## 기본 정보
- **기능**: 클라이언트에 필요한 서버 라이선스 정보의 일부를 조회한다.
- **Endpoint**: `GET /api/v4/license/client`
- **인증**: Bearer Token 불필요
- **권한**: 없음 (`manage_system` 권한이 있으면 더 많은 정보 반환)

## 설명
클라이언트가 필요로 하는 서버 라이선스 정보의 하위 집합을 반환한다. 권한 없이 호출 가능하며, `manage_system` 권한 보유 시 더 많은 정보가 반환된다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| format | string | Yes | - | 반드시 `old`여야 함. 다른 형식은 미구현 |

## Response

### 200 - License retrieval successful
응답 스키마는 문서에 명시되지 않음.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 29. Get license load metric

## 기본 정보
- **기능**: 현재 라이선스 부하 지표(load metric)를 조회한다.
- **Endpoint**: `GET /api/v4/license/load_metric`
- **인증**: Bearer Token 필요
- **권한**: 없음 (로그인만 필요)

## 설명
월간 활성 사용자 수를 라이선스 사용자 수와 비교하여 계산한 현재 라이선스 부하 지표를 반환한다. 라이선스가 없거나 라이선스에 사용자 수가 없으면 0을 반환한다. 최소 서버 버전은 10.8이다.

## Request

파라미터 없음.

## Response

### 200 - License load metric retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| load | integer | 현재 라이선스 부하 지표 (정수) |

```json
{
  "load": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 명시되지 않음 |
| 500 | 명시되지 않음 |

---

# 35. Add log message

## 기본 정보
- **기능**: 서버 로그에 로그 메시지를 기록한다.
- **Endpoint**: `POST /api/v4/logs`
- **인증**: Bearer Token 필요 (일반 사용자 기준)
- **권한**: 없음 — 단, 일반 로그인 사용자는 `ServiceSettings.EnableDeveloper`가 true이면 ERROR/DEBUG, false이면 DEBUG만 기록 가능

## 설명
서버 로그에 메시지를 추가한다. `manage_system` 권한 사용자는 항상 ERROR/DEBUG를 기록할 수 있고, 일반 로그인 사용자는 `EnableDeveloper` 설정에 따라 기록 가능한 레벨이 달라진다 (false이면 DEBUG만 가능). 비로그인 사용자는 `EnableDeveloper`가 true일 때만 기록할 수 있다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| level | string | Yes | 로그 레벨, ERROR 또는 DEBUG |
| message | string | Yes | 서버 로그에 보낼 메시지 |

```json
{
  "level": "DEBUG",
  "message": "string"
}
```

## Response

### 200 - Logs sent successful

```json
{}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 403 | 명시되지 않음 |

## 주의 사항
- 일반 멤버 계정은 `EnableDeveloper`가 false인 서버에서 DEBUG 레벨만 기록할 수 있다.

---

# 43. Get redirect location

## 기본 정보
- **기능**: 주어진 URL의 리다이렉트 위치를 조회한다.
- **Endpoint**: `GET /api/v4/redirect_location`
- **인증**: Bearer Token 필요
- **권한**: 없음 (로그인만 필요)

## 설명
지정한 URL이 리다이렉트되는 위치를 반환한다. 최소 서버 버전은 3.10이다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| url | string | Yes | - | 확인할 URL |

## Response

### 200 - Got redirect location
| 필드 | 타입 | 설명 |
|---|---|---|
| location | string | 리다이렉트 위치 |

```json
{
  "location": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 404 | 명시되지 않음 |

---

# 44. Get an image by url

## 기본 정보
- **기능**: Mattermost 이미지 프록시를 통해 이미지를 가져온다.
- **Endpoint**: `GET /api/v4/image`
- **인증**: Bearer Token 필요
- **권한**: 없음 (로그인만 필요)

## 설명
Mattermost 이미지 프록시를 경유하여 이미지를 가져온다. 최소 서버 버전은 3.10이다.

## Response

### 200 - Image found
image/* 형식의 이미지 데이터가 반환된다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 404 | 명시되지 않음 |
