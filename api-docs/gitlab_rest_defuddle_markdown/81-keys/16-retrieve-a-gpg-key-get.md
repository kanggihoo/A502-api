# 16-Retrieve a GPG key [GET]

`GET /api/v4/user/gpg_keys/{key_id}`

Retrieves a GPG key for the currently authenticated user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
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

