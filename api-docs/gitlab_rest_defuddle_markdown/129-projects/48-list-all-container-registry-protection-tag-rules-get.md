# 48-List all container registry protection tag rules [GET]

`GET /api/v4/projects/{id}/registry/protection/tag/rules`

Lists all container registry protection tag rules for a project. This feature was introduced in GitLab 18.7.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "tag_name_pattern": string,
  "minimum_access_level_for_push": string,
  "minimum_access_level_for_delete": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

