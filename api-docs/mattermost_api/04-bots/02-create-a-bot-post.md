# 02-Create a bot [POST]

`POST /api/v4/bots`

Create a new bot account on the system. Username is required.
##### Permissions
Must have `create_bot` permission.
__Minimum server version__: 5.10


### Request Body (application/json)

```json
{
  "username": string (required),
  "display_name": string,
  "description": string,
}
```
### Responses

#### 201 - Bot creation successful

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

