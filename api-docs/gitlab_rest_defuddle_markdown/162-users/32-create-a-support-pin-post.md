# 32-Create a Support PIN [POST]

`POST /api/v4/user/support_pin`

Creates a Support PIN. The PIN expires seven days after creation. GitLab Support may ask for this PIN to validate your identity.

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "pin": string, // The security PIN
  "expires_at": string, // The expiration time of the PIN
}
```

#### 400 - Bad Request

