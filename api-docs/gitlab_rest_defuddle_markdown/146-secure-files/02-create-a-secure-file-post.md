# 02-Create a secure file [POST]

`POST /api/v4/projects/{id}/secure_files`

Creates a secure file in a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the<br>        authenticated user |

### Request Body (multipart/form-data)

```json
{
  "name": string (required), // The name of the file being uploaded. The filename must be unique within             the project
  "file": string (required), // The secure file being uploaded
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "checksum": string,
  "checksum_algorithm": string,
  "created_at": string,
  "expires_at": string,
  "metadata": {},
  "file_extension": string,
}
```

#### 400 - 400 Bad Request

#### 404 - Not Found

