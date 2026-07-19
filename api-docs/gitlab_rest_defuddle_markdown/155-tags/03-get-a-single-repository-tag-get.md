# 03-Get a single repository tag [GET]

`GET /api/v4/projects/{id}/repository/tags/{tag_name}`

Get a single repository tag

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `tag_name` | `string` | `path` | Yes | The name of the tag |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "message": string,
  "target": string,
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
  "release": {
    "tag_name": string,
    "description": string,
  },
  "protected": boolean,
  "created_at": string,
}
```

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not found

