# 11-Get file info for post [GET]

`GET /api/v4/posts/{post_id}/files/info`

Gets a list of file information objects for the files attached to a post.
##### Permissions
Must have `read_channel` permission for the channel the post is in.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | ID of the post |
| `include_deleted` | `boolean` | `query` | No | Defines if result should include deleted posts, must have 'manage_system' (admin) permission. |

### Responses

#### 200 - File info retrieval successful

Schema (application/json):
```json
[
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
]
```

#### 400 - 

#### 401 - 

#### 403 - 

