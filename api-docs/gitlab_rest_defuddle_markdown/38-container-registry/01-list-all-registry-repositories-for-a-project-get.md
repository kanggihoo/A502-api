# 01-List all registry repositories for a project [GET]

`GET /api/v4/projects/{id}/registry/repositories`

Lists all registry repositories for a specified project. Responses are paginated and return 20 results by default.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `tags` | `boolean` | `query` | No | Determines if tags should be included |
| `tags_count` | `boolean` | `query` | No | Determines if the tags count should be included |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "path": string,
  "project_id": integer,
  "location": string,
  "created_at": string,
  "cleanup_policy_started_at": string,
  "tags_count": integer,
  "tags": {
    "name": string,
    "path": string,
    "location": string,
  },
  "delete_api_path": string,
  "size": integer,
  "status": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

