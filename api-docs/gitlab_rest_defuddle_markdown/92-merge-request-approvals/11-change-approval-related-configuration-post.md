# 11-Change approval-related configuration [POST]

`POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approvals`

Deprecated in 16.0. Use the merge request approvals API instead.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Request Body (application/json)

```json
{
  "approvals_required": integer (required), // The amount of approvals required. Must be higher than the project approvals
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "iid": integer,
  "project_id": integer,
  "title": string,
  "description": string,
  "state": string,
  "created_at": string,
  "updated_at": string,
  "merge_status": string,
  "approved": boolean,
  "approvals_required": integer,
  "approvals_left": integer,
  "require_password_to_approve": boolean,
  "approved_by": [
    {
      "user": {
        "id": integer,
        "username": string,
        "public_email": string,
        "name": string,
        "state": string,
        "locked": boolean,
        "avatar_url": string,
        "avatar_path": string,
        "custom_attributes": [
          {
            "key": string,
            "value": string,
          }
        ],
        "web_url": string,
      },
      "approved_at": string,
    }
  ],
  "suggested_approvers": [
    {
      "id": integer,
      "username": string,
      "public_email": string,
      "name": string,
      "state": string,
      "locked": boolean,
      "avatar_url": string,
      "avatar_path": string,
      "custom_attributes": [
        {
          "key": string,
          "value": string,
        }
      ],
      "web_url": string,
    }
  ],
  "approvers": [
    {}
  ],
  "approver_groups": [
    {}
  ],
  "user_has_approved": boolean,
  "user_can_approve": boolean,
  "approval_rules_left": [
    {
      "id": integer,
      "name": string,
      "rule_type": string,
    }
  ],
  "has_approval_rules": boolean,
  "merge_request_approvers_available": boolean,
  "multiple_approval_rules_available": boolean,
  "invalid_approvers_rules": [
    {
      "id": integer,
      "name": string,
      "rule_type": string,
    }
  ],
}
```

#### 400 - Bad Request

#### 404 - Not Found

