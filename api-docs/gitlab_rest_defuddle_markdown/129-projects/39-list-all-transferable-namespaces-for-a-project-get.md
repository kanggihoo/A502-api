# 39-List all transferable namespaces for a project [GET]

`GET /api/v4/projects/{id}/transfer_locations`

Lists all namespaces where a specified project can be transferred.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `search` | `string` | `query` | No | Return list of namespaces matching the search criteria |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "web_url": string,
  "name": string,
  "avatar_url": string,
  "full_name": string,
  "full_path": string,
}
```

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not Found

