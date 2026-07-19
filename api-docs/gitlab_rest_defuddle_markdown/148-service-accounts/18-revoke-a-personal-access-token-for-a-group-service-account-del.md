# 18-Revoke a personal access token for a group service account [DEL]

`DELETE /api/v4/groups/{id}/service_accounts/{user_id}/personal_access_tokens/{token_id}`

Revokes a specified personal access token for a group service account.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `user_id` | `integer` | `path` | Yes | The ID of the service account |
| `token_id` | `any` | `path` | Yes |  |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

