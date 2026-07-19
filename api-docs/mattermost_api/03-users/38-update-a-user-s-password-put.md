# 38-Update a user's password [PUT]

`PUT /api/v4/users/{user_id}/password`

Update a user's password. New password must meet password policy set by server configuration. Current password is required if you're updating your own password.
##### Permissions
Must be logged in as the user the password is being changed for or have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "current_password": string, // The current password for the user
  "new_password": string (required), // The new password for the user
}
```
### Responses

#### 200 - User password update successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

