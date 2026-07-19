# 08-Retrieve a group epic board list [GET]

`GET /api/v4/groups/{id}/epic_boards/{board_id}/lists/{list_id}`

Retrieves a specified group epic board list. This feature was introduced in GitLab 15.9.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `board_id` | `integer` | `path` | Yes | The ID of an epic board |
| `list_id` | `integer` | `path` | Yes | The ID of a list |

### Responses

#### 200 - OK

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
  "list_type": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

