# 30-Get unreads for a team [GET]

`GET /api/v4/users/{user_id}/teams/{team_id}/unread`

Get the unread mention and message counts for a team for the specified user.
##### Permissions
Must be the user or have `edit_other_users` permission and have `view_team` permission for the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Responses

#### 200 - Team unread count retrieval successful

Schema (application/json):
```json
{
  "team_id": string,
  "msg_count": integer,
  "mention_count": integer,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

