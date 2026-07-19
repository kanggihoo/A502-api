# 06-Delete a project service account [DEL]

`DELETE /api/v4/projects/{id}/service_accounts/{user_id}`

Deletes a specified project service account. Available only for project Owners, Maintainers, and administrators.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `user_id` | `integer` | `path` | Yes | The ID of the service account |
| `hard_delete` | `boolean` | `query` | No | Whether to remove a user's contributions |

### Responses

#### 204 - No Content

#### 400 - 400 Bad request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Project not found

