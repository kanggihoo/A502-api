# 04-Revoke an impersonation token [DEL]

`DELETE /api/v4/users/{user_id}/impersonation_tokens/{impersonation_token_id}`

Revokes an impersonation token for a specified user. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `integer` | `path` | Yes | The ID of the user |
| `impersonation_token_id` | `integer` | `path` | Yes | The ID of the impersonation token |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

