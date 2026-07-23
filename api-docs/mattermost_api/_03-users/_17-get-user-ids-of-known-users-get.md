# 17-Get user IDs of known users [GET]

`GET /api/v4/users/known`

Get the list of user IDs of users with any direct relationship with a
user. That means any user sharing any channel, including direct and
group channels.
##### Permissions
Must be authenticated.

__Minimum server version__: 5.23


### Responses

#### 200 - Known users' IDs retrieval successful

Schema (application/json):
```json
any
```

#### 401 - 

