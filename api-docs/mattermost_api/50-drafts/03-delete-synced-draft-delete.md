# 03-Delete synced draft [DELETE]

`DELETE /api/v4/users/{user_id}/channels/{channel_id}/drafts`

Delete a synced draft for a channel.
##### Permissions
Must be authenticated as the draft owner and synced drafts must be enabled.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User ID |
| `channel_id` | `string` | `path` | Yes | Channel ID |

### Responses

#### 200 - Draft deletion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 401 - 

#### 403 - 

#### 501 - 

