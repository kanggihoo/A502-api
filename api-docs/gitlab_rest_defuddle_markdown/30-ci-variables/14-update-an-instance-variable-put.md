# 14-Update an instance variable [PUT]

`PUT /api/v4/admin/ci/variables/{key}`

Updates a specified instance variable.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | `string` | `path` | Yes | The key of a variable |

### Request Body (application/json)

```json
{
  "description": string, // The description of the variable
  "value": string, // The value of a variable
  "protected": boolean, // Whether the variable is protected
  "masked": boolean, // Whether the variable is masked
  "raw": boolean, // Whether the variable will be expanded
  "variable_type": enum("env_var" | "file"), // The type of a variable. Available types are: env_var (default) and file
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "variable_type": string,
  "key": string,
  "value": string,
  "hidden": boolean,
  "protected": boolean,
  "masked": boolean,
  "raw": boolean,
  "environment_scope": string,
  "description": string,
}
```

#### 400 - Bad Request

#### 404 - Instance Variable Not Found

