# 06-List all pipelines triggered by a pipeline schedule [GET]

`GET /api/v4/projects/{id}/pipeline_schedules/{pipeline_schedule_id}/pipelines`

Lists all pipelines triggered by a pipeline schedule in a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `pipeline_schedule_id` | `integer` | `path` | Yes | The pipeline schedule ID |
| `scope` | `string` | `query` | No | The scope of pipelines |
| `status` | `string` | `query` | No | The status of pipelines |
| `updated_before` | `string` | `query` | No | Return pipelines updated before the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `updated_after` | `string` | `query` | No | Return pipelines updated after the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `created_before` | `string` | `query` | No | Return pipelines created before the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `created_after` | `string` | `query` | No | Return pipelines created after the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `sort` | `string` | `query` | No | Sort pipelines |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "iid": integer,
  "project_id": integer,
  "sha": string,
  "ref": string,
  "status": string,
  "source": string,
  "created_at": string,
  "updated_at": string,
  "web_url": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

