# 04-List all group and project access tokens for a group [GET]

`GET /api/v4/groups/{id}/manage/resource_access_tokens`

Lists all group and project access tokens associated with a top-level-group. This feature was introduced in GitLab 17.10.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `revoked` | `boolean` | `query` | No | Filter tokens where revoked state matches parameter |
| `state` | `string` | `query` | No | Filter tokens which are either active or not |
| `created_before` | `string` | `query` | No | Filter tokens which were created before given datetime |
| `created_after` | `string` | `query` | No | Filter tokens which were created after given datetime |
| `last_used_before` | `string` | `query` | No | Filter tokens which were used before given datetime |
| `last_used_after` | `string` | `query` | No | Filter tokens which were used after given datetime |
| `expires_before` | `string` | `query` | No | Filter tokens which expire before given datetime |
| `expires_after` | `string` | `query` | No | Filter tokens which expire after given datetime |
| `search` | `string` | `query` | No | Filters tokens by name |
| `sort` | `string` | `query` | No | Sort tokens |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

