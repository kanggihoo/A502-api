# 03-Get bots [GET]

`GET /api/v4/bots`

Get a page of a list of bots.
##### Permissions
Must have `read_bots` permission for bots you are managing, and `read_others_bots` permission for bots others are managing.
__Minimum server version__: 5.10


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of users per page. |
| `include_deleted` | `boolean` | `query` | No | If deleted bots should be returned. |
| `only_orphaned` | `boolean` | `query` | No | When true, only orphaned bots will be returned. A bot is considered orphaned if its owner has been deactivated. |

### Responses

#### 200 - Bot page retrieval successful

Schema (application/json):
```json
[
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
]
```

#### 400 - 

#### 401 - 

#### 403 - 

