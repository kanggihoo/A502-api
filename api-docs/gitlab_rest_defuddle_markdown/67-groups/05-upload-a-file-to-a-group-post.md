# 05-Upload a file to a group [POST]

`POST /api/v4/groups/{id}/uploads`

Uploads a file to the specified group. Returns a markdown-formatted link to the file.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Request Body (multipart/form-data)

```json
{
  "file": string (required), // The file to upload
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer, // The ID of the file
  "alt": string, // The name of the file
  "url": string, // The URL to access the file
  "full_path": string, // The full path to the file
  "markdown": string, // A markdown-formatted link to the file.
}
```

#### 400 - Bad request

#### 404 - Not found

