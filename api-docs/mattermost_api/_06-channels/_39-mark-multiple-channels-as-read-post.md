# 39-Mark multiple channels as read [POST]

`POST /api/v4/channels/members/{user_id}/mark_read`

Mark multiple channels as viewed for the given user.
##### Permissions
Must be logged in as the user or have `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User ID to mark channels read for |

### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 200 - Channels marked as read

Schema (application/json):
```json
{
  "status": string,
  "last_viewed_at_times": {},
}
```

#### 400 - 

#### 401 - 

#### 403 - 

