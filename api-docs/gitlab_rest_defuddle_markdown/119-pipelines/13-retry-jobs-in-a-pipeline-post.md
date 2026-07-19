# 13-Retry jobs in a pipeline [POST]

`POST /api/v4/projects/{id}/pipelines/{pipeline_id}/retry`

Retries failed or canceled jobs in a pipeline. If there are no failed or canceled jobs in the pipeline, calling this endpoint has no effect.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID or URL-encoded path |
| `pipeline_id` | `integer` | `path` | Yes | The pipeline ID |

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

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

