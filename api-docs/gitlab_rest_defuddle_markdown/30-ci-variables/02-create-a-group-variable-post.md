# 02-Create a group variable [POST]

`POST /api/v4/groups/{id}/variables`

Creates a group variable.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group or URL-encoded path of the group owned by the authenticated<br>      user |

### Request Body (application/json)

```json
{
  "key": string (required), // The ID of a group or URL-encoded path of the group owned by the         authenticated user
  "value": string (required), // The value of a variable
  "protected": boolean, // Whether the variable is protected
  "masked_and_hidden": boolean, // Whether the variable is masked and hidden
  "masked": boolean, // Whether the variable is masked
  "raw": boolean, // Whether the variable will be expanded
  "variable_type": enum("env_var" | "file"), // The type of the variable. Default: env_var
  "environment_scope": string, // The environment scope of the variable
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

