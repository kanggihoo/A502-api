# 02-Delete a Terraform state version [DEL]

`DELETE /api/v4/projects/{id}/terraform/state/{name}/versions/{serial}`

Delete a Terraform state version

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `name` | `string` | `path` | Yes | The name of a Terraform state |
| `serial` | `integer` | `path` | Yes | The version number of the state |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

