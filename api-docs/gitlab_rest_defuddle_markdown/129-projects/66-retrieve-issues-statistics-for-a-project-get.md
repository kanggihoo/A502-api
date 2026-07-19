# 66-Retrieve issues statistics for a project [GET]

`GET /api/v4/projects/{id}/issues_statistics`

Retrieves statistics for issues in a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `labels` | `array` | `query` | No | Comma-separated list of label names |
| `milestone` | `string` | `query` | No | Milestone title |
| `milestone_id` | `string` | `query` | No | Return issues assigned to milestones with the specified timebox value ("Any", "None", "Upcoming" or "Started") |
| `iids` | `array` | `query` | No | The IID array of issues |
| `search` | `string` | `query` | No | Search issues for text present in the title, description, or any combination of these |
| `in` | `string` | `query` | No | `title`, `description`, or a string joining them with comma |
| `author_id` | `integer` | `query` | No | Return issues which are authored by the user with the given ID |
| `author_username` | `string` | `query` | No | Return issues which are authored by the user with the given username |
| `assignee_id` | `any` | `query` | No | Return issues which are assigned to the user with the given ID |
| `assignee_username` | `array` | `query` | No | Return issues which are assigned to the user with the given username |
| `created_after` | `string` | `query` | No | Return issues created after the specified time |
| `created_before` | `string` | `query` | No | Return issues created before the specified time |
| `updated_after` | `string` | `query` | No | Return issues updated after the specified time |
| `updated_before` | `string` | `query` | No | Return issues updated before the specified time |
| `not` | `object` | `query` | No | Filters by the specified parameters |
| `not[labels]` | `array` | `query` | No | Comma-separated list of label names |
| `not[milestone]` | `string` | `query` | No | Milestone title |
| `not[milestone_id]` | `string` | `query` | No | Return issues assigned to milestones without the specified timebox value ("Any", "None", "Upcoming" or "Started") |
| `not[iids]` | `array` | `query` | No | The IID array of issues |
| `not[author_id]` | `integer` | `query` | No | Return issues which are not authored by the user with the given ID |
| `not[author_username]` | `string` | `query` | No | Return issues which are not authored by the user with the given username |
| `not[assignee_id]` | `integer` | `query` | No | Return issues which are not assigned to the user with the given ID |
| `not[assignee_username]` | `array` | `query` | No | Return issues which are not assigned to the user with the given username |
| `not[weight]` | `integer` | `query` | No | Return issues without the specified weight |
| `not[iteration_id]` | `any` | `query` | No | Return issues which are not assigned to the iteration with the given ID |
| `not[iteration_title]` | `string` | `query` | No | Return issues which are not assigned to the iteration with the given title |
| `scope` | `string` | `query` | No | Return issues for the given scope: `created_by_me`, `assigned_to_me` or `all` |
| `my_reaction_emoji` | `string` | `query` | No | Return issues reacted by the authenticated user by the given emoji |
| `confidential` | `boolean` | `query` | No | Filter confidential or public issues |
| `weight` | `any` | `query` | No | The weight of the issue |
| `epic_id` | `any` | `query` | No | The ID of an epic associated with the issues |
| `health_status` | `string` | `query` | No | The health status of the issue. Must be one of: on_track, needs_attention, at_risk, none, any |
| `iteration_id` | `any` | `query` | No | Return issues which are assigned to the iteration with the given ID |
| `iteration_title` | `string` | `query` | No | Return issues which are assigned to the iteration with the given title |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

