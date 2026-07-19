# 06-Unsubscribe to a project label [POST]

`POST /api/v4/projects/{id}/labels/{subscribable_id}/unsubscribe`

Unsubscribes the currently authenticated user from a specified project label. They will no longer receive notifications on changes to this item.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `subscribable_id` | `string` | `path` | Yes | The ID of a resource |

### Responses

#### 201 - Created

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

