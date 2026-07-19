# 09-Download the latest version of a module [GET]

`GET /api/v4/projects/{id}/packages/terraform/modules/{module_name}/{module_system}`

Downloads the latest version of a specified module. This feature was introduced in GitLab 16.7.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or full path of a project |
| `module_name` | `string` | `path` | Yes | Module name |
| `module_system` | `string` | `path` | Yes | Module system |
| `terraform-get` | `string` | `query` | No | Terraform get redirection flag |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

