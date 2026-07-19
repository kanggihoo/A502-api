# 08-Create multiple workflow checkpoint writes [POST]

`POST /api/v4/ai/duo_workflows/workflows/{id}/checkpoint_writes_batch`

Create multiple workflow checkpoint writes

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow |

### Request Body (application/json)

```json
{
  "thread_ts": string (required), // The thread ts
  "checkpoint_writes": [
    {
      "task": string (required), // The task id
      "idx": integer (required), // The index of checkpoint write
      "channel": string (required), // The channel
      "write_type": string (required), // The type of data
      "data": string (required), // The checkpoint write data
    }
  ] (required), // List of checkpoint writes
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

