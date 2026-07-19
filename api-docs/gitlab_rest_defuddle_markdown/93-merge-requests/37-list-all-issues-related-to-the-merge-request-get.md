# 37-List all issues related to the merge request [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/related_issues`

Lists all issues related to the merge request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

