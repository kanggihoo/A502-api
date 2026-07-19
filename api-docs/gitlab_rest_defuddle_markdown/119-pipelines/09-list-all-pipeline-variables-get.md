# 09-List all pipeline variables [GET]

`GET /api/v4/projects/{id}/pipelines/{pipeline_id}/variables`

Lists all pipeline variables for a specified pipeline. Use the `page` and `per_page` pagination parameters to control the pagination of results.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID or URL-encoded path |
| `pipeline_id` | `integer` | `path` | Yes | The pipeline ID |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "variable_type": string,
  "key": string,
  "value": string,
  "hidden": boolean,
  "protected": boolean,
  "masked": boolean,
  "raw": boolean,
  "environment_scope": string,
  "description": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

