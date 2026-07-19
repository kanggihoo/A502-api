# 75-Delete synced thread draft [DELETE]

`DELETE /api/v4/users/{user_id}/channels/{channel_id}/drafts/{thread_id}`

Delete a synced draft for a channel thread.
##### Permissions
Must be authenticated as the draft owner and synced drafts must be enabled.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User ID |
| `channel_id` | `string` | `path` | Yes | Channel ID |
| `thread_id` | `string` | `path` | Yes | Root post ID of the thread |

### Responses

#### 200 - Thread draft deletion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 401 - 

#### 403 - 

#### 501 - 

