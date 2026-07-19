# 10-Gets an MLFlow Run, which maps to GitLab Candidates [GET]

`GET /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/runs/get`

https://www.mlflow.org/docs/1.28.0/rest-api.html#get-run

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `run_id` | `string` | `query` | Yes | UUID of the candidate. |
| `run_uuid` | `string` | `query` | No | This parameter is ignored |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

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

