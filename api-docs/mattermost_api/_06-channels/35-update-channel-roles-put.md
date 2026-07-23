# 35-Update channel roles [PUT]

`PUT /api/v4/channels/{channel_id}/members/{user_id}/roles`

Update a user's roles for a channel.
##### Permissions
Must have `manage_channel_roles` permission for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "roles": string (required),
}
```
### Responses

#### 200 - Channel roles update successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

