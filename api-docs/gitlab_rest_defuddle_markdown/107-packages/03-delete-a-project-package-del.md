# 03-Delete a project package [DEL]

`DELETE /api/v4/projects/{id}/packages/{package_id}`

Deletes a specified project package.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `package_id` | `integer` | `path` | Yes | The ID of a package |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

