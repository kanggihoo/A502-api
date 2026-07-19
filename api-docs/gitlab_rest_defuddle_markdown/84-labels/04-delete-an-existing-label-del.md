# 04-Delete an existing label [DEL]

`DELETE /api/v4/projects/{id}/labels`

Deprecated in GitLab 12.4. Use DELETE /projects/:id/labels/:name instead.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `label_id` | `integer` | `query` | No | The ID of the label to be deleted |
| `name` | `string` | `query` | No | The name of the label to be deleted |

### Responses

#### 204 - No Content

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

