# 12-Upload an attachment to a project wiki [POST]

`POST /api/v4/projects/{id}/wikis/attachments`

Uploads a file to the `uploads` directory in a specified project wiki.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

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

