# 05-Delete a pipeline schedule [DEL]

`DELETE /api/v4/projects/{id}/pipeline_schedules/{pipeline_schedule_id}`

Deletes a pipeline schedule for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `pipeline_schedule_id` | `integer` | `path` | Yes | The pipeline schedule id |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 412 - Precondition Failed

