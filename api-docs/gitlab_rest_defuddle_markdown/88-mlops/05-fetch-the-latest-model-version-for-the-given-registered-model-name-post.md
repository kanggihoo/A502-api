# 05-Fetch the latest Model Version for the given Registered Model Name [POST]

`POST /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/registered-models/get-latest-versions`

https://mlflow.org/docs/2.19.0/rest-api.html#get-latest-modelversions

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string, // Registered model unique name identifier, in reference to the project
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

