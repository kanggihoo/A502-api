# 03-List all registry repository tags for a project [GET]

`GET /api/v4/projects/{id}/registry/repositories/{repository_id}/tags`

Lists all tags for a specified registry repository. Responses are paginated and return 20 results by default.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `repository_id` | `integer` | `path` | Yes | The ID of the repository |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "path": string,
  "location": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

#### 405 - Method Not Allowed

