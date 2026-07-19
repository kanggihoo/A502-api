# 04-Append a patch to the job trace [PATCH]

`PATCH /api/v4/jobs/{id}/trace`

Append a patch to the job trace

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | Job's ID |

### Request Body (application/json)

```json
{
  "token": string, // Job's authentication token
  "debug_trace": boolean, // Enable or disable the debug trace
}
```
### Responses

#### 202 - Trace was patched

#### 400 - Missing Content-Range header

#### 403 - Forbidden

#### 404 - Not Found

#### 416 - Range not satisfiable

#### 429 - Too Many Requests

