# 07-Retrieve a merge request diff version [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/versions/{version_id}`

Retrieves a merge request diff version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The internal ID of the merge request |
| `version_id` | `integer` | `path` | Yes | The ID of the merge request diff version |
| `unidiff` | `boolean` | `query` | No | A diff in a Unified diff format |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "head_commit_sha": string,
  "base_commit_sha": string,
  "start_commit_sha": string,
  "created_at": string,
  "merge_request_id": integer,
  "state": string,
  "real_size": string,
  "patch_id_sha": string,
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
}
```

#### 400 - Bad Request

#### 404 - Not Found

