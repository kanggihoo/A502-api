# 22-Gets metric history for a run [GET]

`GET /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/metrics/get-history`

https://www.mlflow.org/docs/2.19.0/rest-api.html#get-metric-history

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `run_id` | `string` | `query` | Yes | UUID of the run |
| `metric_key` | `string` | `query` | Yes | Name of the metric |
| `max_results` | `integer` | `query` | No | Maximum number of metrics to return. Default is 1000. |
| `page_token` | `string` | `query` | No | Token for pagination |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "metrics": [
    {
      "key": string,
      "value": number,
      "timestamp": integer, // Unix timestamp in milliseconds
      "step": integer,
    }
  ],
  "next_page_token": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

