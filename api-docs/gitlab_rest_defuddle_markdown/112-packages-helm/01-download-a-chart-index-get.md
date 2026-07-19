# 01-Download a chart index [GET]

`GET /api/v4/projects/{id}/packages/helm/{channel}/index.yaml`

Downloads a specified chart index for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or full path of a project |
| `channel` | `string` | `path` | Yes | Helm channel |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

