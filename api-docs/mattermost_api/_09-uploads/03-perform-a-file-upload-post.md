# 03-Perform a file upload [POST]

`POST /api/v4/uploads/{upload_id}`

Starts or resumes a file upload.  
To resume an existing (incomplete) upload, data should be sent starting from the offset specified in the upload session object.

The request body can be in one of two formats:
- Binary file content streamed in request's body
- multipart/form-data

##### Permissions
Must be logged in as the user who created the upload session.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `upload_id` | `string` | `path` | Yes | The ID of the upload session the data belongs to. |

### Request Body (application/octet-stream)

```json
string
```
### Responses

#### 201 - Upload successful

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

#### 204 - Upload incomplete

#### 400 - 

#### 401 - 

#### 403 - 

#### 413 - 

#### 501 - 

