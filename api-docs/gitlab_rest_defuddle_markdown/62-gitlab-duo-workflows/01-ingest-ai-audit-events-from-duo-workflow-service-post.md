# 01-Ingest AI audit events from Duo Workflow Service [POST]

`POST /api/v4/ai/duo_workflows/workflows/{id}/audit_events`

Ingest AI audit events from Duo Workflow Service

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow |

### Request Body (application/json)

```json
{
  "events": [
    {
      "id": string (required), // CloudEvent id (UUID)
      "type": string (required), // Event type (e.g., ai_llm_input_sent)
      "source": string (required), // CloudEvent source
      "time": string (required), // Event timestamp (ISO 8601) from the gateway
      "data": {}, // Event-specific payload
    }
  ] (required), // Array of CloudEvents v1.0 envelopes
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

