# 13-Check CWS connection [GET]

`GET /api/v4/cloud/check-cws-connection`

Checks whether the Customer Web Server (CWS) is reachable from this instance. Used to detect if the deployment is air-gapped.
##### Permissions
No permissions required.
__Minimum server version__: 5.28 __Note:__ This is intended for internal use and is subject to change.


### Responses

#### 200 - CWS connection status returned successfully

Schema (application/json):
```json
{
  "status": enum("available" | "unavailable"), // Connection status - "available" if CWS is reachable, "unavailable" if not
}
```

