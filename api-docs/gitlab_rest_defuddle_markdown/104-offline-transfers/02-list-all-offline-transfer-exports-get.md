# 02-List all offline transfer exports [GET]

`GET /api/v4/offline_exports`

Lists all offline transfer exports

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `sort` | `string` | `query` | No | Return offline transfer exports sorted in created by `asc` or `desc` order. |
| `status` | `string` | `query` | No | Return offline transfer exports with specified status |

### Responses

#### 200 - OK

#### 400 - Bad Request

