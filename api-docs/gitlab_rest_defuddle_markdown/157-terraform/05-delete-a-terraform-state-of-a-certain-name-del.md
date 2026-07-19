# 05-Delete a Terraform state of a certain name [DEL]

`DELETE /api/v4/projects/{id}/terraform/state/{name}`

Delete a Terraform state of a certain name

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `name` | `string` | `path` | Yes | The name of a Terraform state |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

#### 422 - Validation failure

