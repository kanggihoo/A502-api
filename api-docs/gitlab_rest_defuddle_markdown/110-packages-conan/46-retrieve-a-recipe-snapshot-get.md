# 46-Retrieve a recipe snapshot [GET]

`GET /api/v4/packages/conan/v1/conans/{package_name}/{package_version}/{package_username}/{package_channel}`

Retrieves a snapshot of the files for a specified Conan recipe. The snapshot is a list of filenames with their associated MD5 hash.

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
  "recipe_snapshot": {},
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

