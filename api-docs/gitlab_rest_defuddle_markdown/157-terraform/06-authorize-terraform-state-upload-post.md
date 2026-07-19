# 06-Authorize Terraform state upload [POST]

`POST /api/v4/projects/{id}/terraform/state/{name}/authorize`

This feature was introduced in GitLab 18.5

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `name` | `string` | `path` | Yes | The name of a Terraform state |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

