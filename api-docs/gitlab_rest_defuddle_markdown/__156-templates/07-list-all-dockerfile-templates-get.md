# 07-List all Dockerfile templates [GET]

`GET /api/v4/templates/dockerfiles`

Lists all Dockerfile templates.

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

