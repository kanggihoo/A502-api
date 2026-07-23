# 24-Delete a URL variable [DEL]

`DELETE /api/v4/projects/{id}/hooks/{hook_id}/url_variables/{key}`

Deletes a URL variable from a specified webhook.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `hook_id` | `integer` | `path` | Yes | The ID of the hook |
| `key` | `string` | `path` | Yes | The key of the variable |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

