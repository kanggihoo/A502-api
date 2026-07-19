# 05-Disable two-factor authentication for an enterprise user [PATCH]

`PATCH /api/v4/groups/{id}/enterprise_users/{user_id}/disable_two_factor`

Disables two-factor authentication (2FA) for a specified enterprise user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `user_id` | `integer` | `path` | Yes | ID of user account. |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

