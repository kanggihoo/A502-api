# 07-Remove public certificate [DELETE]

`DELETE /api/v4/saml/certificate/public`

Delete the current public certificate being used with your SAML configuration. This will also disable encryption for SAML on your system as this certificate is required for that.
##### Permissions
Must have `sysconsole_write_authentication` permission.


### Responses

#### 200 - SAML certificate delete successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 401 - 

#### 403 - 

#### 501 - 

