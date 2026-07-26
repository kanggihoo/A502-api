# 41-View channel [POST]

`POST /api/v4/channels/members/{user_id}/view`

Perform all the actions involved in viewing a channel. This includes marking channels as read, clearing push notifications, and updating the active channel.
##### Permissions
Must be logged in as user or have `edit_other_users` permission.

__Response only includes `last_viewed_at_times` in Mattermost server 4.3 and newer.__


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User ID to perform the view action for |

### Request Body (application/json)

```json
{
  "channel_id": string (required), // The channel ID that is being viewed. Use a blank string to indicate that all channels have lost focus.
  "prev_channel_id": string, // The channel ID of the previous channel, used when switching channels. Providing this ID will cause push notifications to clear on the channel being switched to.
}
```
### Responses

#### 200 - Channel view successful

Schema (application/json):
```json
{
  "status": string, // Value should be "OK" if successful
  "last_viewed_at_times": {}, // A JSON object mapping channel IDs to the channel view times
}
```

#### 400 - 

#### 401 - 

#### 403 - 

