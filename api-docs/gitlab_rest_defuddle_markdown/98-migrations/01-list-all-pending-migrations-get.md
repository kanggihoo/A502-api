# 01-List all pending migrations [GET]

`GET /api/v4/admin/migrations/pending`

Lists all pending migrations for the instance.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `database` | `string` | `query` | No | The name of the database |

### Responses

#### 200 - 200 OK

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

