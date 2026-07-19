# 12-Remove private key [DELETE]

`DELETE /api/v4/ldap/certificate/private`

Delete the current private key being used with your TLS verification.
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

