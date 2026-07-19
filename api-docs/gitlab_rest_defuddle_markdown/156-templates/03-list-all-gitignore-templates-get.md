# 03-List all .gitignore templates [GET]

`GET /api/v4/templates/gitignores`

Lists all .gitignore templates.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "key": string,
  "name": string,
}
```

#### 400 - Bad Request

