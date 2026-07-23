# 29-Get channel members [GET]

`GET /api/v4/channels/{channel_id}/members`

Get a page of members for a channel.
##### Permissions
`read_channel` permission for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of members per page. |

### Responses

#### 200 - Channel members retrieval successful

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

