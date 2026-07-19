# 01-Retrieve a batched background migration [GET]

`GET /api/v4/admin/batched_background_migrations/{id}`

Retrieve a batched background migration

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `database` | `string` | `query` | No | The name of the database |
| `id` | `integer` | `path` | Yes | The batched background migration id |

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

