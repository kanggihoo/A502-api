# 42-Mark all direct and group messages as read [PUT]

`PUT /api/v4/channels/members/{user_id}/direct/read`

Mark all direct and group messages as read for a user.

##### Permissions

Must be logged in as user or have `edit_other_users` permission.

__Minimum server version__: 11.3


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User ID to mark messages as read for |

### Responses

#### 200 - Direct messages marked as read successfully

Schema (application/json):
```json
{
  "status": string, // Value should be "OK" if successful
  "last_viewed_at_times": {}, // A JSON object mapping channel IDs to the last viewed times
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

