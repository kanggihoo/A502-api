# 15-Unassign a runner from a project [DEL]

`DELETE /api/v4/projects/{id}/runners/{runner_id}`

Unassigns a specified project runner from a project. You cannot unassign a runner from the owner project. Use the delete a runner operation instead.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `runner_id` | `integer` | `path` | Yes | The ID of a runner |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": integer,
  "description": string,
  "ip_address": string,
  "active": boolean,
  "paused": boolean,
  "is_shared": boolean,
  "runner_type": string,
  "name": string,
  "online": boolean,
  "created_by": {
    "id": integer,
    "username": string,
    "public_email": string,
    "name": string,
    "state": string,
    "locked": boolean,
    "avatar_url": string,
    "avatar_path": string,
    "custom_attributes": [
      {
        "key": string,
        "value": string,
      }
    ],
    "web_url": string,
  },
  "created_at": string,
  "status": string,
  "job_execution_status": string,
}
```

#### 400 - Bad Request

#### 403 - You cannot unassign a runner from the owner project. Delete the runner instead

#### 404 - Runner not found

#### 412 - Precondition Failed

