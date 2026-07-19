# 14-Send a test notification [POST]

`POST /api/v4/notifications/test`

Send a test notification to make sure you have your notification settings configured correctly.
##### Permissions
Must be logged in.


### Responses

#### 200 - Notification successfully sent

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 403 - 

#### 500 - 

