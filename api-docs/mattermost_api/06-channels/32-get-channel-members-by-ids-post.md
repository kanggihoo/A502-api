# 32-Get channel members by ids [POST]

`POST /api/v4/channels/{channel_id}/members/ids`

Get a list of channel members based on the provided user ids.
##### Permissions
Must have the `read_channel` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 200 - Channel member list retrieval successful

Schema (application/json):
```json
[
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
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

