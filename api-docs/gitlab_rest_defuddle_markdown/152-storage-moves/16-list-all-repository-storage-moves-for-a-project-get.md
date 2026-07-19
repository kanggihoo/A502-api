# 16-List all repository storage moves for a project [GET]

`GET /api/v4/projects/{id}/repository_storage_moves`

Lists all repository storage moves for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
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

