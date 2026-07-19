# 04-Download the results of a job. [GET]

`GET /api/v4/jobs/{job_id}/download`

Download the result of a single job.
__Minimum server version: 5.28__
##### Permissions
Must have `download_compliance_export_result` permission for message export jobs.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `job_id` | `string` | `path` | Yes | Job GUID |

### Responses

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

