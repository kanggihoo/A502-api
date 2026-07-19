# 02-Add instance scope [POST]

`POST /api/v4/runner_controllers/{id}/scopes/instance`

Adds an instance scope to a runner controller. When added, the runner controller evaluates jobs for all runners in the GitLab instance. A runner controller can have only one instance scope. If an instance scope already exists, this operation returns an error.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the runner controller |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

#### 409 - Conflict

