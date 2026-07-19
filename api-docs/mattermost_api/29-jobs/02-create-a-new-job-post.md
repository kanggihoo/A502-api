# 02-Create a new job. [POST]

`POST /api/v4/jobs`

Create a new job.
__Minimum server version: 4.1__
##### Permissions
Must have permission to create the requested job type. Required permission depends on `type`:

- `create_data_retention_job` — `data_retention`
- `create_compliance_export_job` — `message_export`
- `create_elasticsearch_post_indexing_job` — `elasticsearch_post_indexing`
- `create_elasticsearch_post_aggregation_job` — `elasticsearch_post_aggregation`
- `create_ldap_sync_job` — `ldap_sync`
- `manage_jobs` — `migrations`, `plugins`, `product_notices`, `expiry_notify`, `active_users`, `import_process`, `import_delete`, `export_process`, `export_delete`, `cloud`, `extract_content`
- `access_control_sync` — `manage_system`, or `manage_channel_access_rules` on the channel given in job `data`, or `manage_team_access_rules` on the team in job `data` (see server logic for scoped sync jobs)


### Request Body (application/json)

```json
{
  "type": string (required), // The type of job to create
  "data": {}, // An object containing any additional data required for this job type
}
```
### Responses

#### 201 - Job creation successful

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

