# 14-List all group deploy tokens [GET]

`GET /api/v4/groups/{id}/deploy_tokens`

Lists all group deploy tokens.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group owned by the authenticated user |
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

#### 404 - Not found

