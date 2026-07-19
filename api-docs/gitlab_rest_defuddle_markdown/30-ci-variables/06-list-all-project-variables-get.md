# 06-List all project variables [GET]

`GET /api/v4/projects/{id}/variables`

Lists all variables for a project. Use the `page` and `per_page` pagination parameters to control the pagination of results.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID of a project or URL-encoded NAMESPACE/PROJECT_NAME of the project owned by the authenticated user |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

#### 404 - Not Found

