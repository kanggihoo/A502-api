# 02-List all Geo sites [GET]

`GET /api/v4/geo_sites`

Lists all Geo sites for the instance.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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
  "blob_download_timeout": integer,
  "sync_object_storage": boolean,
  "web_edit_url": string,
  "web_geo_replication_details_url": string,
  "_links": {},
}
```

#### 400 - 400 Bad request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

