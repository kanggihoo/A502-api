# 02-List all runner controllers [GET]

`GET /api/v4/runner_controllers`

Lists all runner controllers.

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
  "description": string,
  "state": string,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

