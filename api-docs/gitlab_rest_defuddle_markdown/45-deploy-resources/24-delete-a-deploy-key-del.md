# 24-Delete a deploy key [DEL]

`DELETE /api/v4/projects/{id}/deploy_keys/{key_id}`

Deletes a deploy key from the project. If the deploy key is used only for this project, it is deleted from the system.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `key_id` | `integer` | `path` | Yes | The ID of the deploy key |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

