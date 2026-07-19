# 08-Run a pipeline schedule [POST]

`POST /api/v4/projects/{id}/pipeline_schedules/{pipeline_schedule_id}/play`

Runs a pipeline schedule immediately. The next scheduled run of this pipeline is not affected.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `pipeline_schedule_id` | `integer` | `path` | Yes | The pipeline schedule id |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

