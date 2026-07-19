# 12-Retrieve a single Geo node [GET]

`GET /api/v4/geo_nodes/{id}`

Retrieves a single Geo Node.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes |  |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "url": string,
  "internal_url": string,
  "primary": boolean,
  "enabled": boolean,
  "current": boolean,
  "files_max_capacity": integer,
  "repos_max_capacity": integer,
  "verification_max_capacity": integer,
  "container_repositories_max_capacity": integer,
  "selective_sync_type": string,
  "selective_sync_shards": [
    any
  ],
  "selective_sync_namespace_ids": [
    any
  ],
  "selective_sync_organization_ids": [
    any
  ],
  "minimum_reverification_interval": integer,
  "sync_object_storage": boolean,
  "clone_protocol": string,
  "web_edit_url": string,
  "web_geo_replication_details_url": string,
  "_links": {},
}
```

#### 400 - 400 Bad request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 GeoNode Not Found

