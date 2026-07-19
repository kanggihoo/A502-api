# 09-Update MR approval settings for a group [PUT]

`PUT /api/v4/groups/{id}/merge_request_approval_setting`

Updates the merge request approval settings for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of a group |

### Request Body (application/json)

```json
{
  "allow_author_approval": boolean, // Allow authors to self-approve merge requests
  "allow_committer_approval": boolean, // Allow committers to approve merge requests
  "allow_overrides_to_approver_list_per_merge_request": boolean, // Allow overrides to approver list per merge request
  "retain_approvals_on_push": boolean, // Retain approval count on a new push
  "selective_code_owner_removals": boolean, // Reset approvals from Code Owners if their files changed
  "require_password_to_approve": boolean, // Require approver to authenticate before approving
  "require_reauthentication_to_approve": boolean, // Require approver to authenticate before approving
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "allow_author_approval": boolean,
  "allow_committer_approval": boolean,
  "allow_overrides_to_approver_list_per_merge_request": boolean,
  "retain_approvals_on_push": boolean,
  "selective_code_owner_removals": boolean,
  "require_password_to_approve": boolean,
  "require_reauthentication_to_approve": boolean,
}
```

#### 400 - Validation error

#### 403 - Forbidden

#### 404 - Not Found

