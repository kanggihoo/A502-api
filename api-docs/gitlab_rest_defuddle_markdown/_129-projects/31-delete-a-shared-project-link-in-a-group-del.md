# 31-Delete a shared project link in a group [DEL]

`DELETE /api/v4/projects/{id}/share/{group_id}`

Deletes a shared project link in a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `group_id` | `integer` | `path` | Yes | The ID of the group |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 404 - Not found

