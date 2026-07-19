# 18-Create a project access token [POST]

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

