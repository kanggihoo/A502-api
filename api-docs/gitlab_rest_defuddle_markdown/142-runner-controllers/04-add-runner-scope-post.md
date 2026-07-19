# 04-Add runner scope [POST]

`POST /api/v4/runner_controllers/{id}/scopes/runners/{runner_id}`

Adds a runner scope to a runner controller. When added, the runner controller evaluates jobs only for a specified runner. A runner controller with an instance scope cannot have runner scopes. Remove the instance scope before adding runner scopes.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the runner controller |
| `runner_id` | `integer` | `path` | Yes | ID of the runner |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "runner_id": integer,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

#### 409 - Conflict

#### 422 - Unprocessable Entity

