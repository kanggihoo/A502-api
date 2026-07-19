# 02-List commands for a team [GET]

`GET /api/v4/commands`

List commands for a team.
##### Permissions
`manage_slash_commands` if need list custom commands.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `query` | No | The team id. |
| `custom_only` | `boolean` | `query` | No | To get only the custom commands. If set to false will get the custom<br>if the user have access plus the system commands, otherwise just the system commands.<br> |

### Responses

#### 200 - List Commands retrieve successful

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

#### 501 - 

