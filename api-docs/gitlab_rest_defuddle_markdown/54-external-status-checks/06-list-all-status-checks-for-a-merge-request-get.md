# 06-List all status checks for a merge request [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/status_checks`

Lists all external status check services for a specified merge request and their status.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "external_url": string,
  "status": string,
}
```

#### 404 - Not Found

