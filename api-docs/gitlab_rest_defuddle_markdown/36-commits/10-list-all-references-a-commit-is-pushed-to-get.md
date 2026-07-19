# 10-List all references a commit is pushed to [GET]

`GET /api/v4/projects/{id}/repository/commits/{sha}/refs`

Lists all references (from branches or tags) a commit is pushed to. The pagination parameters `page` and `per_page` can be used to restrict the list of references.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `sha` | `string` | `path` | Yes | A commit sha |
| `type` | `string` | `query` | No | Scope |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "type": string,
  "name": string,
}
```

#### 400 - Bad Request

#### 404 - Not found

