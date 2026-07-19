# 02-Get the list of batched background migrations [GET]

`GET /api/v4/admin/batched_background_migrations`

Get the list of batched background migrations

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `database` | `string` | `query` | No | The name of the database, the default `main` |
| `job_class_name` | `string` | `query` | No | Filter migrations by job class name. |

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

