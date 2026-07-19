# 01-List dictionary tables [GET]

`GET /api/v4/databases/{database_name}/dictionary/tables`

Returns database dictionary tables filtered by database and optional table size

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `database_name` | `string` | `path` | Yes | The database name |
| `table_size` | `string` | `query` | No | Filter by table size classification |

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

#### 404 - Not Found

