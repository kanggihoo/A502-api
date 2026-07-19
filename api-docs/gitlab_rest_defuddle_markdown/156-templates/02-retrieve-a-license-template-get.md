# 02-Retrieve a license template [GET]

`GET /api/v4/templates/licenses/{name}`

Retrieves a specified license template. You can pass parameters to replace the license placeholder.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `path` | Yes | The name of the license template |
| `project` | `string` | `query` | No | The copyrighted project name |
| `fullname` | `string` | `query` | No | The full-name of the copyright holder |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "key": string,
  "name": string,
  "nickname": string,
  "html_url": string,
  "source_url": string,
  "popular": boolean,
  "description": string,
  "conditions": [
    string
  ],
  "permissions": [
    string
  ],
  "limitations": [
    string
  ],
  "content": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

