# 32-Retrieve a personal access token [GET]

`GET /api/v4/personal_access_tokens/{id}`

Retrieves details for a specified personal access token. Administrators can retrieve details on any token. Non-administrators can only retrieve details on their own tokens.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes |  |

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

#### 401 - Unauthorized

#### 404 - Not found

