# 07-Create or update ownership of a pipeline schedule [POST]

`POST /api/v4/projects/{id}/pipeline_schedules/{pipeline_schedule_id}/take_ownership`

Creates or updates the owner of a pipeline schedule for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `pipeline_schedule_id` | `integer` | `path` | Yes | The pipeline schedule id |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "description": string,
  "ref": string,
  "cron": string,
  "cron_timezone": string,
  "next_run_at": string,
  "active": boolean,
  "created_at": string,
  "updated_at": string,
  "owner": {
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
  "inputs": {
    "name": string,
    "value": string,
  },
  "last_pipeline": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "sha": string,
    "ref": string,
    "status": string,
    "source": string,
    "created_at": string,
    "updated_at": string,
    "web_url": string,
  },
  "variables": {
    "variable_type": string,
    "key": string,
    "value": string,
    "hidden": boolean,
    "protected": boolean,
    "masked": boolean,
    "raw": boolean,
    "environment_scope": string,
    "description": string,
  },
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

