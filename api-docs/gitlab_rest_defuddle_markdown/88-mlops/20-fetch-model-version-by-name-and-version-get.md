# 20-Fetch model version by name and version [GET]

`GET /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/model-versions/get`

https://mlflow.org/docs/2.19.0/rest-api.html#get-modelversion

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `query` | Yes | Model version name |
| `version` | `string` | `query` | Yes | Model version number |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "version": string,
  "creation_timestamp": integer,
  "last_updated_timestamp": integer,
  "user_id": string,
  "current_stage": string,
  "description": string,
  "source": string,
  "run_id": string,
  "status": string,
  "status_message": string,
  "tags": [
    {
      "key": string,
      "value": string,
    }
  ],
  "run_link": string,
  "aliases": [
    string
  ],
}
```

#### 400 - Bad Request

#### 404 - Not Found

