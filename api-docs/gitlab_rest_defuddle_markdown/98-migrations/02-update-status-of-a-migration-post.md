# 02-Update status of a migration [POST]

`POST /api/v4/admin/migrations/{timestamp}/mark`

Updates the status of a migration to indicate a successful execution. This prevent them from being executed by the `db:migrate` tasks. Use this API to skip failing migrations after you determine they are safe to skip.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `timestamp` | `integer` | `path` | Yes | The migration version timestamp |

### Request Body (application/json)

```json
{
  "database": enum("main" | "ci" | "sec" | "embedding" | "geo"), // The name of the database
}
```
### Responses

#### 201 - 201 Created

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

#### 422 - You can mark only pending migrations

