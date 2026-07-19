# 14-Delete a group milestone [DEL]

`DELETE /api/v4/groups/{id}/milestones/{milestone_id}`

Deletes the specified group milestone.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `milestone_id` | `integer` | `path` | Yes | The ID of a group milestone |

### Responses

#### 204 - 204 No Content

#### 400 - Bad Request

#### 404 - Not Found

