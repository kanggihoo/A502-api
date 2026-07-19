# 05-Remove runner scope [DEL]

`DELETE /api/v4/runner_controllers/{id}/scopes/runners/{runner_id}`

Removes a runner scope from a runner controller.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the runner controller |
| `runner_id` | `integer` | `path` | Yes | ID of the runner |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

