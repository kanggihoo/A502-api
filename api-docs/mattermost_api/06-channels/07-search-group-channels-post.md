# 07-Search Group Channels [POST]

`POST /api/v4/channels/group/search`

Get a list of group channels for a user which members' usernames match the search term.

__Minimum server version__: 5.14


### Request Body (application/json)

```json
{
  "term": string (required), // The search term to match against the members' usernames of the group channels
}
```
### Responses

#### 200 - Channels search successful

Schema (application/json):
```json
[
  {
    "id": string,
    "create_at": integer, // The time in milliseconds a channel was created
    "update_at": integer, // The time in milliseconds a channel was last updated
    "delete_at": integer, // The time in milliseconds a channel was deleted
    "team_id": string,
    "type": string,
    "display_name": string,
    "name": string,
    "header": string,
    "purpose": string,
    "last_post_at": integer, // The time in milliseconds of the last post of a channel
    "total_msg_count": integer,
    "extra_update_at": integer, // Deprecated in Mattermost 5.0 release
    "creator_id": string,
  }
]
```

#### 400 - 

#### 401 - 

