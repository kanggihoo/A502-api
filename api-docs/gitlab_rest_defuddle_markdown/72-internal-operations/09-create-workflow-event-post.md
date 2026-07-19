# 09-Create workflow event [POST]

`POST /api/v4/ai/duo_workflows/workflows/{id}/events`

Create workflow event

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow |

### Request Body (application/json)

```json
{
  "event_type": enum("pause" | "resume" | "stop" | "message" | "response" | "require_input") (required), // The type of event
  "message": string (required), // Message from the human
  "correlation_id": string, // Correlation ID for tracking events
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

