# 06-Download a Cargo crate [GET]

`GET /api/v4/projects/{id}/packages/cargo/{package_name}/{package_version}/download`

This endpoint serves the .crate file for a given package name and version

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `package_name` | `string` | `path` | Yes | The cargo package name |
| `package_version` | `string` | `path` | Yes | The cargo package version |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

