# 03-Update an existing label. At least one optional parameter is required. [PUT]

`PUT /api/v4/projects/{id}/labels`

Deprecated in GitLab 12.4. Use PUT /projects/:id/labels/:name instead.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "label_id": integer, // The ID of the label to be updated
  "name": string, // The name of the label to be updated
  "new_name": string, // The new name of the label
  "color": string, // The new color of the label given in 6-digit hex notation with leading '#' sign (e.g. #FFAABB) or one of the allowed CSS color names
  "description": string, // The new description of label
  "archived": boolean, // Whether the label is archived
  "priority": integer, // The priority of the label
}
```
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

