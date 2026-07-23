# 26-Restore a group [POST]

`POST /api/v4/groups/{id}/restore`

Restores a specified group that was previously scheduled for deletion. Can not restore groups outside of the retention period (30 days by default).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

