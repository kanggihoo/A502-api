# 79-Gets the server limits for the server [GET]

`GET /api/v4/limits/server`

Gets the server limits for the server
##### Permissions
Requires `sysconsole_read_user_management_users`.


### Responses

#### 200 - App limits for server

Schema (application/json):
```json
[
  {
    "maxUsersLimit": integer, // The maximum number of users allowed on server
    "activeUserCount": integer, // The number of active users in the server
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

