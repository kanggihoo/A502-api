# 13-Retrieve latest package revision [GET]

`GET /api/v4/projects/{id}/packages/conan/v2/conans/{package_name}/{package_version}/{package_username}/{package_channel}/revisions/{recipe_revision}/packages/{conan_package_reference}/latest`

Retrieves the revision hash and creation date of the latest package revision for a specified recipe revision and package reference. This feature was introduced in GitLab 17.11.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `package_name` | `string` | `path` | Yes | Package name |
| `package_version` | `string` | `path` | Yes | Package version |
| `package_username` | `string` | `path` | Yes | Package username |
| `package_channel` | `string` | `path` | Yes | Package channel |
| `recipe_revision` | `string` | `path` | Yes | Recipe revision |
| `conan_package_reference` | `string` | `path` | Yes | Package reference |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "revision": string, // The revision hash of the Conan recipe or package
  "time": string, // The UTC timestamp when the revision was created
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

