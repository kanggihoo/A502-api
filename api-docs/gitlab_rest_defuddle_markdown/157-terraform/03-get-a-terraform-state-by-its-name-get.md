# 03-Get a Terraform state by its name [GET]

`GET /api/v4/projects/{id}/terraform/state/{name}`

Get a Terraform state by its name

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `name` | `string` | `path` | Yes | The name of a Terraform state |
| `ID` | `string` | `query` | No | Terraform state lock ID |

### Responses

#### 200 - OK

#### 204 - Empty state

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

#### 422 - Validation failure

