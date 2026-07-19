# 03-Update push rules of a group [PUT]

`PUT /api/v4/groups/{id}/push_rule`

Updates the push rules for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of a group |

### Request Body (application/json)

```json
{
  "deny_delete_tag": boolean, // Deny deleting a tag
  "member_check": boolean, // Restrict commits by author (email) to existing GitLab users
  "prevent_secrets": boolean, // GitLab will reject any files that are likely to contain secrets
  "commit_message_regex": string, // All commit messages must match this
  "commit_message_negative_regex": string, // No commit message is allowed to match this
  "branch_name_regex": string, // All branches names must match this
  "author_email_regex": string, // All commit author emails must match this
  "file_name_regex": string, // All committed filenames must not match this
  "max_file_size": integer, // Maximum file size (MB)
  "commit_committer_check": boolean, // Users can only push commits to this repository if the committer email is one of their own verified emails.
  "commit_committer_name_check": boolean, // Users can only push commits to this repository if the commit author name is consistent with their GitLab account name.
  "reject_unsigned_commits": boolean, // Reject commit when it’s not signed.
  "reject_non_dco_commits": boolean, // Reject commit when it’s not DCO certified.
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "created_at": string,
  "commit_message_regex": string,
  "commit_message_negative_regex": string,
  "branch_name_regex": string,
  "author_email_regex": string,
  "file_name_regex": string,
  "deny_delete_tag": boolean,
  "member_check": boolean,
  "prevent_secrets": boolean,
  "max_file_size": integer,
  "commit_committer_check": boolean,
  "commit_committer_name_check": boolean,
  "reject_unsigned_commits": boolean,
  "reject_non_dco_commits": boolean,
}
```

#### 400 - Validation error

#### 404 - Not found

#### 422 - Unprocessable entity

