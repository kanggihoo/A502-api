# 12-Create instance variable [POST]

`POST /api/v4/admin/ci/variables`

Creates a instance-level variable. The maximum number of instance-level variables can be changed.

### Request Body (application/json)

```json
{
  "key": string (required), // The key of the variable. Max 255 characters
  "description": string, // The description of the variable
  "value": string (required), // The value of a variable
  "protected": boolean, // Whether the variable is protected
  "masked": boolean, // Whether the variable is masked
  "raw": boolean, // Whether the variable will be expanded
  "variable_type": enum("env_var" | "file"), // The type of a variable. Available types are: env_var (default) and file
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

