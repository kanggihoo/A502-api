# 19-Reset the runner registration token for a group [POST]

`POST /api/v4/groups/{id}/runners/reset_registration_token`

Resets the runner registration token for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "token": string,
  "token_expires_at": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Group Not Found

