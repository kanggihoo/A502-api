# 15-Delete instance variable [DEL]

`DELETE /api/v4/admin/ci/variables/{key}`

Deletes a specified instance variable.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | `string` | `path` | Yes | The key of a variable |

### Responses

#### 204 - No Content

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

