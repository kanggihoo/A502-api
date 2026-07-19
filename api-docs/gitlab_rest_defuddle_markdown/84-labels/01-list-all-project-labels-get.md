# 01-List all project labels [GET]

`GET /api/v4/projects/{id}/labels`

Lists all labels for a specified project. By default, this request returns 20 results at a time because the API results are paginated.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `with_counts` | `boolean` | `query` | No | Include issue and merge request counts |
| `include_ancestor_groups` | `boolean` | `query` | No | Include ancestor groups |
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
  "priority": integer,
  "is_project_label": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not Found

