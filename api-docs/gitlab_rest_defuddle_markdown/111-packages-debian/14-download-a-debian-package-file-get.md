# 14-Download a Debian package file [GET]

`GET /api/v4/projects/{id}/packages/debian/pool/{distribution}/{letter}/{package_name}/{package_version}/{file_name}`

Downloads a specified Debian package file for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `distribution` | `string` | `path` | Yes | The Debian Codename or Suite |
| `letter` | `string` | `path` | Yes | The Debian Classification (first-letter or lib-first-letter) |
| `package_name` | `string` | `path` | Yes | The Debian Source Package Name |
| `package_version` | `string` | `path` | Yes | The Debian Source Package Version |
| `file_name` | `string` | `path` | Yes | The Debian File Name |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

