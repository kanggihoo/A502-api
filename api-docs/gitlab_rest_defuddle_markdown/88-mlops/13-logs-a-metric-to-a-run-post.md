# 13-Logs a metric to a run. [POST]

`POST /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/runs/log-metric`

https://www.mlflow.org/docs/1.28.0/rest-api.html#log-metric

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "run_id": string (required), // UUID of the run.
  "key": string (required), // Name for the metric.
  "value": number (required), // Value of the metric.
  "timestamp": integer (required), // Unix timestamp in milliseconds when metric was recorded
  "step": integer, // Step at which the metric was recorded
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

