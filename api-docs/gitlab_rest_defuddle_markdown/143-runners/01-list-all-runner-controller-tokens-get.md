# 01-List all runner controller tokens [GET]

`GET /api/v4/runner_controllers/{runner_controller_id}/tokens`

Lists all runner controller tokens.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `runner_controller_id` | `integer` | `path` | Yes | ID of the runner controller |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "runner_controller_id": integer,
  "description": string,
  "last_used_at": string,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

