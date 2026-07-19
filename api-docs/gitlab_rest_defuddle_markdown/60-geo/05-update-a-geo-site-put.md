# 05-Update a Geo site [PUT]

`PUT /api/v4/geo_sites/{id}`

Updates a specified Geo site.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes |  |

### Request Body (application/json)

```json
{
  "enabled": boolean, // Flag indicating if the Geo site is enabled
  "name": string, // The unique identifier for the Geo site. Must match `geo_node_name` if it is set in gitlab.rb, otherwise it must match `external_url`
  "url": string, // The user-facing URL of the Geo site
  "internal_url": string, // The URL defined on the primary site that secondary sites should use to contact it. Returns `url` if not set.
  "files_max_capacity": integer, // Control the maximum concurrency of LFS/attachment backfill for this secondary site
  "repos_max_capacity": integer, // Control the maximum concurrency of repository backfill for this secondary site
  "verification_max_capacity": integer, // Control the maximum concurrency of repository verification for this site
  "container_repositories_max_capacity": integer, // Control the maximum concurrency of container repository sync for this site
  "sync_object_storage": boolean, // Flag indicating if the secondary Geo site will replicate blobs in Object Storage
  "selective_sync_type": string, // Limit syncing to only specific groups, or shards. Valid values: `"namespaces"`, `"shards"`, or `null`
  "selective_sync_shards": [
    string
  ], // The repository storages whose projects should be synced, if `selective_sync_type` == `shards`
  "selective_sync_namespace_ids": [
    integer
  ], // The IDs of groups that should be synced, if `selective_sync_type` == `namespaces`
  "selective_sync_organization_ids": [
    integer
  ], // The IDs of organizations that should be synced, if `selective_sync_type` == `organizations`
  "minimum_reverification_interval": integer, // The interval (in days) in which the repository verification is valid. Once expired, it will be reverified. This has no effect when set on a secondary site.
  "blob_download_timeout": integer, // Maximum time (in seconds) for blob downloads during Geo sync. Defaults to 28800 (8 hours). Maximum is 86400 (24 hours).
}
```
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

#### 404 - 404 GeoSite Not Found

