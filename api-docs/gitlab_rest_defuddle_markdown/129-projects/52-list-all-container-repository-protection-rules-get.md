# 52-List all container repository protection rules [GET]

`GET /api/v4/projects/{id}/registry/protection/repository/rules`

Lists all container repository protection rules for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "repository_path_pattern": string,
  "minimum_access_level_for_push": string,
  "minimum_access_level_for_delete": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

