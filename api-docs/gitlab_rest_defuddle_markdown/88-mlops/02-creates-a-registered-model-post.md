# 02-Creates a Registered Model. [POST]

`POST /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/registered-models/create`

MLFlow Registered Models map to GitLab Models. https://mlflow.org/docs/2.19.0/rest-api.html#create-registeredmodel

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // Register models under this name.
  "description": string, // Optional description for registered model.
  "tags": [
    any
  ], // Additional metadata for registered model.
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "name": string,
  "creation_timestamp": integer,
  "last_updated_timestamp": integer,
  "description": string,
  "user_id": string,
  "tags": [
    {
      "key": string,
      "value": string,
    }
  ],
  "latest_versions": [
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
  ],
}
```

#### 400 - Bad Request

#### 404 - Not Found

