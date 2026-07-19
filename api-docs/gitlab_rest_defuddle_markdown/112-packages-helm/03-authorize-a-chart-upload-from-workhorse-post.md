# 03-Authorize a chart upload from workhorse [POST]

`POST /api/v4/projects/{id}/packages/helm/api/{channel}/charts/authorize`

This feature was introduced in GitLab 14.0

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

