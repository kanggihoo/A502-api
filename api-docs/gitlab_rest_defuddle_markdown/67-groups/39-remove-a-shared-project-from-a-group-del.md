# 39-Remove a shared project from a group [DEL]

`DELETE /api/v4/groups/{id}/shared_projects/{project_id}`

Removes a shared project targeting this group. The group Owner can remove a shared project without access to the source project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `project_id` | `integer` | `path` | Yes | The ID of the shared project |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 403 - Forbidden

#### 404 - Not found

