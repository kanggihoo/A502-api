# 05-Create a personal access token for a user [POST]

`POST /api/v4/users/{user_id}/personal_access_tokens`

Creates a personal access token for a user. Token values are included with the response, but cannot be retrieved later. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `integer` | `path` | Yes | The ID of the user |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the access token
  "description": string, // The description of the access token
  "expires_at": string, // Expiration date of the access token in ISO format (YYYY-MM-DD). If undefined, the date is set to the maximum allowable lifetime limit.
  "scopes": [
    string
  ] (required), // The array of scopes of the personal access token
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

