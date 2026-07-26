# 1. Open a dialog

## 기본 정보
- **기능**: slash command 등 다른 액션에서 제공받은 trigger ID로 interactive dialog를 연다.
- **Endpoint**: `POST /api/v4/actions/dialogs/open`
- **인증**: Bearer Token 필요
- **권한**: 별도의 이름있는 권한 불요 (trigger_id 기반의 일반 사용자 대상 상호작용 endpoint)

## 설명
slash command 또는 다른 액션 페이로드에서 제공받은 trigger ID를 사용하여 interactive dialog를 여는 API이다. 동시에 최대 3개의 interactive dialog를 열 수 있으며(서버 11.10 이상), 이 제한을 초과하는 `open_dialog` 이벤트는 클라이언트에서 조용히 무시된다. 최소 서버 버전은 5.6이다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| trigger_id | string | Yes | 다른 액션에서 제공받은 Trigger ID |
| url | string | Yes | 제출된 dialog 페이로드를 전송할 URL |
| dialog | object | Yes | dialog 정의 객체 |
| dialog.callback_id | string | No | dialog 제출 시 함께 포함될 ID |
| dialog.title | string | Yes | dialog의 제목 |
| dialog.introduction_text | string | No | Markdown 형식의 도입 문단 |
| dialog.elements | array | Yes | 입력 요소 목록. 지원 타입: `text`, `textarea`, `select`, `radio`, `bool`, `action_button`. `action_button`(서버 11.10 이상)은 클릭 가능한 버튼으로, `name`, `display_name`, `type`("action_button"), `action_button` 객체(필수 `url`은 유효한 lookup URL, 선택 `context`는 문자열 맵)를 가진다. 클릭 시 `POST /api/v4/actions/dialogs/execute`가 호출되며, `action_button` 요소는 dialog 제출 페이로드에 포함되지 않는다 |
| dialog.submit_label | string | No | 제출 버튼의 라벨 |
| dialog.notify_on_cancel | boolean | No | true로 설정 시 사용자가 dialog를 취소할 때도 페이로드를 수신 |
| dialog.state | string | No | dialog 제출 시 그대로 되돌려 받을 상태 값 |

```json
{
  "trigger_id": "string",
  "url": "string",
  "dialog": {
    "callback_id": "string",
    "title": "string",
    "introduction_text": "string",
    "elements": [{}],
    "submit_label": "string",
    "notify_on_cancel": false,
    "state": "string"
  }
}
```

## Response

### 200 - Dialog open successful
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

## 주의 사항
trigger ID는 slash command 등 다른 액션에서 발급받아야 하며, 동시에 열 수 있는 dialog는 최대 3개이다.

---

# 2. Submit a dialog

## 기본 정보
- **기능**: 사용자가 작성한 interactive dialog를 제출한다.
- **Endpoint**: `POST /api/v4/actions/dialogs/submit`
- **인증**: Bearer Token 필요
- **권한**: 별도의 이름있는 권한 불요 (Mattermost 클라이언트가 사용하는 일반 사용자 대상 endpoint)

## 설명
Mattermost 클라이언트가 interactive dialog 제출에 사용하는 API이다. 제출 페이로드는 지정한 URL의 통합(integration)으로 전송된다. 최소 서버 버전은 5.6이다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| url | string | Yes | 제출된 dialog 페이로드를 전송할 URL |
| channel_id | string | Yes | 사용자가 dialog를 제출한 채널의 ID |
| team_id | string | No | 선택 사항. 서버가 채널로부터 팀을 결정하므로 클라이언트 제공 값은 무시됨. DM/GM 채널은 팀이 없어 빈 값 |
| submission | object | Yes | 요소 이름을 키, 입력 값을 값으로 하는 문자열 맵 |
| callback_id | string | No | dialog가 열릴 때 전송된 Callback ID |
| state | string | No | dialog가 열릴 때 전송된 상태 값 |
| cancelled | boolean | No | dialog가 취소된 경우 true |
| file_ids | array of string | No | dialog 제출과 함께 업로드된 파일 ID 목록. 각 파일은 제출하는 사용자가 업로드한 것이어야 하며, 최대 10개까지 제출 가능 |

```json
{
  "url": "string",
  "channel_id": "string",
  "submission": {},
  "callback_id": "string",
  "state": "string",
  "cancelled": false,
  "file_ids": ["string"]
}
```

## Response

### 200 - Dialog submission successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 요청 성공 시 "ok" 반환 |

```json
{ "status": "ok" }
```

### 429 - The upstream integration rate-limited the request
업스트림 통합이 요청을 rate-limit한 경우. 클라이언트가 재시도 규칙을 지킬 수 있도록 원래 상태 코드가 유지된다.

| 필드 | 타입 | 설명 |
|---|---|---|
| status_code | integer | 상태 코드 |
| id | string | 에러 ID |
| message | string | 에러 메시지 |
| request_id | string | 요청 ID |

```json
{
  "status_code": 429,
  "id": "string",
  "message": "string",
  "request_id": "string"
}
```

