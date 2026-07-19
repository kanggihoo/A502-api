# 03-Revoke a runner controller token [DEL]

`DELETE /api/v4/runner_controllers/{runner_controller_id}/tokens/{id}`

Revokes an existing runner controller token.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `runner_controller_id` | `integer` | `path` | Yes | ID of the runner controller |
| `id` | `integer` | `path` | Yes | ID of the runner controller token |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

