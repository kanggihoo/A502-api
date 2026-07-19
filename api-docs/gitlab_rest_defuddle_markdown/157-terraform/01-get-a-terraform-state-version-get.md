# 01-Get a Terraform state version [GET]

`GET /api/v4/projects/{id}/terraform/state/{name}/versions/{serial}`

Get a Terraform state version

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `name` | `string` | `path` | Yes | The name of a Terraform state |
| `serial` | `integer` | `path` | Yes | The version number of the state |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

