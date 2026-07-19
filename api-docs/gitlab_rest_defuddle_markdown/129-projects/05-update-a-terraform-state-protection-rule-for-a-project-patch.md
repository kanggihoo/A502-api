# 05-Update a Terraform state protection rule for a project [PATCH]

`PATCH /api/v4/projects/{id}/terraform/state_protection_rules/{terraform_state_protection_rule_id}`

This feature was introduced in GitLab 19.0.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `terraform_state_protection_rule_id` | `integer` | `path` | Yes | The ID of the Terraform state protection rule |

### Request Body (application/json)

```json
{
  "state_name": string, // Terraform state name to protect.
  "minimum_access_level_for_write": enum("developer" | "maintainer" | "owner" | "admin"), // If defined, sets the minimum GitLab access level required to write to the Terraform state.
  "allowed_from": enum("anywhere" | "ci_only" | "ci_on_protected_branch_only"), // If defined, write requests must be made from the specific source.
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "state_name": string,
  "minimum_access_level_for_write": string,
  "allowed_from": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

#### 422 - Unprocessable Entity

