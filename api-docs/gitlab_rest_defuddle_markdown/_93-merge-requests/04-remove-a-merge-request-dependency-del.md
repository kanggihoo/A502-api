# 04-Remove a merge request dependency [DEL]

`DELETE /api/v4/projects/{id}/merge_requests/{merge_request_iid}/blocks/{block_id}`

Removes a merge request dependency.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The internal ID of the merge request |
| `block_id` | `integer` | `path` | Yes | The ID of the merge request dependency |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

