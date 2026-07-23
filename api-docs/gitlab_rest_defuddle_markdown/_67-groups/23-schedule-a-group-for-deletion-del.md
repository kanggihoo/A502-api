# 23-Schedule a group for deletion [DEL]

`DELETE /api/v4/groups/{id}`

Schedules a group for deletion. Groups are deleted at the end of the retention period (30 days by default). Use the `permanently_remove` param to override the retention period.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Responses

#### 202 - Accepted

#### 400 - Bad Request

#### 404 - Not Found

