# 02-Revoke a Support PIN for a user [POST]

`POST /api/v4/users/{id}/support_pin/revoke`

Revokes a Support PIN for a specified user. This immediately expires and removes the PIN. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

