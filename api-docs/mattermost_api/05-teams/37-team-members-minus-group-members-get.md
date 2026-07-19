# 37-Team members minus group members. [GET]

`GET /api/v4/teams/{team_id}/members_minus_group_members`

Get the set of users who are members of the team minus the set of users who are members of the given groups.
Each user object contains an array of group objects representing the group memberships for that user.
Each user object contains the boolean fields `scheme_guest`, `scheme_user`, and `scheme_admin` representing the roles that user has for the given team.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.14


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `group_ids` | `string` | `query` | Yes | A comma-separated list of group ids. |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of users per page. |

### Responses

#### 200 - Successfully returns users specified by the pagination, and the total_count.

#### 400 - 

#### 401 - 

#### 403 - 

