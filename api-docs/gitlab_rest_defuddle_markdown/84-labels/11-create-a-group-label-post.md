# 11-Create a group label [POST]

`POST /api/v4/groups/{id}/labels`

Creates a group label.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the label to be created
  "color": string (required), // The color of the label given in 6-digit hex notation with leading '#' sign (e.g. #FFAABB) or one of the allowed CSS color names
  "description": string, // The description of label to be created
  "archived": boolean, // Whether the label is archived
}
```
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
}
```

#### 400 - Bad Request

#### 404 - Not Found

