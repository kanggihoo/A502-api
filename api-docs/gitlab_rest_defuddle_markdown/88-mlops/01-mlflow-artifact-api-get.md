# 01-MLflow artifact API [GET]

`GET /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow-artifacts/artifacts`

MLflow artifacts mapping to GitLab artifacts

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `path` | `string` | `query` | No | Path to the artifact, model version id, optionally followed by path. E.g. 15/MLmodel |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

