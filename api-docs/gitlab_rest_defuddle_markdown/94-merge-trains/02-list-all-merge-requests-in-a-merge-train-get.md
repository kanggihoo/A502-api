# 02-List all merge requests in a merge train [GET]

`GET /api/v4/projects/{id}/merge_trains/{target_branch}`

Lists all merge requests in a merge train for a target branch.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `target_branch` | `string` | `path` | Yes | The target branch of the merge request |
| `scope` | `string` | `query` | No | The scope of merge trains |
| `sort` | `string` | `query` | No | Sort by asc (ascending) or desc (descending) |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "merge_request": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "title": string,
    "description": string,
    "state": string,
    "created_at": string,
    "updated_at": string,
    "web_url": string,
  },
  "user": {
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
  "pipeline": {
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
  },
  "created_at": string,
  "updated_at": string,
  "target_branch": string,
  "status": string,
  "merged_at": string,
  "duration": integer, // Time spent in seconds
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

