# 10-List all group milestones [GET]

`GET /api/v4/groups/{id}/milestones`

Lists all group milestones for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `state` | `string` | `query` | No | Return "active", "closed", or "all" milestones |
| `iids` | `array` | `query` | No | The IIDs of the milestones |
| `title` | `string` | `query` | No | The title of the milestones |
| `search` | `string` | `query` | No | The search criteria for the title or description of the milestone |
| `include_parent_milestones` | `boolean` | `query` | No | Deprecated: see `include_ancestors` |
| `include_ancestors` | `boolean` | `query` | No | Include milestones from all parent groups |
| `updated_before` | `string` | `query` | No | Return milestones updated before the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `updated_after` | `string` | `query` | No | Return milestones updated after the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `include_descendants` | `boolean` | `query` | No | Include milestones from all subgroups and subprojects |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "iid": integer,
  "project_id": integer,
  "group_id": string,
  "title": string,
  "description": string,
  "state": string,
  "created_at": string,
  "updated_at": string,
  "due_date": string,
  "start_date": string,
  "expired": boolean,
  "web_url": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

