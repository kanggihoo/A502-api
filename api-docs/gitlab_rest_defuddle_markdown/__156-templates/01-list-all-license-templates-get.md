# 01-List all license templates [GET]

`GET /api/v4/templates/licenses`

Lists all available license templates.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `popular` | `boolean` | `query` | No | If passed, returns only popular licenses |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

