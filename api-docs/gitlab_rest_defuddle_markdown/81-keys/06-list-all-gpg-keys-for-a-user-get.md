# 06-List all GPG keys for a user [GET]

`GET /api/v4/users/{id}/gpg_keys`

Lists all GPG keys for a specified user account. This endpoint does not require authentication.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

