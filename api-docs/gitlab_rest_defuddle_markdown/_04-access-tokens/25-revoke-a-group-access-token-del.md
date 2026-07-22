# 25-Revoke a group access token [DEL]

`DELETE /api/v4/groups/{id}/access_tokens/{token_id}`

Revokes a specified group access token.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The group ID |
| `token_id` | `string` | `path` | Yes | The ID of the token |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not found

