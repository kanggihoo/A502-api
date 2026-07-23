# 09-List all deploy tokens [GET]

`GET /api/v4/deploy_tokens`

Lists all deploy tokens for the instance.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `active` | `boolean` | `query` | No | Limit by active status |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "username": string,
  "expires_at": string,
  "scopes": [
    any
  ],
  "revoked": boolean,
  "expired": boolean,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

