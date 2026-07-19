# 07-Update the status of a job [PATCH]

`PATCH /api/v4/jobs/{job_id}/status`

Update the status of a job. Valid status updates:
- 'in_progress' -> 'pending'
- 'in_progress' | 'pending' -> 'cancel_requested'
- 'cancel_requested' -> 'canceled'

Add force to the body of the PATCH request to bypass the given rules, the only statuses you can go to are: pending, cancel_requested and canceled. This can have unexpected consequences and should be used with caution.

##### Permissions
Must have permission to manage the job's type:

- `manage_data_retention_job` — `data_retention`
- `manage_compliance_export_job` — `message_export`
- `manage_elasticsearch_post_indexing_job` — `elasticsearch_post_indexing`
- `manage_elasticsearch_post_aggregation_job` — `elasticsearch_post_aggregation`
- `manage_ldap_sync_job` — `ldap_sync`
- `manage_jobs` — `migrations`, `plugins`, `product_notices`, `expiry_notify`, `active_users`, `import_process`, `import_delete`, `export_process`, `export_delete`, `cloud`, `extract_content`
- `manage_system` — `access_control_sync`


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `job_id` | `string` | `path` | Yes | Job GUID |

### Request Body (application/json)

```json
{
  "status": string (required), // The status you want to set
  "force": boolean, // Set this to true to bypass status restrictions
}
```
### Responses

#### 200 - Status successfully set.

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

