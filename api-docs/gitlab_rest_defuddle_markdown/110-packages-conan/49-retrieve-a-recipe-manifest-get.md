# 49-Retrieve a recipe manifest [GET]

`GET /api/v4/packages/conan/v1/conans/{package_name}/{package_version}/{package_username}/{package_channel}/digest`

Retrieves a manifest that includes a list of files and associated download URLs for a specified recipe.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
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

