# 05-Delete a project milestone [DEL]

`DELETE /api/v4/projects/{id}/milestones/{milestone_id}`

Deletes a specified project milestone. Only for users with the Planner, Reporter, Developer, Maintainer, or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `milestone_id` | `integer` | `path` | Yes | The ID of a project milestone |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

