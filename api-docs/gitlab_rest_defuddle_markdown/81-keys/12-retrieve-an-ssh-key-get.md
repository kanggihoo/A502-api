# 12-Retrieve an SSH key [GET]

`GET /api/v4/user/keys/{key_id}`

Retrieves a specified SSH key for the currently authenticated user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
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

