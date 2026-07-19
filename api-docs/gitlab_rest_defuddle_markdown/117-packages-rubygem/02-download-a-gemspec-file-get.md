# 02-Download a gemspec file [GET]

`GET /api/v4/projects/{id}/packages/rubygems/quick/Marshal.4.8/{file_name}`

Downloads a gemspec file in Marshal format for a specified gem version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `file_name` | `string` | `path` | Yes | Gemspec file name |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

