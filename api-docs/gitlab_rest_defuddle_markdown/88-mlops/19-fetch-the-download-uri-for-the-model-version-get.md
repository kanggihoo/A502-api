# 19-Fetch the download URI for the model version. [GET]

`GET /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/model-versions/get-download-uri`

Returns version in MLflow format "mlflow-artifacts:<version>" https://mlflow.org/docs/2.19.0/rest-api.html#get-download-uri-for-modelversion-artifacts

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `query` | Yes | Model version name |
| `version` | `integer` | `query` | Yes | Model version ID |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "artifact_uri": string, // Download URI for MLflow artifact
}
```

#### 400 - Bad Request

#### 404 - Not Found

