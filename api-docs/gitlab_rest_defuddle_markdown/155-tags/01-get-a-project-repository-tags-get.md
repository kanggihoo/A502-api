# 01-Get a project repository tags [GET]

`GET /api/v4/projects/{id}/repository/tags`

Get a project repository tags

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `sort` | `string` | `query` | No | Return tags sorted in updated by `asc` or `desc` order. |
| `order_by` | `string` | `query` | No | Return tags ordered by `name`, `updated`, `version` fields. |
| `search` | `string` | `query` | No | Return list of tags matching the search criteria |
| `page_token` | `string` | `query` | No | Name of tag to start the pagination from |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

#### 422 - Unprocessable entity

#### 503 - Service unavailable

