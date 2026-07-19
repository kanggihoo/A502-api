# 43-Revoke all active sessions for a user [POST]

`POST /api/v4/users/{user_id}/sessions/revoke/all`

Revokes all user sessions from the provided user id and session id strings.
##### Permissions
Must be logged in as the user being updated or have the `edit_other_users` permission.
__Minimum server version__: 4.4


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - User sessions revoked successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

