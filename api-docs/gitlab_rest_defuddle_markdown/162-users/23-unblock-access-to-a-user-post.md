# 23-Unblock access to a user [POST]

`POST /api/v4/users/{id}/unblock`

Unblocks a specified user account that was previously blocked. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

