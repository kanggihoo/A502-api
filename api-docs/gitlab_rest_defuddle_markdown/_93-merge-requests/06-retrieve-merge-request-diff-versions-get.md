# 06-Retrieve merge request diff versions [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/versions`

Retrieves merge request diff versions.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The internal ID of the merge request |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "head_commit_sha": string,
  "base_commit_sha": string,
  "start_commit_sha": string,
  "created_at": string,
  "merge_request_id": integer,
  "state": string,
  "real_size": string,
  "patch_id_sha": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

