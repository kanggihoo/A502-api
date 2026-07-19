# 01-List all merge request draft notes [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/draft_notes`

Lists all merge request draft notes.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a project |
| `merge_request_iid` | `integer` | `path` | Yes | The ID of a merge request |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "author_id": integer,
  "merge_request_id": integer,
  "resolve_discussion": boolean,
  "discussion_id": string,
  "note": string,
  "commit_id": string,
  "line_code": string,
  "position": {},
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

