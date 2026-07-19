# 04-Mark a thread that user is following as unread based on a post id [POST]

`POST /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/set_unread/{post_id}`

Mark a thread that user is following as unread

__Minimum server version__: 6.7

##### Permissions
Must have `read_channel` permission for the channel the thread is in or if the channel is public, have the `read_public_channels` permission for the team.

Must have `edit_other_users` permission if the user is not the one marking the thread for himself.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The ID of the user. This can also be "me" which will point to the current user. |
| `team_id` | `string` | `path` | Yes | The ID of the team in which the thread is. |
| `thread_id` | `string` | `path` | Yes | The ID of the thread to update |
| `post_id` | `string` | `path` | Yes | The ID of a post belonging to the thread to mark as unread. |

### Responses

#### 200 - User's thread update successful

#### 400 - 

#### 401 - 

#### 404 - 

