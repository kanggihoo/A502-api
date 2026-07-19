# 42-Clears the server busy (high load) flag [DELETE]

`DELETE /api/v4/server_busy`

Marks the server as not having high load which re-enables non-critical services such as search, statuses and typing notifications.

__Minimum server version__: 5.20

##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Server busy flag cleared successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 403 - 

