# 26-Search experiments [POST]

`POST /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/experiments/search`

https://www.mlflow.org/docs/2.19.0/rest-api.html#search-experiments

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "max_results": integer, // Maximum number of experiments to fetch in a page. Default is 200, maximum is 1000.
  "order_by": string, // Order criteria. Can be by a column of the experiment (created_at, name).
  "page_token": string, // Token for pagination
  "filter": string, // This parameter is ignored
}
```
### Responses

#### 201 - Created

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

#### 400 - Bad Request

#### 404 - Not Found

