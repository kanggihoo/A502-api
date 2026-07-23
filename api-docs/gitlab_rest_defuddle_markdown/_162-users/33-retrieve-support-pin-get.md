# 33-Retrieve Support PIN [GET]

`GET /api/v4/user/support_pin`

Retrieves a Support PIN for the currently authenticated user. GitLab Support may ask for this PIN to validate your identity.

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "pin": string, // The security PIN
  "expires_at": string, // The expiration time of the PIN
}
```

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

