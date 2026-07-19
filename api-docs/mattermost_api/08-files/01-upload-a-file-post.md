# 01-Upload a file [POST]

`POST /api/v4/files`

Uploads a file that can later be attached to a post.

This request can either be a multipart/form-data request with a channel_id, files and optional
client_ids defined in the FormData, or it can be a request with the channel_id and filename
defined as query parameters with the contents of a single file in the body of the request.

Only multipart/form-data requests are supported by server versions up to and including 4.7.
Server versions 4.8 and higher support both types of requests.

__Minimum server version__: 9.4
Starting with server version 9.4 when uploading a file for a channel bookmark, the bookmark=true query parameter should be included in the query string

##### Permissions
Must have `upload_file` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `query` | No | The ID of the channel that this file will be uploaded to |
| `filename` | `string` | `query` | No | The name of the file to be uploaded |

### Request Body (multipart/form-data)

```json
{
  "files": string, // A file to be uploaded
  "channel_id": string, // The ID of the channel that this file will be uploaded to
  "client_ids": string, // A unique identifier for the file that will be returned in the response
}
```
### Responses

#### 201 - Corresponding lists of the provided client_ids and the metadata that has been stored in the database for each one

Schema (application/json):
```json
{
  "file_infos": [
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
  ], // A list of file metadata that has been stored in the database
  "client_ids": [
    string
  ], // A list of the client_ids that were provided in the request
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 413 - 

#### 501 - 

