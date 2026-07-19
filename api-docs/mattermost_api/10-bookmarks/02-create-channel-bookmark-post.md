# 02-Create channel bookmark [POST]

`POST /api/v4/channels/{channel_id}/bookmarks`

Creates a new channel bookmark for this channel.

__Minimum server version__: 9.5

##### Permissions
Must have the `add_bookmark_public_channel` or
`add_bookmark_private_channel` depending on the channel
type. If the channel is a DM or GM, must be a non-guest
member.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Request Body (application/json)

```json
{
  "file_id": string, // The ID of the file associated with the channel bookmark. Required for bookmarks of type 'file'
  "display_name": string (required), // The name of the channel bookmark
  "link_url": string, // The URL associated with the channel bookmark. Required for bookmarks of type 'link'
  "image_url": string, // The URL of the image associated with the channel bookmark. Optional, only applies for bookmarks of type 'link'
  "emoji": string, // The emoji of the channel bookmark
  "type": enum("link" | "file") (required), // * `link` for channel bookmarks that reference a link. `link_url` is required * `file` for channel bookmarks that reference a file. `file_id` is required 
}
```
### Responses

#### 201 - Channel Bookmark creation successful

Schema (application/json):
```json
any
```

#### 400 - 

#### 401 - 

#### 403 - 

