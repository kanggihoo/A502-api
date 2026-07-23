# 05-Unprotect repository branches [DEL]

`DELETE /api/v4/groups/{id}/protected_branches/{name}`

Unprotects a specified protected branch Unprotect multiple branches by using a wildcard in the `name`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of a group |
| `name` | `string` | `path` | Yes | The name of the protected branch |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 404 - 404 ProtectedBranch Not Found

