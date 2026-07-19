# 09-List all managers for a runner [GET]

`GET /api/v4/runners/{id}/managers`

List all managers for a specified runner.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of a runner |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "system_id": string,
  "version": string,
  "revision": string,
  "platform": string,
  "architecture": string,
  "created_at": string,
  "contacted_at": string,
  "ip_address": string,
  "status": string,
  "job_execution_status": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

