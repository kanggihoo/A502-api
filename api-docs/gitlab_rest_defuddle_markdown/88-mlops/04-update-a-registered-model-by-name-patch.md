# 04-Update a Registered Model by Name [PATCH]

`PATCH /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/registered-models/update`

https://mlflow.org/docs/2.19.0/rest-api.html#update-registeredmodel

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string, // Registered model unique name identifier, in reference to the project
  "description": string, // Optional description for registered model.
}
```
### Responses

#### 200 - OK

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

