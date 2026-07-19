# 06-Retrieve all limit exclusions [GET]

`GET /api/v4/namespaces/storage/limit_exclusions`

Gets all records for namespaces that have been excluded

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "namespace_id": integer,
  "namespace_name": string,
  "reason": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

