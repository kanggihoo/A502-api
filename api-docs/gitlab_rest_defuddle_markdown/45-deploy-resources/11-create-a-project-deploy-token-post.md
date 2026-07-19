# 11-Create a project deploy token [POST]

`POST /api/v4/projects/{id}/deploy_tokens`

Creates a project deploy token.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Request Body (application/json)

```json
{
  "name": string (required), // New deploy token's name
  "scopes": [
    string
  ] (required), // Indicates the deploy token scopes. Must be at least one of `read_repository`, `read_registry`, `write_registry`, `read_package_registry`, `write_package_registry`, `read_virtual_registry`, or `write_virtual_registry`.
  "expires_at": string, // Expiration date for the deploy token. Does not expire if no value is provided. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`).
  "username": string, // Username for deploy token. Default is `gitlab+deploy-token-{n}`
}
```
### Responses

#### 201 - Created

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
  "token": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

