# 12-Retrieve latest version for a module [GET]

`GET /api/v4/packages/terraform/modules/v1/{module_namespace}/{module_name}/{module_system}`

Retrieves latest version for a specified module.

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
  "name": string,
  "provider": string,
  "providers": string,
  "root": string,
  "source": string,
  "submodules": string,
  "version": string,
  "versions": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

