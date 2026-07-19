# 29-Retrieve merge request raw diffs [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/raw_diffs`

Retrieves the raw diffs of the files changed in a merge request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

