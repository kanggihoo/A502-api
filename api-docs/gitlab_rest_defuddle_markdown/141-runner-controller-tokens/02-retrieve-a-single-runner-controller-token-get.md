# 02-Retrieve a single runner controller token [GET]

`GET /api/v4/runner_controllers/{runner_controller_id}/tokens/{id}`

Retrieves details of a specified runner controller token by its ID.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `runner_controller_id` | `integer` | `path` | Yes | ID of the runner controller |
| `id` | `integer` | `path` | Yes | ID of the runner controller token |

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

