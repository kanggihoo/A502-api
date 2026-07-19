# 01-Mark all channels and threads in a team as read [PUT]

`PUT /api/v4/users/{user_id}/teams/{team_id}/read`

Mark all channels and threads in a team as read for a user.

##### Permissions

Must be logged in as user or have `edit_other_users` permission. Must have `view_team` permission for the team.

__Minimum server version__: 11.3


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User ID to mark channels as read for |
| `team_id` | `string` | `path` | Yes | Team ID to mark all channels as read in |

### Responses

#### 200 - Team channels marked as read successfully

Schema (application/json):
```json
{
  "status": string, // Value should be "OK" if successful
  "last_viewed_at_times": {}, // A JSON object mapping channel IDs to the last viewed times
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 501 - 

