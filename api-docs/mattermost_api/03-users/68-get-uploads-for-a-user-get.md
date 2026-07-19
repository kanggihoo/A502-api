# 68-Get uploads for a user [GET]

`GET /api/v4/users/{user_id}/uploads`

Gets all the upload sessions belonging to a user.

__Minimum server version__: 5.28

##### Permissions
Must be logged in as the user who created the upload sessions.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The ID of the user. This can also be "me" which will point to the current user. |

### Responses

#### 200 - User's uploads retrieval successful

Schema (application/json):
```json
[
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
]
```

#### 400 - 

#### 401 - 

#### 404 - 

