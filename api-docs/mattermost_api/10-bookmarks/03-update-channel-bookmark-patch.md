# 03-Update channel bookmark [PATCH]

`PATCH /api/v4/channels/{channel_id}/bookmarks/{bookmark_id}`

Partially update a channel bookmark by providing only the
fields you want to update. Ommited fields will not be
updated. The fields that can be updated are defined in the
request body, all other provided fields will be ignored.

__Minimum server version__: 9.5

##### Permissions
Must have the `edit_bookmark_public_channel` or
`edit_bookmark_private_channel` depending on the channel
type. If the channel is a DM or GM, must be a non-guest
member.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `bookmark_id` | `string` | `path` | Yes | Bookmark GUID |

### Request Body (application/json)

```json
{
  "file_id": string, // The ID of the file associated with the channel bookmark. Required for bookmarks of type 'file'
  "display_name": string, // The name of the channel bookmark
  "sort_order": integer, // The order of the channel bookmark
  "link_url": string, // The URL associated with the channel bookmark. Required for type bookmarks of type 'link'
  "image_url": string, // The URL of the image associated with the channel bookmark
  "emoji": string, // The emoji of the channel bookmark
  "type": enum("link" | "file"), // * `link` for channel bookmarks that reference a link. `link_url` is required * `file` for channel bookmarks that reference a file. `file_id` is required 
}
```
### Responses

#### 200 - Channel Bookmark update successful

Schema (application/json):
```json
{
  "updated": any,
  "deleted": any,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

