# 12-Recycle database connections [POST]

`POST /api/v4/database/recycle`

Recycle database connections by closing and reconnecting all connections to master and read replica databases.
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Database recycle successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 403 - 

