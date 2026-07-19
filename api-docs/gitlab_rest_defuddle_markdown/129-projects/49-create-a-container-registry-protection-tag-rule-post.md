# 49-Create a container registry protection tag rule [POST]

`POST /api/v4/projects/{id}/registry/protection/tag/rules`

Creates a container registry protection tag rule for a project to control who can push or delete container tags. This feature was introduced in GitLab 18.8.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |

### Request Body (application/json)

```json
{
  "tag_name_pattern": string (required), // Container tag name pattern protected by the protection rule. For example, `v*-release`. Wildcard character `*` allowed.
  "minimum_access_level_for_push": enum("maintainer" | "owner" | "admin") (required), // Minimum GitLab access level required to push container tags. For example, Maintainer, Owner, or Admin.
  "minimum_access_level_for_delete": enum("maintainer" | "owner" | "admin") (required), // Minimum GitLab access level required to delete container tags. For example, Maintainer, Owner, or Admin.
}
```
### Responses

#### 201 - Created

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

