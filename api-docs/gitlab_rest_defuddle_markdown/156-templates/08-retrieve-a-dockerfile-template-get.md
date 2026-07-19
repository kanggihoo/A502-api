# 08-Retrieve a Dockerfile template [GET]

`GET /api/v4/templates/dockerfiles/{name}`

Retrieves a specified Dockerfile template.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `path` | Yes | The name of the Dockerfile template |

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

