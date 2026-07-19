# 08-Delete a GPG key for a user [DEL]

`DELETE /api/v4/users/{id}/gpg_keys/{key_id}`

Deletes a GPG key from a specified user account. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |
| `key_id` | `integer` | `path` | Yes | The ID of the GPG key |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

