# 16-Delete an emoji reaction from a merge request comment [DEL]

`DELETE /api/v4/projects/{id}/merge_requests/{merge_request_iid}/notes/{note_id}/award_emoji/{award_id}`

Deletes a specified emoji reaction from a comment on a merge request. Only an administrator or the user who added the reaction can delete it.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `award_id` | `integer` | `path` | Yes | ID of an emoji reaction. |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |
| `note_id` | `any` | `path` | Yes |  |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

