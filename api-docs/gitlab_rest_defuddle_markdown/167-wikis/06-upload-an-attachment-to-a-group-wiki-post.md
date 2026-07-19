# 06-Upload an attachment to a group wiki [POST]

`POST /api/v4/groups/{id}/wikis/attachments`

Uploads a file to the `uploads` directory in a specified group wiki.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Request Body (multipart/form-data)

```json
{
  "file": string (required), // The attachment file to be uploaded
  "branch": string, // The name of the branch
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "file_name": string,
  "file_path": string,
  "branch": string,
  "link": {},
}
```

#### 400 - Bad Request

#### 404 - Not found

