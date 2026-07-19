# 02-Retrieve dictionary details [GET]

`GET /api/v4/admin/databases/{database_name}/dictionary/tables/{table_name}`

Retrieve dictionary details

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `database_name` | `string` | `path` | Yes | The database name |
| `table_name` | `string` | `path` | Yes | The table name |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "table_name": string,
  "feature_categories": [
    string
  ],
  "table_size": string,
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

