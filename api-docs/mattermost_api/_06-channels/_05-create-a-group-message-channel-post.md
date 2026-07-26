# 05-Create a group message channel [POST]

`POST /api/v4/channels/group`

Create a new group message channel to group of users. If the logged in user's id is not included in the list, it will be appended to the end.
##### Permissions
Must have `create_group_channel` permission.


### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 201 - Group channel creation successful

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

