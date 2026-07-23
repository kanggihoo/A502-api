# 05-List all commit comments [GET]

`GET /api/v4/projects/{id}/repository/commits/{sha}/comments`

Lists all the comments of a commit in a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `sha` | `string` | `path` | Yes | A commit sha, or the name of a branch or tag |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "note": string,
  "path": string,
  "line": integer,
  "line_type": string,
  "author": {
    "id": integer,
    "username": string,
    "public_email": string,
    "name": string,
    "state": string,
    "locked": boolean,
    "avatar_url": string,
    "avatar_path": string,
    "custom_attributes": [
      {
        "key": string,
        "value": string,
      }
    ],
    "web_url": string,
  },
  "created_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not found

