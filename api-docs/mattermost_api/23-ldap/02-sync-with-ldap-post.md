# 02-Sync with LDAP [POST]

`POST /api/v4/ldap/sync`

Synchronize any user attribute changes in the configured AD/LDAP server with Mattermost.
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - LDAP sync successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 501 - 

