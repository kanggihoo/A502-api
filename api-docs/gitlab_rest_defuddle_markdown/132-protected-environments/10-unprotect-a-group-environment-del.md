# 10-Unprotect a group environment [DEL]

`DELETE /api/v4/groups/{id}/protected_environments/{name}`

Unprotects a specified protected environment for a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group maintained by the authenticated user |
| `name` | `string` | `path` | Yes | The tier name of the protected environment |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

