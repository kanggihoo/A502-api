# 21-Rotate a project access token [POST]

`POST /api/v4/projects/{id}/access_tokens/{token_id}/rotate`

Rotates a project access token. This immediately revokes the previous token and creates a token. Generally, this endpoint rotates a specific project access token by authenticating with a personal access token. You can also use a project access token to rotate itself. If you attempt to use this endpoint to rotate a token that was previously revoked, any active tokens from the same token family are revoked. This feature was introduced in GitLab 16.0.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `token_id` | `string` | `path` | Yes | The ID of the token |

### Request Body (application/json)

```json
{
  "expires_at": string, // The expiration date of the token
}
```
### Responses

#### 200 - OK

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

