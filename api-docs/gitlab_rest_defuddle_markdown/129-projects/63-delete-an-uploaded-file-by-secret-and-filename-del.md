# 63-Delete an uploaded file by secret and filename [DEL]

`DELETE /api/v4/projects/{id}/uploads/{secret}/{filename}`

Deletes an uploaded file with a specified secret and filename. You must have the Maintainer or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `secret` | `string` | `path` | Yes | The 32-character secret of a project upload |
| `filename` | `string` | `path` | Yes | The filename of a project upload |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 403 - Unauthenticated

#### 404 - Not found

