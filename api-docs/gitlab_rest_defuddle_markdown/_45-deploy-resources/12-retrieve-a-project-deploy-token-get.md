# 12-Retrieve a project deploy token [GET]

`GET /api/v4/projects/{id}/deploy_tokens/{token_id}`

Retrieves a project deploy token.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `token_id` | `integer` | `path` | Yes | The ID of the deploy token |

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

#### 404 - Not found

