# 16-List all email addresses for a user [GET]

`GET /api/v4/users/{id}/emails`

Lists all email addresses for a specified user account. Administrators only.

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
  "id": string,
  "email": string,
  "confirmed_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

