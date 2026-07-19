# 03-Get a job. [GET]

`GET /api/v4/jobs/{job_id}`

Gets a single job.
__Minimum server version: 4.1__
##### Permissions
Must have permission to read the job's type:

- `read_data_retention_job` — `data_retention`
- `read_compliance_export_job` — `message_export`
- `read_elasticsearch_post_indexing_job` — `elasticsearch_post_indexing`
- `read_elasticsearch_post_aggregation_job` — `elasticsearch_post_aggregation`
- `read_ldap_sync_job` — `ldap_sync`
- `read_jobs` — `migrations`, `plugins`, `product_notices`, `expiry_notify`, `active_users`, `import_process`, `import_delete`, `export_process`, `export_delete`, `cloud`, `mobile_session_metadata`, `extract_content`
- `manage_system` — `access_control_sync`


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `job_id` | `string` | `path` | Yes | Job GUID |

### Responses

#### 200 - Job retrieval successful

Schema (application/json):
```json
{
  "id": string, // The unique id of the job
  "type": string, // The type of job
  "create_at": integer, // The time at which the job was created
  "start_at": integer, // The time at which the job was started
  "last_activity_at": integer, // The last time at which the job had activity
  "status": string, // The status of the job
  "progress": integer, // The progress (as a percentage) of the job
  "data": {}, // A freeform data field containing additional information about the job
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

