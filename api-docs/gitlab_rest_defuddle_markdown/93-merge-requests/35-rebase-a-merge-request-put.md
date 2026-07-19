# 35-Rebase a merge request [PUT]

`PUT /api/v4/projects/{id}/merge_requests/{merge_request_iid}/rebase`

Rebases a merge request. Automatically rebases the `source_branch` of the merge request against its `target_branch`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Request Body (application/json)

```json
{
  "skip_ci": boolean, // Set to true to skip creating a CI pipeline.
}
```
### Responses

#### 202 - Accepted

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

#### 409 - Conflict

