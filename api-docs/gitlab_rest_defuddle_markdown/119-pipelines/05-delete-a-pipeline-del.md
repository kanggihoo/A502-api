# 05-Delete a pipeline [DEL]

`DELETE /api/v4/projects/{id}/pipelines/{pipeline_id}`

Deletes a specified pipeline for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID or URL-encoded path |
| `pipeline_id` | `integer` | `path` | Yes | The pipeline ID |

### Responses

#### 204 - Pipeline was deleted

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

