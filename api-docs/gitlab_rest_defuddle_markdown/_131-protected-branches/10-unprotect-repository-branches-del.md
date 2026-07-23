# 10-Unprotect repository branches [DEL]

`DELETE /api/v4/projects/{id}/protected_branches/{name}`

Unprotects a specified protected branch or wildcard protected branch.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `name` | `string` | `path` | Yes | The name of the protected branch |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 404 - 404 Project Not Found

