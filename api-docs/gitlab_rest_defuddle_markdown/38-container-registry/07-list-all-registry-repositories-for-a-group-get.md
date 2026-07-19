# 07-List all registry repositories for a group [GET]

`GET /api/v4/groups/{id}/registry/repositories`

Lists all registry repositories for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group accessible by the authenticated user |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

#### 404 - Group Not Found

