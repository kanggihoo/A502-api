# 17-Delete a GPG key [DEL]

`DELETE /api/v4/user/gpg_keys/{key_id}`

Deletes a GPG key from your user account.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key_id` | `integer` | `path` | Yes | The ID of the SSH key |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

