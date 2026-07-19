# 04-Delete an SSH key for a user [DEL]

`DELETE /api/v4/users/{id}/keys/{key_id}`

Deletes an SSH key from a specified user account. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |
| `key_id` | `integer` | `path` | Yes | The ID of the SSH key |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": integer,
  "title": string,
  "created_at": string,
  "expires_at": string,
  "last_used_at": string,
  "key": string,
  "usage_type": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

