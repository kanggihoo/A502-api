# 12-Updates a Run. [POST]

`POST /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/runs/update`

MLFlow Runs map to GitLab Candidates. https://www.mlflow.org/docs/2.19.0/rest-api.html#update-run

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "run_id": string (required), // UUID of the candidate.
  "status": enum("RUNNING" | "SCHEDULED" | "FINISHED" | "FAILED" | "KILLED"), // Status of the run. Accepts: ["RUNNING", "SCHEDULED", "FINISHED", "FAILED", "KILLED"].
  "end_time": integer, // Ending time of the run
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "run_info": {
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
}
```

#### 400 - Bad Request

#### 404 - Not Found

