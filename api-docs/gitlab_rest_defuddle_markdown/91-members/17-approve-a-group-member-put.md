# 17-Approve a group member [PUT]

`PUT /api/v4/groups/{id}/members/{member_id}/approve`

Approves a specified pending user for a top-level group and any subgroups or projects.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `member_id` | `integer` | `path` | Yes | The ID of the member requiring approval |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

