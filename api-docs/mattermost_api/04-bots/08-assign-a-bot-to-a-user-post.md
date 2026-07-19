# 08-Assign a bot to a user [POST]

`POST /api/v4/bots/{bot_user_id}/assign/{user_id}`

Assign a bot to a specified user.
##### Permissions
Must have `manage_bots` permission. 
__Minimum server version__: 5.10


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `bot_user_id` | `string` | `path` | Yes | Bot user ID |
| `user_id` | `string` | `path` | Yes | The user ID to assign the bot to. |

### Responses

#### 200 - Bot successfully assigned.

Schema (application/json):
```json
{
  "user_id": string, // The user id of the associated user entry.
  "create_at": integer, // The time in milliseconds a bot was created
  "update_at": integer, // The time in milliseconds a bot was last updated
  "delete_at": integer, // The time in milliseconds a bot was deleted
  "username": string,
  "display_name": string,
  "description": string,
  "owner_id": string, // The user id of the user that currently owns this bot.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

