# 03-Update a job [PUT]

`PUT /api/v4/jobs/{id}`

Update a job

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | Job's ID |

### Request Body (application/json)

```json
{
  "token": string (required), // Job's authentication token
  "state": string, // Job's status: running, success, failed
  "checksum": string, // Job's trace CRC32 checksum
  "failure_reason": string, // Job's failure_reason
  "output": {
    "checksum": string, // Job's trace CRC32 checksum
    "bytesize": integer, // Job's trace size in bytes
  }, // Build log state
  "exit_code": integer, // Job's exit code
}
```
### Responses

#### 200 - Job was updated

#### 202 - Update accepted

#### 400 - Unknown parameters

#### 403 - Forbidden

#### 404 - Not Found

#### 409 - Conflict

#### 429 - Too Many Requests

