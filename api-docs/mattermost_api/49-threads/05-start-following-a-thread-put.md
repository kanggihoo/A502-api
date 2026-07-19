# 05-Start following a thread [PUT]

`PUT /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/following`

Start following a thread

__Minimum server version__: 5.29

##### Permissions
Must be logged in as the user or have `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The ID of the user. This can also be "me" which will point to the current user. |
| `team_id` | `string` | `path` | Yes | The ID of the team in which the thread is. |
| `thread_id` | `string` | `path` | Yes | The ID of the thread to follow |

### Responses

#### 200 - User's thread update successful

#### 400 - 

#### 401 - 

#### 404 - 

