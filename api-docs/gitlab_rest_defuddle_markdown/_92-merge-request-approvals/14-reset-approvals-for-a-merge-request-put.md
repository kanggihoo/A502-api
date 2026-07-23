# 14-Reset approvals for a merge request [PUT]

`PUT /api/v4/projects/{id}/merge_requests/{merge_request_iid}/reset_approvals`

Resets all approvals for a specified merge request. Available only to bot users with a valid project or group token. Human users receive a `401 Unauthorized` response.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

