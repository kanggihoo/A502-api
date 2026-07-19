# 07-Mark as unread from a post. [POST]

`POST /api/v4/users/{user_id}/posts/{post_id}/set_unread`

Mark a channel as being unread from a given post.
##### Permissions
Must have `read_channel` permission for the channel the post is in or if the channel is public, have the `read_public_channels` permission for the team.
Must have `edit_other_users` permission if the user is not the one marking the post for himself.

__Minimum server version__: 5.18


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `post_id` | `string` | `path` | Yes | Post GUID |

### Responses

#### 200 - Post marked as unread successfully

Schema (application/json):
```json
{
  "team_id": string, // The ID of the team the channel belongs to.
  "channel_id": string, // The ID of the channel the user has access to..
  "msg_count": integer, // No. of messages the user has already read.
  "mention_count": integer, // No. of mentions the user has within the unread posts of the channel.
  "last_viewed_at": integer, // time in milliseconds when the user last viewed the channel.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

