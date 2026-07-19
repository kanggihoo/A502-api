# 03-Download a gem file [GET]

`GET /api/v4/projects/{id}/packages/rubygems/gems/{file_name}`

Downloads a specified gem file for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `file_name` | `string` | `path` | Yes | Package file name |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

