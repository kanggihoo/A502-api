# 05-Download a secure file [GET]

`GET /api/v4/projects/{id}/secure_files/{secure_file_id}/download`

Downloads the contents of a specified secure file in a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the<br>        authenticated user |
| `secure_file_id` | `integer` | `path` | Yes | The ID of a secure file |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - 404 Not found

