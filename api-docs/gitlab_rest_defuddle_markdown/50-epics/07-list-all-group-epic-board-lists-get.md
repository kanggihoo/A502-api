# 07-List all group epic board lists [GET]

`GET /api/v4/groups/{id}/epic_boards/{board_id}/lists`

Lists all group epic board lists for a specified board. Does not include `open` and `closed` lists. This feature was introduced in GitLab 15.9.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `board_id` | `integer` | `path` | Yes | The ID of an epic board |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

