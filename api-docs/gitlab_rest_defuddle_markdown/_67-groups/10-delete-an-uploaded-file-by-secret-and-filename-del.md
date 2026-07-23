# 10-Delete an uploaded file by secret and filename [DEL]

`DELETE /api/v4/groups/{id}/uploads/{secret}/{filename}`

Deletes an uploaded file with a specified secret and filename. You must have the Maintainer or Owner role for the group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `secret` | `string` | `path` | Yes | The 32-character secret of a group upload |
| `filename` | `string` | `path` | Yes | The filename of a group upload |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 403 - Unauthenticated

#### 404 - Not found

