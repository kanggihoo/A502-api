# 18-Revoke a GPG key [POST]

`POST /api/v4/user/gpg_keys/{key_id}/revoke`

This feature was added in GitLab 10.0

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key_id` | `integer` | `path` | Yes | The ID of the GPG key |

### Responses

#### 202 - Accepted

#### 400 - Bad Request

#### 404 - Not Found

