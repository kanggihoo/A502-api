# 61-Delete an uploaded file by ID [DEL]

`DELETE /api/v4/projects/{id}/uploads/{upload_id}`

Deletes an uploaded file with a specified ID. You must have the Maintainer or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `upload_id` | `integer` | `path` | Yes | The ID of a project upload |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 403 - Unauthenticated

#### 404 - Not found

