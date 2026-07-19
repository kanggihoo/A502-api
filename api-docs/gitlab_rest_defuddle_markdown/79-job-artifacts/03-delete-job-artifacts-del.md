# 03-Delete job artifacts [DEL]

`DELETE /api/v4/projects/{id}/jobs/{job_id}/artifacts`

Deletes job artifacts from a specified job in a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `job_id` | `integer` | `path` | Yes | The ID of a job |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

#### 409 - Conflict

