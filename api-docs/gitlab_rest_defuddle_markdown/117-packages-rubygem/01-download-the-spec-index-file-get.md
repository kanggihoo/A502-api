# 01-Download the spec index file [GET]

`GET /api/v4/projects/{id}/packages/rubygems/{file_name}`

Downloads a RubyGems spec index file (specs.4.8.gz, latest_specs.4.8.gz, or prerelease_specs.4.8.gz) for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `file_name` | `string` | `path` | Yes | Spec file name |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

