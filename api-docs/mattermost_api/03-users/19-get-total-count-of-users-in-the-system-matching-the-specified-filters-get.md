# 19-Get total count of users in the system matching the specified filters [GET]

`GET /api/v4/users/stats/filtered`

Get a count of users in the system matching the specified filters.

__Minimum server version__: 5.26

##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `in_team` | `string` | `query` | No | The ID of the team to get user stats for. |
| `in_channel` | `string` | `query` | No | The ID of the channel to get user stats for. |
| `include_deleted` | `boolean` | `query` | No | If deleted accounts should be included in the count. |
| `include_bots` | `boolean` | `query` | No | If bot accounts should be included in the count. |
| `roles` | `string` | `query` | No | Comma separated string used to filter users based on any of the specified system roles<br><br>Example: `?roles=system_admin,system_user` will include users that are either system admins or system users<br> |
| `channel_roles` | `string` | `query` | No | Comma separated string used to filter users based on any of the specified channel roles, can only be used in conjunction with `in_channel`<br><br>Example: `?in_channel=4eb6axxw7fg3je5iyasnfudc5y&channel_roles=channel_user` will include users that are only channel users and not admins or guests<br> |
| `team_roles` | `string` | `query` | No | Comma separated string used to filter users based on any of the specified team roles, can only be used in conjunction with `in_team`<br><br>Example: `?in_team=4eb6axxw7fg3je5iyasnfudc5y&team_roles=team_user` will include users that are only team users and not admins or guests<br> |

### Responses

#### 200 - Filtered User stats retrieval successful

Schema (application/json):
```json
{
  "total_users_count": integer,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