### 502 - The upstream integration returned a 5xx (other than 503)
업스트림 통합이 503 이외의 5xx를 반환한 경우. 장애가 Mattermost 상류에 있으므로 Bad Gateway로 표면화된다.

### 503 - The upstream integration is unavailable
업스트림 통합을 사용할 수 없는 경우. 클라이언트가 재시도 규칙을 지킬 수 있도록 원래 상태 코드가 유지된다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 429 | 업스트림 통합의 rate limit |
| 502 | 업스트림 통합의 5xx 오류 (503 제외) |
| 503 | 업스트림 통합 사용 불가 |

## 주의 사항
`file_ids`의 파일은 제출자 본인이 업로드한 것이어야 하며 최대 10개까지 허용된다. `team_id`는 서버가 채널 기준으로 결정하므로 클라이언트 값은 무시된다.

---

# 3. Lookup dialog elements

## 기본 정보
- **기능**: interactive dialog의 동적 요소(dynamic elements)를 조회한다.
- **Endpoint**: `POST /api/v4/actions/dialogs/lookup`
- **인증**: Bearer Token 필요
- **권한**: 별도의 이름있는 권한 불요 (Mattermost 클라이언트가 사용하는 일반 사용자 대상 endpoint)

## 설명
Mattermost 클라이언트가 dialog의 동적 요소를 조회(lookup)하는 데 사용하는 API이다. 지정한 URL의 통합으로 lookup 요청을 전달하고 선택지 목록을 돌려받는다. 최소 서버 버전은 11.0이다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| url | string | Yes | lookup 요청을 전송할 URL |
| channel_id | string | Yes | 사용자가 lookup을 수행하는 채널의 ID |
| team_id | string | No | 선택 사항. 서버가 채널로부터 팀을 결정하므로 클라이언트 제공 값은 무시됨. DM/GM 채널은 팀이 없어 빈 값 |
| submission | object | Yes | 요소 이름을 키, 입력 값을 값으로 하는 문자열 맵 |
| callback_id | string | No | dialog가 열릴 때 전송된 Callback ID |
| state | string | No | dialog가 열릴 때 전송된 상태 값 |

```json
{
  "url": "string",
  "channel_id": "string",
  "submission": {},
  "callback_id": "string",
  "state": "string"
}
```

## Response

### 200 - Dialog lookup successful
| 필드 | 타입 | 설명 |
|---|---|---|
| options | array | lookup에서 반환된 선택지 목록 |
| options[].text | string | 선택지의 표시 텍스트 |
| options[].value | string | 선택지의 값 |

```json
{
  "options": [
    {
      "text": "string",
      "value": "string"
    }
  ]
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 429 | 업스트림 통합의 rate limit (원래 상태 코드 유지) |
| 502 | 업스트림 통합의 5xx 오류 (503 제외, Bad Gateway로 표면화) |
| 503 | 업스트림 통합 사용 불가 (원래 상태 코드 유지) |

## 주의 사항
최소 서버 버전 11.0 이상에서만 사용 가능하다.

---

# 4. Execute a dialog action button

## 기본 정보
- **기능**: interactive dialog 내의 `action_button` 요소 클릭을 처리한다.
- **Endpoint**: `POST /api/v4/actions/dialogs/execute`
- **인증**: Bearer Token 필요
- **권한**: 별도의 이름있는 권한 불요 (Mattermost 클라이언트가 사용하는 일반 사용자 대상 endpoint)

## 설명
사용자가 interactive dialog 안의 `action_button` 요소를 클릭했을 때 Mattermost 클라이언트가 사용하는 API이다. 서버는 새 trigger ID를 생성하여 버튼의 context와 함께 통합 URL로 전달하며, 통합은 이 trigger ID로 자식(스택형) dialog를 열 수 있다. 요청은 항상 서버 측에서 처리된다. 최소 서버 버전은 11.10이다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| url | string | Yes | 액션 페이로드를 전송할 action button URL. 유효한 lookup URL이어야 함 |
| context | object | No | action button에 설정된 context 값의 문자열 맵. 통합으로 전달됨 |
| channel_id | string | Yes | 사용자가 action button을 클릭한 채널의 ID |
| team_id | string | No | 선택 사항. 서버가 채널로부터 팀을 결정하므로 클라이언트 제공 값은 무시됨. DM/GM 채널은 팀이 없어 빈 값 |

```json
{
  "url": "string",
  "context": {},
  "channel_id": "string"
}
```

## Response

### 200 - Dialog action executed successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 요청 상태 ("OK") |
| trigger_id | string | 통합이 자식 dialog를 여는 데 사용할 수 있는 새 trigger ID |

```json
{
  "status": "OK",
  "trigger_id": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

## 주의 사항
클라이언트는 동시에 열리는 interactive dialog를 최대 3개로 제한하므로, 결과 `open_dialog` 이벤트가 이 제한을 초과하면 추가 dialog 렌더링은 조용히 생략된다. 최소 서버 버전 11.10 이상에서만 사용 가능하다.

---
