# 06-Update a project label [PUT]

`PUT /api/v4/projects/{id}/labels/{name}`

Updates a specified label for a project with a different name or color. At least one parameter is required to update the label.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `name` | `string` | `path` | Yes | The name or id of the label to be updated |

### Request Body (application/json)

```json
{
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

