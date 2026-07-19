# 14-Retrieve a group label [GET]

`GET /api/v4/groups/{id}/labels/{name}`

Retrieves a specified group label.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `include_ancestor_groups` | `boolean` | `query` | No | Include ancestor groups |
| `include_descendant_groups` | `boolean` | `query` | No | Include descendant groups. This feature was added in GitLab 13.6 |
| `only_group_labels` | `boolean` | `query` | No | Toggle to include only group labels or also project labels. This feature was added in GitLab 13.6 |
| `name` | `string` | `path` | Yes | The name or id of the label to be updated |

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

