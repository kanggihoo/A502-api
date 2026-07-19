# 21-Add a deploy key for a project [POST]

`POST /api/v4/projects/{id}/deploy_keys`

Adds a deploy key for a specified project. If the deploy key already exists in another project, it is joined to the current project only if the original one is accessible by the same user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Request Body (application/json)

```json
{
  "key": string (required), // New deploy key
  "title": string (required), // New deploy key's title
  "can_push": boolean, // Can deploy key push to the project's repository
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
  "can_push": boolean,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

