# 49-Send verification email [POST]

`POST /api/v4/users/email/verify/send`

Send an email with a verification link to a user that has an email matching the one in the request body. This endpoint will return success even if the email does not match any users on the system.
##### Permissions
No permissions required.


### Request Body (application/json)

```json
{
  "email": string (required), // Email of a user
}
```
### Responses

#### 200 - Email send successful if email exists

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

