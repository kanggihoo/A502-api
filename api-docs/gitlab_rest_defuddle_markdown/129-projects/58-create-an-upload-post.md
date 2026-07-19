# 58-Create an upload [POST]

`POST /api/v4/projects/{id}/uploads`

Creates an upload.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (multipart/form-data)

```json
{
  "file": string (required), // The attachment file to be uploaded
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "alt": string,
  "url": string,
  "full_path": string,
  "markdown": string,
}
```

#### 400 - Bad Request

#### 404 - Not found

