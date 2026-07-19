# 08-Delete a project from a CI/CD job token allowlist [DEL]

`DELETE /api/v4/projects/{id}/job_token_scope/allowlist/{target_project_id}`

Deletes a project from the CI/CD job token allowlist of a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of user project |
| `target_project_id` | `integer` | `path` | Yes | ID of the project to be removed from the allowlist |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

