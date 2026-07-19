# 14-Delete a group service account [DEL]

`DELETE /api/v4/groups/{id}/service_accounts/{user_id}`

Deletes a specified group service account. Available only for group Owners and administrators.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `user_id` | `integer` | `path` | Yes | The ID of the service account |
| `hard_delete` | `boolean` | `query` | No | Whether to remove a user's contributions |

### Responses

#### 204 - Resource deleted

#### 400 - 400 Bad request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Group not found

