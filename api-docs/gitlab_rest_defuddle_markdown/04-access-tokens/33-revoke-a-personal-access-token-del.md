# 33-Revoke a personal access token [DEL]

`DELETE /api/v4/personal_access_tokens/{id}`

Revokes a specified personal access token. Administrators can revoke tokens for any user. Non-administrators can only revoke their own tokens.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes |  |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

