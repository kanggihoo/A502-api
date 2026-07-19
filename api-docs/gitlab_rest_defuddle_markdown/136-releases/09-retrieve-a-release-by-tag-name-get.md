# 09-Retrieve a release by tag name [GET]

`GET /api/v4/projects/{id}/releases/{tag_name}`

Retrieves a release with a specified tag name.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `tag_name` | `string` | `path` | Yes | The Git tag the release is associated with |
| `include_html_description` | `boolean` | `query` | No | If `true`, a response includes HTML rendered markdown of the release description |

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

#### 401 - Unauthorized

#### 404 - Not found

