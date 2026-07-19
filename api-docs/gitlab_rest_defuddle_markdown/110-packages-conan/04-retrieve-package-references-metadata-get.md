# 04-Retrieve package references metadata [GET]

`GET /api/v4/projects/{id}/packages/conan/v2/conans/{package_name}/{package_version}/{package_username}/{package_channel}/search`

Retrieves the metadata for all package references of a specified package. This feature was introduced in GitLab 18.0.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `package_name` | `string` | `path` | Yes | Package name |
| `package_version` | `string` | `path` | Yes | Package version |
| `package_username` | `string` | `path` | Yes | Package username |
| `package_channel` | `string` | `path` | Yes | Package channel |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

