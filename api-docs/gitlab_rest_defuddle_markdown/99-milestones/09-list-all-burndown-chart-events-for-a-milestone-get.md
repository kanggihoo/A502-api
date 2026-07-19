# 09-List all burndown chart events for a milestone [GET]

`GET /api/v4/projects/{id}/milestones/{milestone_id}/burndown_events`

Lists all burndown chart events for a specified milestone.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `milestone_id` | `integer` | `path` | Yes | The ID of a project milestone |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

