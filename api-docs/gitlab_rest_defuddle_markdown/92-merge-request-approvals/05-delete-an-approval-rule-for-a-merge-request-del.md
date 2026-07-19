# 05-Delete an approval rule for a merge request [DEL]

`DELETE /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approval_rules/{approval_rule_id}`

Deletes a specified approval rule for a merge request. The `report_approver` or `code_owner` rules are system-generated, and you cannot edit them.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |
| `approval_rule_id` | `integer` | `path` | Yes | The ID of a merge request approval rule |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

