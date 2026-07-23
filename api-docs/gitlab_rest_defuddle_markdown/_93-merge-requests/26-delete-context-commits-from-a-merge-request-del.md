# 26-Delete context commits from a merge request [DEL]

`DELETE /api/v4/projects/{id}/merge_requests/{merge_request_iid}/context_commits`

Deletes specified context commits from a merge request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `commits` | `array` | `query` | Yes | The context commits’ SHA. |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

