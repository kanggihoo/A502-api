# 01-Create an upload [POST]

`POST /api/v4/uploads`

Creates a new upload session.

__Minimum server version__: 5.28
##### Permissions
Must have `upload_file` permission.


### Request Body (application/json)

```json
{
  "channel_id": string (required), // The ID of the channel to upload to.
  "filename": string (required), // The name of the file to upload.
  "file_size": integer (required), // The size of the file to upload in bytes.
}
```
### Responses

#### 201 - Upload creation successful.

Schema (application/json):
```json
{
  "id": string, // The unique identifier for the upload.
  "type": enum("attachment" | "import"), // The type of the upload.
  "create_at": integer, // The time the upload was created in milliseconds.
  "user_id": string, // The ID of the user performing the upload.
  "channel_id": string, // The ID of the channel to upload to.
  "filename": string, // The name of the file to upload.
  "file_size": integer, // The size of the file to upload in bytes.
  "file_offset": integer, // The amount of data uploaded in bytes.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 413 - 

#### 501 - 

