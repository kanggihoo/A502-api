# 18-Delete a merge request [DEL]

`DELETE /api/v4/projects/{id}/merge_requests/{merge_request_iid}`

Deletes a specified merge request for a project. Administrators and project Owners only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `merge_request_iid` | `integer` | `path` | Yes | The internal ID of the merge request. |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

#### 412 - Precondition failed

