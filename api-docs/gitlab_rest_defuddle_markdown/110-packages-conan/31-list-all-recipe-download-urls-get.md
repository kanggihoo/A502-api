# 31-List all recipe download URLs [GET]

`GET /api/v4/projects/{id}/packages/conan/v1/conans/{package_name}/{package_version}/{package_username}/{package_channel}/download_urls`

Lists all files and associated download URLs for a specified recipe in the package registry. Returns the same payload as the recipe manifest endpoint.

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

Schema (application/json):
```json
{
  "recipe_urls": {},
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

