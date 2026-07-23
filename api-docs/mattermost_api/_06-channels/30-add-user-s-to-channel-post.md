# 30-Add user(s) to channel [POST]

`POST /api/v4/channels/{channel_id}/members`

Add a user(s) to a channel by creating a channel member object(s).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | The channel ID |

### Request Body (application/json)

```json
{
  "user_id": string, // The ID of user to add into the channel, for backwards compatibility.
  "user_ids": [
    string
  ], // The IDs of users to add into the channel, required if 'user_id' doess not exist.
  "post_root_id": string, // The ID of root post where link to add channel member originates
}
```
### Responses

#### 201 - Channel member creation successful

Schema (application/json):
```json
{
  "channel_id": string,
  "user_id": string,
  "roles": string,
  "last_viewed_at": integer, // The time in milliseconds the channel was last viewed by the user
  "msg_count": integer,
  "mention_count": integer,
  "notify_props": {
    "email": string, // Set to "true" to enable email notifications, "false" to disable, or "default" to use the global user notification setting.
    "push": string, // Set to "all" to receive push notifications for all activity, "mention" for mentions and direct messages only, "none" to disable, or "default" to use the global user notification setting.
    "desktop": string, // Set to "all" to receive desktop notifications for all activity, "mention" for mentions and direct messages only, "none" to disable, or "default" to use the global user notification setting.
    "mark_unread": string, // Set to "all" to mark the channel unread for any new message, "mention" to mark unread for new mentions only. Defaults to "all".
  },
  "last_update_at": integer, // The time in milliseconds the channel member was last updated
}
```

#### 400 - 

#### 401 - 

#### 403 - 

