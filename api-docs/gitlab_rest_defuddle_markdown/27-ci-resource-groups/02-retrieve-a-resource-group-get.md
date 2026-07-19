# 02-Retrieve a resource group [GET]

`GET /api/v4/projects/{id}/resource_groups/{key}`

Retrieves a specified resource group for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `key` | `string` | `path` | Yes | The key of the resource group |

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

