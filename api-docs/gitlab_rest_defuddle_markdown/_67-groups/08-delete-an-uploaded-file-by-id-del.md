# 08-Delete an uploaded file by ID [DEL]

`DELETE /api/v4/groups/{id}/uploads/{upload_id}`

Deletes an uploaded file with a specified ID. You must have the Maintainer or Owner role for the group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `upload_id` | `integer` | `path` | Yes | The ID of a group upload |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 403 - Unauthenticated

#### 404 - Not found

