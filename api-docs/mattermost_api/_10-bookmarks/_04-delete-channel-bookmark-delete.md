# 04-Delete channel bookmark [DELETE]

`DELETE /api/v4/channels/{channel_id}/bookmarks/{bookmark_id}`

Archives a channel bookmark. This will set the `deleteAt` to
the current timestamp in the database.

__Minimum server version__: 9.5

##### Permissions
Must have the `delete_bookmark_public_channel` or
`delete_bookmark_private_channel` depending on the channel
type. If the channel is a DM or GM, must be a non-guest
member.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `bookmark_id` | `string` | `path` | Yes | Bookmark GUID |

### Responses

#### 200 - Channel Bookmark deletion successful

Schema (application/json):
```json
any
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

