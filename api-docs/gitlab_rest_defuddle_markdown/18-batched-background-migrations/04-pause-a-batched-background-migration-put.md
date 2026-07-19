# 04-Pause a batched background migration [PUT]

`PUT /api/v4/admin/batched_background_migrations/{id}/pause`

Pause a batched background migration

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The batched background migration id |

### Request Body (application/json)

```json
{
  "database": enum("main" | "ci" | "sec" | "embedding" | "geo"), // The name of the database
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": string,
  "job_class_name": string,
  "table_name": string,
  "column_name": string,
  "status": string,
  "progress": number,
  "created_at": string,
  "estimated_time_remaining": string,
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

#### 422 - You can pause only `active` batched background migrations.

