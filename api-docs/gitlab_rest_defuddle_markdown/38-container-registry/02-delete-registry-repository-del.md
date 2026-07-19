# 02-Delete registry repository [DEL]

`DELETE /api/v4/projects/{id}/registry/repositories/{repository_id}`

Deletes a specified repository in the registry. This operation is executed asynchronously and might take some time to execute.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `repository_id` | `integer` | `path` | Yes | The ID of the repository |

### Responses

#### 204 - Success

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

