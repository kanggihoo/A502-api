# 01-Trigger a pipeline with a token [POST]

`POST /api/v4/projects/{id}/(ref/{ref}/)trigger/pipeline`

Triggers a pipeline with a token. With a CI/CD job token, the triggered pipeline is a multi-project pipeline. The job that authenticates the request becomes associated with the upstream pipeline, which is visible on the pipeline graph. If you use a trigger token in a job, the job is not associated with the upstream pipeline.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `ref` | `string` | `path` | Yes | The commit sha or name of a branch or tag |

### Request Body (application/json)

```json
{
  "token": string (required), // The unique token of trigger or job token
  "variables": {}, // The list of variables to be injected into build
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

