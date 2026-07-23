# 34-Remove user from channel [DELETE]

`DELETE /api/v4/channels/{channel_id}/members/{user_id}`

Delete a channel member, effectively removing them from a channel.

In server version 5.3 and later, channel members can only be deleted from public or private channels.
##### Permissions
`manage_public_channel_members` permission if the channel is public.
`manage_private_channel_members` permission if the channel is private.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - Channel member deletion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

