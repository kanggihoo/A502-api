# 03-Mark a thread that user is following read state to the timestamp [PUT]

`PUT /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/read/{timestamp}`

Mark a thread that user is following as read

__Minimum server version__: 5.29

##### Permissions
Must be logged in as the user or have `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The ID of the user. This can also be "me" which will point to the current user. |
| `team_id` | `string` | `path` | Yes | The ID of the team in which the thread is. |
| `thread_id` | `string` | `path` | Yes | The ID of the thread to update |
| `timestamp` | `string` | `path` | Yes | The timestamp to which the thread's "last read" state will be reset. |

### Responses

#### 200 - User's thread update successful

#### 400 - 

#### 401 - 

#### 404 - 

