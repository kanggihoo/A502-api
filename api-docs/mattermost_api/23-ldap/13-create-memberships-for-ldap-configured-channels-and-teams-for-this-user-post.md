# 13-Create memberships for LDAP configured channels and teams for this user [POST]

`POST /api/v4/ldap/users/{user_id}/group_sync_memberships`

Add the user to each channel and team configured for each LDAP group of whicht the user is a member.
##### Permissions
Must have `sysconsole_write_user_management_groups` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User Id |

### Responses

#### 200 - Channel and team memberships created as needed.

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

