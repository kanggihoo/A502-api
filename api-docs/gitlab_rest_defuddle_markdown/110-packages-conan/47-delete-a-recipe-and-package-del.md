# 47-Delete a recipe and package [DEL]

`DELETE /api/v4/packages/conan/v1/conans/{package_name}/{package_version}/{package_username}/{package_channel}`

Deletes a specified Conan recipe and associated package files from the package registry.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `package_name` | `string` | `path` | Yes | Package name |
| `package_version` | `string` | `path` | Yes | Package version |
| `package_username` | `string` | `path` | Yes | Package username |
| `package_channel` | `string` | `path` | Yes | Package channel |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

