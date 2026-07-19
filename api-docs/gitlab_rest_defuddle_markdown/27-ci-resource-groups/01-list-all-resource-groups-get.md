# 01-List all resource groups [GET]

`GET /api/v4/projects/{id}/resource_groups`

Lists all resource groups for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "key": string,
  "process_mode": string,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

