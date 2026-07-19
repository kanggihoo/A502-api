# 02-Retrieve a batched background operation [GET]

`GET /api/v4/admin/batched_background_operations/{id}`

This feature was introduced in GitLab 19.1.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The batched background operation id |
| `database` | `string` | `query` | No | The name of the database |

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

