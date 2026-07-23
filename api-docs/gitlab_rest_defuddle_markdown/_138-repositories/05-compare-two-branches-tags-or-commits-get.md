# 05-Compare two branches, tags, or commits [GET]

`GET /api/v4/projects/{id}/repository/compare`

Compare two branches, tags, or commits

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `from` | `string` | `query` | Yes | The commit, branch name, or tag name to start comparison |
| `to` | `string` | `query` | Yes | The commit, branch name, or tag name to stop comparison |
| `from_project_id` | `integer` | `query` | No | The project to compare from |
| `straight` | `boolean` | `query` | No | Comparison method, `true` for direct comparison between `from` and `to` (`from`..`to`), `false` to compare using merge base (`from`...`to`) |
| `unidiff` | `boolean` | `query` | No | A diff in a Unified diff format |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
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
  "commits": [
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
  ],
  "diffs": [
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
  ],
  "compare_timeout": boolean,
  "compare_same_ref": boolean,
  "web_url": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

