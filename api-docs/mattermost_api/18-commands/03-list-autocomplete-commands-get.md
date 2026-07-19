# 03-List autocomplete commands [GET]

`GET /api/v4/teams/{team_id}/commands/autocomplete`

List autocomplete commands in the team.
##### Permissions
`view_team` for the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Responses

#### 200 - Autocomplete commands retrieval successful

Schema (application/json):
```json
[
  {
    "id": string, // The ID of the slash command
    "token": string, // The token which is used to verify the source of the payload
    "create_at": integer, // The time in milliseconds the command was created
    "update_at": integer, // The time in milliseconds the command was last updated
    "delete_at": integer, // The time in milliseconds the command was deleted, 0 if never deleted
    "creator_id": string, // The user id for the commands creator
    "team_id": string, // The team id for which this command is configured
    "trigger": string, // The string that triggers this command
    "method": string, // Is the trigger done with HTTP Get ('G') or HTTP Post ('P')
    "username": string, // What is the username for the response post
    "icon_url": string, // The url to find the icon for this users avatar
    "auto_complete": boolean, // Use auto complete for this command
    "auto_complete_desc": string, // The description for this command shown when selecting the command
    "auto_complete_hint": string, // The hint for this command
    "display_name": string, // Display name for the command
    "description": string, // Description for this command
    "url": string, // The URL that is triggered
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

