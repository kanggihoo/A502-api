# 10-Retrieve a variable for a pipeline schedule [GET]

`GET /api/v4/projects/{id}/pipeline_schedules/{pipeline_schedule_id}/variables/{key}`

Retrieves a specified variable for a pipeline schedule.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `pipeline_schedule_id` | `integer` | `path` | Yes | The pipeline schedule id |
| `key` | `string` | `path` | Yes | The key of the variable |

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

