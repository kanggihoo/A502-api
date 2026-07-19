# 09-Revoke a GPG key for a user. [POST]

`POST /api/v4/users/{id}/gpg_keys/{key_id}/revoke`

Deletes a GPG key from a specified user account. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |
| `key_id` | `integer` | `path` | Yes | The ID of the GPG key |

### Responses

#### 202 - Accepted

#### 400 - Bad Request

#### 404 - Not Found

