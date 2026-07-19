# 08-Gets a Model Version by alias [GET]

`GET /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/registered-models/alias`

https://mlflow.org/docs/2.19.0/rest-api.html#get-model-version-by-alias

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `query` | No | The name of the model |
| `alias` | `string` | `query` | No | The alias of the model, e.g. the Semantic Version `1.0.0` |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

