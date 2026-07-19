# 10-List all available versions for a module [GET]

`GET /api/v4/packages/terraform/modules/v1/{module_namespace}/{module_name}/{module_system}/versions`

Lists all available versions for a specified module.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `module_namespace` | `string` | `path` | Yes | Group's ID or slug |
| `module_name` | `string` | `path` | Yes | Name of the module |
| `module_system` | `string` | `path` | Yes | System of the module |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "modules": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

