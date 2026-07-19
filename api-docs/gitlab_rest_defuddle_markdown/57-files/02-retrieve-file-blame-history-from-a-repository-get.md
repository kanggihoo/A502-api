# 02-Retrieve file blame history from a repository [GET]

`GET /api/v4/projects/{id}/repository/files/{file_path}/blame`

Retrieves blame history for a specified file in a repository. Each blame range contains lines and their corresponding commit information.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `file_path` | `string` | `path` | Yes | The URL-encoded path to the file. |
| `ref` | `string` | `query` | Yes | The name of branch, tag or commit |
| `range` | `object` | `query` | No | Object that contains the blame range |
| `range[start]` | `integer` | `query` | Yes | The first line of the range to blame |
| `range[end]` | `integer` | `query` | Yes | The last line of the range to blame |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "commit": {
    "id": string,
    "parent_ids": [
      string
    ],
    "message": string,
    "authored_date": string,
    "author_name": string,
    "author_email": string,
    "committed_date": string,
    "committer_name": string,
    "committer_email": string,
  },
  "lines": [
    string
  ],
}
```

#### 400 - Bad Request

#### 404 - Not Found

