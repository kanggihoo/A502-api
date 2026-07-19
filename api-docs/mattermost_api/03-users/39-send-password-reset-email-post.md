# 39-Send password reset email [POST]

`POST /api/v4/users/password/reset/send`

Send an email containing a link for resetting the user's password. The link will contain a one-use, timed recovery code tied to the user's account. Only works for non-SSO users.
##### Permissions
No permissions required.


### Request Body (application/json)

```json
{
  "email": string (required), // The email of the user
}
```
### Responses

#### 200 - Email sent if account exists

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

