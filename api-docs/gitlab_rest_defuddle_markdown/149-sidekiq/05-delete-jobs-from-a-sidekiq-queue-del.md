# 05-Delete jobs from a Sidekiq queue [DEL]

`DELETE /api/v4/admin/sidekiq/queues/{queue_name}`

Deletes jobs from a Sidekiq queue that match the specified metadata.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `organization_id` | `string` | `query` | No | Metadata key to match |
| `user` | `string` | `query` | No | Metadata key to match |
| `user_id` | `string` | `query` | No | Metadata key to match |
| `gl_user_id` | `string` | `query` | No | Metadata key to match |
| `scoped_user` | `string` | `query` | No | Metadata key to match |
| `scoped_user_id` | `string` | `query` | No | Metadata key to match |
| `project` | `string` | `query` | No | Metadata key to match |
| `root_namespace` | `string` | `query` | No | Metadata key to match |
| `client_id` | `string` | `query` | No | Metadata key to match |
| `caller_id` | `string` | `query` | No | Metadata key to match |
| `remote_ip` | `string` | `query` | No | Metadata key to match |
| `job_id` | `string` | `query` | No | Metadata key to match |
| `pipeline_id` | `string` | `query` | No | Metadata key to match |
| `related_class` | `string` | `query` | No | Metadata key to match |
| `feature_category` | `string` | `query` | No | Metadata key to match |
| `artifact_size` | `string` | `query` | No | Metadata key to match |
| `artifact_used_cdn` | `string` | `query` | No | Metadata key to match |
| `artifacts_dependencies_size` | `string` | `query` | No | Metadata key to match |
| `artifacts_dependencies_count` | `string` | `query` | No | Metadata key to match |
| `root_caller_id` | `string` | `query` | No | Metadata key to match |
| `merge_action_status` | `string` | `query` | No | Metadata key to match |
| `bulk_import_entity_id` | `string` | `query` | No | Metadata key to match |
| `sidekiq_destination_shard_redis` | `string` | `query` | No | Metadata key to match |
| `kubernetes_agent_id` | `string` | `query` | No | Metadata key to match |
| `mvcc_manifest` | `string` | `query` | No | Metadata key to match |
| `subscription_plan` | `string` | `query` | No | Metadata key to match |
| `ai_resource` | `string` | `query` | No | Metadata key to match |
| `policy_sync_config_id` | `string` | `query` | No | Metadata key to match |
| `worker_class` | `string` | `query` | No | Metadata key to match |
| `queue_name` | `any` | `path` | Yes |  |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

