# 01-Get a project repository tree [GET]

`GET /api/v4/projects/{id}/repository/tree`

Get a project repository tree

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `ref` | `string` | `query` | No | The name of a repository branch or tag, if not given the default branch is used |
| `path` | `string` | `query` | No | The path of the tree |
| `recursive` | `boolean` | `query` | No | Used to get a recursive tree |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `pagination` | `string` | `query` | No | Specify the pagination method ("none" is only valid if "recursive" is true) |
| `page_token` | `string` | `query` | No | Record from which to start the keyset pagination |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": string,
  "name": string,
  "type": string,
  "path": string,
  "mode": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

