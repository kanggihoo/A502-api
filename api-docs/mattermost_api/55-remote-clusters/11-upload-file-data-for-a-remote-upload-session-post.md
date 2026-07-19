# 11-Upload file data for a remote upload session. [POST]

`POST /api/v4/remotecluster/upload/{upload_id}`

Streams file data into an existing upload session from a linked
remote cluster. This endpoint is authenticated with a remote-cluster token.

##### Permissions
No user session permissions required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `upload_id` | `string` | `path` | Yes | The upload session ID. |

### Request Body (application/octet-stream)

```json
string
```
### Responses

#### 200 - Upload chunk accepted

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

#### 204 - Upload data accepted with no file completion yet

#### 400 - 

#### 401 - 

