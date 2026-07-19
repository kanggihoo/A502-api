# 03-Rotate a personal access token for an enterprise user [POST]

`POST /api/v4/groups/{id}/manage/personal_access_tokens/{pat_id}/rotate`

Rotates a specified personal access token for an enterprise user associated with the top-level group. This revokes the previous token and creates a token that expires after one week.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID or URL-encoded path of the group |
| `pat_id` | `any` | `path` | Yes |  |

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

