# 29-Delete an experiment. [POST]

`POST /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/experiments/delete`

https://mlflow.org/docs/2.19.0/rest-api.html#delete-experiment

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "experiment_id": string (required), // ID of the experiment.
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

