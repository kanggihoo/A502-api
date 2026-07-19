# 04-Retrieve a repository branch [GET]

`GET /api/v4/projects/{id}/repository/branches/{branch}`

Retrieves a specified project repository branch.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `branch` | `string` | `path` | Yes | The name of the branch |

### Responses

#### 200 - OK

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

#### 400 - Bad Request

#### 404 - Project Not Found

