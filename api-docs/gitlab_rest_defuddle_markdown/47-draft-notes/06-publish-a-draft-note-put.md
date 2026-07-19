# 06-Publish a draft note [PUT]

`PUT /api/v4/projects/{id}/merge_requests/{merge_request_iid}/draft_notes/{draft_note_id}/publish`

Publishes a draft note for a specified merge request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a project |
| `merge_request_iid` | `integer` | `path` | Yes | The ID of a merge request |
| `draft_note_id` | `integer` | `path` | Yes | The ID of a draft note |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

