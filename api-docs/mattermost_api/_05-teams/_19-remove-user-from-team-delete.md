# 19-Remove user from team [DELETE]

`DELETE /api/v4/teams/{team_id}/members/{user_id}`

Delete the team member object for a user, effectively removing them from a team.
##### Permissions
Must be logged in as the user or have the `remove_user_from_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - Team member deletion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

