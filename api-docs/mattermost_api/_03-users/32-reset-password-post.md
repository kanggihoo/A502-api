# 32-Reset password [POST]

`POST /api/v4/users/password/reset`

Update the password for a user using a one-use, timed recovery code tied to the user's account. Only works for non-SSO users.
##### Permissions
No permissions required.


### Request Body (application/json)

```json
{
  "code": string (required), // The recovery code
  "new_password": string (required), // The new password for the user
}
```
### Responses

#### 200 - User password update successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

