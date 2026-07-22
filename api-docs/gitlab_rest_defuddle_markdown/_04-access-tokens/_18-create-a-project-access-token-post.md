# 18-Create a project access token [POST]

#### 시나리오 및 활용법
1. 팀장(Maintainer)이 우리 서비스에 **OAuth2 로그인/승인**.
2. 백엔드가 팀장의 OAuth2 토큰으로 `POST /projects/{id}/access_tokens` API 호출.
3. **우리 서비스 전용 봇 토큰(Project Access Token)을 자동으로 발급받아 DB에 저장**.
4. **이후 효과**: 팀장의 개인 OAuth2 토큰 만료 여부와 상관없이, **발급받은 봇 토큰으로 24시간 자동화/알림/리뷰/연동 동작 가능**.

---

### 부가적으로 쓸 만한 API
- **`23-create-a-group-access-token-post`**: 프로젝트가 아닌 그룹 단위 봇 토큰 생성 시.
- **`21-rotate-a-project-access-token-post`**: 봇 토큰 만료 전 **자동 토큰 갱신(Rotation)** 구현 시.

`POST /api/v4/projects/{id}/access_tokens`

Creates a project access token for a specified project. You cannot create a token with an access level greater than your account. For example, a user with the Maintainer role cannot create a project access token with the Owner role. You must use a personal access token with this endpoint. You cannot authenticate with a project access token.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the access token
  "description": string, // The description of the access token
  "expires_at": string, // The expiration date of the token. If 'Require personal access token expiry' is enabled, you must provide a valid value, if not, the token will never expire.
  "scopes": [
    string
  ] (required), // The permissions of the token
  "access_level": enum(10 | 15 | 20 | 25 | 30 | 40 | 50), // The access level of the token in the project
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "revoked": boolean,
  "created_at": string,
  "description": string,
  "scopes": [
    any
  ],
  "user_id": integer,
  "last_used_at": string,
  "active": boolean,
  "granular": boolean,
  "expires_at": string,
  "last_used_ips": [
    string
  ], // The five most recent unique IP addresses that have authenticated with this token. When the limit is reached, the oldest IP address is removed. The list updates once per minute per token.
  "granular_scopes": [
    {
      "access": string,
      "permissions": [
        any
      ],
      "project_id": integer,
      "group_id": integer,
    }
  ],
  "access_level": integer,
  "resource_type": string,
  "resource_id": integer,
  "token": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

