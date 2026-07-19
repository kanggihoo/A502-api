# 06-Delete a package file [DEL]

`DELETE /api/v4/projects/{id}/packages/{package_id}/package_files/{package_file_id}`

Deletes a specified package file.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | ID or URL-encoded path of the project |
| `package_id` | `integer` | `path` | Yes | ID of a package |
| `package_file_id` | `integer` | `path` | Yes | ID of a package file |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

