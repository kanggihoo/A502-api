# 11-Add an SSH key [POST]

`POST /api/v4/user/keys`

Adds an SSH key for the currently authenticated user.

### Request Body (application/json)

```json
{
  "key": string (required), // The new SSH key
  "title": string (required), // The title of the new SSH key
  "expires_at": string, // The expiration date of the SSH key in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
  "usage_type": enum("auth_and_signing" | "auth" | "signing"), // Scope of usage for the SSH key
}
```
### Responses

#### 201 - Created

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

