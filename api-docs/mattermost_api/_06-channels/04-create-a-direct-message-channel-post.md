# 04-Create a direct message channel [POST]

`POST /api/v4/channels/direct`

Create a new direct message channel between two users.
##### Permissions
Must be one of the two users and have `create_direct_channel` permission. Having the `manage_system` permission voids the previous requirements.


### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 201 - Direct channel creation successful

Schema (application/json):
```json
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
```

#### 400 - 

#### 401 - 

#### 403 - 

