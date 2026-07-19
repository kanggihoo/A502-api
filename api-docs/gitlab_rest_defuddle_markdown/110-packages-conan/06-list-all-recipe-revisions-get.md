# 06-List all recipe revisions [GET]

`GET /api/v4/projects/{id}/packages/conan/v2/conans/{package_name}/{package_version}/{package_username}/{package_channel}/revisions`

Lists all revisions for a package recipe. This feature was introduced in GitLab 17.11.

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
  "reference": string, // The Conan package reference
  "revisions": [
    {
      "revision": string, // The revision hash of the Conan recipe or package
      "time": string, // The UTC timestamp when the revision was created
    }
  ], // List of recipe revisions
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

