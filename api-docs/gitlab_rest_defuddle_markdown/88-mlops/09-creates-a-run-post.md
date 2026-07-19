# 09-Creates a Run. [POST]

`POST /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/runs/create`

MLFlow Runs map to GitLab Candidates. https://www.mlflow.org/docs/2.19.0/rest-api.html#create-run

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "experiment_id": integer (required), // Id for the experiment, relative to the project
  "start_time": integer, // Unix timestamp in milliseconds of when the run started.
  "user_id": string, // This will be ignored
  "tags": [
    any
  ], // Tags are stored, but not displayed
  "run_name": string, // A name for this run
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "info": {
    "run_id": string,
    "run_uuid": string,
    "experiment_id": string,
    "start_time": integer, // Unix timestamp in milliseconds
    "end_time": integer, // Unix timestamp in milliseconds
    "run_name": string,
    "status": string,
    "artifact_uri": string,
    "lifecycle_stage": string,
    "user_id": string,
  },
  "data": {},
}
```

#### 400 - Bad Request

#### 404 - Not Found

