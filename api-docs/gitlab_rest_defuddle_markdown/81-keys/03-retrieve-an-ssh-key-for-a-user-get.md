# 03-Retrieve an SSH key for a user [GET]

`GET /api/v4/users/{id}/keys/{key_id}`

Retrieves an SSH key for a specified user account. This endpoint does not require authentication.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |
| `key_id` | `integer` | `path` | Yes | The ID of the SSH key |

### Responses

#### 200 - OK

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

