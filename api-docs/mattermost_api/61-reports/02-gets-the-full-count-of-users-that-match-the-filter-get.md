# 02-Gets the full count of users that match the filter. [GET]

`GET /api/v4/reports/users/count`

Get the full count of users admin reporting purposes, based on provided parameters.
##### Permissions
Requires `sysconsole_read_user_management_users`.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `role_filter` | `string` | `query` | No | Filter users by their role. |
| `team_filter` | `string` | `query` | No | Filter users by a specified team ID. |
| `has_no_team` | `boolean` | `query` | No | If true, show only users that have no team. Will ignore provided "team_filter" if true. |
| `hide_active` | `boolean` | `query` | No | If true, show only users that are inactive. Cannot be used at the same time as "hide_inactive" |
| `hide_inactive` | `boolean` | `query` | No | If true, show only users that are active. Cannot be used at the same time as "hide_active" |
| `search_term` | `string` | `query` | No | A filtering search term that allows filtering by Username, FirstName, LastName, Nickname or Email |

### Responses

#### 200 - User count retrieval successful

Schema (application/json):
```json
number
```

