# 08-Create workflow checkpoint [POST]

`POST /api/v4/ai/duo_workflows/workflows/{id}/checkpoints`

Create workflow checkpoint

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow |

### Request Body (application/json)

```json
{
  "thread_ts": string (required), // The thread ts
  "parent_ts": string, // The parent ts
  "checkpoint": {}, // Checkpoint content
  "compressed_checkpoint": string, // Checkpoint content zlib compressed and base64 encoded
  "metadata": {} (required), // Checkpoint metadata
  "model_metadata_json": string, // JSON string of the model metadata
  "current_thread": integer, // Thread grouping hint for blob reconstruction
  "channel_blobs": [
    {
      "channel": string (required), // Channel name
      "version": string (required), // Channel version
      "write_type": string (required), // Serialization type (e.g. msgpack)
      "step_action": enum("conversation" | "compaction") (required), // Append or replace signal (conversation or compaction)
      "data": string (required), // Base64-encoded blob bytes
    }
  ], // Per-channel blobs for incremental checkpoint storage
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

