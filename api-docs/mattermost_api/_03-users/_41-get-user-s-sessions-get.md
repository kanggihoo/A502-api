# 41-Get user's sessions [GET]

`GET /api/v4/users/{user_id}/sessions`

Get a list of sessions by providing the user GUID. Sensitive information will be sanitized out.
##### Permissions
Must be logged in as the user being updated or have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - User session retrieval successful

Schema (application/json):
```json
[
  {
    "create_at": integer, // The time in milliseconds a session was created
    "device_id": string,
    "voip_device_id": string, // VoIP push token. Same prefix shape as device_id.
    "expires_at": integer, // The time in milliseconds a session will expire
    "id": string,
    "is_oauth": boolean,
    "last_activity_at": integer, // The time in milliseconds of the last activity of a session
    "props": {},
    "roles": string,
    "team_members": [
      {
        "team_id": string, // The ID of the team this member belongs to.
        "user_id": string, // The ID of the user this member relates to.
        "roles": string, // The complete list of roles assigned to this team member, as a space-separated list of role names, including any roles granted implicitly through permissions schemes.
        "delete_at": integer, // The time in milliseconds that this team member was deleted.
        "scheme_user": boolean, // Whether this team member holds the default user role defined by the team's permissions scheme.
        "scheme_admin": boolean, // Whether this team member holds the default admin role defined by the team's permissions scheme.
        "explicit_roles": string, // The list of roles explicitly assigned to this team member, as a space separated list of role names. This list does *not* include any roles granted implicitly through permissions schemes.
      }
    ],
    "token": string,
    "user_id": string,
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

