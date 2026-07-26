# 40-Set the server busy (high load) flag [POST]

`POST /api/v4/server_busy`

Marks the server as currently having high load which disables non-critical services such as search, statuses and typing notifications.

__Minimum server version__: 5.20

##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `seconds` | `string` | `query` | No | Number of seconds until server is automatically marked as not busy. |

### Responses

#### 200 - Server busy flag set successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 403 - 

