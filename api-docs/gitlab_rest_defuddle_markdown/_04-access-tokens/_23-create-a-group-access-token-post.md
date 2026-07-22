# 23-Create a group access token [POST]

**응, 맞음! 상위 그룹 토큰 1개로 하위 모든 프로젝트 접근 가능.**


### 이유 (GitLab 권한 상속 규칙)
- GitLab 권한 구조는 **상위 ➔ 하위 상속(Inheritance)** 구조.
- Group Access Token 발급 시 (`Developer` 또는 `Maintainer` 부여) ➔ **그 그룹 속한 모든 하위 프로젝트 및 서브 그룹에 동일 권한 자동 적용**.

---

### SSAFY 워크스페이스 구축 시 엄청난 이점
- 팀 프로젝트 저장소가 백엔드(`backend`), 프론트엔드(`frontend`), AI(`ai`) 등 여러 개로 나눠져 있어도:
  - 프로젝트마다 토큰 3개 만들 필요 없음 ❌
  - **상위 팀 그룹 토큰 1개만 생성 ➔ 전체 레포 자동 연결 ⭕**

---

### 단, 조건
- 토큰 생성 요청자(팀장)가 해당 그룹의 **Owner (또는 Maintainer)** 권한 보유 필수.


`POST /api/v4/groups/{id}/access_tokens`

Creates a group access token for a specified group. You cannot create a token with an access level greater than your account. For example, a user with the Maintainer role cannot create a group access token with the Owner role. You must use a personal access token with this endpoint. You cannot authenticate with a group access token.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The group ID |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the access token
  "description": string, // The description of the access token
  "expires_at": string, // The expiration date of the token. If 'Require personal access token expiry' is enabled, you must provide a valid value, if not, the token will never expire.
  "scopes": [
    string
  ] (required), // The permissions of the token
  "access_level": enum(10 | 15 | 20 | 25 | 30 | 40 | 50), // The access level of the token in the group
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

