# 66-Revoke all sessions from all users. [POST]

`POST /api/v4/users/sessions/revoke/all`

For any session currently on the server (including admin) it will be revoked.
Clients will be notified to log out users.

__Minimum server version__: 5.14

##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Sessions successfully revoked.

#### 401 - 

#### 403 - 

