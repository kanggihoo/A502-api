# 07-Lock a Terraform state of a certain name [POST]

`POST /api/v4/projects/{id}/terraform/state/{name}/lock`

Lock a Terraform state of a certain name

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `name` | `string` | `path` | Yes | The name of a Terraform state |

### Request Body (application/json)

```json
{
  "ID": string (required), // Terraform state lock ID
  "Operation": string (required), // Terraform operation
  "Info": string (required), // Terraform info
  "Who": string (required), // Terraform state lock owner
  "Version": string (required), // Terraform version
  "Created": string (required), // Terraform state lock timestamp
  "Path": string (required), // Terraform path
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

#### 409 - Conflict

#### 422 - Validation failure

