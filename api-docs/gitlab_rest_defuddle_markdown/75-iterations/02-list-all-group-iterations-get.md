# 02-List all group iterations [GET]

`GET /api/v4/groups/{id}/iterations`

Lists all iterations for a specified group. Iterations created by **Enable automatic scheduling** in iteration cadences return `null` for the `title` and `description` fields. This feature was introduced in GitLab 13.5.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `state` | `string` | `query` | No | Return "opened", "upcoming", "current (previously started)", "closed", or "all" iterations. Filtering by `started` state is deprecated starting with 14.1, please use `current` instead. |
| `search` | `string` | `query` | No | The search criteria for the title of the iteration |
| `in` | `array` | `query` | No | Fields in which fuzzy search should be performed with the query given in the argument `search`. The available options are `title` and `cadence_title`. Defaults to `[title]` |
| `include_ancestors` | `boolean` | `query` | No | Include iterations from parent and its ancestors |
| `include_descendants` | `boolean` | `query` | No | Include iterations from parent and its descendants |
| `updated_before` | `string` | `query` | No | Return milestones updated before the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `updated_after` | `string` | `query` | No | Return milestones updated after the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "iid": integer,
  "sequence": integer,
  "group_id": integer,
  "title": string,
  "description": string,
  "state": integer,
  "created_at": string,
  "updated_at": string,
  "start_date": string,
  "due_date": string,
  "web_url": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

