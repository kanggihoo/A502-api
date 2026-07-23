# 38-Remove a group from a group [DEL]

`DELETE /api/v4/groups/{id}/share/{group_id}`

Removes a group from a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `group_id` | `integer` | `path` | Yes | The ID of the shared group |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

