# 33-Merge to default merge ref path [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/merge_ref`

Merges the changes between the merge request source and target branches into the `refs/merge-requests/:iid/merge` ref, of the target project repository, if possible. This ref has the state the target branch would have if a regular merge action was taken.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Responses

#### 200 - OK

#### 400 - Bad request

#### 404 - Not Found

