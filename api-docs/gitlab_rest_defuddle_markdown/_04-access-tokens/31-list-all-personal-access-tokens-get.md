# 31-List all personal access tokens [GET]

`GET /api/v4/personal_access_tokens`

Lists all personal access tokens accessible by the authenticated user. For administrators, returns all personal access tokens in the instance. For non-administrators, returns all of their personal access tokens.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `integer` | `query` | No | Filter PATs by User ID |
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
  "last_used_ips": [
    string
  ], // The five most recent unique IP addresses that have authenticated with this token. When the limit is reached, the oldest IP address is removed. The list updates once per minute per token.
  "granular_scopes": [
    {
      "access": string,
      "permissions": [
        any
      ],
      "project_id": integer,
      "group_id": integer,
    }
  ],
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

