# 37-Update channel notifications [PUT]

`PUT /api/v4/channels/{channel_id}/members/{user_id}/notify_props`

Update a user's notification properties for a channel. Only the provided fields are updated.
##### Permissions
Must be logged in as the user or have `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "email": string, // Set to "true" to enable email notifications, "false" to disable, or "default" to use the global user notification setting.
  "push": string, // Set to "all" to receive push notifications for all activity, "mention" for mentions and direct messages only, "none" to disable, or "default" to use the global user notification setting.
  "desktop": string, // Set to "all" to receive desktop notifications for all activity, "mention" for mentions and direct messages only, "none" to disable, or "default" to use the global user notification setting.
  "mark_unread": string, // Set to "all" to mark the channel unread for any new message, "mention" to mark unread for new mentions only. Defaults to "all".
}
```
### Responses

#### 200 - Channel notification properties update successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

