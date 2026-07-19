# 48-Verify user email [POST]

`POST /api/v4/users/email/verify`

Verify the email used by a user to sign-up their account with.
##### Permissions
No permissions required.


### Request Body (application/json)

```json
{
  "token": string (required), // The token given to validate the email
}
```
### Responses

#### 200 - User email verification successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

