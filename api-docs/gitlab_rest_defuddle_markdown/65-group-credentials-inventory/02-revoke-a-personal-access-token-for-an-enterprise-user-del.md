# 02-Revoke a personal access token for an enterprise user [DEL]

`DELETE /api/v4/groups/{id}/manage/personal_access_tokens/{pat_id}`

Revokes a specified personal access token for an enterprise user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID or URL-encoded path of the group |
| `pat_id` | `any` | `path` | Yes |  |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

