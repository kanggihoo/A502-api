# 37-Delete an email address [DEL]

`DELETE /api/v4/user/emails/{email_id}`

Deletes the specified email address. You cannot delete a primary email address. Any future emails sent to the deleted email address are sent to the primary email address instead.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `email_id` | `integer` | `path` | Yes | The ID of the email |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

