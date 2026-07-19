# 07-Search Registered Models within a project [GET]

`GET /api/v4/projects/{id}/ml/mlflow/api/2.0/mlflow/registered-models/search`

https://mlflow.org/docs/2.19.0/rest-api.html#search-registeredmodels

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `filter` | `string` | `query` | No | Filter to search models. must be in the format `name='value'`. Only filtering by name is supported |
| `max_results` | `integer` | `query` | No | Maximum number of models desired. Default is 200. Max threshold is 1000. |
| `order_by` | `string` | `query` | No | Order criteria. Can be by name or last_updated_timestamp, with optional DESC or ASC (default)Valid examples: `name`, `name DESC`, `last_updated_timestamp DESC`Sorting by model metadata is not supported. |
| `page_token` | `string` | `query` | No | Token for pagination |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

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

