# 08-Delete an SSH key for an enterprise user [DEL]

`DELETE /api/v4/groups/{id}/manage/ssh_keys/{key_id}`

Deletes a specified SSH public key for an enterprise user associated with the top-level group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `key_id` | `any` | `path` | Yes |  |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

