# 54-Update a container repository protection rule [PATCH]

`PATCH /api/v4/projects/{id}/registry/protection/repository/rules/{protection_rule_id}`

Updates a container repository protection rule for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `protection_rule_id` | `integer` | `path` | Yes | The ID of the container protection rule |

### Request Body (application/json)

```json
{
  "repository_path_pattern": string, // Container repository path pattern protected by the protection rule.               For example `flight/flight-*`. Wildcard character `*` allowed.
  "minimum_access_level_for_push": enum("maintainer" | "owner" | "admin" | ""), // Minimum GitLab access level to allow to push container images to the container registry.               For example maintainer, owner or admin. To unset the value, use an empty string `""`.
  "minimum_access_level_for_delete": enum("maintainer" | "owner" | "admin" | ""), // Minimum GitLab access level to allow to delete container images in the container registry.               For example maintainer, owner or admin. To unset the value, use an empty string `""`.
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "repository_path_pattern": string,
  "minimum_access_level_for_push": string,
  "minimum_access_level_for_delete": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

#### 422 - Unprocessable Entity

