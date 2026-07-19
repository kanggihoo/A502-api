# 53-Create a container repository protection rule [POST]

`POST /api/v4/projects/{id}/registry/protection/repository/rules`

Creates a container repository protection rule for a specified project to control who can push or delete container images.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "repository_path_pattern": string (required), // Container repository path pattern protected by the protection rule.             For example `flight/flight-*`. Wildcard character `*` allowed.
  "minimum_access_level_for_push": enum("maintainer" | "owner" | "admin"), // Minimum GitLab access level to allow to push container images to the container registry.             For example maintainer, owner or admin.
  "minimum_access_level_for_delete": enum("maintainer" | "owner" | "admin"), // Minimum GitLab access level to allow to delete container images in the container registry.             For example maintainer, owner or admin.
}
```
### Responses

#### 201 - Created

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

