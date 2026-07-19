# 06-Get the jobs of the given type. [GET]

`GET /api/v4/jobs/type/{job_type}`

Get a page of jobs of the given type. Use the query parameters to modify
the behaviour of this endpoint.

__Minimum server version: 4.1__

##### Permissions
Must have permission to read the path `job_type`, using the same mapping as `GET /api/v4/jobs`:

- `read_data_retention_job` — `data_retention`
- `read_compliance_export_job` — `message_export`
- `read_elasticsearch_post_indexing_job` — `elasticsearch_post_indexing`
- `read_elasticsearch_post_aggregation_job` — `elasticsearch_post_aggregation`
- `read_ldap_sync_job` — `ldap_sync`
- `read_jobs` — `migrations`, `plugins`, `product_notices`, `expiry_notify`, `active_users`, `import_process`, `import_delete`, `export_process`, `export_delete`, `cloud`, `mobile_session_metadata`, `extract_content`
- `manage_system` — `access_control_sync`

When `job_type` is `access_control_sync` and query parameter `team_id` is set to a valid team GUID, team admins with `manage_team_access_rules` on that team may list jobs scoped to that team without `manage_system`. When `team_id` is set, results include only jobs whose stored data matches that team for the requested type.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `job_type` | `string` | `path` | Yes | Job type |
| `team_id` | `string` | `query` | No | Optional team GUID. When set, the server returns jobs of the given `job_type` whose job data includes this `team_id` (see server filtering). For `access_control_sync`, team admins with `manage_team_access_rules` on this team may use this parameter to read team-scoped jobs without `manage_system`.<br> |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of jobs per page. |

### Responses

#### 200 - Job list retrieval successful

Schema (application/json):
```json
[
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
]
```

#### 400 - 

#### 401 - 

#### 403 - 

