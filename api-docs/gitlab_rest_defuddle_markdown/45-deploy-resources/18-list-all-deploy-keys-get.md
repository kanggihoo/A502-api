# 18-List all deploy keys [GET]

`GET /api/v4/deploy_keys`

Lists all deploy keys for the instance.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `public` | `boolean` | `query` | No | Only return deploy keys that are public |

### Responses

#### 200 - OK

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

#### 403 - Forbidden

