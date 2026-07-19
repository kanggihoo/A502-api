# 10-List all group labels [GET]

`GET /api/v4/groups/{id}/labels`

Lists all group labels for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `with_counts` | `boolean` | `query` | No | Include issue and merge request counts |
| `include_ancestor_groups` | `boolean` | `query` | No | Include ancestor groups |
| `include_descendant_groups` | `boolean` | `query` | No | Include descendant groups. This feature was added in GitLab 13.6 |
| `only_group_labels` | `boolean` | `query` | No | Toggle to include only group labels or also project labels. This feature was added in GitLab 13.6 |
| `search` | `string` | `query` | No | Keyword to filter labels by. This feature was added in GitLab 13.6 |
| `archived` | `boolean` | `query` | No | Filter by archived status. This feature was added in GitLab 18.10 |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "description": string,
  "text_color": string,
  "description_html": string,
  "color": string,
  "archived": boolean,
  "open_issues_count": integer,
  "closed_issues_count": integer,
  "open_merge_requests_count": integer,
  "subscribed": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not Found

