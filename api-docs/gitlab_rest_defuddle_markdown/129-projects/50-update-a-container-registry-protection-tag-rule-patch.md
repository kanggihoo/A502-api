# 50-Update a container registry protection tag rule [PATCH]

`PATCH /api/v4/projects/{id}/registry/protection/tag/rules/{protection_rule_id}`

Updates a container registry protection tag rule for a project. This feature was introduced in GitLab 18.9.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `protection_rule_id` | `integer` | `path` | Yes | The ID of the container protection tag rule. |

### Request Body (application/json)

```json
{
  "tag_name_pattern": string, // Container tag name pattern protected by the protection rule. For example, `v*-release`. Wildcard character `*` allowed.
  "minimum_access_level_for_push": enum("maintainer" | "owner" | "admin" | ""), // Minimum GitLab access level required to push container tags. For example, Maintainer, Owner, or Admin. To unset the value, use an empty string (`""`).
  "minimum_access_level_for_delete": enum("maintainer" | "owner" | "admin" | ""), // Minimum GitLab access level required to delete container tags. For example, Maintainer, Owner, or Admin. To unset the value, use an empty string (`""`).
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "tag_name_pattern": string,
  "minimum_access_level_for_push": string,
  "minimum_access_level_for_delete": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

#### 422 - Unprocessable Entity

