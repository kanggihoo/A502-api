# 05-Revoke a group or project access token for a group [DEL]

`DELETE /api/v4/groups/{id}/manage/resource_access_tokens/{prat_id}`

Revokes a specified group or project access token associated with a top-level group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `expires_at` | `string` | `query` | No | The expiration date of the token |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `prat_id` | `any` | `path` | Yes |  |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

