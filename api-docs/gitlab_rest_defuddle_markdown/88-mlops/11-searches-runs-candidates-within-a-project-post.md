# 11-Searches runs/candidates within a project [POST]

`POST /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/runs/search`

https://www.mlflow.org/docs/2.19.0/rest-api.html#search-runsexperiment_ids supports only a single experiment ID.Introduced in GitLab 16.4

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "experiment_ids": [
    any
  ] (required), // IDs of the experiments to get searches from, relative to the project
  "max_results": integer, // Maximum number of runs/candidates to fetch in a page. Default is 200, maximum in 1000
  "order_by": string, // Order criteria. Can be by a column of the run/candidate (created_at, name) or by a metric ifprefixed by `metrics`. Valid examples: `created_at`, `created_at DESC`, `metrics.my_metric DESC`Sorting by candidate parameter or metadata is not supported.
  "page_token": string, // Token for pagination
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

