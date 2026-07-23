# 16-Add multiple users to team [POST]

`POST /api/v4/teams/{team_id}/members/batch`

Add a number of users to the team by user_id.
##### Permissions
Must be authenticated. Authenticated user must have the `add_user_to_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `graceful` | `boolean` | `query` | No | Instead of aborting the operation if a user cannot be added, return an arrray that will contain both the success and added members and the ones with error, in form of `[{"member": {...}, "user_id", "...", "error": {...}}]` |

### Request Body (application/json)

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
### Responses

#### 201 - Team members created successfully.

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

#### 404 - 

