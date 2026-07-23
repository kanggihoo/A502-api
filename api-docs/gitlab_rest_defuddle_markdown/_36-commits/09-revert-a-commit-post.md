# 09-Revert a commit [POST]

`POST /api/v4/projects/{id}/repository/commits/{sha}/revert`

Reverts a commit in a specified branch.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `sha` | `string` | `path` | Yes | Commit SHA to revert |

### Request Body (application/json)

```json
{
  "branch": string (required), // Target branch name
  "dry_run": boolean, // Does not commit any changes
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
}
```

#### 400 - Bad request

#### 404 - Not found

