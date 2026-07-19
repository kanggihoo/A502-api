# 07-Retrieve a commit sequence [GET]

`GET /api/v4/projects/{id}/repository/commits/{sha}/sequence`

Retrieves the commit sequence for a specified commit.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `sha` | `string` | `path` | Yes | A commit SHA |
| `first_parent` | `boolean` | `query` | No | Only include the first parent of merges |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "count": integer,
}
```

#### 400 - Bad Request

#### 404 - Not found

