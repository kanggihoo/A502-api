# 14-Add user to team [POST]

`POST /api/v4/teams/{team_id}/members`

Add user to the team by user_id.
##### Permissions
Must be authenticated and team be open to add self. For adding another user, authenticated user must have the `add_user_to_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Request Body (application/json)

```json
{
  "team_id": string,
  "user_id": string,
}
```
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

