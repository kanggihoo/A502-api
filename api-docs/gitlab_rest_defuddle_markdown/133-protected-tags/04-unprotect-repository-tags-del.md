# 04-Unprotect repository tags [DEL]

`DELETE /api/v4/projects/{id}/protected_tags/{name}`

Unprotects a specified protected tag or wildcard protected tag.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `name` | `string` | `path` | Yes | The name of the protected tag |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not found

#### 412 - Precondition Failed

