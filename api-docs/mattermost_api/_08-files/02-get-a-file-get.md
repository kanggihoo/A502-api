# 02-Get a file [GET]

`GET /api/v4/files/{file_id}`

Gets a file that has been uploaded previously.
##### Permissions
Must have `read_channel` permission or be uploader of the file.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `file_id` | `string` | `path` | Yes | The ID of the file to get |

### Responses

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

