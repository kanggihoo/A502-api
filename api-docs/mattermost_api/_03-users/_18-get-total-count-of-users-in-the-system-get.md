# 18-Get total count of users in the system [GET]

`GET /api/v4/users/stats`

Get a total count of users in the system.
##### Permissions
Must be authenticated.


### Responses

#### 200 - User stats retrieval successful

Schema (application/json):
```json
{
  "total_users_count": integer,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

