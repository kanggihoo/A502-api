# 44-List all package protection rules [GET]

`GET /api/v4/projects/{id}/packages/protection/rules`

Lists all package protection rules for a specified project.

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
  "package_name_pattern": string,
  "package_type": string,
  "minimum_access_level_for_delete": string,
  "minimum_access_level_for_push": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

