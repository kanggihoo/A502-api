# 12-Get a user's teams [GET]

`GET /api/v4/users/{user_id}/teams`

Get a list of teams that a user is on.
##### Permissions
Must be authenticated as the user or have the `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - Team list retrieval successful

Schema (application/json):
```json
[
  {
    "id": string,
    "create_at": integer, // The time in milliseconds a team was created
    "update_at": integer, // The time in milliseconds a team was last updated
    "delete_at": integer, // The time in milliseconds a team was deleted
    "display_name": string,
    "name": string,
    "description": string,
    "email": string,
    "type": string,
    "allowed_domains": string,
    "invite_id": string,
    "allow_open_invite": boolean,
    "policy_id": string, // The data retention policy to which this team has been assigned. If no such policy exists, or the caller does not have the `sysconsole_read_compliance_data_retention` permission, this field will be null.
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

