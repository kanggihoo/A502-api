# 1. Register OAuth app

## 기본 정보
- **기능**: OAuth 2.0 클라이언트 애플리케이션을 Mattermost에 등록한다.
- **Endpoint**: `POST /api/v4/oauth/apps`
- **인증**: Bearer Token 필요
- **권한**: `manage_oauth`

## 설명
Mattermost를 서비스 제공자로 하는 OAuth 2.0 클라이언트 애플리케이션을 등록한다. 애플리케이션 이름, 설명, 콜백 URL, 홈페이지 등을 지정해야 하며, `is_public`을 `true`로 설정하면 클라이언트 시크릿이 없는 퍼블릭 클라이언트(PKCE 필수)로 생성된다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| name | string | Yes | 클라이언트 애플리케이션 이름 |
| description | string | Yes | 애플리케이션에 대한 짧은 설명 |
| icon_url | string | No | 애플리케이션과 함께 표시할 아이콘 URL |
| callback_urls | string[] | Yes | 애플리케이션의 콜백 URL 목록 |
| homepage | string | Yes | 애플리케이션 웹사이트 링크 |
| is_trusted | boolean | No | `true`로 설정하면 사용자에게 권한 승인을 묻지 않음 |
| is_public | boolean | No | `true`로 설정하면 클라이언트 시크릿이 없는 퍼블릭 클라이언트 생성 (PKCE 필수) |

```json
{
  "name": "My App",
  "description": "An example OAuth app",
  "callback_urls": ["https://example.com/callback"],
  "homepage": "https://example.com",
  "is_trusted": false,
  "is_public": false
}
```

## Response

### 201 - App registration successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 애플리케이션의 클라이언트 id |
| client_secret | string | 애플리케이션의 클라이언트 시크릿 |
| name | string | 클라이언트 애플리케이션 이름 |
| description | string | 애플리케이션에 대한 짧은 설명 |
| icon_url | string | 애플리케이션과 함께 표시할 아이콘 URL |
| callback_urls | string[] | 애플리케이션의 콜백 URL 목록 |
| homepage | string | 애플리케이션 웹사이트 링크 |
| is_trusted | boolean | 사용자에게 권한 승인을 묻지 않는지 여부 |
| create_at | integer | 애플리케이션 등록 시각 |
| update_at | integer | 애플리케이션 마지막 수정 시각 |

