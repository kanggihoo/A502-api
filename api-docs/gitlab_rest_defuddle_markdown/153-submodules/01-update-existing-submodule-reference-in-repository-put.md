# 01-Update existing submodule reference in repository [PUT]

`PUT /api/v4/projects/{id}/repository/submodules/{submodule}`

Update existing submodule reference in repository

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of a project |
| `submodule` | `string` | `path` | Yes | URL-encoded full path to submodule. |

### Request Body (application/json)

```json
{
  "commit_sha": string (required), // Commit sha to update the submodule to.
  "branch": string (required), // Name of the branch to commit into.
  "commit_message": string, // Commit message. If no message is provided a default one will be set.
}
```
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

#### 400 - The repository is empty

#### 401 - 401 Unauthorized

#### 404 - 404 Project Not Found

