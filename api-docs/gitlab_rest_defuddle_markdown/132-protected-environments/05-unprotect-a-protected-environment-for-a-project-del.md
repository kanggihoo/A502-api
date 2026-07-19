# 05-Unprotect a protected environment for a project [DEL]

`DELETE /api/v4/projects/{id}/protected_environments/{name}`

Unprotects a specified protected environment for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `name` | `string` | `path` | Yes | The name of the protected environment |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

