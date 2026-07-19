# 05-Get the sparse index for a Cargo crate (4+ character name) [GET]

`GET /api/v4/projects/{id}/packages/cargo/{prefix_1}/{prefix_2}/{package_name}`

Returns newline-delimited JSON, one line per published version, most recently published first. Limited to the 500 most recently published versions.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `prefix_1` | `string` | `path` | Yes | First two characters of the cargo package name |
| `prefix_2` | `string` | `path` | Yes | Next two characters of the cargo package name |
| `package_name` | `string` | `path` | Yes | The cargo package name |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

