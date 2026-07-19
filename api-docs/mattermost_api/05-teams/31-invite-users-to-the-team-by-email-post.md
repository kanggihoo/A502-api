# 31-Invite users to the team by email [POST]

`POST /api/v4/teams/{team_id}/invite/email`

Invite users to the existing team using the user's email.

The number of emails that can be sent is rate limited to 20 per hour with a burst of 20 emails. If the rate limit exceeds, the error message contains details on when to retry and when the timer will be reset.
##### Permissions
Must have `invite_user` and `add_user_to_team` permissions for the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 200 - Users invite successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 413 - 

