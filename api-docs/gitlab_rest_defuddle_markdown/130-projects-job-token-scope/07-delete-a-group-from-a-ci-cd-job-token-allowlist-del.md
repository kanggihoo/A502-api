# 07-Delete a group from a CI/CD job token allowlist [DEL]

`DELETE /api/v4/projects/{id}/job_token_scope/groups_allowlist/{target_group_id}`

Deletes a group from the CI/CD job token allowlist of a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of user project |
| `target_group_id` | `integer` | `path` | Yes | ID of the group to be removed from the allowlist |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

