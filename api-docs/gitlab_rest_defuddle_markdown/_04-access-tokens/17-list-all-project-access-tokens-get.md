# 17-List all project access tokens [GET]

`GET /api/v4/projects/{id}/access_tokens`

Lists all project access tokens for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | ID or URL-encoded path of the project |
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
  "access_level": integer,
  "resource_type": string,
  "resource_id": integer,
}
```

#### 400 - Bad Request

#### 404 - Not Found

