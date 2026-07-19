# 01-List all templates of a particular type [GET]

`GET /api/v4/projects/{id}/templates/{type}`

Lists all templates of a specified type for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `type` | `string` | `path` | Yes | The type (dockerfiles|gitignores|gitlab_ci_ymls|licenses|issues|merge_requests) of the template |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "key": string,
  "name": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

