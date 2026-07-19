# 17-Delete an email address for a user [DEL]

`DELETE /api/v4/users/{id}/emails/{email_id}`

Deletes a specified email address for a user account. You cannot delete a primary email address. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |
| `email_id` | `integer` | `path` | Yes | The ID of the email |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": string,
  "email": string,
  "confirmed_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

