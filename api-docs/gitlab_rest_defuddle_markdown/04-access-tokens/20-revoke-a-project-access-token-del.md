# 20-Revoke a project access token [DEL]

`DELETE /api/v4/projects/{id}/access_tokens/{token_id}`

Revokes a specified project access token.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `token_id` | `string` | `path` | Yes | The ID of the token |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not found

