# 07-Download a package file [GET]

`GET /api/v4/projects/{id}/packages/{package_id}/package_files/{package_file_id}/download`

This feature was introduced in GitLab 18.4

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | ID or URL-encoded path of the project |
| `package_id` | `integer` | `path` | Yes | ID of a package |
| `package_file_id` | `integer` | `path` | Yes | ID of a package file |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

