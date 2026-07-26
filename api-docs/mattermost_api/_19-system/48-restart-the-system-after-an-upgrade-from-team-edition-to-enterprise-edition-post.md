# 48-Restart the system after an upgrade from Team Edition to Enterprise Edition [POST]

`POST /api/v4/restart`

It restarts the current running mattermost instance to execute the new Enterprise binary.
__Minimum server version__: 5.27
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Restart started

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 403 - 

