# 06-Logout from the Mattermost server [POST]

`POST /api/v4/users/logout`

##### Permissions
An active session is required


### Responses

#### 201 - User logout successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 403 - 

