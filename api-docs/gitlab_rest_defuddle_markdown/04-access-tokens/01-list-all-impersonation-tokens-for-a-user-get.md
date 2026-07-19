# 01-List all impersonation tokens for a user [GET]

`GET /api/v4/users/{user_id}/impersonation_tokens`

Lists all impersonation tokens for a specified user. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `integer` | `path` | Yes | The ID of the user |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `state` | `string` | `query` | No | Filters (all|active|inactive) impersonation_tokens |

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
  "impersonation": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

