# 04-Create a Terraform state protection rule for a project [POST]

`POST /api/v4/projects/{id}/terraform/state_protection_rules`

This feature was introduced in GitLab 19.1.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "state_name": string (required), // Terraform state name to protect. Maximum 255 characters. Must be unique per project.
  "minimum_access_level_for_write": enum("developer" | "maintainer" | "owner" | "admin") (required), // Minimum GitLab access level required to write to the Terraform state. Valid values: developer, maintainer, owner, admin.
  "allowed_from": enum("anywhere" | "ci_only" | "ci_on_protected_branch_only"), // Source restriction for write requests. Default: anywhere. Valid values: anywhere, ci_only, ci_on_protected_branch_only.
}
```
### Responses

#### 201 - Created

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

