# 06-Get repository health [GET]

`GET /api/v4/projects/{id}/repository/health`

Get repository health

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `generate` | `boolean` | `query` | No | Triggers a new health report to be generated |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "size": integer,
  "references": {
    "loose_count": integer,
    "packed_size": integer,
    "reference_backend": string,
  },
  "objects": {
    "size": integer,
    "recent_size": integer,
    "stale_size": integer,
    "keep_size": integer,
    "packfile_count": integer,
    "reverse_index_count": integer,
    "cruft_count": integer,
    "keep_count": integer,
    "loose_objects_count": integer,
    "stale_loose_objects_count": integer,
    "loose_objects_garbage_count": integer,
  },
  "commit_graph": {
    "commit_graph_chain_length": integer,
    "has_bloom_filters": boolean,
    "has_generation_data": boolean,
    "has_generation_data_overflow": boolean,
  },
  "bitmap": {
    "has_hash_cache": boolean,
    "has_lookup_table": boolean,
    "version": integer,
  },
  "multi_pack_index": {
    "packfile_count": integer,
    "version": integer,
  },
  "multi_pack_index_bitmap": {
    "has_hash_cache": boolean,
    "has_lookup_table": boolean,
    "version": integer,
  },
  "alternates": {},
  "is_object_pool": boolean,
  "last_full_repack": {
    "seconds": integer,
    "nanos": integer,
  },
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

