# 03-Retrieve a merge request dependency [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/blocks/{block_id}`

Retrieves a specified merge request dependency.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The internal ID of the merge request |
| `block_id` | `integer` | `path` | Yes | The ID of the merge request dependency |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

