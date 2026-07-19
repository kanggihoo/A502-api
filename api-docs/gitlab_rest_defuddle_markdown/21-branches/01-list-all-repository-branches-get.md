# 01-List all repository branches [GET]

`GET /api/v4/projects/{id}/repository/branches`

Lists all repository branches from a specified project, sorted alphabetically by name. Search by name, or use regular expressions to find specific branch patterns. Returns detailed information about the branch, including its protection status, merge status, and commit details.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `search` | `string` | `query` | No | Return list of branches matching the search criteria |
| `regex` | `string` | `query` | No | Return list of branches matching the regex |
| `sort` | `string` | `query` | No | Return list of branches sorted by the given field |
| `page_token` | `string` | `query` | No | Name of branch to start the pagination from |

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

#### 404 - 404 Project Not Found

