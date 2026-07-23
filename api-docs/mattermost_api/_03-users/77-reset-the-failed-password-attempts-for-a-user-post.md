# 77-Reset the failed password attempts for a user [POST]

`POST /api/v4/users/{user_id}/reset_failed_attempts`

Reset the FailedAttempts field for a user to 0. This will only work for ldap and email/password users.

##### Permissions

Requires `sysconsole_write_user_management_users` permission.


### Responses

#### 200 - User's thread update successful

#### 400 - 

#### 401 - 

#### 404 - 

