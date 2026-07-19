# 03-Retrieve a commit [GET]

`GET /api/v4/projects/{id}/repository/commits/{sha}`

Retrieves a specified commit identified by the commit hash or name of a branch or tag.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `sha` | `string` | `path` | Yes | A commit sha, or the name of a branch or tag |
| `stats` | `boolean` | `query` | No | Include commit stats |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": string,
  "short_id": string,
  "created_at": string,
  "parent_ids": [
    string
  ],
  "title": string,
  "message": string,
  "author_name": string,
  "author_email": string,
  "authored_date": string,
  "committer_name": string,
  "committer_email": string,
  "committed_date": string,
  "trailers": {},
  "extended_trailers": {},
  "web_url": string,
  "stats": {
    "additions": integer,
    "deletions": integer,
    "total": integer,
  },
  "status": string,
  "project_id": integer,
  "last_pipeline": {},
}
```

#### 400 - Bad Request

#### 404 - Not found

