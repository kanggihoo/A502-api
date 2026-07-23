# 04-Retrieve a commit diff [GET]

`GET /api/v4/projects/{id}/repository/commits/{sha}/diff`

Retrieves the diff of a commit in a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `sha` | `string` | `path` | Yes | A commit sha, or the name of a branch or tag |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `unidiff` | `boolean` | `query` | No | A diff in a Unified diff format |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "diff": string,
  "collapsed": boolean,
  "too_large": boolean,
  "new_path": string,
  "old_path": string,
  "a_mode": string,
  "b_mode": string,
  "new_file": boolean,
  "renamed_file": boolean,
  "deleted_file": boolean,
  "generated_file": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not found

