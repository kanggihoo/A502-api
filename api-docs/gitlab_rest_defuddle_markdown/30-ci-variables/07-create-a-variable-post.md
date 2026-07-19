# 07-Create a variable [POST]

`POST /api/v4/projects/{id}/variables`

Creates a variable. If a variable with the same `key` already exists, the variable must have a different `environment_scope`. Otherwise, GitLab returns a message similar to: `VARIABLE_NAME has already been taken`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID of a project or URL-encoded NAMESPACE/PROJECT_NAME of the project owned by the authenticated user |

### Request Body (application/json)

```json
{
  "key": string (required), // The key of a variable
  "value": string (required), // The value of a variable
  "protected": boolean, // Whether the variable is protected
  "masked": boolean, // Whether the variable is masked
  "masked_and_hidden": boolean, // Whether the variable is masked and hidden
  "raw": boolean, // Whether the variable will be expanded
  "variable_type": enum("env_var" | "file"), // The type of the variable. Default: env_var
  "environment_scope": string, // The environment_scope of the variable
  "description": string, // The description of the variable
}
```
### Responses

#### 201 - Created

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

#### 400 - 400 Bad Request

#### 404 - Not Found

