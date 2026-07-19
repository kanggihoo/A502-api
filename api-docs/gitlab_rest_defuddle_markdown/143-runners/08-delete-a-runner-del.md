# 08-Delete a runner [DEL]

`DELETE /api/v4/runners/{id}`

Deletes a specified runner.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of a runner |

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

#### 401 - Unauthorized

#### 403 - Runner associated with more than one project

#### 404 - Runner not found

#### 412 - Precondition Failed

