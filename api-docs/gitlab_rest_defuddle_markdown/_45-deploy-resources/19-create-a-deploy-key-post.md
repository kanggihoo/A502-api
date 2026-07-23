# 19-Create a deploy key [POST]

`POST /api/v4/deploy_keys`

Creates a deploy key for the GitLab instance. Requires administrator access.

### Request Body (application/json)

```json
{
  "key": string (required), // New deploy key
  "title": string (required), // New deploy key's title
  "expires_at": string, // The expiration date of the SSH key in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
}
```
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

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

