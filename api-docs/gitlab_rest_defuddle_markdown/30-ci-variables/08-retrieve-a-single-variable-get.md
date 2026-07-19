# 08-Retrieve a single variable [GET]

`GET /api/v4/projects/{id}/variables/{key}`

Retrieves details of a specified variable. If there are multiple variables with the same key, use `filter` to select the correct `environment_scope`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID of a project or URL-encoded NAMESPACE/PROJECT_NAME of the project owned by the authenticated user |
| `key` | `string` | `path` | Yes | The key of a variable |
| `filter` | `object` | `query` | No | Available filters: [environment_scope]. Example: filter[environment_scope]=production |
| `filter[environment_scope]` | `string` | `query` | No | The environment scope of a variable |

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

