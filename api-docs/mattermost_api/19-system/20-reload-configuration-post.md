# 20-Reload configuration [POST]

`POST /api/v4/config/reload`

Reload the configuration file to pick up on any changes made to it.
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Configuration reload successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 403 - 

