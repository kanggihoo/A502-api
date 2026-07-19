# 30-List all package download URLs [GET]

`GET /api/v4/projects/{id}/packages/conan/v1/conans/{package_name}/{package_version}/{package_username}/{package_channel}/packages/{conan_package_reference}/download_urls`

Lists all files and associated download URLs for a specified package in the package registry. Returns the same payload as the package manifest endpoint.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `package_name` | `string` | `path` | Yes | Package name |
| `package_version` | `string` | `path` | Yes | Package version |
| `package_username` | `string` | `path` | Yes | Package username |
| `package_channel` | `string` | `path` | Yes | Package channel |
| `conan_package_reference` | `string` | `path` | Yes | Conan package ID |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "package_urls": {},
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

