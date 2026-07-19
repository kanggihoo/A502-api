# 30-Add an email address [POST]

`POST /api/v4/user/emails`

Adds an email address for the currently authenticated user.

### Request Body (application/json)

```json
{
  "email": string (required), // The new email
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": string,
  "email": string,
  "confirmed_at": string,
}
```

#### 400 - Bad Request

