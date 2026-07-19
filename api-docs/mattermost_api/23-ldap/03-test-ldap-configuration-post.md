# 03-Test LDAP configuration [POST]

`POST /api/v4/ldap/test`

Test the current AD/LDAP configuration to see if the AD/LDAP server can be contacted successfully.
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - LDAP test successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 500 - 

#### 501 - 

