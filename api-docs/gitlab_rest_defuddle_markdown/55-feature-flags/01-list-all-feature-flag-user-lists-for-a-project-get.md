# 01-List all feature flag user lists for a project [GET]

`GET /api/v4/projects/{id}/feature_flags_user_lists`

Lists all feature flag user lists for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `search` | `string` | `query` | No | Return user lists matching the search criteria |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "iid": integer,
  "name": string,
  "user_xids": string,
  "project_id": integer,
  "created_at": string,
  "updated_at": string,
  "path": string,
  "edit_path": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

