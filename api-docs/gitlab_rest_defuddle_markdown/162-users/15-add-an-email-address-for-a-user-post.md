# 15-Add an email address for a user [POST]

`POST /api/v4/users/{id}/emails`

Adds an email address for a specified user account. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |

### Request Body (application/json)

```json
{
  "email": string (required), // The email of the user
  "skip_confirmation": boolean, // Skip confirmation of email and assume it is verified
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

#### 404 - Not Found

