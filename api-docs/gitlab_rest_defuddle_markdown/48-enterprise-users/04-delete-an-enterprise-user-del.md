# 04-Delete an enterprise user [DEL]

`DELETE /api/v4/groups/{id}/enterprise_users/{user_id}`

Deletes a specified enterprise user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `user_id` | `integer` | `path` | Yes | ID of user account. |
| `hard_delete` | `boolean` | `query` | No | If `false`, deletes the user and moves their contributions to a system-wide "Ghost User". If `true`, deletes the user, their associated contributions, and any groups owned solely by the user. Default value: `false`. |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

