# 05-Update channel bookmark's order [POST]

`POST /api/v4/channels/{channel_id}/bookmarks/{bookmark_id}/sort_order`

Updates the order of a channel bookmark, setting its new order
from the parameters and updating the rest of the bookmarks of
the channel to accomodate for this change.

__Minimum server version__: 9.5

##### Permissions
Must have the `order_bookmark_public_channel` or
`order_bookmark_private_channel` depending on the channel
type. If the channel is a DM or GM, must be a non-guest
member.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `bookmark_id` | `string` | `path` | Yes | Bookmark GUID |

### Request Body (application/json)

```json
number
```
### Responses

#### 200 - Channel Bookmark Sort Order update successful

Schema (application/json):
```json
[
  any
]
```

#### 400 - 

#### 401 - 

#### 403 - 

