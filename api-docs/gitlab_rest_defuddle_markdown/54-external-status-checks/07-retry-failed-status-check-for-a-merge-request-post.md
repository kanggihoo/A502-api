# 07-Retry failed status check for a merge request [POST]

`POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/status_checks/{external_status_check_id}/retry`

Retries a specified failed external status check for a merge request. Even though the merge request has not changed, this endpoint resends the current state of merge request to the defined external service.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of a project |
| `merge_request_iid` | `integer` | `path` | Yes | IID of a merge request |
| `external_status_check_id` | `integer` | `path` | Yes | ID of a failed external status check |

### Responses

#### 202 - Accepted

#### 400 - Bad Request

#### 404 - Not Found

