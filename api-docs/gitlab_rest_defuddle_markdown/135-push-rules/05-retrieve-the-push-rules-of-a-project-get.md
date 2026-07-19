# 05-Retrieve the push rules of a project [GET]

`GET /api/v4/projects/{id}/push_rule`

Retrieves the push rules of a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "created_at": string,
  "commit_message_regex": string,
  "commit_message_negative_regex": string,
  "branch_name_regex": string,
  "deny_delete_tag": boolean,
  "member_check": boolean,
  "prevent_secrets": boolean,
  "author_email_regex": string,
  "file_name_regex": string,
  "max_file_size": integer,
  "commit_committer_check": boolean,
  "commit_committer_name_check": boolean,
  "reject_unsigned_commits": boolean,
  "reject_non_dco_commits": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not found

