# 45-Create a package protection rule [POST]

`POST /api/v4/projects/{id}/packages/protection/rules`

Creates a package protection rule for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "package_name_pattern": string (required), // Package name protected by the rule. For example @my-scope/my-package-*.             Wildcard character * allowed.
  "package_type": enum("cargo" | "conan" | "generic" | "helm" | "maven" | "npm" | "nuget" | "pypi" | "terraform_module") (required), // Package type protected by the rule. For example npm.
  "minimum_access_level_for_delete": enum("owner" | "admin"), // Minimum GitLab access level required to delete a package. Valid values include `null`, `owner` or `admin`. If the value is `null`, the default minimum access level is `maintainer`. Must be provided when `minimum_access_level_for_push` is not set. Behind a feature flag named `packages_protected_packages_delete`. Disabled by default.
  "minimum_access_level_for_push": enum("maintainer" | "owner" | "admin"), // Minimum GitLab access level required to push a package. Valid values include `null`, `maintainer`, `owner` or `admin`. If the value is `null`, the default minimum access level is `developer`. Must be provided when `minimum_access_level_for_delete` is not set.
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "package_name_pattern": string,
  "package_type": string,
  "minimum_access_level_for_delete": string,
  "minimum_access_level_for_push": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

#### 422 - Unprocessable Entity

