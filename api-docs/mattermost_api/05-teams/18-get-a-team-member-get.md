# 18-Get a team member [GET]

`GET /api/v4/teams/{team_id}/members/{user_id}`

Get a team member on the system.
##### Permissions
Must be authenticated and have the `view_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - Team member retrieval successful

Schema (application/json):
```json
{
  "team_id": string, // The ID of the team this member belongs to.
  "user_id": string, // The ID of the user this member relates to.
  "roles": string, // The complete list of roles assigned to this team member, as a space-separated list of role names, including any roles granted implicitly through permissions schemes.
  "delete_at": integer, // The time in milliseconds that this team member was deleted.
  "scheme_user": boolean, // Whether this team member holds the default user role defined by the team's permissions scheme.
  "scheme_admin": boolean, // Whether this team member holds the default admin role defined by the team's permissions scheme.
  "explicit_roles": string, // The list of roles explicitly assigned to this team member, as a space separated list of role names. This list does *not* include any roles granted implicitly through permissions schemes.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

