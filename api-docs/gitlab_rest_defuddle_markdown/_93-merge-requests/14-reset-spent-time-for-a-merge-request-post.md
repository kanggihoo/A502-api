# 14-Reset spent time for a merge request [POST]

`POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/reset_spent_time`

Resets the total spent time for a specified merge request to `0` seconds.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `merge_request_iid` | `integer` | `path` | Yes | The internal ID of the merge_request |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "time_estimate": integer,
  "total_time_spent": integer,
  "human_time_estimate": string,
  "human_total_time_spent": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

