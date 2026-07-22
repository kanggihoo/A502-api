# 30-List all token associations [GET]

`GET /api/v4/personal_access_tokens/self/associations`

Lists all groups and projects accessible by the personal access token used to authenticate the request. Generally, this includes any groups or projects that the user is a member of.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `min_access_level` | `integer` | `query` | No | Limit by minimum access level of authenticated user |
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
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

