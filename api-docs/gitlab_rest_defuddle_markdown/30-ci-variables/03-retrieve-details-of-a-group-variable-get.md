# 03-Retrieve details of a group variable [GET]

`GET /api/v4/groups/{id}/variables/{key}`

Retrieves details of a specified group variable. If there are multiple variables with the same key, use `filter` to select the correct `environment_scope`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group or URL-encoded path of the group owned by the authenticated<br>      user |
| `key` | `string` | `path` | Yes | The key of the variable |

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

#### 404 - Group Variable Not Found

