# 03-Get user statuses by id [POST]

`POST /api/v4/users/status/ids`

Get a list of user statuses by id from the server.
##### Permissions
Must be authenticated.


### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 200 - User statuses retrieval successful

Schema (application/json):
```json
[
  {
    "user_id": string,
    "status": string,
    "manual": boolean,
    "last_activity_at": integer,
  }
]
```

#### 400 - 

#### 401 - 

