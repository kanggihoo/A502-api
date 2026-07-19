# 07-Retrieve a GPG key for a user [GET]

`GET /api/v4/users/{id}/gpg_keys/{key_id}`

Retrieves a GPG key for a specified user account. This endpoint does not require authentication.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |
| `key_id` | `integer` | `path` | Yes | The ID of the GPG key |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "key": string,
  "created_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

