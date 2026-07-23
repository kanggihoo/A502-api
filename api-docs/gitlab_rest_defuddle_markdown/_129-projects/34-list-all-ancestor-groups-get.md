# 34-List all ancestor groups [GET]

`GET /api/v4/projects/{id}/groups`

Lists all ancestor groups for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `search` | `string` | `query` | No | Return list of groups matching the search criteria |
| `skip_groups` | `array` | `query` | No | Array of group ids to exclude from list |
| `with_shared` | `boolean` | `query` | No | Include shared groups |
| `shared_visible_only` | `boolean` | `query` | No | Limit to shared groups user has access to |
| `shared_min_access_level` | `integer` | `query` | No | Limit returned shared groups by minimum access level to the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "web_url": string,
  "name": string,
  "avatar_url": string,
  "full_name": string,
  "full_path": string,
}
```

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not found

