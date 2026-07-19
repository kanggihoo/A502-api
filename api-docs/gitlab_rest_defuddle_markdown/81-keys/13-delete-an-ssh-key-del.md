# 13-Delete an SSH key [DEL]

`DELETE /api/v4/user/keys/{key_id}`

Deletes a specified SSH key from the currently authenticated user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
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

