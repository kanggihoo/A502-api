# 30-List all merge request pipelines [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/pipelines`

Lists all merge request pipelines.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `merge_request_iid` | `integer` | `path` | Yes | The internal ID of the merge request. |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "iid": integer,
  "project_id": integer,
  "sha": string,
  "ref": string,
  "status": string,
  "source": string,
  "created_at": string,
  "updated_at": string,
  "web_url": string,
}
```

#### 400 - Bad Request

#### 404 - Not found

