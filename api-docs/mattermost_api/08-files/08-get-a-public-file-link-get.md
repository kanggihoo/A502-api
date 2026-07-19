# 08-Get a public file link [GET]

`GET /api/v4/files/{file_id}/link`

Gets a public link for a file that can be accessed without logging into Mattermost.
##### Permissions
Must have `read_channel` permission or be uploader of the file.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `file_id` | `string` | `path` | Yes | The ID of the file to get a link for |

### Responses

#### 200 - A publicly accessible link to the given file

Schema (application/json):
```json
{
  "link": string,
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

