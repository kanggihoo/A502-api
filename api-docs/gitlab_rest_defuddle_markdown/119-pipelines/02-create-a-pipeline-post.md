# 02-Create a pipeline [POST]

`POST /api/v4/projects/{id}/pipeline`

Creates a pipeline in the specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID or URL-encoded path |

### Request Body (application/json)

```json
{
  "ref": string (required), // Reference
  "variables": [
    {
      "key": string, // The key of the variable
      "value": string, // The value of the variable
      "variable_type": enum("env_var" | "file"), // The type of variable, must be one of env_var or file. Defaults to env_var
    }
  ], // Array of variables available in the pipeline
  "inputs": {}, // The list of inputs to be used to create the pipeline.
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
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
  "before_sha": string,
  "tag": boolean,
  "yaml_errors": string,
  "user": {
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
  "started_at": string,
  "finished_at": string,
  "committed_at": string,
  "duration": integer, // Time spent running in seconds
  "queued_duration": integer, // Time spent enqueued in seconds
  "coverage": number,
  "detailed_status": {
    "icon": string,
    "text": string,
    "label": string,
    "group": string,
    "tooltip": string,
    "has_details": boolean,
    "details_path": string,
    "illustration": {},
    "favicon": string,
    "action": string,
  },
  "archived": boolean,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

