# 16-Delete a custom header [DEL]

`DELETE /api/v4/hooks/{hook_id}/custom_headers/{key}`

Deletes a custom header from a specified webhook.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `hook_id` | `integer` | `path` | Yes | The ID of the hook |
| `key` | `string` | `path` | Yes | The name of the custom header |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

