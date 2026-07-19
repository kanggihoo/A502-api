# 15-Retrieve a project repository storage move [GET]

`GET /api/v4/project_repository_storage_moves/{repository_storage_move_id}`

Retrieves a specified project repository storage move.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `repository_storage_move_id` | `integer` | `path` | Yes | The ID of a project repository storage move |

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
  "project": {
    "id": integer,
    "description": string,
    "name": string,
    "name_with_namespace": string,
    "path": string,
    "path_with_namespace": string,
    "created_at": string,
  },
}
```

#### 400 - Bad Request

#### 404 - Not Found

