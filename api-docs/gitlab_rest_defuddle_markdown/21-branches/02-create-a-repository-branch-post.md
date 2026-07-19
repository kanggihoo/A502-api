# 02-Create a repository branch [POST]

`POST /api/v4/projects/{id}/repository/branches`

Creates a branch in the repository.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "branch": string (required), // The name of the branch
  "ref": string (required), // Create branch from commit sha or existing branch
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "name": string,
  "commit": {
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
  },
  "merged": boolean,
  "protected": boolean,
  "developers_can_push": boolean,
  "developers_can_merge": boolean,
  "can_push": boolean,
  "default": boolean,
  "web_url": string,
}
```

#### 400 - Branch already exists

#### 404 - Not Found

