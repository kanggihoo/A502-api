# 32-List all package upload URLs [POST]

`POST /api/v4/projects/{id}/packages/conan/v1/conans/{package_name}/{package_version}/{package_username}/{package_channel}/packages/{conan_package_reference}/upload_urls`

Lists all the upload URLs for a specified collection of package files. The request must include a JSON object with the name and size of the individual files.

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
  "upload_urls": {},
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

