# 25-Enable a deploy key [POST]

`POST /api/v4/projects/{id}/deploy_keys/{key_id}/enable`

Enables a deploy key for a project so this can be used. Returns the enabled key, with a status code 201 when successful.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `key_id` | `integer` | `path` | Yes | The ID of the deploy key |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "title": string,
  "created_at": string,
  "expires_at": string,
  "last_used_at": string,
  "key": string,
  "usage_type": string,
  "fingerprint": string,
  "fingerprint_sha256": string,
  "projects_with_write_access": {
    "id": integer,
    "description": string,
    "name": string,
    "name_with_namespace": string,
    "path": string,
    "path_with_namespace": string,
    "created_at": string,
  },
  "projects_with_readonly_access": {
    "id": integer,
    "description": string,
    "name": string,
    "name_with_namespace": string,
    "path": string,
    "path_with_namespace": string,
    "created_at": string,
  },
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

