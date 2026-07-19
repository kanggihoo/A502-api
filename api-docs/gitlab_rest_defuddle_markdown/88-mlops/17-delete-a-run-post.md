# 17-Delete a run. [POST]

`POST /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/runs/delete`

https://mlflow.org/docs/2.19.0/rest-api.html#delete-run

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "run_id": string (required), // UUID of the run.
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

