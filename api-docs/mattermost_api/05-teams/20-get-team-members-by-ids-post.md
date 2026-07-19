# 20-Get team members by ids [POST]

`POST /api/v4/teams/{team_id}/members/ids`

Get a list of team members based on a provided array of user ids.
##### Permissions
Must have `view_team` permission for the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 200 - Team members retrieval successful

Schema (application/json):
```json
[
  {
    "team_id": string, // The ID of the team this member belongs to.
    "user_id": string, // The ID of the user this member relates to.
    "roles": string, // The complete list of roles assigned to this team member, as a space-separated list of role names, including any roles granted implicitly through permissions schemes.
    "delete_at": integer, // The time in milliseconds that this team member was deleted.
    "scheme_user": boolean, // Whether this team member holds the default user role defined by the team's permissions scheme.
    "scheme_admin": boolean, // Whether this team member holds the default admin role defined by the team's permissions scheme.
    "explicit_roles": string, // The list of roles explicitly assigned to this team member, as a space separated list of role names. This list does *not* include any roles granted implicitly through permissions schemes.
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

