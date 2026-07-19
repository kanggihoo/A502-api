# 13-Delete a group label [DEL]

`DELETE /api/v4/groups/{id}/labels`

Deletes a specified group label.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `name` | `string` | `query` | Yes | The name of the label to be deleted |

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
}
```

#### 400 - Bad Request

#### 404 - Not Found

