# 02-Create a merge request dependency [POST]

`POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/blocks`

Creates a merge request dependency between two merge requests. The merge request is blocked until the dependency merges.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The internal IID of the blocked merge request |

### Request Body (application/json)

```json
{
  "blocking_merge_request_id": integer, // The global ID of the blocking merge request
  "blocking_merge_request_iid": integer, // The IID of the blocking merge request
  "blocking_project_id": any,
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

