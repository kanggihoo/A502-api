# 01-List all repository commits [GET]

`GET /api/v4/projects/{id}/repository/commits`

Lists all commits for a specified project repository.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `ref_name` | `string` | `query` | No | The name of a repository branch or tag, if not given the default branch is used |
| `since` | `string` | `query` | No | Only commits after or on this date will be returned |
| `until` | `string` | `query` | No | Only commits before or on this date will be returned |
| `path` | `string` | `query` | No | The file path |
| `follow` | `boolean` | `query` | No | Follow file renames when filtering by path |
| `author` | `string` | `query` | No | Search commits by commit author |
| `all` | `boolean` | `query` | No | Every commit will be returned |
| `with_stats` | `boolean` | `query` | No | Stats about each commit will be added to the response |
| `first_parent` | `boolean` | `query` | No | Only include the first parent of merges |
| `order` | `string` | `query` | No | List commits in order |
| `trailers` | `boolean` | `query` | No | Parse and include Git trailers for every commit |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `pagination` | `string` | `query` | No | Specify the pagination method |
| `page_token` | `string` | `query` | No | Record from which to start the keyset pagination |

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

#### 401 - Unauthorized

#### 404 - Not found

