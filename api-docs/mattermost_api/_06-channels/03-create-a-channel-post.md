# 03-Create a channel [POST]

`POST /api/v4/channels`

Create a new channel.
##### Permissions
If creating a public channel, `create_public_channel` permission is required. If creating a private channel, `create_private_channel` permission is required.


### Request Body (application/json)

```json
{
  "team_id": string (required), // The team ID of the team to create the channel on
  "name": string (required), // The unique handle for the channel, will be present in the channel URL
  "display_name": string (required), // The non-unique UI name for the channel
  "purpose": string, // A short description of the purpose of the channel
  "header": string, // Markdown-formatted text to display in the header of the channel
  "type": string (required), // 'O' for a public channel, 'P' for a private channel
  "managed_category_name": string, // The name of the managed category to assign this channel to. Requires an Enterprise license and the `ManagedChannelCategories` feature flag to be enabled.
  "default_category_name": string, // Default sidebar category name for members when joining this channel. Requires `EnableChannelCategorySorting` to be enabled on the server.
}
```
### Responses

#### 201 - Channel creation successful

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

