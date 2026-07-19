# 04-Update a group variable [PUT]

`PUT /api/v4/groups/{id}/variables/{key}`

Updates a specified group variable. If there are multiple variables with the same key, use `filter` to select the correct `environment_scope`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group or URL-encoded path of the group owned by the authenticated<br>      user |
| `key` | `string` | `path` | Yes | The key of a variable |

### Request Body (application/json)

```json
{
  "value": string, // The value of a variable
  "protected": boolean, // Whether the variable is protected
  "masked": boolean, // Whether the variable is masked
  "raw": boolean, // Whether the variable will be expanded
  "variable_type": enum("env_var" | "file"), // The type of the variable. Default: env_var
  "environment_scope": string, // The environment scope of the variable
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

#### 400 - 400 Bad Request

#### 404 - Group Variable Not Found

