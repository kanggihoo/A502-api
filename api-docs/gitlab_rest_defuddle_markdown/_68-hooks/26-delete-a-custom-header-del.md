# 26-Delete a custom header [DEL]

`DELETE /api/v4/projects/{id}/hooks/{hook_id}/custom_headers/{key}`

Deletes a custom header from a specified webhook.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `hook_id` | `integer` | `path` | Yes | The ID of the hook |
| `key` | `string` | `path` | Yes | The name of the custom header |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

