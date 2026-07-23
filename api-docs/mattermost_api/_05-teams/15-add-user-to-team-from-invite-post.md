# 15-Add user to team from invite [POST]

`POST /api/v4/teams/members/invite`

Using either an invite id or hash/data pair from an email invite link, add a user to a team.
##### Permissions
Must be authenticated.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `token` | `string` | `query` | Yes | Token id from the invitation |

### Responses

#### 201 - Team member creation successful

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

