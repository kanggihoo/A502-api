# 06-Delete all job artifacts in a project [DEL]

`DELETE /api/v4/projects/{id}/artifacts`

Deletes job artifacts from all jobs in a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 202 - Accepted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

#### 409 - Conflict

