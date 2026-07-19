# 08-Deny an access request [DEL]

`DELETE /api/v4/projects/{id}/access_requests/{user_id}`

Denies an access request for a specified user in a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `user_id` | `integer` | `path` | Yes | The user ID of the access requester |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

