# 17-Create an issue board list [POST]

`POST /api/v4/projects/{id}/boards/{board_id}/lists`

Creates an issue board list.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `board_id` | `integer` | `path` | Yes | The ID of a board |

### Request Body (application/json)

```json
{
  "label_id": integer, // The ID of an existing label
  "milestone_id": integer, // The ID of an existing milestone
  "iteration_id": integer, // The ID of an assignee iteration
  "assignee_id": integer, // The ID of an assignee
}
```
### Responses

#### 201 - Created

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

