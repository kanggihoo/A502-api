# 13-Download Debian package [GET]

`GET /api/v4/groups/{id}/-/packages/debian/pool/{distribution}/{project_id}/{letter}/{package_name}/{package_version}/{file_name}`

This feature was introduced in GitLab 14.2

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The group ID or full group path. |
| `project_id` | `integer` | `path` | Yes | The Project Id |
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

