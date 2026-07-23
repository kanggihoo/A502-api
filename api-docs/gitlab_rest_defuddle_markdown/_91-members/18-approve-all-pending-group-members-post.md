# 18-Approve all pending group members [POST]

`POST /api/v4/groups/{id}/members/approve_all`

Approves all pending users for a specified top-level group and any subgroups or projects.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

