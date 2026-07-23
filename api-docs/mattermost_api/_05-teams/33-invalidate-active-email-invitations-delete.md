# 33-Invalidate active email invitations [DELETE]

`DELETE /api/v4/teams/invites/email`

Invalidate active email invitations that have not been accepted by the user.
##### Permissions
Must have `sysconsole_write_authentication` permission.


### Responses

#### 200 - Email invites successfully revoked

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

