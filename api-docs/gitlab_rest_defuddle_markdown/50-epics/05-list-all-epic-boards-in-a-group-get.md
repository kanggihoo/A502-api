# 05-List all epic boards in a group [GET]

`GET /api/v4/groups/{id}/epic_boards`

Lists all epic boards for a specified group. This feature was introduced in GitLab 15.9.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "hide_backlog_list": boolean,
  "hide_closed_list": boolean,
  "group": {
    "id": integer,
    "web_url": string,
    "name": string,
  },
  "labels": [
    {
      "id": integer,
      "name": string,
      "description": string,
      "text_color": string,
      "description_html": string,
      "color": string,
      "archived": boolean,
    }
  ],
  "lists": [
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
  ],
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

