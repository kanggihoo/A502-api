# 08-Retrieve MR approval settings for a group [GET]

`GET /api/v4/groups/{id}/merge_request_approval_setting`

Retrieves the merge request approval settings for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of a group |

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

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

