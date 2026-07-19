# 04-Delete a secure file [DEL]

`DELETE /api/v4/projects/{id}/secure_files/{secure_file_id}`

Deletes a specified secure file from a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the<br>        authenticated user |
| `secure_file_id` | `integer` | `path` | Yes | The ID of a secure file |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - 404 Not found

