# 04-Get a post [GET]

`GET /api/v4/posts/{post_id}`

Get a single post.
##### Permissions
Must have `read_channel` permission for the channel the post is in or if the channel is public, have the `read_public_channels` permission for the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | ID of the post to get |
| `include_deleted` | `boolean` | `query` | No | Defines if result should include deleted posts, must have 'manage_system' (admin) permission. |

### Responses

#### 200 - Post retrieval successful

Schema (application/json):
```json
{
  "id": string,
  "create_at": integer, // The time in milliseconds a post was created
  "update_at": integer, // The time in milliseconds a post was last updated
  "delete_at": integer, // The time in milliseconds a post was deleted
  "edit_at": integer,
  "user_id": string,
  "channel_id": string,
  "root_id": string,
  "original_id": string,
  "message": string,
  "type": string,
  "props": {},
  "hashtag": string,
  "file_ids": [
    string
  ],
  "pending_post_id": string,
  "metadata": {
    "embeds": [
      {
        "type": enum("image" | "message_attachment" | "opengraph" | "link"), // The type of content that is embedded in this point.
        "url": string, // The URL of the embedded content, if one exists.
        "data": {}, // Any additional information about the embedded content. Only used at this time to store OpenGraph metadata. This field will be null for non-OpenGraph embeds. 
      }
    ], // Information about content embedded in the post including OpenGraph previews, image link previews, and message attachments. This field will be null if the post does not contain embedded content. 
    "emojis": [
      {
        "id": string, // The ID of the emoji
        "creator_id": string, // The ID of the user that made the emoji
        "name": string, // The name of the emoji
        "create_at": integer, // The time in milliseconds the emoji was made
        "update_at": integer, // The time in milliseconds the emoji was last updated
        "delete_at": integer, // The time in milliseconds the emoji was deleted
      }
    ], // The custom emojis that appear in this point or have been used in reactions to this post. This field will be null if the post does not contain custom emojis. 
    "files": [
      {
        "id": string, // The unique identifier for this file
        "user_id": string, // The ID of the user that uploaded this file
        "post_id": string, // If this file is attached to a post, the ID of that post
        "create_at": integer, // The time in milliseconds a file was created
        "update_at": integer, // The time in milliseconds a file was last updated
        "delete_at": integer, // The time in milliseconds a file was deleted
        "name": string, // The name of the file
        "extension": string, // The extension at the end of the file name
        "size": integer, // The size of the file in bytes
        "mime_type": string, // The MIME type of the file
        "width": integer, // If this file is an image, the width of the file
        "height": integer, // If this file is an image, the height of the file
        "has_preview_image": boolean, // If this file is an image, whether or not it has a preview-sized version
      }
    ], // The FileInfo objects for any files attached to the post. This field will be null if the post does not have any file attachments. 
    "images": {}, // An object mapping the URL of an external image to an object containing the dimensions of that image. This field will be null if the post or its embedded content does not reference any external images. 
    "reactions": [
      {
        "user_id": string, // The ID of the user that made this reaction
        "post_id": string, // The ID of the post to which this reaction was made
        "emoji_name": string, // The name of the emoji that was used for this reaction
        "create_at": integer, // The time in milliseconds this reaction was made
      }
    ], // Any reactions made to this point. This field will be null if no reactions have been made to this post. 
    "priority": any, // Post priority set for this post. This field will be null if no priority metadata has been set. 
    "acknowledgements": [
      {
        "user_id": string, // The ID of the user that made this acknowledgement.
        "post_id": string, // The ID of the post to which this acknowledgement was made.
        "acknowledged_at": integer, // The time in milliseconds in which this acknowledgement was made.
      }
    ], // Any acknowledgements made to this point. 
  },
}
```

#### 400 - 

#### 401 - 

#### 403 - 

