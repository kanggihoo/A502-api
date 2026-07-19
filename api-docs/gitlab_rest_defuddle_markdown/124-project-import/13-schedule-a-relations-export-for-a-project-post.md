# 13-Schedule a relations export for a project [POST]

`POST /api/v4/projects/{id}/export_relations`

Schedules a relations export for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "batched": boolean, // Whether to export in batches
}
```
### Responses

#### 202 - Accepted

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 503 - Service unavailable

