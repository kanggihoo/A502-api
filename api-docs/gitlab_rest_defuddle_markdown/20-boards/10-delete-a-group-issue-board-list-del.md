# 10-Delete a group issue board list [DEL]

`DELETE /api/v4/groups/{id}/boards/{board_id}/lists/{list_id}`

Deletes a specified group issue board list. Only for administrators and users with the Owner role for the group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `board_id` | `integer` | `path` | Yes | The ID of a board |
| `list_id` | `integer` | `path` | Yes | The ID of a board list |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": integer,
  "label": {
    "id": integer,
    "name": string,
    "description": string,
    "text_color": string,
    "description_html": string,
    "color": string,
    "archived": boolean,
  },
  "position": integer,
  "milestone": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "group_id": string,
    "title": string,
    "description": string,
    "state": string,
    "created_at": string,
    "updated_at": string,
    "due_date": string,
    "start_date": string,
    "expired": boolean,
    "web_url": string,
  },
  "iteration": {
    "id": integer,
    "iid": integer,
    "sequence": integer,
    "group_id": integer,
    "title": string,
    "description": string,
    "state": integer,
    "created_at": string,
    "updated_at": string,
    "start_date": string,
    "due_date": string,
    "web_url": string,
  },
  "assignee": {
    "id": integer,
    "username": string,
    "public_email": string,
    "name": string,
  },
  "max_issue_count": integer,
  "max_issue_weight": integer,
  "limit_metric": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

