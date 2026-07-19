# 02-Download a chart [GET]

`GET /api/v4/projects/{id}/packages/helm/{channel}/charts/{file_name}.tgz`

Downloads a specified chart for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or full path of a project |
| `channel` | `string` | `path` | Yes | Helm channel |
| `file_name` | `string` | `path` | Yes | Helm package file name |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

