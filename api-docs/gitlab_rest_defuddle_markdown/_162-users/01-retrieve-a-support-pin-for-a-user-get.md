# 01-Retrieve a Support PIN for a user [GET]

`GET /api/v4/users/{id}/support_pin`

Retrieves a Support PIN for a specified user. GitLab Support may ask for this PIN to validate your identity. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "pin": string, // The security PIN
  "expires_at": string, // The expiration time of the PIN
}
```

#### 400 - Bad Request

#### 404 - Not Found

