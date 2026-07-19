# 01-Get the list of batched background operations [GET]

`GET /api/v4/admin/batched_background_operations`

This feature was introduced in GitLab 19.1.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `database` | `string` | `query` | No | The name of the database, the default `main` |
| `job_class_name` | `string` | `query` | No | Filter operations by job class name. |

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

