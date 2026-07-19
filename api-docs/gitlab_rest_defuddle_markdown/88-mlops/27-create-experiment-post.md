# 27-Create experiment [POST]

`POST /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/experiments/create`

https://www.mlflow.org/docs/2.19.0/rest-api.html#create-experiment

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // Experiment name
  "tags": [
    any
  ], // Tags with information about the experiment
  "artifact_location": string, // This will be ignored
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "experiment_id": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

