# 12-Delete an emoji reaction from a merge request [DEL]

`DELETE /api/v4/projects/{id}/merge_requests/{merge_request_iid}/award_emoji/{award_id}`

Deletes a specified emoji reaction from a merge request. Only an administrator or the user who added the reaction can delete it.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `award_id` | `integer` | `path` | Yes | ID of an emoji reaction. |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

