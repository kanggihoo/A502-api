# 01-List all topics [GET]

`GET /api/v4/topics`

Lists all project topics sorted by the number of associated projects.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `search` | `string` | `query` | No | Return list of topics matching the search criteria |
| `without_projects` | `boolean` | `query` | No | Return list of topics without assigned projects |
| `organization_id` | `integer` | `query` | No | The organization id for the topics |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "title": string,
  "description": string,
  "total_projects_count": integer,
  "organization_id": integer,
  "avatar_url": string,
}
```

#### 400 - Bad Request

