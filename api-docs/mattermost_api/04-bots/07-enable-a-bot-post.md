# 07-Enable a bot [POST]

`POST /api/v4/bots/{bot_user_id}/enable`

Enable a bot.
##### Permissions
Must have `manage_bots` permission. 
__Minimum server version__: 5.10


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `bot_user_id` | `string` | `path` | Yes | Bot user ID |

### Responses

#### 200 - Bot successfully enabled.

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

