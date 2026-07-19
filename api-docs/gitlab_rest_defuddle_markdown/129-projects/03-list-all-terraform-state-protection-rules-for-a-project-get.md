# 03-List all Terraform state protection rules for a project [GET]

`GET /api/v4/projects/{id}/terraform/state_protection_rules`

Lists all Terraform state protection rules for a project. This feature was introduced in GitLab 18.11.

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
  "state_name": string,
  "minimum_access_level_for_write": string,
  "allowed_from": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

