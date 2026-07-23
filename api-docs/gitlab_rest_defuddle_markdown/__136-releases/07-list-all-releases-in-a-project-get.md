# 07-List all releases in a project [GET]

`GET /api/v4/projects/{id}/releases`

Lists all releases for a specified project. Sorted by `released_at`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `order_by` | `string` | `query` | No | The field to use as order. Either `released_at` (default) or `created_at` |
| `sort` | `string` | `query` | No | The direction of the order. Either `desc` (default) for descending order or `asc` for ascending order |
| `include_html_description` | `boolean` | `query` | No | If `true`, a response includes HTML rendered markdown of the release description |
| `updated_before` | `string` | `query` | No | Return releases updated before the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `updated_after` | `string` | `query` | No | Return releases updated after the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "tag_name": string,
  "description": string,
  "created_at": string,
  "released_at": string,
  "upcoming_release": boolean,
  "description_html": string,
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
  "milestones": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "group_id": string,
    "title": string,
    "description": string,
    "state": string,
    "created_at": string,
    "updated_at": string,
    "due_date": string,
    "start_date": string,
    "expired": boolean,
    "web_url": string,
    "issue_stats": {},
  },
  "commit_path": string,
  "tag_path": string,
  "assets": string,
  "evidences": {
    "sha": string,
    "filepath": string,
    "collected_at": string,
  },
  "_links": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