```json
{
  "id": "string",
  "client_secret": "string",
  "name": "string",
  "description": "string",
  "icon_url": "string",
  "callback_urls": ["string"],
  "homepage": "string",
  "is_trusted": false,
  "create_at": 0,
  "update_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 2. Get OAuth apps

## 기본 정보
- **기능**: Mattermost에 등록된 OAuth 2.0 클라이언트 애플리케이션 목록을 페이지 단위로 조회한다.
- **Endpoint**: `GET /api/v4/oauth/apps`
- **인증**: Bearer Token 필요
- **권한**: `manage_oauth` (로그인한 사용자가 등록한 앱만 조회) 또는 `manage_system_wide_oauth` (생성자와 무관하게 모든 앱 조회)

## 설명
등록된 OAuth 2.0 클라이언트 애플리케이션 목록을 반환한다. `manage_oauth` 권한만 있는 경우 로그인한 사용자 본인이 등록한 앱만 반환되며, `manage_system_wide_oauth` 권한이 있으면 생성자에 관계없이 모든 앱이 반환된다. `page`, `per_page` 쿼리 파라미터로 페이지네이션이 가능하다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| page | integer | No | 선택할 페이지 |
| per_page | integer | No | 페이지당 앱 개수 |

## Response

### 200 - OAuthApp list retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 애플리케이션의 클라이언트 id |
| client_secret | string | 애플리케이션의 클라이언트 시크릿 |
| name | string | 클라이언트 애플리케이션 이름 |
| description | string | 애플리케이션에 대한 짧은 설명 |
| icon_url | string | 애플리케이션과 함께 표시할 아이콘 URL |
| callback_urls | string[] | 애플리케이션의 콜백 URL 목록 |
| homepage | string | 애플리케이션 웹사이트 링크 |
| is_trusted | boolean | 사용자에게 권한 승인을 묻지 않는지 여부 |
| create_at | integer | 애플리케이션 등록 시각 |
| update_at | integer | 애플리케이션 마지막 수정 시각 |

```json
[
  {
    "id": "string",
    "client_secret": "string",
    "name": "string",
    "description": "string",
    "icon_url": "string",
    "callback_urls": ["string"],
    "homepage": "string",
    "is_trusted": false,
    "create_at": 0,
    "update_at": 0
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 3. Get an OAuth app

## 기본 정보
- **기능**: Mattermost에 등록된 특정 OAuth 2.0 클라이언트 애플리케이션 정보를 조회한다.
- **Endpoint**: `GET /api/v4/oauth/apps/{app_id}`
- **인증**: Bearer Token 필요
- **권한**: 앱 생성자인 경우 `manage_oauth`, 그 외에는 `manage_system_wide_oauth` 필요

## 설명
지정한 `app_id`에 해당하는 OAuth 2.0 클라이언트 애플리케이션 정보를 조회한다. 요청자가 해당 앱의 생성자인 경우 `manage_oauth` 권한만으로 조회할 수 있으며, 생성자가 아닌 경우에는 `manage_system_wide_oauth` 권한이 필요하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| app_id | string | Yes | 애플리케이션 클라이언트 id |

## Response

### 200 - App retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 애플리케이션의 클라이언트 id |
| client_secret | string | 애플리케이션의 클라이언트 시크릿 |
| name | string | 클라이언트 애플리케이션 이름 |
| description | string | 애플리케이션에 대한 짧은 설명 |
| icon_url | string | 애플리케이션과 함께 표시할 아이콘 URL |
| callback_urls | string[] | 애플리케이션의 콜백 URL 목록 |
| homepage | string | 애플리케이션 웹사이트 링크 |
| is_trusted | boolean | 사용자에게 권한 승인을 묻지 않는지 여부 |
| create_at | integer | 애플리케이션 등록 시각 |
| update_at | integer | 애플리케이션 마지막 수정 시각 |

```json
{
  "id": "string",
  "client_secret": "string",
  "name": "string",
  "description": "string",
  "icon_url": "string",
  "callback_urls": ["string"],
  "homepage": "string",
  "is_trusted": false,
  "create_at": 0,
  "update_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 4. Update an OAuth app

## 기본 정보
- **기능**: OAuth struct를 기반으로 OAuth 2.0 클라이언트 애플리케이션을 수정한다.
- **Endpoint**: `PUT /api/v4/oauth/apps/{app_id}`
- **인증**: Bearer Token 필요
- **권한**: 앱 생성자인 경우 `manage_oauth`, 그 외에는 `manage_system_wide_oauth` 필요

## 설명
지정한 `app_id`에 해당하는 OAuth 2.0 클라이언트 애플리케이션 정보를 수정한다. 요청자가 해당 앱의 생성자인 경우 `manage_oauth` 권한만으로 수정할 수 있으며, 생성자가 아닌 경우에는 `manage_system_wide_oauth` 권한이 필요하다. `is_trusted` 값을 제공하지 않으면 `false`로 설정된다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| app_id | string | Yes | 애플리케이션 클라이언트 id |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 클라이언트 애플리케이션의 id |
| name | string | Yes | 클라이언트 애플리케이션 이름 |
| description | string | Yes | 애플리케이션에 대한 짧은 설명 |
| icon_url | string | No | 애플리케이션과 함께 표시할 아이콘 URL |
| callback_urls | string[] | Yes | 애플리케이션의 콜백 URL 목록 |
| homepage | string | Yes | 애플리케이션 웹사이트 링크 |
| is_trusted | boolean | No | `true`로 설정하면 사용자에게 권한 승인을 묻지 않음. 값이 없으면 `false`로 설정됨 |

```json
{
  "id": "appid123",
  "name": "My App",
  "description": "An example OAuth app",
  "callback_urls": ["https://example.com/callback"],
  "homepage": "https://example.com",
  "is_trusted": false
}
```

## Response

### 200 - App update successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 애플리케이션의 클라이언트 id |
| client_secret | string | 애플리케이션의 클라이언트 시크릿 |
| name | string | 클라이언트 애플리케이션 이름 |
| description | string | 애플리케이션에 대한 짧은 설명 |
| icon_url | string | 애플리케이션과 함께 표시할 아이콘 URL |
| callback_urls | string[] | 애플리케이션의 콜백 URL 목록 |
| homepage | string | 애플리케이션 웹사이트 링크 |
| is_trusted | boolean | 사용자에게 권한 승인을 묻지 않는지 여부 |
| create_at | integer | 애플리케이션 등록 시각 |
| update_at | integer | 애플리케이션 마지막 수정 시각 |

```json
{
  "id": "string",
  "client_secret": "string",
  "name": "string",
  "description": "string",
  "icon_url": "string",
  "callback_urls": ["string"],
  "homepage": "string",
  "is_trusted": false,
  "create_at": 0,
  "update_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 5. Delete an OAuth app

## 기본 정보
- **기능**: OAuth 2.0 클라이언트 애플리케이션을 삭제하고 등록을 해제한다.
- **Endpoint**: `DELETE /api/v4/oauth/apps/{app_id}`
- **인증**: Bearer Token 필요
- **권한**: 앱 생성자인 경우 `manage_oauth`, 그 외에는 `manage_system_wide_oauth` 필요

## 설명
지정한 `app_id`에 해당하는 OAuth 2.0 클라이언트 애플리케이션을 삭제하고 등록을 해제한다. 요청자가 해당 앱의 생성자인 경우 `manage_oauth` 권한만으로 삭제할 수 있으며, 생성자가 아닌 경우에는 `manage_system_wide_oauth` 권한이 필요하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| app_id | string | Yes | 애플리케이션 클라이언트 id |

## Response

### 200 - App deletion successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 요청이 성공하고 반환할 다른 내용이 없으면 "ok"를 포함 |

```json
{
  "status": "ok"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 6. Regenerate OAuth app secret

## 기본 정보
- **기능**: Mattermost에 등록된 OAuth 2.0 클라이언트 애플리케이션의 클라이언트 시크릿을 재생성한다.
- **Endpoint**: `POST /api/v4/oauth/apps/{app_id}/regen_secret`
- **인증**: Bearer Token 필요
- **권한**: 앱 생성자인 경우 `manage_oauth`, 그 외에는 `manage_system_wide_oauth` 필요

## 설명
지정한 `app_id`에 해당하는 OAuth 2.0 클라이언트 애플리케이션의 클라이언트 시크릿을 재생성한다. 요청자가 해당 앱의 생성자인 경우 `manage_oauth` 권한만으로 재생성할 수 있으며, 생성자가 아닌 경우에는 `manage_system_wide_oauth` 권한이 필요하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| app_id | string | Yes | 애플리케이션 클라이언트 id |

## Response

### 200 - Secret regeneration successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 애플리케이션의 클라이언트 id |
| client_secret | string | 애플리케이션의 클라이언트 시크릿 |
| name | string | 클라이언트 애플리케이션 이름 |
| description | string | 애플리케이션에 대한 짧은 설명 |
| icon_url | string | 애플리케이션과 함께 표시할 아이콘 URL |
| callback_urls | string[] | 애플리케이션의 콜백 URL 목록 |
| homepage | string | 애플리케이션 웹사이트 링크 |
| is_trusted | boolean | 사용자에게 권한 승인을 묻지 않는지 여부 |
| create_at | integer | 애플리케이션 등록 시각 |
| update_at | integer | 애플리케이션 마지막 수정 시각 |

```json
{
  "id": "string",
  "client_secret": "string",
  "name": "string",
  "description": "string",
  "icon_url": "string",
  "callback_urls": ["string"],
  "homepage": "string",
  "is_trusted": false,
  "create_at": 0,
  "update_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 7. Get info on an OAuth app

## 기본 정보
- **기능**: Mattermost에 등록된 OAuth 2.0 클라이언트 애플리케이션의 공개 정보를 조회한다.
- **Endpoint**: `GET /api/v4/oauth/apps/{app_id}/info`
- **인증**: 인증 필요 (Bearer Token)
- **권한**: 권한 불요 (인증된 사용자면 충분)

## 설명
지정한 `app_id`에 해당하는 OAuth 2.0 클라이언트 애플리케이션의 공개 정보를 조회한다. 응답에서 애플리케이션의 클라이언트 시크릿은 빈 값으로 처리(blank out)된다. 인증된 사용자라면 별도의 이름있는 권한 없이 조회할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| app_id | string | Yes | 애플리케이션 클라이언트 id |

## Response

### 200 - App retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 애플리케이션의 클라이언트 id |
| client_secret | string | 애플리케이션의 클라이언트 시크릿 (빈 값으로 처리됨) |
| name | string | 클라이언트 애플리케이션 이름 |
| description | string | 애플리케이션에 대한 짧은 설명 |
| icon_url | string | 애플리케이션과 함께 표시할 아이콘 URL |
| callback_urls | string[] | 애플리케이션의 콜백 URL 목록 |
| homepage | string | 애플리케이션 웹사이트 링크 |
| is_trusted | boolean | 사용자에게 권한 승인을 묻지 않는지 여부 |
| create_at | integer | 애플리케이션 등록 시각 |
| update_at | integer | 애플리케이션 마지막 수정 시각 |

```json
{
  "id": "string",
  "client_secret": "string",
  "name": "string",
  "description": "string",
  "icon_url": "string",
  "callback_urls": ["string"],
  "homepage": "string",
  "is_trusted": false,
  "create_at": 0,
  "update_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 8. Get OAuth 2.0 Authorization Server Metadata

## 기본 정보
- **기능**: RFC 8414에 정의된 OAuth 2.0 Authorization Server Metadata를 조회한다.
- **Endpoint**: `GET /.well-known/oauth-authorization-server`
- **인증**: 인증 불요
- **권한**: 권한 불요 (공개적으로 접근 가능한 엔드포인트)

## 설명
지원하는 엔드포인트, grant type, response type, 인증 방식 등 OAuth 2.0 인가 서버의 설정에 대한 메타데이터를 제공한다. RFC 8414(OAuth 2.0 Authorization Server Metadata)를 구현하며, 메타데이터는 서버 설정에 따라 동적으로 생성된다. 이 엔드포인트가 사용 가능하려면 시스템 설정에서 OAuth Service Provider가 활성화되어 있어야 한다.

## Response

### 200 - Metadata retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| issuer | string | 인가 서버의 발급자 식별자 (https 스킴을 사용하는 URL) |
| authorization_endpoint | string | 인가 서버의 authorization 엔드포인트 URL |
| token_endpoint | string | 인가 서버의 token 엔드포인트 URL |
| response_types_supported | string[] | 인가 서버가 지원하는 OAuth 2.0 response_type 값 목록 |
| registration_endpoint | string | 인가 서버의 OAuth 2.0 Dynamic Client Registration 엔드포인트 URL |
| scopes_supported | string[] | 인가 서버가 지원하는 OAuth 2.0 scope 값 목록 |
| grant_types_supported | string[] | 인가 서버가 지원하는 OAuth 2.0 grant type 값 목록 |
| token_endpoint_auth_methods_supported | string[] | token 엔드포인트가 지원하는 클라이언트 인증 방식 목록 |
| code_challenge_methods_supported | string[] | 인가 서버가 지원하는 PKCE code challenge 방식 목록 |

```json
{
  "issuer": "https://example.com",
  "authorization_endpoint": "https://example.com/oauth/authorize",
  "token_endpoint": "https://example.com/oauth/access_token",
  "response_types_supported": ["code"],
  "registration_endpoint": "https://example.com/api/v4/oauth/apps/register",
  "scopes_supported": ["string"],
  "grant_types_supported": ["authorization_code"],
  "token_endpoint_auth_methods_supported": ["client_secret_post"],
  "code_challenge_methods_supported": ["S256"]
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 501 | OAuth Service Provider is not enabled |

```json
{
  "status_code": 501,
  "id": "string",
  "message": "string",
  "request_id": "string"
}
```

## 주의 사항
RFC 8414(OAuth 2.0 Authorization Server Metadata)를 구현하며, 메타데이터는 서버 설정에 따라 동적으로 생성됨. OAuth Service Provider가 시스템 설정에서 활성화되어 있어야 사용 가능함.

---

# 9. Register OAuth client using Dynamic Client Registration

## 기본 정보
- **기능**: Dynamic Client Registration(DCR)을 이용해 OAuth 2.0 클라이언트 애플리케이션을 등록한다.
- **Endpoint**: `POST /api/v4/oauth/apps/register`
- **인증**: 인증 불요
- **권한**: 권한 불요 (인증되지 않은 클라이언트도 호출 가능)

## 설명
RFC 7591에 정의된 OAuth 2.0 Dynamic Client Registration Protocol을 구현하며, 관리자 승인 없이 클라이언트를 등록할 수 있다. `client_uri` 필드가 제공되면 OAuth 앱의 homepage로 매핑되며, 이 방식으로 등록된 모든 클라이언트는 동적으로 등록된 것으로 표시된다. 시스템 설정에서 Dynamic Client Registration이 활성화되어 있어야 한다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| redirect_uris | string[] | Yes | authorization code, implicit flow 등에서 사용할 리다이렉션 URI 배열 |
| client_name | string | No | 인가 과정에서 최종 사용자에게 표시할 클라이언트의 사람이 읽을 수 있는 이름 |
| client_uri | string | No | 클라이언트에 대한 정보를 제공하는 웹페이지 URL |

```json
{
  "redirect_uris": ["https://example.com/callback"],
  "client_name": "My App",
  "client_uri": "https://example.com"
}
```

## Response

### 201 - Client registration successful
| 필드 | 타입 | 설명 |
|---|---|---|
| client_id | string | OAuth 2.0 클라이언트 식별자 |
| client_secret | string | OAuth 2.0 클라이언트 시크릿 |
| redirect_uris | string[] | 등록된 리다이렉션 URI 배열 |
| token_endpoint_auth_method | enum("client_secret_post"\|"none") | token 엔드포인트에 대해 요청된 인증 방식 |
| grant_types | string[] | 클라이언트가 token 엔드포인트에서 사용할 수 있는 OAuth 2.0 grant type 배열 |
| response_types | string[] | 클라이언트가 authorization 엔드포인트에서 사용할 수 있는 OAuth 2.0 response type 배열 |
| scope | string | 클라이언트가 액세스 토큰 요청 시 사용할 수 있는 scope 값 목록 (공백으로 구분) |
| client_name | string | 인가 과정에서 최종 사용자에게 표시할 클라이언트 이름 |
| client_uri | string | 클라이언트에 대한 정보를 제공하는 웹페이지 URL |

```json
{
  "client_id": "string",
  "client_secret": "string",
  "redirect_uris": ["string"],
  "token_endpoint_auth_method": "client_secret_post",
  "grant_types": ["authorization_code"],
  "response_types": ["code"],
  "scope": "string",
  "client_name": "string",
  "client_uri": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 501 | 명시되지 않음 |

## 주의 사항
RFC 7591(OAuth 2.0 Dynamic Client Registration Protocol)을 따르며, 관리자 승인 없이 등록 가능. 이 방식으로 등록된 모든 클라이언트는 동적으로 등록된 것으로 표시됨. 시스템 설정에서 Dynamic Client Registration이 활성화되어 있어야 함.

---

# 10. Get authorized OAuth apps

## 기본 정보
- **기능**: 특정 사용자의 계정에 접근 권한이 부여된 OAuth 2.0 클라이언트 애플리케이션 목록을 페이지 단위로 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/oauth/apps/authorized`
- **인증**: Bearer Token 필요
- **권한**: 본인 계정 조회 시 별도 권한 불요 (본인 인증만 필요), 타인 계정 조회 시 `edit_other_users` 권한 필요

## 설명
지정한 `user_id` 사용자의 계정 접근이 승인된 OAuth 2.0 클라이언트 애플리케이션 목록을 조회한다. 요청자가 해당 사용자 본인으로 인증된 경우 별도의 이름있는 권한 없이 조회할 수 있으며, 본인이 아닌 경우에는 `edit_other_users` 권한이 필요하다. `page`, `per_page` 쿼리 파라미터로 페이지네이션이 가능하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 GUID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| page | integer | No | 선택할 페이지 |
| per_page | integer | No | 페이지당 앱 개수 |

## Response

### 200 - OAuthApp list retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 애플리케이션의 클라이언트 id |
| client_secret | string | 애플리케이션의 클라이언트 시크릿 |
| name | string | 클라이언트 애플리케이션 이름 |
| description | string | 애플리케이션에 대한 짧은 설명 |
| icon_url | string | 애플리케이션과 함께 표시할 아이콘 URL |
| callback_urls | string[] | 애플리케이션의 콜백 URL 목록 |
| homepage | string | 애플리케이션 웹사이트 링크 |
| is_trusted | boolean | 사용자에게 권한 승인을 묻지 않는지 여부 |
| create_at | integer | 애플리케이션 등록 시각 |
| update_at | integer | 애플리케이션 마지막 수정 시각 |

```json
[
  {
    "id": "string",
    "client_secret": "string",
    "name": "string",
    "description": "string",
    "icon_url": "string",
    "callback_urls": ["string"],
    "homepage": "string",
    "is_trusted": false,
    "create_at": 0,
    "update_at": 0
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 501 | 명시되지 않음 |
