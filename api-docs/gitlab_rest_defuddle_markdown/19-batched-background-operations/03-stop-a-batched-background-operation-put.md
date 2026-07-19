# 03-Stop a batched background operation [PUT]

`PUT /api/v4/admin/batched_background_operations/{id}/stop`

This feature was introduced in GitLab 19.2.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The batched background operation id |

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
  "partition": integer,
  "job_class_name": string,
  "table_name": string,
  "column_name": string,
  "status": string,
  "created_at": string,
  "started_at": string,
  "finished_at": string,
  "on_hold_until": string,
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

#### 422 - You can stop only `queued`, `active` or `paused` operations.

