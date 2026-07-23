# 13-Get team members [GET]

`GET /api/v4/teams/{team_id}/members`

Get a page team members list based on query string parameters - team id, page and per page.
##### Permissions
Must be authenticated and have the `view_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of users per page. |
| `sort` | `string` | `query` | No | To sort by Username, set to 'Username', otherwise sort is by 'UserID' |
| `exclude_deleted_users` | `boolean` | `query` | No | Excludes deleted users from the results |

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

#### 404 - 

