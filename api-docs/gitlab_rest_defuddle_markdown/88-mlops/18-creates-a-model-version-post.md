# 18-Creates a Model Version. [POST]

`POST /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/model-versions/create`

MLFlow Model Versions map to GitLab Model Versions. https://mlflow.org/docs/2.19.0/rest-api.html#create-modelversion

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string, // Register model under this name This field is required.
  "description": string, // Optional description for model version.
  "tags": [
    any
  ], // Additional metadata for a model version.
  "run_id": string, // Run ID of the candidate to be promoted to a model version
}
```
### Responses

#### 201 - Created

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

