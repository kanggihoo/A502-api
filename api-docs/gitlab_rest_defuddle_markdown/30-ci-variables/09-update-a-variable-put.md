# 09-Update a variable [PUT]

`PUT /api/v4/projects/{id}/variables/{key}`

Updates a project variable. If there are multiple variables with the same key, use `filter` to select the correct `environment_scope`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID of a project or URL-encoded NAMESPACE/PROJECT_NAME of the project owned by the authenticated user |
| `key` | `string` | `path` | Yes | The key of a variable |

### Request Body (application/json)

```json
{
  "value": string, // The value of a variable
  "protected": boolean, // Whether the variable is protected
  "masked": boolean, // Whether the variable is masked
  "environment_scope": string, // The environment_scope of a variable
  "raw": boolean, // Whether the variable will be expanded
  "variable_type": enum("env_var" | "file"), // The type of the variable. Default: env_var
  "filter": {
    "environment_scope": string, // The environment scope of a variable
  }, // Available filters: [environment_scope]. Example: filter[environment_scope]=production
  "description": string, // The description of the variable
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

#### 404 - Variable Not Found

