# 11-Retrieve download URL for latest module version [GET]

`GET /api/v4/packages/terraform/modules/v1/{module_namespace}/{module_name}/{module_system}/download`

Retrieves download URL for latest module version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `module_namespace` | `string` | `path` | Yes | Group's ID or slug |
| `module_name` | `string` | `path` | Yes | Name of the module |
| `module_system` | `string` | `path` | Yes | System of the module |

### Responses

#### 302 - Found

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

