# 05-Schedule a relations export for a group [POST]

`POST /api/v4/groups/{id}/export_relations`

Schedules a relations export for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Request Body (application/json)

```json
{
  "batched": boolean, // Whether to export in batches
}
```
### Responses

#### 202 - Accepted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 503 - Service unavailable

