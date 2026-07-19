# 25-List experiments [GET]

`GET /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/experiments/list`

https://www.mlflow.org/docs/2.19.0/rest-api.html#search-experiments

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "experiments": [
    {
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
    }
  ],
}
```

#### 404 - Not Found

