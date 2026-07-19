# 24-Fetch experiment by experiment_name [GET]

`GET /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/experiments/get-by-name`

https://www.mlflow.org/docs/2.19.0/rest-api.html#get-experiment-by-name

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `experiment_name` | `string` | `query` | No | Experiment name |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "experiment": {
    "experiment_id": string,
    "name": string,
    "lifecycle_stage": string,
    "artifact_location": string,
    "tags": [
      {
        "key": string,
        "value": string,
      }
    ],
  },
}
```

#### 400 - Bad Request

#### 404 - Not Found

