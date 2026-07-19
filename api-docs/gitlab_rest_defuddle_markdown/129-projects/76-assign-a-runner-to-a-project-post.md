# 76-Assign a runner to a project [POST]

`POST /api/v4/projects/{id}/runners`

Assigns an available project runner to a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Request Body (application/json)

```json
{
  "runner_id": integer (required), // The ID of a runner
}
```
### Responses

#### 201 - Created

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

#### 403 - Runner is locked

#### 404 - Runner not found

