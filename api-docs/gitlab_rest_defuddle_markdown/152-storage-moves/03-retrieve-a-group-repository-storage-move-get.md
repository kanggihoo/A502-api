# 03-Retrieve a group repository storage move [GET]

`GET /api/v4/group_repository_storage_moves/{repository_storage_move_id}`

Retrieves a specified group repository storage move. This feature was introduced in GitLab 13.9.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `repository_storage_move_id` | `integer` | `path` | Yes | The ID of a group repository storage move |

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

#### 404 - Not Found

