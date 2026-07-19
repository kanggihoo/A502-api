# 12-Update a group label [PUT]

`PUT /api/v4/groups/{id}/labels`

Updates an existing group label. At least one parameter is required to update the group label.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Request Body (application/json)

```json
{
  "label_id": integer, // The ID of the label to be updated
  "name": string, // The name of the label to be updated
  "new_name": string, // The new name of the label
  "color": string, // The new color of the label given in 6-digit hex notation with leading '#' sign (e.g. #FFAABB) or one of the allowed CSS color names
  "description": string, // The new description of label
  "archived": boolean, // Whether the label is archived
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
}
```

#### 400 - Bad Request

#### 404 - Not Found

