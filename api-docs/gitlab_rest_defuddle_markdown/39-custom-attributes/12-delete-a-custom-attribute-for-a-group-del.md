# 12-Delete a custom attribute for a group [DEL]

`DELETE /api/v4/groups/{id}/custom_attributes/{key}`

Deletes a specified custom attribute for a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | `string` | `path` | Yes | The key of the custom attribute |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

