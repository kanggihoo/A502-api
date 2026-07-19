# 16-List all personal access tokens for a group service account [GET]

`GET /api/v4/groups/{id}/service_accounts/{user_id}/personal_access_tokens`

Lists all personal access tokens for a specified group service account

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
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
| `user_id` | `integer` | `path` | Yes | The ID of the service account |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "revoked": boolean,
  "created_at": string,
  "description": string,
  "scopes": [
    any
  ],
  "user_id": integer,
  "last_used_at": string,
  "active": boolean,
  "granular": boolean,
  "expires_at": string,
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - Forbidden

#### 404 - 404 Group Not Found

