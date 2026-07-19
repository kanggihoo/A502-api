# 03-Update a resource group [PUT]

`PUT /api/v4/projects/{id}/resource_groups/{key}`

Updates the properties for a specified resource group. It returns `200` if the resource group was successfully updated. In case of an error, a status code `400` is returned.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `key` | `string` | `path` | Yes | The key of the resource group |

### Request Body (application/json)

```json
{
  "process_mode": enum("unordered" | "oldest_first" | "newest_first" | "newest_ready_first"), // The process mode of the resource group
}
```
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

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

