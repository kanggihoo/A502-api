# 10-Rotate a personal access token for a project service account [POST]

`POST /api/v4/projects/{id}/service_accounts/{user_id}/personal_access_tokens/{token_id}/rotate`

Rotates a specified personal access token for a project service account. This revokes the existing token and creates a token with the same name, description, and scopes.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `user_id` | `integer` | `path` | Yes | The ID of the service account |
| `token_id` | `any` | `path` | Yes |  |

### Request Body (application/json)

```json
{
  "expires_at": string, // The expiration date of the token
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
  "token": string,
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
}
```

#### 400 - Bad Request

#### 404 - Not Found

