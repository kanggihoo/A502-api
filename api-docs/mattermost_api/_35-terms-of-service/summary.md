# 1. Records user action when they accept or decline custom terms of service

## 기본 정보
- **기능**: 사용자가 커스텀 이용약관(terms of service)에 동의하거나 거부한 행위를 기록한다.
- **Endpoint**: `POST /api/v4/users/{user_id}/terms_of_service`
- **인증**: 로그인 필요
- **권한**: 본인(user_id) 계정에 대해서만 가능 (별도의 이름있는 권한 불요)

## 설명
사용자가 커스텀 이용약관에 동의하거나 거부한 행위를 audit table에 기록하는 API이다. 동의한 경우 사용자의 마지막으로 동의한 이용약관 ID를 갱신한다. 본인(user_id)으로 로그인한 경우에만 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| serviceTermsId | string | Yes | 사용자가 대상으로 하는 이용약관 ID |
| accepted | string | Yes | 동의(true) 또는 거부(false) 여부 |

```json
{
  "serviceTermsId": "string",
  "accepted": "true"
}
```

## Response

### 200 - Terms of service action recorded successfully
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
| 401 | 인증되지 않음 |
| 403 | 권한 없음 (본인이 아닌 경우) |

## 주의 사항
본인(user_id)에 대해서만 호출 가능하다.

---

# 2. Fetches user's latest terms of service action if the latest action was for acceptance

## 기본 정보
- **기능**: 사용자의 최신 이용약관 동의/거부 행위 중, 마지막 행위가 동의였을 경우 그 정보를 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/terms_of_service`
- **인증**: 로그인 필요
- **권한**: 본인(user_id) 계정에 대해서만 가능 (별도의 이름있는 권한 불요)

## 설명
사용자의 가장 최근 이용약관 관련 행위가 "동의"였을 경우, 그 동의 행위에 대한 정보를 조회하는 API이다. v6.0에서 deprecated 예정이다. 본인(user_id)으로 로그인한 경우에만 호출할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 GUID |

## Response

### 200 - User's accepted terms of service action
| 필드 | 타입 | 설명 |
|---|---|---|
| user_id | string | 이 이용약관 행위를 수행한 사용자의 고유 식별자 |
| terms_of_service_id | string | 행위 대상이 된 이용약관의 고유 식별자 |
| create_at | integer | 행위가 수행된 시각 (밀리초) |

```json
{
  "user_id": "string",
  "terms_of_service_id": "string",
  "create_at": 0
}
```

### 404 - User hasn't performed an action or the latest action was a rejection
| 필드 | 타입 | 설명 |
|---|---|---|
| status_code | integer | 상태 코드 |
| id | string | 에러 ID |
| message | string | 에러 메시지 |
| request_id | string | 요청 ID |

```json
{
  "status_code": 404,
  "id": "string",
  "message": "string",
  "request_id": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 행위 기록이 없거나 최신 행위가 거부였음 |

## 주의 사항
본인(user_id)에 대해서만 조회 가능하며, v6.0에서 deprecated 예정이다.

---

# 3. Get latest terms of service

## 기본 정보
- **기능**: 서버에 등록된 최신 이용약관을 조회한다.
- **Endpoint**: `GET /api/v4/terms_of_service`
- **인증**: 로그인 필요
- **권한**: 인증만 필요 (별도 권한 불요)

## 설명
서버에 등록된 가장 최신의 이용약관 내용을 조회하는 API이다. 인증된 사용자라면 누구나 호출할 수 있다.

## Response

### 200 - Terms of service fetched successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 이용약관의 고유 식별자 |
| create_at | integer | 이용약관이 생성된 시각 |
| user_id | string | 이 이용약관을 생성한 사용자의 고유 식별자 |
| text | string | 이용약관 본문 (Markdown 지원) |

```json
{
  "id": "string",
  "create_at": 0,
  "user_id": "string",
  "text": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |

## 주의 사항
없음.

---

## 제외된 API
- **04-Creates a new terms of service**: `manage_system` 권한이 필요하나 부여된 권한 목록에 없어 제외됨.
