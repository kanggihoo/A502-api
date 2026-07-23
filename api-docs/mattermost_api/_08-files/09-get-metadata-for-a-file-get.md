# 09-Get metadata for a file [GET]

`GET /api/v4/files/{file_id}/info`

Gets a file's info.
##### Permissions
Must have `read_channel` permission or be uploader of the file.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `file_id` | `string` | `path` | Yes | The ID of the file info to get |

### Responses

#### 200 - The stored metadata for the given file

Schema (application/json):
```json
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
```

#### 400 - 

#### 401 - 

#### 403 - Do not have appropriate permissions

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

#### 404 - 

#### 501 - 

