# 06-Delete a Terraform state protection rule [DEL]

`DELETE /api/v4/projects/{id}/terraform/state_protection_rules/{terraform_state_protection_rule_id}`

This feature was introduced in GitLab 19.0.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `terraform_state_protection_rule_id` | `integer` | `path` | Yes | The ID of the Terraform state protection rule |

### Responses

#### 204 - 204 No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

