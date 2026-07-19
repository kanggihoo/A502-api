# 25-Retrieve a package snapshot [GET]

`GET /api/v4/projects/{id}/packages/conan/v1/conans/{package_name}/{package_version}/{package_username}/{package_channel}/packages/{conan_package_reference}`

Retrieves a snapshot of the files for a specified Conan package and reference. The snapshot is a list of filenames with their associated MD5 hash.

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
  "package_snapshot": {},
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

