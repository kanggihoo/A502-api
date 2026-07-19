# 11-Retrieve a test report summary for a pipeline [GET]

`GET /api/v4/projects/{id}/pipelines/{pipeline_id}/test_report_summary`

Retrieves a test report summary for a pipeline.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID or URL-encoded path |
| `pipeline_id` | `integer` | `path` | Yes | The pipeline ID |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "total": {},
  "test_suites": {
    "name": string,
    "total_time": integer,
    "total_count": integer,
    "success_count": integer,
    "failed_count": integer,
    "skipped_count": integer,
    "error_count": integer,
    "suite_error": string,
    "test_cases": [
      {
        "status": string,
        "name": string,
        "classname": string,
        "file": string,
        "execution_time": integer,
        "system_output": string,
        "stack_trace": string,
        "recent_failures": {},
        "attachment_url": string,
      }
    ],
    "build_ids": [
      integer
    ],
  },
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

