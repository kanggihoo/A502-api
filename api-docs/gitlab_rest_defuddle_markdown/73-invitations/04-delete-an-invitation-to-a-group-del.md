# 04-Delete an invitation to a group [DEL]

`DELETE /api/v4/groups/{id}/invitations/{email}`

Deletes a pending invitation to a specified email address for a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The group ID |
| `email` | `string` | `path` | Yes | The email address of the invitation |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

#### 409 - Could not delete invitation

