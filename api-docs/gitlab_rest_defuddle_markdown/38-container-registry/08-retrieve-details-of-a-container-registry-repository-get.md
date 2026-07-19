# 08-Retrieve details of a container registry repository [GET]

`GET /api/v4/registry/repositories/{id}`

Retrieves details of a specified container registry repository.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID of the repository |
| `tags` | `boolean` | `query` | No | Determines if tags should be included |
| `tags_count` | `boolean` | `query` | No | Determines if the tags count should be included |
| `size` | `boolean` | `query` | No | Determines if the size should be included |

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

#### 404 - Repository Not Found

