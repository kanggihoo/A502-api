# 05-List all custom attributes for a project [GET]

`GET /api/v4/projects/{id}/custom_attributes`

Lists all custom attributes for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "key": string,
  "value": string,
}
```

#### 404 - Not Found

