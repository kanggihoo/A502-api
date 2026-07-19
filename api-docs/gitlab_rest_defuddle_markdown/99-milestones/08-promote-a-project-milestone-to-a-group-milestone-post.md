# 08-Promote a project milestone to a group milestone [POST]

`POST /api/v4/projects/{id}/milestones/{milestone_id}/promote`

Promotes a specified project milestone to a group milestone. Only for users with the Planner, Reporter, Developer, Maintainer, or Owner role for the group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `milestone_id` | `integer` | `path` | Yes | The ID of a project milestone |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

