# 03-Remove member role of a group [DEL]

`DELETE /api/v4/groups/{id}/member_roles/{member_role_id}`

Removes a specified member role from a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `member_role_id` | `integer` | `path` | Yes | The ID of the Group-Member Role to be deleted |

### Responses

#### 204 - 204 No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - 404 Member Role Not Found

