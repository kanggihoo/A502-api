# 41-Get server busy expiry time. [GET]

`GET /api/v4/server_busy`

Gets the timestamp corresponding to when the server busy flag will be automatically cleared.

__Minimum server version__: 5.20

##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Server busy expires timestamp retrieved successfully

Schema (application/json):
```json
{
  "busy": boolean, // True if the server is marked as busy (under high load)
  "expires": integer, // timestamp - number of seconds since Jan 1, 1970 UTC.
}
```

#### 403 - 

