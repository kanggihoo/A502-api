# 09-Create a Geo node [POST]

`POST /api/v4/geo_nodes`

Creates a Geo node.

### Request Body (application/json)

```json
{
  "primary": boolean, // Specifying whether this node will be primary. Defaults to false.
  "enabled": boolean, // Specifying whether this node will be enabled. Defaults to true.
  "name": string (required), // The unique identifier for the Geo node. Must match `geo_node_name` if it is set in `gitlab.rb`, otherwise it must match `external_url`
  "url": string (required), // The user-facing URL for the Geo node
  "internal_url": string, // The URL defined on the primary node that secondary nodes should use to contact it. Returns `url` if not set.
  "files_max_capacity": integer, // Control the maximum concurrency of LFS/attachment backfill for this secondary node. Defaults to 10.
  "repos_max_capacity": integer, // Control the maximum concurrency of repository backfill for this secondary node. Defaults to 25.
  "verification_max_capacity": integer, // Control the maximum concurrency of repository verification for this node. Defaults to 100.
  "container_repositories_max_capacity": integer, // Control the maximum concurrency of container repository sync for this node. Defaults to 10.
  "sync_object_storage": boolean, // Flag indicating if the secondary Geo node will replicate blobs in Object Storage. Defaults to false.
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
  "minimum_reverification_interval": integer, // The interval (in days) in which the repository verification is valid. Once expired, it will be reverified. This has no effect when set on a secondary node.
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
  "sync_object_storage": boolean,
  "clone_protocol": string,
  "web_edit_url": string,
  "web_geo_replication_details_url": string,
  "_links": {},
}
```

#### 400 - Validation error

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

