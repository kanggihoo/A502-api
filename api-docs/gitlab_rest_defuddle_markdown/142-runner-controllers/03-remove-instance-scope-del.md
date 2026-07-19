# 03-Remove instance scope [DEL]

`DELETE /api/v4/runner_controllers/{id}/scopes/instance`

Removes an instance scope from a runner controller.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the runner controller |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

