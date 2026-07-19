# 07-Get repository contributors [GET]

`GET /api/v4/projects/{id}/repository/contributors`

Get repository contributors

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `ref` | `string` | `query` | No | The name of a repository branch or tag, if not given the default branch is used |
| `order_by` | `string` | `query` | No | Return contributors ordered by `name` or `email` or `commits` |
| `sort` | `string` | `query` | No | Sort by asc (ascending) or desc (descending) |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "email": string,
  "commits": integer,
  "additions": integer,
  "deletions": integer,
}
```

#### 400 - Bad Request

#### 404 - Not Found

