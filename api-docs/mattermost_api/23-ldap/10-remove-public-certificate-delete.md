# 10-Remove public certificate [DELETE]

`DELETE /api/v4/ldap/certificate/public`

Delete the current public certificate being used for TLS verification.
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - LDAP certificate delete successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 401 - 

#### 403 - 

#### 501 - 

