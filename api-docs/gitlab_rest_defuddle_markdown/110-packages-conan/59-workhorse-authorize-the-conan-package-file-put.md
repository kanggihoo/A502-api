# 59-Workhorse authorize the Conan package file [PUT]

`PUT /api/v4/packages/conan/v1/files/{package_name}/{package_version}/{package_username}/{package_channel}/{recipe_revision}/package/{conan_package_reference}/{package_revision}/{file_name}/authorize`

Authorizes the Conan package file.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `package_name` | `string` | `path` | Yes | Package name |
| `package_version` | `string` | `path` | Yes | Package version |
| `package_username` | `string` | `path` | Yes | Package username |
| `package_channel` | `string` | `path` | Yes | Package channel |
| `recipe_revision` | `string` | `path` | Yes | Conan Recipe Revision |
| `conan_package_reference` | `string` | `path` | Yes | Conan Package ID |
| `package_revision` | `string` | `path` | Yes | Conan Package Revision |
| `file_name` | `string` | `path` | Yes | Package file name |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

