# 04-Rotate a runner controller token [POST]

`POST /api/v4/runner_controllers/{runner_controller_id}/tokens/{id}/rotate`

Rotates an existing runner controller token.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `runner_controller_id` | `integer` | `path` | Yes | ID of the runner controller |
| `id` | `integer` | `path` | Yes | ID of the runner controller token |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "runner_controller_id": integer,
  "description": string,
  "last_used_at": string,
  "created_at": string,
  "updated_at": string,
  "token": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

