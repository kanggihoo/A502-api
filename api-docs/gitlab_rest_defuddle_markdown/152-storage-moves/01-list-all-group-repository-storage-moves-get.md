# 01-List all group repository storage moves [GET]

`GET /api/v4/group_repository_storage_moves`

Lists all group repository storage moves for an instance.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "created_at": string,
  "state": string,
  "source_storage_name": string,
  "destination_storage_name": string,
  "error_message": string,
  "group": {
    "id": integer,
    "web_url": string,
    "name": string,
  },
}
```

#### 400 - Bad Request

