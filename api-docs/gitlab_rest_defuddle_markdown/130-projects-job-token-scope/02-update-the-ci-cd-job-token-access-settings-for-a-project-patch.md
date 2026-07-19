# 02-Update the CI/CD job token access settings for a project [PATCH]

`PATCH /api/v4/projects/{id}/job_token_scope`

Updates the **Authorized groups and projects** setting (job token scope) of a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "enabled": boolean (required), // Indicates CI/CD job tokens generated in other projects have restricted access to this project.
}
```
### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

