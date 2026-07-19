# 46-Get unread messages [GET]

`GET /api/v4/users/{user_id}/channels/{channel_id}/unread`

Get the total unread messages and mentions for a channel for a user.
##### Permissions
Must be logged in as user and have the `read_channel` permission, or have `edit_other_usrs` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Responses

#### 200 - Channel unreads retrieval successful

Schema (application/json):
```json
{
  "team_id": string,
  "channel_id": string,
  "msg_count": integer,
  "mention_count": integer,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

