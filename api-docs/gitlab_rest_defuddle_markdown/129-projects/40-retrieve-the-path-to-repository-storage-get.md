# 40-Retrieve the path to repository storage [GET]

`GET /api/v4/projects/{id}/storage`

Retrieves the path to repository storage for a specified project. If you are using Gitaly Cluster (Praefect), see Praefect-generated replica paths instead. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of a project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "disk_path": string,
  "project_id": integer,
  "repository_storage": string,
  "created_at": string,
}
```

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not Found

