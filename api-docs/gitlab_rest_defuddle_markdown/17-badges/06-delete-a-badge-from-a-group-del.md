# 06-Delete a badge from a group [DEL]

`DELETE /api/v4/groups/{id}/badges/{badge_id}`

Deletes a specified badge from a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of the group owned by the authenticated user. |
| `badge_id` | `integer` | `path` | Yes | The badge ID |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

