# 04-Retrieve a .gitignore template [GET]

`GET /api/v4/templates/gitignores/{name}`

Retrieves a specified .gitignore template.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `path` | Yes | The name of the .gitignore template |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "content": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

